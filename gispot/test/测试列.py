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
import os
try:
	import xlwings as xw
except ImportError as e:
	print e
# xpath =ur"G:\高标准农田\甘孜州 附件：“十二五”以来高标准农田建设评估复核统计表（以此为准）.xlsx"
xpath =ur"G:\高标准农田\附件：“十二五”以来高标准农田建设评估复核统计表（以此为准） - 副本.xlsx"
os.chdir(os.path.dirname(xpath))
# fujian_path = ur"甘孜县“十二五”以来高标准农田建设清理检查数据统计表.xlsx"
fujian_path = ur"jjj.xlsx"
# xpath = fujian_path


try:
	print "\n"
	app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
	app1.display_alerts = False  # 关闭Excel的提示和警告信息
	# app1.screen_updating = False  # 不更新屏幕显示
	app1.screen_updating = True
	# 打开清理统计表
	wb1 = app1.books.open(fujian_path)
	wb1_sheet1 = wb1.sheets[0]
	names = wb1_sheet1.range("D4:D100")
	wb1_sheet1.api.Columns("A1:B1").Insert()
	for name in names:
		if name.value:
			print name.address
	print wb1_sheet1.range("a9").value
	wb1.save("jjj")
finally:
	app1.quit()
	print "\n close application"