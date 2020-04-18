#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/7 10:00
# Reference:
"""
Description:快速添加CJQYDM、MC;XJQYDM、MC
Usage: 已经导入自定义工具箱 @村、乡字段添加
"""
# ---------------------------------------------------------------------------
import arcpy

layer = arcpy.GetParameterAsText(0)
# 新建字段名称 默认 XJQYMC XJQYDM CJQYDM CJQYMC
new_names = arcpy.GetParameterAsText(1)
# new_names = "XJQYMC;XJQYDM;CJQYDM;CJQYMC"
# 字段长度 默认100
length = arcpy.GetParameterAsText(2)
# length = 100


mxd0 = arcpy.mapping.MapDocument("CURRENT")
# layer = arcpy.mapping.ListLayers(mxd0)[0]
the_fields = arcpy.ListFields(layer)
# 当前图层的字段名称列表
fields_array = []
for field in the_fields:
	fields_array.append(field.aliasName)
arcpy.AddMessage("\n")
new_names = new_names.split(";")
for new_name in new_names:
	if new_name not in fields_array:
		arcpy.AddField_management(layer,new_name,"TEXT",field_length = length)
		# arcpy.AddMessage("\n")
		arcpy.AddMessage(new_name)
	

arcpy.AddMessage("Done")
arcpy.AddMessage("\n")

