#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# User: liaochenchen
# Date: 2020/3/11
# Python2 arcgis10.6 arcgis10.3
# Reference:
"""
Description: 来自hybag_base 中的方法三和方法二
*已经导入工具箱
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy,os

def hybag_addshp(shp_path,fresh=True):
	"""
	import arcpy,os
	加载shp文件到当前mxd
	:param shp_path: file path.
	:param df_name: dataframe name; default first df.
	:param fresh:bollean; refresh; default ture.
	:return: None
	"""
	mxd = arcpy.mapping.MapDocument("CURRENT")
	dataframe = arcpy.mapping.ListDataFrames(mxd)[0]
	layer = arcpy.mapping.Layer(shp_path)
	arcpy.mapping.AddLayer(dataframe, layer)
	if fresh:
		arcpy.RefreshActiveView()  # 刷新地图和布局窗口
		arcpy.RefreshTOC()  # 刷新内容列表

_getall_items = []
_not_get = []
def recur_search(dirs_p, suffix,size_limit, matchword=None):
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	recur 使用递归，特别注意，层数不要太多
	:param size_limit: 文件大小限制 字节
	:param dirs_p: dir address
	:param suffix: 后缀
	:param matchword: 匹配字段，简单筛选出符合匹配字段的项目
	:return: list
	"""
	global _getall_items
	global _not_get
	matchword=str(matchword)
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			# 递归
			recur_search(file_path, suffix,size_limit, matchword)
		else:
			# arcpy.AddMessage(4)
			if matchword: # 保证不使用matchword匹配字段时也能正常运行
				# arcpy.AddMessage(6)
				# if file_p[-3:].lower() == suffix and matchword in file_p and os.path.getsize(file_path)!=100:
				if file_p[-3:].lower() == suffix and matchword in file_p:
					# 使用了文件大小限制且不符合大小要求
					if size_limit and os.path.getsize(file_path)!=size_limit:
						print type(matchword)
						print matchword
						_getall_items.append(file_path)
					# 没有使用大小限制
					elif not size_limit:
						_getall_items.append(file_path)
					# 使用了大小限制，符合大小要求
					else:
						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
						_not_get.append(file_path)
						arcpy.AddMessage("空项目/未添加项：")
						arcpy.AddMessage(os.path.splitext(os.path.basename(file_path))[0])
			else:
				# arcpy.AddMessage(9)
				if file_p[-3:].lower() == suffix:
					# 使用了文件大小限制且不符合大小要求
					if size_limit and os.path.getsize(file_path) != size_limit:
						print type(matchword)
						print matchword
						_getall_items.append(file_path)
					# 没有使用大小限制
					elif not size_limit:
						_getall_items.append(file_path)
					# 使用了大小限制，符合大小要求
					else:
						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
						_not_get.append(file_path)
						arcpy.AddMessage("空项目/未添加项：")
						arcpy.AddMessage(
							os.path.splitext(os.path.basename(file_path))[0])
					# print type(matchword)
					# print matchword
					# __getall_items.append(file_path)
	return _getall_items


dir_path = arcpy.GetParameterAsText(0)
# dir_path = ur"F:\19-20年威远县\威远11-18年\510000高标准农田建设上图入库数据20200702"
match_w = arcpy.GetParameterAsText(1)
# match_w = "GBZ"
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

match_w = str(match_w)
print match_w
print type(match_w)
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

filelist = recur_search(dir_path, "shp",100, matchword=match_w)
count = len(filelist)
count1 = len(_not_get)
arcpy.AddMessage("\n"+"loading...")
for afile in filelist:
	hybag_addshp(afile)
msg1 = str(count)+ " files loaded"
msg2 = str(count1)+ " files not loaded"
arcpy.AddMessage("\n"+msg1)
arcpy.AddMessage(msg2)

# if __name__ == '__main__':
# 	files = hybag_getall_item(
# 		ur"G:\高标准分布图\青川县\510000高标准农田建设上图入库数据20200113","shp","GBZ")
# 	print len(files)
# 	for afile in files:
# 		hybag_addshp(afile)
# 	msg1 = u"{0}个文件加载完成".format(len(files))
# 	print msg1


# filess = hybag_getall_item(ur"G:\高标准分布图\yi经\shp",
# 				  "shp")
# print len(filess)
# print type(filess)
# for afile in filess:
# 	print type(afile)
# 	hybag_addshp(afile)
#
# path1=ur"G:\高标准分布图\yi经\shp"
# print os.path.isfile(path1)
# hybag_addshp(path1)
# hybag_addshp(ur"G:\高标准分布图\江阳\510502江阳区\入库成果数据\510000高标准农田建设上图入库数据20200115\510000CZ20165105022016年财政农业生产发展水稻项目YS\GBZ2016510502CZ2016年财政农业生产发展水稻项目YS.shp")


