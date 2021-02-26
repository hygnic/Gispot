#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/9 17:08
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# import os
# try:
# 	import xlwings as xw
# except ImportError as e:
# 	print e
# # xpath =ur"G:\高标准农田\甘孜州 附件：“十二五”以来高标准农田建设评估复核统计表（以此为准）.xlsx"
# xpath =ur"G:\高标准农田\附件：“十二五”以来高标准农田建设评估复核统计表（以此为准） - 副本.xlsx"
# os.chdir(os.path.dirname(xpath))
# # fujian_path = ur"甘孜县“十二五”以来高标准农田建设清理检查数据统计表.xlsx"
# fujian_path = ur"甘孜县“十二五”以来高标准农田建设清理检查数据统计表 - 副本.xlsx"
# # xpath = fujian_path
#
#
# try:
# 	print "\n"
# 	app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
# 	app1.display_alerts = False  # 关闭Excel的提示和警告信息
# 	# app1.screen_updating = False  # 不更新屏幕显示
# 	app1.screen_updating = True
# 	# 打开清理统计表
# 	wb = app1.books.open(fujian_path)
# 	wb1_sheet1 = wb.sheets[0]
# 	names = wb1_sheet1.range("D4:D100")
# 	# wbs1.api.Columns("AA").Insert()
# 	# wbs1.api.Columns("AB").Insert()
# 	# wbs1.api.Columns(1).Insert()
# 	# 单独添加单元格cell,比如这里添加了A1和A2两个格子
# 	# wbs1.range('A1:A'+str(2)).api.insert
# 	for name in names:
# 		if name.value:
# 			print name.address
# 	print wb1_sheet1.range("a9").value
# 	rows_count = wb1_sheet1.api.UsedRange.Rows.count
# 	year = wb1_sheet1.range("A1:A"+str(rows_count)).value
# 	# wb1_sheet1.range("AA1:AA"+str(rows_count)).options(
# 	# 	transpose=True).value = year
# 	wb1_sheet1.range("AA1:AA"+str(rows_count)).options(
# 		transpose=True).value = year
# 	department = wb1_sheet1.range("B1:B" + str(rows_count)).value
# 	wb1_sheet1.range("AB1:AB" + str(rows_count)).options(
# 		transpose=True).value = department
#
# 	def autofill(sheet, rangee):
# 		"""
# 		sheet, worksheet对象
# 		在处理带有空白单元格的一段单元格时，空白单元格自动填充上一个单元格的值
# 		常用与有合并情况下
# 		usage: autofill(wbs1,"AA1:AA"+str(wbs1_rowcount))
# 		"""
# 		last_year = sheet.range(rangee)
# 		last_value = "blank"
# 		for cell in last_year:
# 			cell_value = cell.value
# 			# 不为空值
# 			if cell_value:
# 				last_value = cell_value
# 			else:
# 				cell.value = last_value
#
#
# 	autofill(wb1_sheet1,"AA1:AA"+str(rows_count))
# 	autofill(wb1_sheet1,"AB1:AB"+str(rows_count))
#
# 	# num = row-8
# 	def order_code(sheet, rrange, num,head_code=1):
# 		"""添加顺序码"""
# 		print "---------------"
#
# 		print sheet.api.UsedRange.Rows.count
# 		print sheet.range(rrange).row
# 		code_list = [x for x in xrange(head_code,num)]
# 		code_cell = sheet.range(rrange).options(
# 			transpose=True).value = code_list
#
# 	print wb1_sheet1.range("a1").value.strip(u"（市、区、旗、团场）“十二五”以来高标准农田建设清理检查数据统计表")
# 	# order_code(wb1_sheet1,"X1:X50",48)
# 	wb.save("jjj")
# finally:
# 	app1.quit()
# 	print "\n close application"
#

#
import os
print os.path.isfile(u"G:\高标准农田\甘孜县“十二五”以来高标准农田建设清理检查数据统计表.xlsx")
