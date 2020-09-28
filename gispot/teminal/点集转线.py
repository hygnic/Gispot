#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/28 9:21
# Reference:
"""
Description: 实现arcgis中的一个功能
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os

# 创建文件夹
# scratch_folder = "scratchfolder"
# if not os.path.isdir(scratch_folder):
# 	os.mkdir(scratch_folder)
# arcpy.env.workspace = scratch_folder

"""--------------------------------------创建数据库--------------------------"""
"""-------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------"""
# make dir
from hybag import ezarcpy
"""-------------------------------------------------------------------------"""
scratch_path = ezarcpy.initialize_environment()[0]
scratch_gdb = ezarcpy.initialize_environment()[1]

inFeatures = os.path.join(scratch_path ,"Export_Output.shp") # 必须要有后缀
outFeatures = os.path.join(scratch_gdb ,"line")
# 点集转线
arcpy.PointsToLine_management(inFeatures, outFeatures)
