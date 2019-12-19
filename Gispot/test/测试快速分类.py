# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/17
# python2 arcgis 10.3

# s_t =  time.clock()
# e_t =  time.clock()
# print str(e_t-s_t)


import os
import arcpy


def path_detect(path_d):
	"""检测目录是否存在并建立"""
	if not os.path.isdir(path_d):
		os.makedirs(path_d)

arcpy.env.overwriteOutput = True

mxd1_path = ur"D:\test\1217.mxd"
# mxd1_path = ur"E:\move on move on\正安县\测试.mxd"
output_dir = os.path.abspath(os.path.dirname(mxd1_path))

mxd_layer = "XJQY5115212019"
# layer_inmxd = "XJQY5203242019"
selected_field = "XJQYDM"
group_dict = {
	"group1":["511521111","511521105"],
	"group2":["511521202","511521107"]
}

# value_list = {
# 	"group1":[520324102,520324105],
# 	"group2":[520324106,520324111]
# }

mxd1 = arcpy.mapping.MapDocument(mxd1_path)
# 选出作为选择母本的图层
raw_layers = arcpy.mapping.ListLayers(mxd1)
cooked_layers = []
for lyr in raw_layers:
	if lyr.name == mxd_layer:
		print "find!"
		target_lyr = lyr
		print "Get {0} layer!".format(mxd_layer)
	else:
		cooked_layers.append(lyr)
		
	
arcpy.MakeFeatureLayer_management(target_lyr,"base")
# print group_dict["group1"]
# print group_dict["group1"][1]
# print "------------"

for group_name in group_dict:
	# print group_name # group1
	group_list = group_dict[group_name] # group_list: [511521111, 511521105]
	for group_value in group_list: # group_value: 511521111
		# print selected_field+" = '"+str(group_value)+"'" # XJQYDM = '520324102'
		arcpy.SelectLayerByAttribute_management(
			target_lyr, "ADD_TO_SELECTION",
			"\"" + selected_field + "\"= \'"
			+ group_value + "'"
		)
		# 对 其余图层 进行选择操作
		# 将一个 group列表中的所有限制条
		for o_layer in cooked_layers:
			arcpy.SelectLayerByLocation_management(
				o_layer, "WITHIN", target_lyr,
				selection_type="ADD_TO_SELECTION"
			)
	group_dir = os.path.join(output_dir,group_name) # D:\test\group1
	# establish dir
	path_detect(group_dir)
	# export shapefile of every layer
	for o_layer in cooked_layers:
		group_filename = os.path.join(group_dir,o_layer.name) # D:\test\group1\CJQY5115212019.shp
		try:
			arcpy.CopyFeatures_management(o_layer,group_filename)
			o_layer.setSelectionSet("NEW",[])
		except Exception as e:
			print e.message
		else:
			print u"保存 {0}".format(o_layer.name)
		
	# mxd1.saveACopy(output_dir + '/' + str(group_name) + ".mxd")
	target_lyr.setSelectionSet("NEW",[])
	print "{0} Done!".format(group_name)