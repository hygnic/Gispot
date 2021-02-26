#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/15 10:53
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# import arcpy
from hybag import ezarcpy

# def add_field(layer, names, f_type, f_length):
# 	"""添加相同类型和长度的多个或者单个字段
# 	:param layer:{String} shp文件路径
# 	  #TODO 按理应该可以使用图层对象，arcpy.mapping.Layer(path)，但是报错（arcgis10.3）
# 	:param names:{List} 新增字段名称
# 	:param f_type: {String} 字段类型
# 	:param f_length: {Long} 字段长度
# 	:return: 返回当前的图层对象
# 	"""
# 	the_fields = arcpy.ListFields(layer)
# 	# 当前图层的字段名称列表
# 	fields_array = []
# 	for field in the_fields:
# 		# fields_array.append(field.aliasName)
# 		fields_array.append(field.name)
# 	arcpy.AddMessage("\n")
# 	for name in names:
# 		if name not in fields_array:
# 			arcpy.AddField_management(layer, name, f_type,
# 									  field_length=f_length)
# 			# arcpy.AddMessage("\n")
# 			arcpy.AddMessage(name)
# 	return layer
#
#
# def setZWMC(layer, reference_field, target_field1, target_field2):
# 	"""根据LQDK图层中的LQLX字段赋予ZZMC1和ZZMC2
# 	  such as: setZWMC(layer, "LQLX", "ZWMC1", "ZWMC2")
# 	:param layer: 图层对象或者shp文件路径
# 	:param reference_field: LQLX字段
# 	:param target_field1: ZZMC1
# 	:param target_field2: ZZMC2
# 	:return:
# 	"""
# 	in_fields = (reference_field, target_field1, target_field2)
# 	# LQLX匹配规则，LQLX代码表示的作物名称
# 	match_list = {
# 		11: (u"水稻", u""),
# 		12: (u"小麦", u""),
# 		13: (u"水稻", u"小麦"),
# 		14: (u"玉米", u""),
# 		15: (u"小麦", u"玉米"),
# 		25: (u"水稻", u"油菜")
# 	}
# 	with arcpy.da.UpdateCursor(layer, in_fields) as cursor:
# 		for row in cursor:
# 			LQLX = row[0]
# 			# match_list = match_list.iteritems()
# 			for m_key in match_list:
# 				if int(LQLX) == m_key:
# 					# print "LQLX:",LQLX
# 					# print "match_list.get:",match_list.get(m_key)[0]
# 					# print "type:",type(match_list.get(m_key)[0])
# 					# print "row[1]:",type(row[1])
# 					row[1] = match_list.get(m_key)[0]
# 					row[2] = match_list.get(m_key)[1]
# 					cursor.updateRow(row)
# 				else:
# 					print "no match"


if __name__ == '__main__':
	layer_p = ur"G:\内江市\工作文件_lcc_19_7\内江出图\基本数据\0615新DK、PK\LQDK5110022019.shp"
	# mxd_layer = arcpy.mapping.Layer(layer_p)
	new_layer = ezarcpy.add_field(layer_p, ["ZWMC1", "ZWMC2"], "TEXT", 50)
	ezarcpy.setZWMC(layer_p, "LQLX", "ZWMC1", "ZWMC2")
	# ezlayer.setZWMC(new_layer,"LQLX","ZWMC1","ZWMC2")
	print "close"