#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/21 14:31
# Reference:
"""
Description: 第三次高标复核修改计算质量等级
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
from shutil import copyfile
import os
from multiprocessing import Process
from hybag import ezarcpy
from hybag import hybasic
import tooltk
from GUIconfig import multication


arcpy.env.overwriteOutput =True
"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
# 测试路径
# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\test"
folder_path = ur"G:\MoveOn\Gispot\Local\test_name\510000高标准农田建设上图入库数据20200114"
# 测试路径
dltb_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\底图数据\DLTB5114002018.shp"
excel_path= ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\附表：“十二五”以来高标准农田建设评估复核修正统计表.xlsx"
"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
scratch_path = ezarcpy.initialize_environment()[0]
scratch_gdb = ezarcpy.initialize_environment()[1]



merge_layer = scratch_gdb+ "/merge1"
out_feature_class = scratch_gdb + "/dissolve_layer"
arcpy.Dissolve_management(merge_layer, out_feature_class, "ZLDJ")

# 按属性选择
arcpy.Delete_management(out_data, "")
arcpy.MakeFeatureLayer_management(out_feature_class, "lyr")
# 可能部分质量等级没有
arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " 'ZLDJ' = '符合' ")
# 加了 U 报错
# arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " 'ZLDJ' = u'符合' ")
arcpy.CopyFeatures_management("lyr", "fuhe")
arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " 'ZLDJ' = '基本符合' ")
arcpy.CopyFeatures_management("lyr", "jibenfuhe")
arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " 'ZLDJ' = '需要提质改造' ")
arcpy.CopyFeatures_management("lyr", "xytzgz")
print u"分离质量等级成功"


