# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/18

"""
提取面矢量自身的相交线
并拆解多部件
"""
# import arcpy
import os

arcpy.env.overwriteOutput = True


"""
路径和默认空间设置
"""
LQDK_path  = r"D:\农业部汇交1120\宜宾\511521宜宾县-最终-勿删\矢量数据\LQDK5115212019.shp"
# 基本农田路径
JBNTBHTB_path = r"D:\农业部汇交1120\宜宾\511521宜宾县-最终-勿删\矢量数据\JBNTBHTB5115212019.shp"
task_list = [LQDK_path, JBNTBHTB_path]

# 默认工作空间
workspace = r"E:\worksapce_1205"

if not os.path.isdir(workspace):
	os.makedirs(workspace)

arcpy.env.workspace = workspace



base = "base.shp"
for task in task_list:
	main_name = os.path.basename(task)[:4]
	# output_base = os.path.join(workspace, "base")
	# arcpy.MakeFeatureLayer_management(task, "base")
	arcpy.CopyFeatures_management(task, main_name+"base.shp")
	arcpy.Intersect_analysis(main_name+"base.shp", main_name+"_Intersect",
							 "", "", "line")
	arcpy.MultipartToSinglepart_management(main_name+"_Intersect.shp",
										   main_name+"_Intersect_single")
