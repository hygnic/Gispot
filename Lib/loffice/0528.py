#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/28 13:59
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import xlwings as xw
infile = ur"G:\高标准农田\复核\雅安市\工作簿1.xlsx"


def autofill(sheet, rangee):
	"""
	<Python Package: xlwings>
	sheet, worksheet对象;rangee, A1:D3
	在处理带有空白单元格的一段单元格时，空白单元格自动填充上一个单元格的值
	常使用在有合并单元格的情况下
	usage: autofill(wbs1,"AA1:AA"+str(wbs1_rowcount))
	"""
	last_year = sheet.range(rangee)
	last_value = "blank"
	for cell in last_year:
		cell_value = cell.value
		# 不为空值
		if cell_value:
			last_value = cell_value
		else:
			cell.value = last_value


try:
	print "\n"
	app1 = xw.App(visible=True, add_book=False)  # 只打开不新增工作簿
	app1.display_alerts = False  # 关闭Excel的提示和警告信息
	# app1.screen_updating = False  # 不更新屏幕显示
	app1.screen_updating = True
	# 打开清理统计表
	wb1 = app1.books.open(infile)
	wbs1 = wb1.sheets[0]
	wbs2 = wb1.sheets[1]
	# v1 = sheet1.range("a1:a7").value
	# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
	
	wbs2_rowcount = wbs2.api.UsedRange.Rows.count
	ss = wbs2.range("A1:A" + str(wbs2_rowcount)).value
	for s in ss:
		print s
	autofill(wbs2,"A1:A"+str(wbs2_rowcount))
	wbs2.range("B1").api.EntireColumn.Insert()
	
	wbs2.range("B1:B" + str(wbs2_rowcount)).options(
	transpose=True).value = ss
	autofill(wbs2,"B1:B"+str(wbs2_rowcount))
	# wb1.save()
	
finally:
	pass
	# app1.quit()