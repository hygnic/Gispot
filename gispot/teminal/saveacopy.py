# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              saveacopy
# Author:            Hygnic
# Created on:        2021/5/13 9:25
# Version:           AecGIS10.3 Python2.7.8
# Reference:         
"""
Description:         重命名多个图层的名称
Usage:               
"""
# -------------------------------------------
from __future__ import unicode_literals
from __future__ import absolute_import
import arcpy
import os

cws = os.getcwd()
new_path = os.path.join(cws, "temp")
mxds = [x for x in os.listdir(cws) if x[-3:] == "mxd"]

for item in mxds:
    name, suff = os.path.splitext(item)
    print name
    name = name.decode("cp936")
    mxd = arcpy.mapping.MapDocument(os.path.join(cws, item))
    mxd.saveACopy(name+"9.3.mxd", version="9.3")
    # mxd.saveACopy(os.path.join(new_path,item), version="10.3")
    del mxd