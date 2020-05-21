#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/21 17:07
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import datetime
import sys
try:
	import xlwings as xw
except ImportError as e:
	print e

def singers_value(v_list, sheet):
	"""
	获取woeksheet某行（列）的数据并
	:param v_list: 行（列）的范围
	:param sheet: woeksheet
	:return: 返回列表[[值],值的个数]
	"""
	_list = []
	for v in v_list:
		value = sheet.range(v).value
		_list.append(value)
	num = len(_list)
	return _list
sss = []

def xxx(pathh):

	# path_s = ur"G:\夹江\夹江县第六批小型农田水利重点县建设项目2015年度实施方案.xls"
	try:
		global sss
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(pathh)
		wbs1 = wb1.sheets[0]
	
		if wbs1.range("A1") == u"附件2" or u"附件" or u"附":
			ss = singers_value(["D3", "J16"], wbs1)
		else:
			ss = singers_value(["D2", "J15"], wbs1)
		sss.append(ss)
	
	finally:
		app1.quit()
		# app1.kill()
		print "\n close application"
	
	print ss

path_s = ur"G:\夹江\夹江县第六批小型农田水利重点县建设项目2015年度实施方案.xls"
dir_p = ur"G:\夹江"
all_GZDG = os.listdir(dir_p)
for ii in all_GZDG:
	real_path = os.path.join(dir_p,ii)
	print real_path
xxx(path_s)