#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/20 14:03
# Reference:
"""
Description: 来自于hybag包中base文件中的005函数
*已经导入工具箱
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy

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
	new_ly = "newlayer_945"
	arcpy.Dissolve_management(layer, new_ly ,name)
	arcpy.DeleteField_management(new_ly, name)
	
	return new_ly

if __name__ == '__main__':
	mxd = arcpy.mapping.MapDocument("CURRENT")
	layerr = arcpy.GetParameterAsText(0)
	merger(layerr)