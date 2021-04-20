#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/4/8 19:24
# Reference: https://gis.stackexchange.com/questions/124987/add-cad-feature-class-to-arcgis-using-arcpy
"""
Description: 使用 arcpy 打开 CAD 文件然后将其文件导出
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os
from hybag import ezarcpy

mxd_p = "path"

class CAD2Shp(object):
    # def __init__(self, mxd, cad,output):
    def __init__(self, cad):
        
        # self.output = output
        self.cad = cad
        # self.m = arcpy.mapping.MapDocument(mxd)
        # self.df = arcpy.mapping.ListDataFrames(self.m)[0]
        self.convert()
        
        
    def convert(self):
        
        pt = arcpy.mapping.Layer(self.cad+"\Point")
        pl = arcpy.mapping.Layer(self.cad+"\Polyline")
        pg = arcpy.mapping.Layer(self.cad+"\Polygon")
        # 使用 CopyFeatures_management 前设置默认工作路径，不然会报错
        arcpy.CopyFeatures_management(pl, "er")


#
# df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
# addPoint = arcpy.mapping.Layer(r"C:\Temp\my.dwg\Point") # reference to point layer
# addPolyline = arcpy.mapping.Layer(r"C:\Temp\my.dwg\Polyline") # reference to Polyline layer
# arcpy.mapping.AddLayer(df, addPoint, "BOTTOM")
# arcpy.mapping.AddLayer(df, addPolyline, "BOTTOM")

if __name__ == '__main__':
    # arcpy.env.workspace = ezarcpy.InitPath()[-1]
    arcpy.env.workspace = os.getcwd()
    CAD2Shp(u"设计图.dwg")