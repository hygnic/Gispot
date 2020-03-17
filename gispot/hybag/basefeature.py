# -*- coding:cp936 -*-
# User: liaochenchen
# Date: 2020/3/4
# python2 arcgis10.6
import arcpy, os

# 导出图片 001
# 添加shp文件 current 002
# 递归遍历 003



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
def hybag_getall_item(dirs_p, suffix, matchword=None):                # 002
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
			hybag_getall_item(file_path, suffix, matchword)
		else:# 保证不使用matchword匹配字段时也能正常运行
			if matchword:
				# 注意matchword是 str 还是 Unicode
				if file_p[-3:].lower() == suffix and matchword in file_p:
					__getall_items.append(file_path)
			else: # 未使用匹配功能
				if file_p[-3:].lower() == suffix:
					__getall_items.append(file_path)
	return __getall_items


def hybag_addshp(shp_path, df_name=None, fresh=True):                   # 003
	"""
	import arcpy,os
	加载shp文件到当前mxd
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



# test
if __name__ == '__main__':
	files = hybag_getall_item(
		ur"G:\高标准分布图\青川县\510000高标准农田建设上图入库数据20200113","shp","GBZ")
	print len(files)
	for afile in files:
		hybag_addshp(afile)


	

