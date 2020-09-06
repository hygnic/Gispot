#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/1 17:44
# Reference:
"""
Description: gd_membership 耕地隶属度
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy

"""-----------------------------------------------------------------------"""
"""-----------------------------global settings---------------------------"""
"""-----------------------------------------------------------------------"""
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
"""-----------------------------------------------------------------------"""
"""-----------------------------------------------------------------------"""
"""-----------------------------------------------------------------------"""


manager_cell = ur"G:\耕地质量等级\阿坝19年\管理单元_全图斑.shp" # 管理单元_全图斑

# Process: 反距离权重法
output_size = "200" # 输出栅格像元大小 200米X200米
point = ur"G:\耕地质量等级\阿坝19年\耕地质量等级调查点位图.shp"
field = "有效磷"
IDW1 = "%scratchGDB%\\IDW1"
arcpy.gp.Idw_sa(point, field, IDW1, output_size, "2", "VARIABLE 12", "")

# Process: 重采样
resample_size = "50 50" # 重采样尺寸 米
IDW_resample = "%scratchGDB%\\IDW_resample" # 重采样输出
arcpy.Resample_management(IDW1, IDW_resample, resample_size, "NEAREST")

# Process: 以表格显示分区统计
zone_field = "BSMinner" # 区域统计时使用的字段
ignore_nodata = "true" # 是否忽略空值
static_type = "MEAN" # 选择分区统计的类型
db = "%scratchGDB%\\db" # 表格输出
arcpy.sa.ZonalStatisticsAsTable(manager_cell, zone_field, IDW_resample, db, ignore_nodata, static_type)

# Process: 添加连接
input_link_field = "BSMinner" # 要素图层字段
output_link_field = "BSMinner" # 连接表字段
manager_cell_feature = "inlayer" # 根据输入要素类或图层文件创建要素图层
arcpy.MakeFeatureLayer_management(manager_cell, manager_cell_feature)
arcpy.AddJoin_management(manager_cell_feature, input_link_field, db, output_link_field, "KEEP_ALL")

# Process: 复制要素
result_path = r"G:\MoveOn\Gispot\gispot\GDZLPJ\we.shp" # 结果输出地址
arcpy.CopyFeatures_management(manager_cell_feature, result_path)


"""-----------------------------------------------------------------------"""
"""-----------------------------test--------------------------------------"""
"""-----------------------------------------------------------------------"""

if __name__ == '__main__':
	pass
