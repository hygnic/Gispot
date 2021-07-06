#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/1 17:44
# Reference:
"""
Description: gd_membership 耕地隶属度
根据点文件进行IDW插值（300米），然后重采样到10x10米，进行区域分析获取平均值然后连接属性，
导出并保存为shp文件
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
from hybag import hytime
import arcpy
import os

"""-----------------------------------------------------------------------"""
"""-----------------------------global settings---------------------------"""
"""-----------------------------------------------------------------------"""
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
delete_scratchGDB = False # 是否删除中间数据库
manager_cell = ur"G:\耕地质量等级\阿坝19年\管理单元_全图斑.shp" # 管理单元_全图斑
point = ur"G:\耕地质量等级\阿坝19年\耕地质量等级调查点位图.shp" # 点shp
result_dir = ur"G:\耕地质量等级\阿坝19年\成果090122"  # 结果输出文件夹
fields = ["有机质","海拔高度","土壤容重","有效土","有效磷","速效钾"] # 字段类型得是数字
# print(arcpy.env.scratchGDB) # C:\Users\ADMINI~1\AppData\Local\Temp\scratch.gdb
"""-----------------------------------------------------------------------"""
"""-----------------------------------------------------------------------"""
"""-----------------------------------------------------------------------"""

for a_field in fields:
	# Process: 反距离权重法
	# 处理范围
	arcpy.env.extent = "34361163.3157208 3386128.2038705 34726672.9492604 3799008.23423741"
	# 选择感兴趣区
	arcpy.env.mask = "G:/MoveOn/Gispot/gispot/GDZLPJ/XZQ.shp"
	output_size = "200" # 输出栅格像元大小 200米X200米
	field = a_field
	IDW1 = "%scratchGDB%\\IDW1"
	# IDW1 = "IDW1"
	arcpy.gp.Idw_sa(point, field, IDW1, output_size, "2", "VARIABLE 12", "")
	print("Idw_sa finished")
	
	# Process: 重采样
	resample_size = "10" # 重采样尺寸 米
	IDW_resample = "%scratchGDB%\\IDW_resample" # 重采样输出
	# IDW_resample = "IDW_resample" # 重采样输出
	arcpy.Resample_management(IDW1, IDW_resample, resample_size, "NEAREST")
	print("Resample_management finished")
	
	# Process: 以表格显示分区统计
	zone_field = "BSMinner" # 区域统计时使用的字段
	ignore_nodata = "true" # 是否忽略空值
	static_type = "MEAN" # 选择分区统计的类型
	db = "%scratchGDB%\\db" # 表格输出
	arcpy.sa.ZonalStatisticsAsTable(manager_cell, zone_field, IDW_resample, db, ignore_nodata, static_type)
	print("ZonalStatisticsAsTable finished")
	
	# Process: 添加连接
	input_link_field = "BSMinner" # 要素图层字段
	output_link_field = "BSMinner" # 连接表字段
	manager_cell_feature = "inlayer" # 根据输入要素类或图层文件创建要素图层
	arcpy.MakeFeatureLayer_management(manager_cell, manager_cell_feature)
	arcpy.AddJoin_management(manager_cell_feature, input_link_field, db, output_link_field, "KEEP_ALL")
	
	# Process: 复制要素
	name = field
	arcpy.CopyFeatures_management(manager_cell_feature, os.path.join(result_dir,name))
	print("{0} done".format(name))
	
if delete_scratchGDB:
	arcpy.Delete_management(arcpy.env.scratchGDB)
	print("Delete success")
