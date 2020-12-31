#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/24 23:35
# Reference:
"""
Description: 处理sheet数据的模块
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
try:
	import xlwings as xw
except ImportError:
	print("no xlwings")
	

def write_excel(inputs, fill_value, range_cell):
	try:
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(inputs)
		ws1 = wb1.sheets[0]
		# v1 = sheet1.range("a1:a7").value
		# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
		wbs1_rowcount = ws1.api.UsedRange.Rows.count
		#
		targe_cells = ws1.range(range_cell)
		targe_cells.value = fill_value
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
		print("write done")
		

if __name__ == '__main__':
	print(ord("种"))