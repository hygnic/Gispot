# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/5
# python2.7  arcpy arcgis10.3、10.6
"""
练习：
选择shp文件，然后获取其属性字段，制作下拉框

初步结论:
	性能捉急，速度慢
	使用OGP试试
"""

import arcpy

shp_path = ur"Edfdfdf7.shp"

# base = "base.shp"
# arcpy.MakeFeatureLayer_management(shp_path, base)

theFields = arcpy.ListFields(shp_path)
# for i in theFields:
# 	print i
FieldsArray = []
for Field in theFields:
	FieldsArray.append(Field.aliasName)

print FieldsArray
# for row in arcpy.da.SearchCursor(inFC, FieldsArray):
#     print row






