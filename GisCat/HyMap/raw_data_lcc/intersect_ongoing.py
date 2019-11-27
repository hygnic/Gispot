# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/18

import arcpy
import os

arcpy.env.overwriteOutput = True


"""
路径和默认空间设置
"""
LQDK_path  = r"E:\lcc_test\矢量数据\LQDK5120022017.shp"
# 默认工作空间
workspace_dir = r"E:\worksapce_1"
gdb_name = "scratchoutput.gdb"
try:
	arcpy.CreateFileGDB_management(workspace_dir, gdb_name)
except Exception as e:
	print e
	print "临时数据库被占用"
if not os.path.isdir(workspace_dir):
	os.makedirs(workspace_dir)
workspace_gdb = os.path.join(workspace_dir,gdb_name)

arcpy.env.workspace = workspace_gdb

# 基本农田路径
JBNT_path = r"E:\lcc_test\矢量数据\JBNTBHTB5120022017.shp"

base = "base"

output_base = os.path.join(workspace_gdb, "base")
arcpy.CopyFeatures_management(LQDK_path, output_base)
arcpy.Intersect_analysis("base", "LQDK_Intersect", "", "", "line")
arcpy.MultipartToSinglepart_management("LQDK_Intersect",
                                       "LQDK_Intersect_single")
