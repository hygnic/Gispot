#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/15 15:03
# Reference:
"""
Description: 修改mxd文档的版本
Usage:
"""
# ---------------------------------------------------------------------------

import arcpy,os,time

path = arcpy.GetParameterAsText(0)
layoutdir = arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True
version = arcpy.GetParameterAsText(2)
print '开始导出:'+str(time.ctime())

for afile in os.listdir(path):
  if afile[-3:].lower()=='mxd':
   mxd=arcpy.mapping.MapDocument(os.path.join(path,afile))
   mxd.saveACopy (layoutdir+'\\'+afile[:-4]+'.mxd',version)
   del mxd
arcpy.AddMessage("OK")
print 'end'+str(time.ctime())
