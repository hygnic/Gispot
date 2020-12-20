#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/20 16:50
# Reference:
"""
Description: 快速处理 “十二五”以来高标准农田建设评估复核修正统计表
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os
from hybag import ezarcpy
from hybag import hybasic


arcpy.env.overwriteOutput =True
get_value = []
"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
dltb_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\底图数据\DLTB5114002018.shp"
"""———————————————————————————————para———————————————————————————————————————"""
"""———————————————————————————————para———————————————————————————————————————"""
scratch_path = ezarcpy.initialize_environment()[0]
scratch_gdb = ezarcpy.initialize_environment()[1]


all_shp = hybasic.getfiles(folder_path, "shp")
gbz_shp = hybasic.HBfilter(all_shp, "GBZ")
count = len(gbz_shp)
get_value.append(count) # 获取项目数量

def zldj(raw_list):
	count1 = 1
	gbz_shp_v = raw_list.reverse()
	layer = gbz_shp_v.pop()
	merge_layer = scratch_gdb + "/merge"+str(count1)
	arcpy.Merge_management(gbz_shp_v, output=merge_layer)
	

# 合并图层
merge_layer = scratch_gdb + "/merge"
arcpy.Merge_management(gbz_shp, output=merge_layer)
# 返回面积
gross_areas = 0
with arcpy.da.SearchCursor(merge_layer, ["SHAPE@AREA"]) as cursor:
	for row in cursor:
		gross_areas+=row[0]
gross_areas = gross_areas*0.0015
print u"总面积（亩）：", gross_areas
get_value.append(gross_areas) # 获取清查面积

# 完全融合一个图层
dissolve_layer=ezarcpy.merger_all(merge_layer)
areas_no_dup = 0
with arcpy.da.SearchCursor(dissolve_layer, ["SHAPE@AREA"]) as cursor:
	for row in cursor:
		areas_no_dup+=row[0]

overlap_area = gross_areas - areas_no_dup*0.0015
print "重叠面积（亩）：", overlap_area
get_value.append(overlap_area) # 获取重叠面积

# 标识
identity_dltb = scratch_gdb + "/identity_dltb"
arcpy.Identity_analysis(
	in_features=dissolve_layer, identity_features=dltb_path, out_feature_class=identity_dltb)

identity_dltb_fields = arcpy.ListFields(identity_dltb)
identity_dltb_name = [i.name for i in identity_dltb_fields]
print identity_dltb_name
if u"地类编码" in identity_dltb_name:
	print 1
	name = u"地类编码"
else:
	print 2
	name = "DLBM" # 大小写是否有影响？
	
print u"标识完成"

gd_area = 0 # 耕地面积
zzyd_area = 0 # 种植用地面积
ld_area = 0 # 林地面积
cd_area = 0 # 草地面积
qt_area = 0 # 其它面积
jsyd_area =  0 # 建设面积

with arcpy.da.SearchCursor(identity_dltb, [name, "SHAPE@AREA"]) as cursor:
	for row in cursor:
		dlbm = row[0]
		area = row[-1]
		if dlbm in ("011", "012", "013"):
			gd_area += area
		elif dlbm.startswith("02"): # 种植用地面积
			zzyd_area += area
		elif dlbm.startswith("03"): # 林地面积
			ld_area += area
		elif dlbm.startswith("04"): # 草地面积
			cd_area += area
		elif dlbm in ("121", "122", "123", "124", "125", "126", "127"): # 其它面积
			qt_area += area
		else:
			jsyd_area += area

get_value.append((zzyd_area+ld_area+cd_area+qt_area+jsyd_area)*0.0015) # 获取非耕地面积
get_value.append(ld_area*0.0015) # 林地
get_value.append(cd_area*0.0015) # 草地
get_value.append(zzyd_area*0.0015) # 种植用地面积
get_value.append(jsyd_area*0.0015) # 建设用地
get_value.append(qt_area*0.0015) # 其它用地


excel_path= ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\附表：“十二五”以来高标准农田建设评估复核修正统计表.xlsx"

import xlwings as xw

try:
	print "\n"
	app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
	app1.display_alerts = False  # 关闭Excel的提示和警告信息
	app1.screen_updating = False  # 不更新屏幕显示
	# app1.screen_updating = True
	# 打开清理统计表
	wb1 = app1.books.open(excel_path)
	ws1 = wb1.sheets[0]
	# v1 = sheet1.range("a1:a7").value
	# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
	wbs1_rowcount = ws1.api.UsedRange.Rows.count
	#
	targe_cells = ws1.range("J7:R7")
	targe_cells.value = get_value
	# # 项目名字
	# XMMC = ws1.range("C1:C" + str(wbs1_rowcount))
	# ZLDJ = ZLDJ.value
	# XMMC = XMMC.value
	# XMMC_ZLDJ= list(zip(XMMC, ZLDJ)) # [(荣县2011年国家农业综合开发高标准农田建设示范工程,需要提质改造),...]
	# for ii in XMMC_ZLDJ:
		# for i in ii:
		# 	print i
	wb1.save()
finally:
	app1.quit()
	print "\n close application"