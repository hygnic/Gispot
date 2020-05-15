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
import arcpy
import os

path = ur"G:\高标准分布图\东坡"
list_p = os.listdir(path)
for i in list_p:
	if i[-3:].lower() == "mxd":
		new_path = ur"G:\高标准分布图\东坡\10.3"
		mxd_p =os.path.join(path,i)
		print mxd_p
		mxd1 = arcpy.mapping.MapDocument(mxd_p)
		name = i[:-4]
		mxd1.saveACopy(new_path+"\\"+name+".mxd",version="10.1")

