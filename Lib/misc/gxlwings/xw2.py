#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/11 20:55
# Reference:
"""
Description: 处理excel表格 添加高标准复核表的公式
Usage:
"""
# ---------------------------------------------------------------------------
import xlwings as xw
import os


def cal_fast(sheet,start_row,rate1,rate2):
	try:
		start_row = str(start_row)
		rate1 = str(rate1)
		rate2 = str(rate2)
		col = ["J","Z","AC","AH","AI","AJ","AK","AB"]
		col_list = [x+start_row for x in col]
		# 建成面积
		GBZ_area = sheet["J"+start_row]
		# 台账面积
		TZ_area = sheet["Z"+start_row]
		# 非耕地剔除面积
		FGD_area = sheet["AC"+start_row]
		# 实际上图入库面积
		shp_area = sheet["AH" + start_row]
		# 符合
		FH = sheet["AI" + start_row]
		# 基本符合
		JBFH = sheet["AJ" + start_row]
		# 需要提质改造
		TZGZ = sheet["AK" + start_row]

		
		# rng.formula = '=sum(b1:b5)'
		FGD_area.formula = "={0}-{1}".format(col_list[1],col_list[0])
		# 实际上图入库面积 = 建成面积 - 重叠未剔除面积
		shp_area.formula = "={0}-{1}".format(col_list[0],col_list[-1])
		FH.formula =  "={0}*{1}".format(col_list[3],rate1)
		JBFH.formula =  "={0}*{1}".format(col_list[3],rate2)
		TZGZ.formula =  "={0}-{1}-{2}".format(col_list[3],col_list[4],col_list[5])
		
		wb.save()
	finally:
		
		app1.quit()
		print "\n close application"


if __name__ == '__main__':
	
	dir_p= ur"G:\高标准农田\复核\蒲江“十二五”以来高标准农田建设评估复核统计表 (自动保存的).xlsx"
	if os.path.isdir(dir_p):
		dirrs = os.listdir(dir_p)
		for dirr in dirrs:
			if not os.path.isdir(os.path.join(dir_p, dirr)):
				rrrnew_path = os.path.join(dir_p, dirr)
				
				excel_path = rrrnew_path
				app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
				app1.display_alerts = True  # 关闭Excel的提示和警告信息
				app1.screen_updating = False  # 更新屏幕显示
				wb = app1.books.open(excel_path)
				ws = wb.sheets[0]
				cal_fast(ws, 12, 0.214, 0.197)
	else:
		excel_path = dir_p
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = True  # 关闭Excel的提示和警告信息
		app1.screen_updating = False  # 更新屏幕显示
		wb = app1.books.open(excel_path)
		ws = wb.sheets[0]
		cal_fast(ws, 12, 0.214, 0.197)
	