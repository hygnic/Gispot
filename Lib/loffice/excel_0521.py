#!/usr/bin/env python
# -*- coding:utf8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/21
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import time
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


def main_1(path):
	"""将制定空格的几个值放到列表中"""
	try:
		global all_v
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		# app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(path)
		wbs1 = wb1.sheets[0]
		# v1 = sheet1.range("a1:a7").value
		# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
		if wbs1.range("A1").value.strip() in [u"附件2",u"附件",u"附"]:
			ss = singers_value(["D3","J16"],wbs1)
		else:
			ss = singers_value(["D2","J15"], wbs1)
		print ss
		all_v.append(ss)
		
	finally:
		app1.quit()
		time.sleep(10)
		print "\n close application"
		
		


def main_2(path,clo,list_m):
	"""插入空白行，然后匹配、赋值"""
	try:
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		# app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(path)
		wbs1 = wb1.sheets[0]
		# v1 = sheet1.range("a1:a7").value
		# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
		wbs1.api.Columns(clo).Insert()
		wbs1_count = wbs1.api.UsedRange.Rows.count
		for i in xrange(wbs1_count):
			pass
		wb1.save()
		
		
		
	finally:
		app1.quit()
		
		print "\n close application"

	
if __name__ == '__main__':
	all_v = []
	# main_1(ur"G:\夹江\夹江县2012年度农业综合开发土地治理项目.xlsx")
	# print all_v
	dir_p = ur"G:\夹江"
	all_GZDG_value = []
	all_GZDG  = os.listdir(dir_p)
	for ii in all_GZDG:
		real_path = os.path.join(dir_p,ii)
		main_1(real_path)
		
		
		
	# path_2 = ur"G:\高标准农田\复核\德阳\德阳市罗江“十二五”以来高标准农田建设评估复核统计表2020年5月12日.xlsx"
	# main_2(path_2,10,all_GZDG_value)