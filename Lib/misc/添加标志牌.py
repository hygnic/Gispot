#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/5 13:38
# Reference:
"""
Description: 快速添加标志牌shp,设置定义查询
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os
from hybag import hybase

# BZP = ur"G:\古蔺县\古蔺县分布图\古蔺县标志牌点位-旭普.shp"
# pathp=ur"G:\古蔺县\古蔺县分布图\成果\永乐镇.mxd"

def labelsetting(layer):
	if layer.supports("LABELCLASSES"):
		layer.showLabels = True
		for lblClass in layer.labelClasses:
			lblClass.expression = "\"<CLR red=\'255\'><FNT size = \'18\'>\" + [BZPBH] + \"</FNT></CLR>\""
	# print "Class Name:  " + lblClass.className
	# print "Expression:  " + lblClass.expression
	# print "SQL Query:   " + lblClass.SQLQuery


def main(mxdpath):
	mxd = arcpy.mapping.MapDocument(mxdpath)
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	
	BZP_layer = arcpy.mapping.ListLayers(mxd, u"*标志牌*", df)[0]
	XZ_zhudi = arcpy.mapping.ListLayers(mxd,u"*乡镇驻地*",df)[0]
	query = XZ_zhudi.definitionQuery
	old_path= BZP_layer.dataSource
	# 更新数据源和定义查询
	BZP_layer.replaceDataSource(ur"G:\古蔺县\古蔺县分布图", 'SHAPEFILE_WORKSPACE', u"古蔺县标志牌点位-旭普")
	BZP_layer.definitionQuery = query
	BZP_layer.visible = True
	labelsetting(BZP_layer)
	# # -----
	# source_layer = arcpy.mapping.Layer(BZP)
	# arcpy.mapping.UpdateLayer(df, update_layer, source_layer, False)
	# # -----
	
	mxd.save()




dir_p = ur"G:\古蔺县\古蔺县分布图\成果"
names = os.listdir(dir_p)
mxd_path = hybase.HBgetfile(dir_p,"mxd",False)
for amxd in mxd_path:
	main(amxd)
	






def show_layer(names):
	pass


class NormalizeMapping(object):
	# 规范化制图
	def __init__(self, mapdocument, lyrs):
		"""
		 :param mapdocument(String):mxd文件地址
		 :param lyrs(Layer):图层对象
		"""""
		self.mxd = arcpy.mapping.MapDocument(mapdocument)
		if isinstance(lyrs, list):
			self.lyrs =lyrs
		else:
			self.lyr = lyrs
		
	@staticmethod
	def visible(layer):
		"""
		修改图层
		:param layer:
		:return:
		"""
		# layer(Layer)
		lyr_name = layer.longName
		change_info = "{0} > True".format(lyr_name)
		layer.visible = True
		return change_info
	
	def labelsetting(self,layer):
		if layer.supports("LABELCLASSES"):
			layer.showLabels = True
			for lblClass in layer.labelClasses:
				lblClass.expression = "\"<CLR red=\'255\'><FNT size = \'18\'>\" + [BZPBH] + \"</FNT></CLR>\""
				# print "Class Name:  " + lblClass.className
				# print "Expression:  " + lblClass.expression
				# print "SQL Query:   " + lblClass.SQLQuery
		
		
		else:
			print "Layer not support LabelClasses"
		
	
	
	def neme2layer(self,lyr_name):
		pass
		



import arcpy
