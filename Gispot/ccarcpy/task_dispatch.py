# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/20
# python2 arcgis10.3

import Tkinter as tk
import arcpy
import os

from multiprocessing import Process
from TkGUIconfig import multication
from ccutility import databutcher
import tooltk


def path_detect(path_d):
	"""检测目录是否存在并建立"""
	if not os.path.isdir(path_d):
		os.makedirs(path_d)

# 主功能函数
def main_f(mxd_path, attr_field, outputclass, cooked_dict):
	"""
	以第一个图层为基准图层，选择基准字段；
	对mxd中所有其余图层按 小组分配 进行筛选导出。
	:param para_dict:
	:param mf_queue:
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
	print "get target layer {0}".format(target_lyr)
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
def mian_wrap(mxd_path, attr_field, outputclass,str_mess):
	cooked_dict = databutcher.str2dict(str_mess)
	main_f(mxd_path, attr_field, outputclass,cooked_dict)
	
	
class StartApp(tooltk.Tooltk):
	commu = multication.MuCation()
	
	""""""
	def __init__(self, master_f):
		"""
		:param master_f: mian_f , a widget from tool_entrance.py
		"""
		super(StartApp, self).__init__(master_f,
										"../docs/task_dispatch.gc",
									   self.confirm)
		# block1
		self.single_file_block(
			[(u'地图文档', '*.mxd'), ('All Files', '*')],"mxd"
		)
		# block2
		input_value = tk.StringVar()
		self.single_vari_block(u"选择字段",input_value)
		# block3
		self.single_dir_block(u"输出文件夹")
		# block4
		self.single_text_block(u"分组")
		self.divider_bar_block(
			self.frame_major, color11="#F1F1F1", color22="#F1F1F1"
		)
		# self.help_text.destroy()
		self.window.mainloop()
		
		
	def confirm(self):
		para = self.get_blockvalue(
			self.input_sfb, self.input_svb,
			self.input_sdb, self.input_tb
		)
		print "para: ",para
		print "began!--------------"
		para1 = para[0]
		para2 = para[1]
		para3 = para[2]
		para4 = para[3]
		# dispatch_group_dict = datacooker.str2dict(para4)
		# main_f(para1,para2,para3,dispatch_group_dict)
		p = Process(
			target=mian_wrap,
			args=(para1, para2,
				  para3, para4)
		)
		# p = Process(target=inner_function)
		p.start()
		# self.commu.process_communication(self.text_major_msg)
		
