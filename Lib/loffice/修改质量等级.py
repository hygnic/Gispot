#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/30 13:10
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import xlwings as xw
import os
import arcpy

from hybag import hybasic


# 确定质量等级的入库清单excel
# excel_path = "path"
excel_path = u"C:/Users/Administrator/Desktop/高标最后一次/自贡市/荣县/自贡市荣县.xlsx"
db_path = u"C:/Users/Administrator/Desktop/高标准成果/荣县/510000高标准农田建设上图入库数据20200630"
# db_path = u"C:/Users/Administrator/Desktop/高标最后一次/自贡市/荣县/测试/510000高标准农田建设上图入库数据20200110"

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
	# 质量等级
	ZLDJ = ws1.range("I1:I" + str(wbs1_rowcount))
	# 项目名字
	XMMC = ws1.range("C1:C" + str(wbs1_rowcount))
	ZLDJ = ZLDJ.value
	XMMC = XMMC.value
	XMMC_ZLDJ= list(zip(XMMC, ZLDJ)) # [(荣县2011年国家农业综合开发高标准农田建设示范工程,需要提质改造),...]
	# for ii in XMMC_ZLDJ:
		# for i in ii:
		# 	print i
finally:
	app1.quit()
	print "\n close application"

# 第二部分
# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
shpfiles = hybasic.getfiles(db_path,"shp",True)
# shpfiles = [os.path.basename(i) for i in shpfiles]
GBZ_shpfiles=hybasic.HBfilter(shpfiles,"GBZ",100)
print "GBZ_shpfiles's len:",len(GBZ_shpfiles)
for path in GBZ_shpfiles:
	for ii in XMMC_ZLDJ:
		basename = os.path.basename(path)  # GBZ2012510321CZ2011年现代农业生产发展项目YS.shp
		basename = basename[15:-6]
		if ii[0] == basename:
			new_ZLDJ = ii[1]
			with arcpy.da.UpdateCursor(path,("ZLDJ",)) as cursor:
				for row in cursor:
					row[0] = new_ZLDJ
					print "shpfiles done:",path
					cursor.updateRow(row)

hybasic._getall_items=[]
XM_shpfiles=hybasic.HBfilter(shpfiles,"XM",100)
print "XM_shpfiles's len:",len(XM_shpfiles)
for path in XM_shpfiles:
	for ii in XMMC_ZLDJ:
		basename = os.path.basename(path)  # GBZ2012510321CZ2011年现代农业生产发展项目YS.shp
		basename = basename[14:-6]
		if ii[0] == basename:
			new_ZLDJ = ii[1]
			with arcpy.da.UpdateCursor(path,("ZLDJ",)) as cursor:
				for row in cursor:
					row[0] = new_ZLDJ
					print "xw shpfiles done:",path
					cursor.updateRow(row)


# 质量等级 v列 国土上过库
# 质量等级 v列 国土没有上过库
# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
hybasic._getall_items=[]

# 第三部分 修改excel表
print "======================================================================"
print "======================================================================"
# 单个项目文件夹中的excel表
new_xlsxs = hybasic.getfiles(db_path, "xlsx", True)
print "Third Part xlsxs:",len(new_xlsxs)

for paths2 in new_xlsxs:
	basename2 = os.path.basename(paths2)
	ss = "SS.xlsx"
	print  "basename2[:-7]:",basename2[-7:]
	if not basename2[-7:]==ss:
		basename2 = basename2[12:-7] # 荣县2011年国家农业综合开发高标准农田建设示范工程
		print "Third Part basename:",basename2
		for ii in XMMC_ZLDJ:
			if ii[0] == basename2:
				try:
					app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
					app1.display_alerts = False  # 关闭Excel的提示和警告信息
					app1.screen_updating = False  # 不更新屏幕显示
					# app1.screen_updating = True
					# 打开清理统计表
					wb1 = app1.books.open(paths2)
					ws1 = wb1.sheets[0]
					# v1 = sheet1.range("a1:a7").value
					# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
					wbs1_rowcount = ws1.api.UsedRange.Rows.count
					# 质量等级
					ws1.range("V2").value = ii[1]
					wb1.save()
					print "Third Part excel file done:",paths2
				finally:
					# wb1.close()
					app1.quit()
					# print "\n close application"
	else:
		print "else=-=========================================================="
		print  "basename2[-7:]:", basename2[-7:]
		basename2 = basename2[12:-7]  # 荣县2011年国家农业综合开发高标准农田建设示范工程
		print "Third Part basename:", basename2
		for ii in XMMC_ZLDJ:
			if ii[0] == basename2:
				try:
					app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
					app1.display_alerts = False  # 关闭Excel的提示和警告信息
					app1.screen_updating = False  # 不更新屏幕显示
					# app1.screen_updating = True
					# 打开清理统计表
					wb1 = app1.books.open(paths2)
					ws1 = wb1.sheets[0]
					# v1 = sheet1.range("a1:a7").value
					# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
					wbs1_rowcount = ws1.api.UsedRange.Rows.count
					# 质量等级
					ws1.range("u2").value = ii[1]
					wb1.save()
					print "Third Part excel file done:", paths2
				finally:
					# wb1.close()
					app1.quit()
			# print "\n close application"