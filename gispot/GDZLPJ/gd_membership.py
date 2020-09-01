#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/1 17:44
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
output_size = "200"
point = ur"G:\耕地质量等级\阿坝19年\耕地质量等级调查点位图.shp" # 一个shp图层
field = "有效磷"
resample_size = "50 50"
# 管理单元_全图斑
manger_cell = ur"G:\耕地质量等级\阿坝19年\管理单元_全图斑.shp" # 一个shp图层
zone_field = "BSMinner" # 区域统计时使用的字段
ignore_nodata = "true" # 是否忽略空值
static_type = "MEAN"
input_link_field = "BSMinner"
output_link_field = "BSMinner"
IDW1 = "%scratchGDB%\\IDW1"
IDW_resample = "%scratchGDB%\\IDW_resample"
db = "%scratchGDB%\\db"
# 结果输出地址
result_path = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\管理单元_全图斑_有效磷lcc"

# Process: 反距离权重法
arcpy.gp.Idw_sa(point, field, IDW1, output_size, "2", "VARIABLE 12", "")

# Process: 重采样
arcpy.Resample_management(IDW1, IDW_resample, resample_size, "NEAREST")

# Process: 以表格显示分区统计
# arcpy.gp.ZonalStatisticsAsTable_sa(管理单元_全图斑, 区域字段, IDW_resample, db, True, "MEAN")
arcpy.sa.ZonalStatisticsAsTable(manger_cell, zone_field, IDW_resample, db, ignore_nodata, static_type)

# Process: 添加连接
arcpy.AddJoin_management(manger_cell, input_link_field, db, output_link_field, "KEEP_ALL")

# Process: 复制要素
arcpy.CopyFeatures_management(manger_cell, result_path, "", "0", "0", "0")
