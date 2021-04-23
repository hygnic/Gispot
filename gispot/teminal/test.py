# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              test
# Author:            Hygnic
# Created on:        2021/4/22 10:28
# Version:           
# Reference:         
"""
Description:         
Usage:               
"""
# -------------------------------------------
import arcpy

arcpy.env.workspace = r"E:\MyD\dem\chengdu\TIF"

arcpy.MosaicToNewRaster_management(
    input_rasters="N31E106.tif;N31E105.tif;N31E104.tif;N31E103.tif;N31E102.tif;N30E107.tif;N30E106.tif;N30E105.tif;N30E104.tif;N30E103.tif;N30E102.tif;N29E107.tif;N29E106.tif;N29E105.tif;N29E104.tif;N29E103.tif;N29E102.tif;N28E107.tif;N28E106.tif;N28E105.tif;N28E104.tif;N28E103.tif;N28E102.tif;N31E107.tif", output_location="E:/doc/Scratch", raster_dataset_name_with_extension="All2.tif", coordinate_system_for_the_raster="", pixel_type="16_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="LAST", mosaic_colormap_mode="FIRST")
    