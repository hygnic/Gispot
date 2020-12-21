#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/21 14:31
# Reference:
"""
Description: 第三次高标复核修改计算质量等级
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
from shutil import copyfile
import os
from multiprocessing import Process
from hybag import ezarcpy
from hybag import hybasic
import tooltk
from GUIconfig import multication


"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
# 测试路径
# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\test"
folder_path = ur"G:\MoveOn\Gispot\Local\test_name\510000高标准农田建设上图入库数据20200114"
# 测试路径
dltb_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\底图数据\DLTB5114002018.shp"
excel_path= ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\附表：“十二五”以来高标准农田建设评估复核修正统计表.xlsx"
"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
scratch_path = ezarcpy.initialize_environment()[0]
scratch_gdb = ezarcpy.initialize_environment()[1]
arcpy.env.workspace = scratch_gdb
arcpy.env.overwriteOutput = True

def cal_shp_area(input_file):
	if arcpy.Exists(input_file):
		_area = 0
		with arcpy.da.SearchCursor(input_file, ["SHAPE@AREA"]) as cursor:
			for roww in cursor:
				_area += roww[0]
		return _area
	else:
		u"待计算的{}图层不存在".format(input_file)

def show_shp_area(input_file):
	if arcpy.Exists(input_file):
		_area = 0
		with arcpy.da.SearchCursor(input_file, ["Shape_Area"]) as cursor:
			for roww in cursor:
				_area += roww[0]
		return _area
	else:
		u"待计算的{}图层不存在".format(input_file)


# merge_layer = scratch_gdb+ "/merge"
merge_layer = "merge" # 项目的合并图层
# out_feature_class = scratch_gdb + "/dissolve_layer"
out_feature_class = "dissolve_layer"
arcpy.Dissolve_management(merge_layer, out_feature_class, "ZLDJ")



# 按属性选择
# if arcpy.Exists(scratch_gdb+)

fuhe = "fuhe"
jibenfuhe = "jibenfuhe"
xytzgz = "xytzgz"

# for _ in [fuhe, jibenfuhe, xytzgz]:
# 	try:
# 		arcpy.Delete_management(_)
# 		print "delete:", _
# 	except:
# 		print 1
	
arcpy.MakeFeatureLayer_management(out_feature_class, "lyr")
print arcpy.Exists("lyr")
# 可能部分质量等级没有
arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " \"ZLDJ\" = '符合' ")
# 加了 U 报错
# arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " 'ZLDJ' = u'符合' ")
arcpy.CopyFeatures_management("lyr", "fuhe")
arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " \"ZLDJ\" = '基本符合' ")
arcpy.CopyFeatures_management("lyr", "jibenfuhe")
arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " \"ZLDJ\" = '需要提质改造' ")
arcpy.CopyFeatures_management("lyr", "xytzgz")
print u"分离质量等级成功"


zldj_layers=[]
if arcpy.Exists(fuhe):
	zldj_layers.append(fuhe)
if arcpy.Exists(jibenfuhe):
	zldj_layers.append(jibenfuhe)
if arcpy.Exists(xytzgz):
	zldj_layers.append(xytzgz)


dltb_fields = arcpy.ListFields(dltb_path)
dltb_field_names = [i.name for i in dltb_fields]
print dltb_field_names
if u"地类编码" in dltb_field_names:
	print 1
	name = u"地类编码"
else:
	print 2
	name = "DLBM"  # 大小写是否有影响？

dltb = "dltb"
arcpy.MakeFeatureLayer_management(dltb_path, dltb)
arcpy.SelectLayerByAttribute_management(dltb, "NEW_SELECTION", name+" LIKE '01%' ")
for a_shp in zldj_layers:
	new_name = a_shp+"_DLTB"
	arcpy.Identity_analysis(
		in_features=a_shp, identity_features=dltb, out_feature_class=new_name)
	print "a_shp：", a_shp
	arcpy.MakeFeatureLayer_management(new_name, "a_shp_2")
	arcpy.SelectLayerByAttribute_management("a_shp_2", "NEW_SELECTION",
											name+" LIKE '01%' ")
	
	arcpy.CopyFeatures_management(new_name, "a_shp")


layername_area = [] # 将图层名和面积组成的列表放进列表 [["fuhe",3455], ["jibenfuhe", 899.976]]
for i in zldj_layers:
	area = cal_shp_area(i)
	layername_area.append([i, area])
	
print layername_area # [['fuhe', 43179889.3465107], ['jibenfuhe', 28166402.1104696], ['xytzgz', 97004089.0362233]]

zldj_area = []
if arcpy.Exists(xytzgz): # 存在需要提质改造的项目
	if len(layername_area) > 2: # 存在前两种情况
		erase_jibenfuhe = "layer0"
		erase_fuhe1 = "layer1"
		erase_fuhe2 = "layer1_2"
		area1 = layername_area[0][1]
		area2 = layername_area[1][1]
		area3 = layername_area[2][1]
		# 需要提质改造和基本符合擦除
		arcpy.Erase_analysis(
			in_features=jibenfuhe, erase_features=xytzgz, out_feature_class=erase_jibenfuhe)
		area_jibenfuhe = show_shp_area(erase_jibenfuhe) # 基本符合的面积
		# 与基本符合擦除，保留符合
		arcpy.Erase_analysis(
			in_features=fuhe, erase_features=erase_jibenfuhe, out_feature_class=erase_fuhe1)
		# area_jibenfu_part1 = area1-area_fuhe1
		# 与xytzgz擦除，保留符合
		arcpy.Erase_analysis(
			in_features=erase_fuhe1, erase_features=xytzgz, out_feature_class=erase_fuhe2)
		area_fuhe = show_shp_area(erase_fuhe2)  # 符合的面积
		
		
		
		# zldj_area = [] # 三种质量等级的列表
		zldj_area.append([u"符合",area_fuhe])
		zldj_area.append([u"基本符合",area_jibenfuhe])
		zldj_area.append([u"需要提质改造",area3])
	elif len(layername_area) == 2:
		# 只有基本符合或者符合图层
		erase_ = "layer1"
		arcpy.Erase_analysis(
			in_features=layername_area[0][0], erase_features=xytzgz, out_feature_class=erase_)
		erase_area = show_shp_area(erase_) # 擦除后的面积就是非 提质改造 图层的真实面积
		area3 = layername_area[1][1] # layername_area表中第二个面积（提质改造）
		overlap_area = layername_area[0][1] - erase_area
		xytzgz_area = area3+overlap_area
		zldj_area = []
		zldj_area.append([layername_area[0][0], erase_area])
		zldj_area.append([u"需要提质改造", xytzgz_area])
	elif len(layername_area) == 1:
		# 只存在提质改造
		xytzgz_area = layername_area[0][1]
		zldj_area = []
		zldj_area.append([u"需要提质改造", xytzgz_area])
else: # 不存在需要提质改造的图层
	if len(layername_area) == 2:
		# 存在符合和基本符合
		erase_fuhe = "layer1"
		# 基本符合和符合擦除
		arcpy.Erase_analysis(
			in_features=fuhe, erase_features=jibenfuhe, out_feature_class=erase_fuhe)
		erase_area = show_shp_area(erase_fuhe)
		area1 = layername_area[0][1]
		area2 = layername_area[1][1]
		overlap_area_fuhe_jibenfuhe = area1 - erase_area  # 符合和基本符合的重叠部分面积
		fuhe_area = area1 - overlap_area_fuhe_jibenfuhe  # 真实的符合面积
		jibenfuhe_area = area2 - overlap_area_fuhe_jibenfuhe  # 真实的基本符合面积
		xytzgz_area = overlap_area_fuhe_jibenfuhe*2
		zldj_area = []
		zldj_area.append([u"符合", fuhe_area])
		zldj_area.append([u"基本符合", jibenfuhe_area])
		zldj_area.append([u"需要提质改造", xytzgz_area])
		
	else:
		# 只存在 符合 或者 基本符合 一种图层
		zldj_area = []
		zldj_area.append([layername_area[0][0], layername_area[0][1]])
a=0
for i in zldj_area:
	name, area = i
	print name, area*0.0015
	a+=area*0.0015
print a


# if arcpy.Exists(fuhe) and arcpy.Exists(jibenfuhe):
# 	erase_fuhe = "layer1"
# 	arcpy.Erase_analysis(
# 		in_features=fuhe, erase_features=jibenfuhe, out_feature_class=erase_fuhe)
# 	erase_fuhe_area = show_shp_area(erase_fuhe)
# 	area1 = layer_area[0][1]
# 	area2 = layer_area[1][1]
# 	overlap_area_fuhe_jibenfuhe = area1 - erase_fuhe_area  # 符合和基本符合的重叠部分面积
# 	fuhe_area = area1 - overlap_area_fuhe_jibenfuhe  # 真实的符合面积
# 	jibenfuhe_area = area2 - overlap_area_fuhe_jibenfuhe  # 真实的基本符合面积
#
# 	if arcpy.Exists(xytzgz): # 同时存在需要提质改造的项目
# 		area3 = layer_area[2][1]
# 		xytzgz_area = area3 + overlap_area_fuhe_jibenfuhe*2 # # 真实的需要提质改造的面积
# 	else: # 没有需要提质改造的项目
# 		xytzgz_area = overlap_area_fuhe_jibenfuhe*2
#
# elif arcpy.Exists(fuhe) and not arcpy.Exists(jibenfuhe):
# 	if arcpy.Exists(xytzgz):
# 		# 擦除
# 		erase_fuhe_xytzgz = "layer2"
# 		arcpy.Erase_analysis(
# 			in_features=fuhe, erase_features=xytzgz, out_feature_class=erase_fuhe_xytzgz)
# 		erase_area = show_shp_area(erase_fuhe_xytzgz) # 擦除面积
# 		fuhe =


		

