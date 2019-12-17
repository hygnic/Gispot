# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/17
import os
import arcpy

mxd1_path = "CURRENT"
# layer_name = "XJQY5115212019"
layer_name = "XJQY5203242019"
selected_field = "XJQYDM"
value_list = {
	"group1":[520324102,520324105],
	"group2":[520324106,520324111]
}

mxd1 = arcpy.mapping.MapDocument(mxd1_path)
# 选出作为选择母本的图层
lyr_base = arcpy.mapping.ListLayers(mxd1,layer_name)[0]
base = "base_2"
arcpy.MakeFeatureLayer_management(lyr_base,base)
print value_list["group1"]
print value_list["group1"][1]
print "------------"
for group_name in value_list:
	print group_name # group1
	group_list = value_list[group_name] # group_list: [511521111, 511521105]
	for group_value in group_list:
		print group_value
		# print selected_field+" = '"+str(group_value)+"'" # XJQYDM = '520324102'
		arcpy.SelectLayerByLocation_management(lyr_base,"NEW_SELECTION",
											   "\""+selected_field+ "\" = \'"
											   +str(group_value)+"'")