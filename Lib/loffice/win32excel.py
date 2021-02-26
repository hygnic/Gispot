#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/21 17:55
# Reference:
"""
Description: 在 高标准农田建设评估复核统计表 中添加一列数据
Usage:
"""
# ---------------------------------------------------------------------------
import os
from win32com.client import Dispatch
import xlwings as xw

_getall_items = []
def recur_search(dirs_p, suffix, recur, counter=0):  # 002.0
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	ss = recur_search(ur"G:\高标准","",True)
	ss = recur_search(ur"G:\高标准","xlsx",True)
	ss = recur_search(ur"G:\高标准",["xlsx","xls"],True)

	recur 使用递归，特别注意，层数不要太多
	:param recur: bool 是否启用递归
	:param dirs_p: dir address
	:param suffix: 后缀 str或者列表
	:param counter: 计数 用于缩进\t
	:return: list
	"""
	global _getall_items
	# global __getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p, file_p)
		if os.path.isdir(file_path):
			print "\t" * counter + "dir:", file_p
			# 递归
			if recur:
				recur_search(file_path, suffix, recur, counter + 1)
		else:
			# print "\t"*counter+file_p
			if suffix:
				# 单个后缀
				if not isinstance(suffix, list):
					# stage 1 筛选后缀
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name = name_and_suffix[0]
					if f_suffix == suffix:
						print "\t" * counter, base_name
						_getall_items.append(file_path)
				# 多个后缀组成列表
				else:
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name = name_and_suffix[0]
					if f_suffix in suffix:
						print "\t" * counter, base_name
						_getall_items.append(file_path)
			# 无后缀要求，获取所有文件
			else:
				_getall_items.append(file_path)
	
	return _getall_items

def mian(path_excel):
	try:
		xlApp = Dispatch('Excel.Application')
		xlApp.DisplayAlerts = False
		xlApp.Visible = False
		# if os.path.splitext(path_excel)[0][:2] == u"I:":
		# 	print "gg:",os.path.splitext(path_excel)[0][:2]
		# 	print "<<<<<<<<<skin hidden file!"
			
		# else:
		wb = xlApp.Workbooks.Open(path_excel)
		# try:
		# 	wb = xlApp.Workbooks.Open(path_excel)
		# except Exception as e:
		# 	base_n = os.path.basename(path_excel)[2:]
		# 	dir_n = os.path.dirname(path_excel)
		# 	new_name = os.path.join(dir_n,base_n)
		# 	wb = xlApp.Workbooks.Open(new_name)
		
		#下面两个都可以
		# wbs = xlApp.Worksheets[0]
		wbs = wb.Worksheets[0]
		value_A1 = wbs.Cells(1,1).Value
		print "value_A1:",value_A1
		if value_A1.strip() in [u"附件2",u"附件",u"附"] or u"附" in value_A1.strip() or "2" in value_A1.strip():
			p_area = wbs.Cells(16, 10).Value
			p_name = wbs.Cells(3, 4).Value
			print "value_J16:",p_area
			print "value_E3:",p_name
		else:
			p_area =  wbs.Cells(15, 10).Value
			p_name = wbs.Cells(2, 4).Value
			print "value_J15:",p_area
			print "value_E2:",p_name
			
		return [p_name, p_area]
		
	finally:
		print "-----"
		xlApp.Workbooks.Close()
		xlApp.Quit()
		# time.sleep(3)
		# exit()
		# xlApp.Workbooks.Close()
	


def main_2(path, clo, list_m):
	"""插入空白行，然后填充值"""
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
		print "wbs1_count:",wbs1_count
		names_list = wbs1["E1:E"+str(wbs1_count)]
		for name in names_list:
			for m in list_m:
				if name.value == m[0]:
					wbs1.range("J"+str(wbs1.range(name.address).row)).value = m[1]
		# for i in xrange(wbs1_count):
		# 	pass
		wb1.save()

	finally:
		app1.quit()
		
		print "\n close application"

xlsx_list = recur_search(ur"I:\高标准农田上图入库\54营山高标准农田上图入库项目",[u"xlsx",u"xls",u"XLSX",u"XLS"],recur=True)
# xlsx_list = recur_search(ur"G:\正安县\正安县分布图\成果\标志牌图\3.自然资源部门",[u"xlsx",u"xls",u"XLSX",u"XLS"],recur=True)
print "xlsx_list:",xlsx_list
xlsx_list2 = [xx for xx in xlsx_list if "~$" not in xx]
xlsx_list = xlsx_list2
GZDG_value = []
# dir_p = ur"G:\夹江\新建文件夹"
# all_GZDG = os.listdir(dir_p)
for ii in xlsx_list:
	try:
		# real_path = os.path.join(dir_p, ii)
		print "ii:",ii
		excel_value = mian(ii)
		GZDG_value.append(excel_value)
	except AttributeError as e:
		print e
		continue
		
# 筛选出隐藏备份文件
GZDG_value2 = [i for i in GZDG_value if "~$" not in i]
print "GZDG_value2:",GZDG_value2


# 复核表
path_2 = ur"G:\高标准农田\复核\成都市\金堂\营山：“十二五”以来高标准农田建设评估复核统计表（上报2）.xlsx"
# path_2 = ur"J:\高标准农田\夹江\新建文件夹\附件：夹江“十二五”以来高标准农田建设评估复核统计表（夹江）(2).xlsx"
main_2(path_2,10,GZDG_value2)