#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/11/19 19:21
# Reference:
"""
Description: 读取高标准复核数据库，统计生成各项目在各个村的建设面积情况
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os
from hybag import hybasic
import pandas as pd

# 设置数据库位置
dbase = ur"G:\跑村面积\510181都江堰市"



gbzs_path = os.path.join(dbase, u"入库成果数据")
CJQY_path = os.path.join(dbase, u"底图数据")


# 入库成果数据
database = ur"G:\跑村面积\510181都江堰市\入库成果数据\510000高标准农田建设上图入库数据20200625"

"""----------获取GBZ shapefile----------------------"""
gbzs = hybasic.getfiles(gbzs_path,"shp")
gbzs = hybasic.HBfilter(gbzs,"GBZ",size_limit=0)
"""----------获取GBZ shapefile----------------------"""

"""----------获取CJQY shapefile----------------------"""
cjqy = hybasic.getfiles(CJQY_path,"shp",recur=False)
cjqy = hybasic.HBfilter(cjqy,"XZQ",size_limit=0)[0]
"""----------获取CJQY shapefile----------------------"""



cjqy_f = "cjqy.shp"
gbz_f = "gbz.shp"
# 建立垃圾数据库
tempDB = u'scrath.gdb'
arcpy.env.overwriteOutput = True
scrath = os.path.join(dbase,tempDB)
if not os.path.isdir(scrath):
	arcpy.CreateFileGDB_management(dbase,tempDB)
arcpy.env.workspace = scrath

print "合并"
merge = "merge"
arcpy.Merge_management(gbzs,merge)
cjqy_j = "cjqy_j"
arcpy.MakeFeatureLayer_management(cjqy, cjqy_f)
print "处理"
arcpy.SpatialJoin_analysis(merge, cjqy_f, cjqy_j, match_option="WITHIN")
print 'ok'


# with arcpy.da.UpdateCursor(cjqy_j, "XZQMC") as cursor:
# 	for row in cursor:
# 		print row[0]
arr = arcpy.da.TableToNumPyArray(cjqy_j, ("XZQMC", "XZQDM","DIKUAIAREA","XMMC","ZLDJ"))

df = pd.DataFrame(arr)
print df

