#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/25 15:07
# Reference:
"""
Description: 拆分合并项，删除子行，保留汇总行
Usage:
"""
# ---------------------------------------------------------------------------
import xlwings
import os
from workbook import EasyXlwings as ex

main_path = ur"G:\芦山县“十二五”以来高标准农田建设评估复核统计表（5.25）(1).xlsx"
os.chdir(ur"G:")
# os.chdir(ur"G:\0525")

book = ex(main_path)
try:
	sheet = book.open(0)
	row_c,column_c= ex.count(sheet)
	ex.autofill(sheet,"E12:E"+str(row_c))
	cells= sheet.range("AI13:AI"+str(row_c))
	new_cells = [cel for cel in cells if cel.value is not None]
	# print "new_cells:",new_cells
	# 行序号的列表
	rownums = [sheet.range(num.address).row for num in new_cells]
	# print "rownums:",rownums
	# 多行数据组成的列表
	rows = [sheet.api.Rows(num).value for num in rownums]
	# print "rows:",rows
	
	columncount = sheet.api.UsedRange.Columns.count
	print columncount
	ex.delete_blank_row(sheet,rows,"a12:a"+str(row_c),'A12:A40',len(rows))
	ex.save(book,"new")
finally:
	ex.quit(book)