# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/23
# Python2 arcgis10.6
"""
截断字段并赋值
"""

import arcpy

def split_attribyte():
	mxd1 = arcpy.mapping.MapDocument("CURRENT")
	layer = arcpy.mapping.ListLayers(mxd1)[0]
	with arcpy.da.UpdateCursor(layer,("XZQMC","CJQYMC","XJQYMC")) as cursor:
		for row in cursor:
			split_index = 3
			XJQYMC = row[0][:split_index]
			row[2] = XJQYMC
			# print XJQYMC
			
			CJQYMC = row[0][split_index:]
			row[1] = CJQYMC
			cursor.updateRow(row)
		# cursor.reset()
		arcpy.RefreshActiveView()
		arcpy.RefreshTOC()

split_attribyte()