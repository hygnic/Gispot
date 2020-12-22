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
import os
# import arcpy

# shp_path = ur"D:\农业部汇交1120\宜宾\511521宜宾县-最终-勿删\矢量数据\CJQY5115212019.shp"
shp_path = ur"E:\天府新区新津_new\510122天府新区\矢量数据\CJQY5101222017.shp"

print u"文件是否存在:", os.path.exists(shp_path)
# base = "base.shp"
# arcpy.MakeFeatureLayer_management(shp_path, base)
#
# theFields = arcpy.ListFields(shp_path)
# print theFields
# for i in theFields:
# 	print i # <geoprocessing describe field object object at 0x0617FCB0>
# FieldsArray = []
# for Field in theFields:
# 	FieldsArray.append(Field.aliasName)
#
# print FieldsArray
# # for row in arcpy.da.SearchCursor(inFC, FieldsArray):
# #     print row


with arcpy.da.SearchCursor(shp_path,"FID") as cursor:
	for row in cursor:
		print row[0]



