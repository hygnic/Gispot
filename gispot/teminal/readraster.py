# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              readraster
# Author:            Hygnic
# Created on:        2021/4/19 23:31
# Version:           
# Reference:         
"""
Description:         将Hgt文件转换为栅格
Usage:               
"""
# -------------------------------------------
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import arcpy


arcpy.env.workspace = r"E:\MyD\dem\chengdu\t"
arcpy.env.overwriteOutput = True


class HGT2TIF(object):
    
    def __init__(self, hgt):
        self.hgt = hgt
        
        # function
        self.convert()

    def convert(self):
        raster = arcpy.Raster(self.hgt)
        name =  os.path.basename(self.hgt) # N28E104.hgt
        purename = os.path.splitext(name)[0]
        raster.save("{}.tif".format(purename))
        
        
if __name__ == '__main__':
    dir_path = r"E:\MyD\dem\chengdu\H48"
    hgt_files = os.listdir(dir_path)
    for hgt in hgt_files:
        hgt_path = os.path.join(dir_path, hgt)
        HGT2TIF(hgt_path)
    
    # 单个
    # HGT2TIF(r"E:\MyD\dem\chengdu\H48\N28E104.hgt")