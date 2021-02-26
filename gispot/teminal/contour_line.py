#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/9 22:51
# Reference:
"""
Description: 复杂的多边形（内部环岛孔洞等）在显示轮廓线时显得非常的乱和臃肿；本工具的作用就是仅仅在
            复杂多边形的外部生成轮廓。
            该方法生成的轮廓线较原始的美观
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
import arcpy
from hybag import ezarcpy

workpath, workgdb = ezarcpy.InitPath()
arcpy.env.overwriteOutput =True
arcpy.env.workspace =workgdb

def better_contour(inputclass, outputclass):
    print("inputclass", inputclass)
    print("outputclass", outputclass)
    arcpy.Merge_management(inputclass, "in_memory/after_merge")
    ezarcpy.merger_all("in_memory/after_merge", "in_memory/after_diss_all")
    arcpy.Delete_management("in_memory/after_merge")
    print("merge all")
    arcpy.EliminatePolygonPart_management ("in_memory/after_diss_all", "in_memory/after_eli", "AREA", 1000000, part_option="CONTAINED_ONLY" )
    arcpy.Delete_management("in_memory/after_diss_all")
    print("create contour")
    arcpy.SimplifyPolygon_cartography ("in_memory/after_eli", outputclass, algorithm="POINT_REMOVE", tolerance = 1, error_option="NO_CHECK" , collapsed_point_option="NO_KEEP")
    print("complete")
    
better_contour(
    [ur"H:\杂项\2021杂项\威远县/base.gdb/GBZ"
     
     ], "cl22")

# if __name__ == '__main__':
#     gdb_path = "G:\MoveOn\mapping/v103/base.gdb"
#     filenames = [filename for _, _, filename in arcpy.da.Walk(gdb_path, datatype="FeatureClass")]
#     filenames = filenames[0]
#     for i in filenames:
#         print(i)