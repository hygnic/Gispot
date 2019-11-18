# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/17

import arcpy
import os

# 两区地块数据

arcpy.env.overwriteOutput = True
LQDK_path  = r"E:\天府新区新津_new\510122天府新区\矢量数据\LQDK5101222017.shp"
# 输出文件夹
output_dir = r"E:\天府新区新津_new\out"
# 村级区域
CJQY_path = r"E:\天府新区新津_new\510122天府新区\矢量数据\CJQY5101222017.shp"

gdb_name = "scratchoutput.gdb"
try:
	arcpy.CreateFileGDB_management(output_dir,gdb_name)
except Exception as e:
	print e
	print "临时数据库被占用"
print "GDB"
# Set the scratchWorkspace environment to local file geodatabase
work_gdb = os.path.join(output_dir,gdb_name)
arcpy.env.workspace = work_gdb
arcpy.MakeFeatureLayer_management(LQDK_path,"base")

# 读取LQLX字段属性并去重
# fields = arcpy.ListFields(LQDK_path)
fields_array = []
for row in arcpy.da.SearchCursor("base", "LQLX"):
	fields_array.append(row[0])
LQLX_fields = list(set(fields_array))
print LQLX_fields # [u'11', u'25', u'14']
# arcpy.CopyFeatures_management("base", os.path.join(work_gdb, "xxx"+ ".shp"))
# 根据LQLX不同导出的图层
agg_layers = []
for LQLX_field in LQLX_fields:
	print LQLX_field # 11
	arcpy.SelectLayerByAttribute_management("base", 'NEW_SELECTION',
									"\"LQLX\" = \'" + LQLX_field +"'")
	# arcpy.MakeFeatureLayer_management("base","base1")
	outFeatureClass = os.path.join(output_dir, str(LQLX_field))
	arcpy.CopyFeatures_management("base",
									  outFeatureClass)
	# 筛选，创建
	LQLX_shp = str(LQLX_field)
	arcpy.MakeFeatureLayer_management("base",LQLX_shp)
	agg_layers.append(LQLX_shp+".shp")
	
# barrier_features = []
# barrier_features = agg_layers.copy()
# 障碍图层

# barrier_features = agg_layers[:]
# # 进行聚合处理
# barrier_features.append(CJQY_path)
# print barrier_features
# for agg_layer in agg_layers:
# 	print agg_layer+ " run agg!"
# 	arcpy.AggregatePolygons_cartography(agg_layer,"Agg" + agg_layer + ".shp","20 Meters",
# 									"","","",
# 									barrier_features,"")
	# outFeatureClass = os.path.join(work_gdb, "Agg" + agg_layer + ".shp")
	# arcpy.CopyFeatures_management("base", outFeatureClass)

# outFeatureClass = os.path.join(work_gdb, "LQLX "+str(LQLX_field)+".shp")
# arcpy.CopyFeatures_management("base",outFeatureClass)



