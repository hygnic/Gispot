# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20


import arcpy
import os

arcpy.env.overwriteOutput = True


LQDK_path = r"E:\中江县\xxx\DK_擦除后_laji.shp"
LQDK_pat2 = r"E:\中江县\xxx\DK_2.shp"

arcpy.MultipartToSinglepart_management(LQDK_path,LQDK_pat2)

