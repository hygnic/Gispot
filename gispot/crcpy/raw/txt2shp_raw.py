#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/16 15:55
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os

def draw_poly(coord_list, sr, y, x):
	"""
	Convert a Python list of coordinates to an ArcPy polygon feature
	Reference from : Curtis Price, USGS, cprice@usgs.gov
	coord_list(List): list of coordinates, example:
		[
			[
				['J1', '4', '3436538.1950', '34012885.9660'],
				['J2', '4', '3436540.7970', '34012503.6880'],
				['J16', '4', '3436517.6030', '34012500.1670'],
				['J17', '4', '3436520.2950', '34012503.2740']
			]
			[
				['J1', '5', '3465542.0410', '34102863.3320'],
				['J2', '5', '3436538.9340', '34702571.2020'],
				['J3', '5', '3536539.5550', '35762578.0360'],
				['J4', '5', '3536544.1120', '35762582.1780'],
				['J5', '5', '3536550.5320', '35762585.2840'],
				['J6', '5', '3536556.9520', '35762586.9410']
			]
		]
	 sr: 投影系
	  y(Int): y坐标行数
	  x(Int): x坐标行数
	"""
	parts = arcpy.Array()
	yuans = arcpy.Array()
	yuan = arcpy.Array()
	for part in coord_list:
		for pnt in part:
			if pnt:
				yuan.add(arcpy.Point(pnt[y], pnt[x]))
			else:
				# null point - we are at the start of a new ring
				yuans.add(yuan)
				yuan.removeAll()
		# we have our last ring, add it
		yuans.add(yuan)
		yuan.removeAll()
		# if we only have one ring: remove nesting
		if len(yuans) == 1:
			yuans = yuans.getObject(0)
		parts.add(yuans)
		yuans.removeAll()
	# if single-part (only one part) remove nesting
	if len(parts) == 1:
		parts = parts.getObject(0)
	return arcpy.Polygon(parts, sr)

if __name__ == '__main__':
	# 一个正方形
	poly1 = [
		[[20.0, 20.0],[30.0, 20.0],[30.0, 10.0],
		 [20.0, 10.0]]
	]
	
	# 两个三角形
	poly2 = [
		[[5.0, 3.0],[3.0, 3.0],[3.0, 5.0],
		 [5.0, 3.0]],
		
		[[7.0, 5.0],[5.0, 5.0],[5.0, 7.0],
		 [7.0, 5.0]],
	]
	
	# 带孔洞
	poly3 = [
		[[40.0, 40.0], [50.0, 40.0], [50.0, 30.0],
		 [40.0, 30.0]],
		
		[[45.0, 35.0], [48.0, 35.0], [48.0, 36.0],
		 [45.0, 36.0]]
	]
	
	arcpy.env.overwriteOutput=True
	
	output_folder = os.getcwd() # 当前路径
	# 创建空白shp
	name = "NewSHP" # shp文件名
	blank_shp = arcpy.CreateFeatureclass_management(output_folder, name, "Polygon")
	# create the polygons and write them
	Rows = arcpy.da.InsertCursor(blank_shp, "SHAPE@")
	
	# print "coords: " + repr(f)
	for f in [poly1, poly2, poly3]:
		p = draw_poly(f, sr=None, y=0, x=1)
		# print "feature: " + repr(p)
		Rows.insertRow([p])
		write_sth = "Write done: " + os.path.join(output_folder, name) + "\n\n"
		print write_sth
	del Rows
