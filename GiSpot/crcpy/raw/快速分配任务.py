# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/17
# python2 arcgis 10.3

# s_t =  time.clock()
# e_t =  time.clock()
# print str(e_t-s_t)
"""
功能概述：
	快速分配任务，比如可以自动将一个mxd文档中的图层分开，
	分别保存到文件夹中。
	<--> crcpy/task_dispatch.py
"""


import os
import arcpy

from ccutility import databutcher


def path_detect(path_d):
	"""检测目录是否存在并建立"""
	if not os.path.isdir(path_d):
		os.makedirs(path_d)


def main_f(mxd_path, attr_field, outputclass, cooked_dict):
	"""
	以第一个图层为基准图层，选择基准字段；
	对mxd中所有其余图层按 小组分配 进行筛选导出。
	:param attr_field: 用作分组属性字段值 基准字段
	:param mxd_path: mxd文档
	:param outputclass: 输出位置
	:param cooked_dict: 处理后的字典，包含分组信息
	:return:
	"""
	arcpy.env.overwriteOutput = True
	
	mxd1 = arcpy.mapping.MapDocument(mxd_path)
	# 选出作为选择母本的图层
	raw_layers = arcpy.mapping.ListLayers(mxd1)
	target_lyr = raw_layers.pop(0)
	msgg1 = "get target layer {0}".format(target_lyr)
	print msgg1
	# 将其余图层放进列表
	left_layers = raw_layers
	# print left_layers
	arcpy.MakeFeatureLayer_management(target_lyr, "base")
	# print cooked_dict["group1"]
	# print cooked_dict["group1"][1]
	# print "------------"
	for group_name in cooked_dict:
		# print group_name # group1
		group_list = cooked_dict[
			group_name]  # group_list: [511521111, 511521105]
		for group_value in group_list:  # group_value: 511521111
			# print attr_field+" = '"+str(group_value)+"'" # XJQYDM = '520324102'
			arcpy.SelectLayerByAttribute_management(
				target_lyr, "ADD_TO_SELECTION",
				"\"" + attr_field + "\"= \'"
				+ group_value + "'"
			)
			# 对 其余图层 进行选择操作
			# 将一个 group列表中的所有限制条
			for o_layer in left_layers:
				arcpy.SelectLayerByLocation_management(
					o_layer, "WITHIN", target_lyr,
					selection_type="ADD_TO_SELECTION"
				)
		group_dir = os.path.join(outputclass, group_name)  # D:\test\group1
		# establish dir
		path_detect(group_dir)
		# export shapefile of every layer
		for o_layer in left_layers:
			group_filename = os.path.join(group_dir,
										  o_layer.name)  # D:\test\group1\CJQY5115212019.shp
			try:
				arcpy.CopyFeatures_management(o_layer, group_filename)
				o_layer.setSelectionSet("NEW", [])
			except Exception as e:
				print e.message
			else:
				print u"保存 {0}".format(o_layer.name)
		
		# mxd1.saveACopy(outputclass + '/' + str(group_name) + ".mxd")
		target_lyr.setSelectionSet("NEW", [])
		print "{0} Done!".format(group_name)


# 主功能函数的外包装饰函数
def mian_wrap(mxd_path, attr_field, outputclass, str_mess):
	"""
	该功能将分组数据的处理、和我们的主功能函数合并放到一个函数中，
	然后启动一个子进程处理。
	"""
	cooked_dict = databutcher.str2dict(str_mess)
	main_f(mxd_path, attr_field, outputclass, cooked_dict)
	
if __name__ == '__main__':
	# mxd1_path = ur"D:\test\1217.mxd"
	mxd1_path = ur"E:\move on move on\正安县\测试.mxd"
	# group_dict = {
	# 	"group1":["511521111","511521105"],
	# 	"group2":["511521202","511521107"]
	# }
	group_dict = {
		"group1":["520324102","520324105"],
		"group2":["520324106","520324111"]
	}
	output_dir = os.path.abspath(os.path.dirname(mxd1_path))
	field = "XJQYDM"
	main_f(mxd1_path,field,output_dir,group_dict)