#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/27 9:56
# Reference:
"""
Description:已经导入arcgis
Usage:
"""
# ---------------------------------------------------------------------------
# import arcpy

features_str = arcpy.GetParameterAsText(0)
out_dir = arcpy.GetParameterAsText(1)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = out_dir
mxd = arcpy.mapping.MapDocument("CURRENT")
features = features_str.split(";")
# 获取图层名
for feature in features:
	# 转换为图层对象
	lyr = arcpy.mapping.Layer(feature)
	real_name =lyr.name # 获取内容列表的名字
	arcpy.AddMessage(real_name)
	arcpy.CopyFeatures_management(lyr, real_name)
	