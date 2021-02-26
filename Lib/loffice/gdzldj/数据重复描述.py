#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/10/30 14:42
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import division
import xlwings as xw

path_excel = ur"G:\耕地质量等级\2020112.xls"
sheet = 3


try:
	print "\n"
	app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
	app1.display_alerts = False  # 关闭Excel的提示和警告信息
	app1.screen_updating = False  # 不更新屏幕显示
	# app1.screen_updating = True
	# 打开清理统计表
	wb1 = app1.books.open(path_excel)
	ws1 = wb1.sheets[sheet]
	# v1 = sheet1.range("a1:a7").value
	# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
	wbs1_rowcount = ws1.api.UsedRange.Rows.count
	# 质量等级
	# ph = ws1.range("J1:J" + str(wbs1_rowcount))
	# 项目名字
	# XMMC = ws1.range("C1:C" + str(wbs1_rowcount))
	# ZLDJ = ZLDJ.value
	# XMMC = XMMC.value
	# XMMC_ZLDJ= list(zip(XMMC, ZLDJ)) # [(荣县2011年国家农业综合开发高标准农田建设示范工程,需要提质改造),...]
	# # for ii in XMMC_ZLDJ:
		# for i in ii:
		# 	print i
	for i in ["B", "C", "D", "E", "F", "G"]:
		ph = ws1.range(i + "1:" + i + str(wbs1_rowcount))
		cell_list = ph.value
		head_name = cell_list[0]
		cell_list = cell_list[1:]  # 去除表头
		
		
		
		
		by=ph.value[7]
		by=round(by*100,2)
		info="土壤{}的变化范围为{}-{}，均值为{}，变异系数为{}%；".format(name,min1,max1,mean,by)
		print info
finally:
	app1.quit()
	print "\n close application"
