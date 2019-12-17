# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/17
# python2 arcgis 10.3

import arcpy

mxd1_path = ur"D:\农业部汇交1120\宜宾\1217.mxd"
layer_name = "XJQY5115212019"
selected_field = "XJQYDM"
value_list = {
	"group1":[511521111,511521105],
	"group2":[511521202,511521107]
}
mxd1 = arcpy.mapping.MapDocument(mxd1_path)
# 选出作为选择母本的图层
lyr_base = arcpy.mapping.ListLayers(mxd1,layer_name)[0]
arcpy.MakeFeatureLayer_management(lyr_base,"base")
print value_list["group1"]
print value_list["group1"][1]
print "------------"
for group_name in value_list:
	print group_name # group1
	group_list = value_list[group_name] # group_list: [511521111, 511521105]
	for group_value in group_list:
		print group_value
		arcpy.SelectLayerByLocation_management("base","NEW_SELECTION",
											   selected_field," = ")
