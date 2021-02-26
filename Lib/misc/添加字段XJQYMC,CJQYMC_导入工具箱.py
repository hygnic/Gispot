#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/7 10:00
# Reference:
"""
Description:快速添加shp文件字段CJQYDM、MC;XJQYDM、MC
Usage: 已经导入自定义工具箱 @村、乡字段添加
"""
# ---------------------------------------------------------------------------
import arcpy
# from ezarcpy import ezlayer
# ezlayer.add_field()
def add_field(layer, names, f_type, f_length):
	"""添加字段
	:param layer:{String} shp文件路径
	:param names:{List} 新增字段名称
	:param f_type: {String} 字段类型
	:param f_length: {Long} 字段长度
	:return: 返回当前的图层对象
	"""
	the_fields = arcpy.ListFields(layer)
	# 当前图层的字段名称列表
	fields_array = []
	for field in the_fields:
		# fields_array.append(field.aliasName)
		fields_array.append(field.name)
	arcpy.AddMessage("\n")
	for name in names:
		if name not in fields_array:
			arcpy.AddField_management(layer, name, f_type, field_length = f_length)
			# arcpy.AddMessage("\n")
			arcpy.AddMessage(name)
	return layer
	
	

if __name__ == '__main__':
	
	in_layer = arcpy.GetParameterAsText(0)
	# 新建字段名称 默认 XJQYMC XJQYDM CJQYDM CJQYMC
	new_names = arcpy.GetParameterAsText(1)
	# new_names = "XJQYMC;XJQYDM;CJQYDM;CJQYMC"
	# 字段长度 默认100
	length = arcpy.GetParameterAsText(2)
	# length = 100
	new_names = new_names.split(";")
	# mxd0 = arcpy.mapping.MapDocument("CURRENT")
	add_field(in_layer,new_names,"TEXT",length)
	
	arcpy.AddMessage("Done")
	arcpy.AddMessage("\n")