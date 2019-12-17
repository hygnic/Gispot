# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/17
# python2 arcgis 10.3

# s_t =  time.clock()
# e_t =  time.clock()
# print str(e_t-s_t)


import os
import arcpy
import time

arcpy.env.overwriteOutput = True

# mxd1_path = ur"D:\农业部汇交1120\宜宾\1217.mxd"
mxd1_path = ur"E:\move on move on\正安县\测试.mxd"
# layer_name = "XJQY5115212019"
layer_name = "XJQY5203242019"
selected_field = "XJQYDM"
# value_list = {
# 	"group1":[511521111,511521105],
# 	"group2":[511521202,511521107]
# }
value_list = {
	"group1":[520324102,520324105],
	"group2":[520324106,520324111]
}

mxd1 = arcpy.mapping.MapDocument(mxd1_path)
# 选出作为选择母本的图层
lyr_base = arcpy.mapping.ListLayers(mxd1,layer_name)[0]
arcpy.MakeFeatureLayer_management(lyr_base,"base")
print value_list["group1"]
print value_list["group1"][1]
print "------------"
sp = "E:\move on move on\正安县"
for group_name in value_list:
	print group_name # group1
	group_list = value_list[group_name] # group_list: [511521111, 511521105]
	for group_value in group_list: # 511521111
		print group_value
		# print selected_field+" = '"+str(group_value)+"'" # XJQYDM = '520324102'
		arcpy.SelectLayerByAttribute_management(lyr_base,"ADD_TO_SELECTION",
											   "\""+selected_field+ "\"= \'"
											   +str(group_value)+"'")

	mxd1.saveACopy(sp+'/'+str(group_name)+".mxd")
	lyr_base.setSelectionSet("NEW",[])
	print "okkk"
	
def _output_lyr(selector,layerlist):
	"""
	示例：根据从XJQY中选择好的乡镇为范围，将其他图层导出
	:param selector 用于选择的图层，比如XJQY
	:param layerlist: 余下图层的列表
	:return:
	"""
	for o_layer in layerlist:
	
	