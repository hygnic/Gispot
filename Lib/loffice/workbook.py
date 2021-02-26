#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/25 15:38
# Reference:
"""
Description: 处理工作簿的插件，主要使用xlwings,部分使用win32com
Usage:
"""
# ---------------------------------------------------------------------------
import xlwings as xw

class EasyXlwings(object):
	# <import xlwings>
	def __init__(self,path):
		self.path = path
		self.app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		self.app1.display_alerts = False  # 关闭Excel的提示和警告信息
		self.app1.screen_updating = False # 不更新屏幕显示
		# app1.screen_updating = True
		self.workbook = self.app1.books.open(self.path)
		# wbs1 = self.workbook.sheets[0]
	
	# 打开工作表
	def open(self, index):
		""""""
		# sheet = self.workbook.sheets[0]
		sheet = self.workbook.sheets[index]
		return sheet
	
	def save(self, name=None):
		if name:
			self.workbook.save(name)
			print "save a copy"
		else:
			print "save"
			self.workbook.save()
	
	# 关闭
	def quit(self):
		self.workbook.close()
		self.app1.quit()
		print "\n close application"
	
	@staticmethod
	def count(sheet):
		"""获取总行数return: int"""
		rowcount = sheet.api.UsedRange.Rows.count
		columnscount = sheet.api.UsedRange.Columns.count
		return rowcount,columnscount
	
	@staticmethod
	def delete_blank_row(sheet, target_rows, range_del, range_insert, row_num):
		"""
		保留我们需要的行，删除其他空白行
		:param sheet:
		:param target_rows: 目标 行数据 组成的列表
		:param range_del: 删除的范围  一般来说是全部删除 "a12:a" + str(sheet.api.UsedRange.Rows.count - 2) str
		:param range_insert: 确定添加行数据的位置范围 'A12:A' + str(11 + add_row) str
		:param row_num: 目标 行数据 的写入行数 int
		:return:
		"""
		# 删除行
		# sheet.range("a12:a" + str(wbs2_rowcount - 2)).api.EntireRow.Delete()
		sheet.range(range_del).api.EntireRow.Delete()
		# 清除内容保留格式
		# wbs2.range("a12:al"+str(wbs2_rowcount-1)).clear_contents()
		
		# add_row = len(_all_row) - 1
		# 添加行
		# method 1
		# for one_1 in xrange(wbs1_excel_num):
		# 	wbs2.api.Rows(12).Insert()
		# method 2
		# wbs2.range('A12:A' + str(11+add_row)).api.EntireRow.insert
		# sheet.range('A12:A' + str(11 + add_row)).api.EntireRow.Insert()
		sheet.range(range_insert).api.EntireRow.Insert()
		# 将目标行数据写入
		count = row_num
		# count = 12
		for a_row in target_rows:
			sheet["A" + str(count)].value = a_row
			count += 1
	
	@staticmethod
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
	
	
		
	
# def autofill(sheet, rangee):
# 	"""
# 	<Python Package: xlwings>
# 	sheet, worksheet对象;rangee, A1:D3
# 	在处理带有空白单元格的一段单元格时，空白单元格自动填充上一个单元格的值
# 	常使用在有合并单元格的情况下
# 	usage: autofill(wbs1,"AA1:AA"+str(wbs1_rowcount))
# 	"""
# 	last_year = sheet.range(rangee)
# 	last_value = "blank"
# 	for cell in last_year:
# 		cell_value = cell.value
# 		# 不为空值
# 		if cell_value:
# 			last_value = cell_value
# 		else:
# 			cell.value = last_value

