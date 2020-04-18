# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/8 16:33
# Reference:
# Description: # python2 arcgis10.6 10.3
	# 导出图片 001
	# 添加shp文件 current 002
	# 递归遍历 003
	# 获取图层中某一个字段的所有值 004

# ---------------------------------------------------------------------------
import arcpy, os

# arcpy 导出JPEG，适用于文件夹或者单个mxd
def export(path,resolution):										 # 001
	arcpy.env.overwriteOutput = True
	if not os.path.isdir(path) and path[-3:].lower() == 'mxd':
		print "file"
		mxd1 = arcpy.mapping.MapDocument(path)
		print 'exporting...'
		arcpy.mapping.ExportToJPEG(
			mxd1, os.path.abspath(path[:-3] + 'jpg'), resolution=resolution)
		a = os.path.split(path)
		print a[1]+" finished"
	else:
		print "folder"
		for afile in os.listdir(path):
			if afile[-3:].lower() == 'mxd':
				mxd1 = arcpy.mapping.MapDocument(os.path.join(path, afile))
				print 'exporting...'
				# ExportToJEPG的第二个参数是导出图片的名称和目录设置
				arcpy.mapping.ExportToJPEG(
					mxd1, os.path.join(path, afile[:-3] + 'jpg'), resolution=resolution
				)
				print afile + ' finished'
				print "\n----------------"
				del mxd1
			else:
				pass
			
			
__getall_items = []
def getall_item(dirs_p, suffix, matchword=None):                # 002
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	recur 使用递归，特别注意，层数不要太多
	:param dirs_p: dir address
	:param suffix: 后缀
	:param matchword: 匹配字段，简单筛选出符合匹配字段的项目
	:return: list
	"""
	global __getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			# 递归
			getall_item(file_path, suffix, matchword)
		else:# 保证不使用matchword匹配字段时也能正常运行
			if matchword:
				# 注意matchword是 str 还是 Unicode
				if file_p[-3:].lower() == suffix and matchword in file_p:
					__getall_items.append(file_path)
			else: # 未使用匹配功能
				if file_p[-3:].lower() == suffix:
					__getall_items.append(file_path)
	return __getall_items


def addshp(shp_path, df_name=None, fresh=True):                   # 003
	"""
	import arcpy,os
	*加载shp文件到   *当前mxd
	:param shp_path: file path.
	:param df_name: dataframe name; default first df.
	:param fresh:bollean; refresh; default ture.
	:return: None
	"""
	mxd = arcpy.mapping.MapDocument("CURRENT")
	dataframe = arcpy.mapping.ListDataFrames(mxd, df_name)[0]
	layer = arcpy.mapping.Layer(shp_path)
	arcpy.mapping.AddLayer(dataframe, layer, "AUTO_ARRANGE")
	if fresh:
		arcpy.RefreshActiveView()  # 刷新地图和布局窗口
		arcpy.RefreshTOC()  # 刷新内容列表

def get_fieldvalue(layer,field):									# 004
	"""
	获取图层中某一个字段的所有值
	layer: mxd layer
	field: 字段,只能选一个字段
	"""
	_list = []
	cursor = arcpy.da.SearchCursor(layer,field)
	for row in cursor:
		if row[0] not in _list:
			_list.append(row[0])
	del cursor
	return _list
	
def merger(layer):
	arcpy.env.addOutputsToMap = True
	arcpy.env.overwriteOutput = True
	"""一键快速合并图层的所有要素"""
	# 判断是否有这个字段
	all_fields = arcpy.ListFields(layer)
	all_name = [i.name for i in all_fields]
	# for f in all_fields:
	# 	print f.name #Todo  neme 和 aliasName 返回的都一样，为什么
		# print f.aliasName
	name = "test_f_lcc"
	if name not in all_name:
		arcpy.AddField_management(layer, name, "LONG")
	cursor = arcpy.da.UpdateCursor(layer, name)
	for row in cursor:
		row[0] = "1"
		cursor.updateRow(row)
	del cursor
	new_ly = "new_layer"
	arcpy.Dissolve_management(layer, new_ly ,name)
	return new_ly
	



# test
if __name__ == '__main__':
	mxd = arcpy.mapping.MapDocument("CURRENT")
	ly = arcpy.mapping.ListLayers(mxd,"村界")[0]
	merger(ly)
	# files = getall_item(
	# 	ur"G:\高标准分布图\青川县\510000高标准农田建设上图入库数据20200113","shp","GBZ")
	# print len(files)
	# for afile in files:
	# 	addshp(afile)


	

