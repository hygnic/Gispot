#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/8 16:33
# Reference:
"""
Description: # python2 arcgis10.6 10.3
	# 导出图片 001
	# 递归查询 002.0
	# 列表筛选（根据大小和字符串匹配） 002.5
	# 添加shp文件到mxd 003
	# 字段展示其 获取图层中某单个字段的所有值 004
	# 一键合并 005
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os

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
def recur_search(dirs_p, suffix, recur=True, counter=0): 				 # 002.0
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	ss = recur_search(ur"G:\高标准","",True)
	ss = recur_search(ur"G:\高标准","xlsx",True)
	ss = recur_search(ur"G:\高标准",["xlsx","xls"],True)

	recur 使用递归，特别注意，层数不要太多
	:param recur: bool 是否启用递归
	:param dirs_p: dir address
	:param suffix: 后缀 str或者列表
	:param counter: 计数 用于缩进\t
	:return: list
	"""
	global __getall_items
	# global __getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p, file_p)
		if os.path.isdir(file_path):
			print "\t" * counter + "dir:", file_p
			# 递归
			if recur:
				recur_search(file_path, suffix, recur, counter + 1)
		else:
			# print "\t"*counter+file_p
			if suffix:
				# 单个后缀
				if not isinstance(suffix, list):
					# stage 1 筛选后缀
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name = name_and_suffix[0]
					if f_suffix == suffix:
						print "\t" * counter, base_name
						__getall_items.append(file_path)
				# 多个后缀组成列表
				else:
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name = name_and_suffix[0]
					if f_suffix in suffix:
						print "\t" * counter, base_name
						__getall_items.append(file_path)
			# 无后缀要求，获取所有文件
			else:
				__getall_items.append(file_path)
	
	return __getall_items


def filter_list(raw_list, matchword, size_limit=None):					# 002.5
	"""
	使用字符匹配和文件大小（如果列表元素是地址的话）对列表中进行筛选
	import os
	oo = filter_list(ss,u"评估")
	oo = filter_list(ss,u"评估",100)
	:param raw_list:
	:param size_limit: int 排除等于该大小的文件 计量单位 字节
	:param matchword: 匹配字段，筛选符合该条件的元素
	:return: list
	"""
	_bridge_list = []
	if matchword:
		for a_raw in raw_list:
			if matchword in os.path.basename(a_raw):
				_bridge_list.append(a_raw)
		raw_list = _bridge_list
	if size_limit:
		_bridge_list = []
		_bridge_list = [x for x in raw_list if os.path.getsize(x) != size_limit]
	return _bridge_list
	
	
# __getall_items = []
# def recur_search(dirs_p, suffix,size_limit, matchword=None):		# 002
# 	"""
# 	import os
# 	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
# 	recur 使用递归，特别注意，层数不要太多
# 	:param size_limit: 文件大小限制 字节
# 	:param dirs_p: dir address
# 	:param suffix: 后缀
# 	:param matchword: 匹配字段，简单筛选出符合匹配字段的项目
# 	:return: list
# 	"""
# 	global __getall_items
# 	matchword=str(matchword)
# 	for file_p in os.listdir(dirs_p):
# 		file_path = os.path.join(dirs_p,file_p)
# 		if os.path.isdir(file_path):
# 			# 递归
# 			recur_search(file_path, suffix,size_limit, matchword)
# 		else:
# 			# arcpy.AddMessage(4)
# 			if matchword: # 保证不使用matchword匹配字段时也能正常运行
# 				# arcpy.AddMessage(6)
# 				# if file_p[-3:].lower() == suffix and matchword in file_p and os.path.getsize(file_path)!=100:
# 				if file_p[-3:].lower() == suffix and matchword in file_p:
# 					# 使用了文件大小限制且不符合大小要求
# 					if size_limit and os.path.getsize(file_path)!=size_limit:
# 						print type(matchword)
# 						print matchword
# 						__getall_items.append(file_path)
# 					# 没有使用大小限制
# 					elif not size_limit:
# 						__getall_items.append(file_path)
# 					# 使用了大小限制，符合大小要求
# 					else:
# 						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
# 						arcpy.AddMessage("空项目/未添加项：")
# 						arcpy.AddMessage(os.path.splitext(os.path.basename(file_path))[0])
# 			else:
# 				# arcpy.AddMessage(9)
# 				if file_p[-3:].lower() == suffix:
# 					# 使用了文件大小限制且不符合大小要求
# 					if size_limit and os.path.getsize(file_path) != size_limit:
# 						print type(matchword)
# 						print matchword
# 						__getall_items.append(file_path)
# 					# 没有使用大小限制
# 					elif not size_limit:
# 						__getall_items.append(file_path)
# 					# 使用了大小限制，符合大小要求
# 					else:
# 						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
# 						arcpy.AddMessage("空项目/未添加项：")
# 						arcpy.AddMessage(
# 							os.path.splitext(os.path.basename(file_path))[0])
# 					# print type(matchword)
# 					# print matchword
# 					# __getall_items.append(file_path)
# 	return __getall_items


def addshp(mapdocument,shp_path, df_name=None, fresh=True):              # 003
	"""
	import arcpy,os
	*加载shp文件到mxd
	:param mapdocument: mxd
	:param shp_path: file path.
	:param df_name: dataframe name; default first df.
	:param fresh:bollean; refresh; default ture.
	:return: None
	"""
	dataframe = arcpy.mapping.ListDataFrames(mapdocument, df_name)[0]
	layer = arcpy.mapping.Layer(shp_path)
	arcpy.mapping.AddLayer(dataframe, layer, "AUTO_ARRANGE")
	if fresh:
		arcpy.RefreshActiveView()  # 刷新地图和布局窗口
		arcpy.RefreshTOC()  # 刷新内容列表

def field_shower(layer, field):									# 004
	"""
	获取图层中某单个字段的所有值
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
	
def merger(layer):													# 005
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
	arcpy.DeleteField_management(new_ly, name)
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


	

