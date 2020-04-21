#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/20 9:54
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy

mxd1 = arcpy.mapping.MapDocument("CURRENT")
layer = arcpy.mapping.ListLayers(mxd1)[0]
DLMC_list = []
cursor = arcpy.da.UpdateCursor(layer, "NEW_DLMC")
cursor.reset()
for row in cursor:
	row[0] = "旱地"
	cursor.updateRow(row)
del cursor
arcpy.RefreshTOC()
arcpy.RefreshActiveView()

def getvalue_from_attribute(mxd_document, static, name):
	# 获取shp属性表中所有相同值的和，比如获取一个同一个乡镇下，所有TBDLMJ的和
	"""
	area: 统计面积  name: 名称
	"""
	mxd = mxd_document
	field_list = [static, name]
	layerrrr = arcpy.mapping.ListLayers(mxd)[-2]
	with arcpy.da.UpdateCursor(layerrrr, field_list) as cursorr:
		name=None
		value_list=[]
		# get the names with list format
		for rowww in cursorr:
			if rowww[1] not in value_list:
				value_list.append(rowww[1])
		cursorr.reset()
		for name in value_list:
			mj = 0
			# cursor 只能遍历一次
			for roww in cursorr:
				if name == roww[1]:
					tbdlmj = float(roww[0])
					mj += round(tbdlmj * 0.0015, 4)
					# mj+=roww[0]
			
			msgg = name + "," + str(mj) + "\n"
			arcpy.AddMessage(msgg)
			cursorr.reset()
getvalue_from_attribute(mxd1,"SHAPE@AREA","NEW_DLMC")