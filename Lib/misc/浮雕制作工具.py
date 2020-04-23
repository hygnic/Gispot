#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/22 16:44
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy

# Check out any necessary licenses
# arcpy.CheckOutExtension("spatial")

# Script arguments
lyrr = arcpy.GetParameterAsText(0)
lyrr
distance_orfield = arcpy.GetParameterAsText(1)

# output_raster = arcpy.GetParameterAsText(2)

out = "inner_buffer"
arcpy.Buffer_analysis(lyrr, out, distance_orfield, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: 欧氏距离
# tempEnvironment0 = arcpy.env.extent
# arcpy.env.extent = ""


# arcpy.gp.EucDistance_sa("inner_buffer", "euc_distance", "", "", "")
# # arcpy.env.extent = tempEnvironment0
#
# # Process: 裁剪
# arcpy.Clip_management( "euc_distance", "", "clip_raster", lyrr, "", True, False)
#
# # Process: 山体阴影
# arcpy.gp.HillShade_sa("clip_raster", output_raster, "315", "45", "NO_SHADOWS", "1")


arcpy.RefreshActiveView()
arcpy.RefreshTOC()