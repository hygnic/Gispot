#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/3/26 14:48
"""
Description:
1.为什么写批量融合，明明就有；因为自带的工具在批量融合导出文件时，
无法统一指定名称和存储位置
2.批量融合，输出文件名称不变
	注意事项
	1.	批量融合的图层不能置于图层组中
Usage:
已经导入
"""
# ---------------------------------------------------------------------------
import arcpy

# 多选;输入;要素图层
in_f  =arcpy.GetParameterAsText(0)
# 输出文件夹
output_dir = arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True
arcpy.env.workspace = output_dir
arcpy.AddMessage("\n")
# 拆散组成列表
in_f = in_f.split(";")
count = 1 # 计数
for feature in in_f:
	arcpy.AddMessage(str(count)+" "+feature)
	arcpy.Dissolve_management(feature,
							  feature,
							  ["XMMC"], "", "MULTI_PART",
							  "DISSOLVE_LINES")
	count+=1
arcpy.AddMessage("\n")


