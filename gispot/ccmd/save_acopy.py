#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/7 9:34
# Reference:
"""
Description: 将高版本的arcgis另存为低版本
Usage:
"""
# ---------------------------------------------------------------------------
# import arcpy
import os
from hybag import hybase

path = ur"G:\正安县\正安县分布图\成果\标志牌图\新建文件夹 (2)"
suff = "mxd"
path_list = hybase.HBgetfile(path, suff, False)

for i in path_list:
	i_base = os.path.basename(i)
	name = os.path.splitext(i_base)[0]
	new_path = ur"G:\正安县\正安县分布图\成果\标志牌图\新建文件夹"
	# mxd_p =os.path.join(path,i)
	# print mxd_p
	mxd1 = arcpy.mapping.MapDocument(i)
	mxd1.saveACopy(new_path+"\\"+name+".mxd",version="10.1")

