#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/9 10:14
# Reference:
"""
Description:将附件三的信息快速与复核表匹配并赋值
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
fujian_path = ur"甘孜县“十二五”以来高标准农田建设清理检查数据统计表.xlsx"
# xpath = fujian_path

def match(ggrange,title, sheet):
	v_name = sheet.range(ggrange).value
	# v_name = wb1_sheet1.range("d1:d300").value
	if isinstance(title,list):
		for i in title:
			v_name.remove(i)
	else:
		v_name.remove(title)
	# remove none value
	# v_name = filter(None, v_name)
	excel_num = len(v_name)
	# for i in v_name:
	# 	print i
	return [v_name,excel_num]
	# return v_name,excel_num

try:
	print "\n"
	app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
	app1.display_alerts = False  # 关闭Excel的提示和警告信息
	# app1.screen_updating = False  # 不更新屏幕显示
	app1.screen_updating = True
	# 打开清理统计表
	wb1 = app1.books.open(fujian_path)
	wb1_sheet1 = wb1.sheets[0]
	# v1 = sheet1.range("a1:a7").value
	# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
	project_name, excel_num = match("d1:d300",u"项目名称", wb1_sheet1)
	
	last_year =  wb1_sheet1.range("A2:A300")
	for cell in last_year:
		cell_value = cell.value
		# 不为空值
		if cell_value:
			last_value = cell_value
		else:
			cell.value = last_value
	
	last_department = wb1_sheet1.range("B2:B300")
	for cell in last_department:
		cell_value = cell.value
		# 不为空值
		if cell_value:
			last_value = cell_value
		else:
			cell.value = last_value
	
	wb1.save("jjj")
	wb2 = app1.books.open(xpath)
	wb2_sheet1 = wb2.sheets[0]
	# 添加行
	if excel_num > 4:
		for one_1 in xrange(excel_num-4):
			wb2_sheet1.api.Rows(14).Insert()
	
	wb2_sheet1.range("E12").options(transpose=True).value = project_name
	
	# ---项目主管部门---
	project_b = match("b1:b300", u"项目主管部门", wb1_sheet1)[0]
	wb2_sheet1.range("d12").options(transpose=True).value = project_b
	
	# ---高标准农田建设任务所属年度---
	project_a = match("a1:a300", u"高标准农田建设任务所属年度", wb1_sheet1)[0]
	project_a.pop(0)
	wb2_sheet1.range("c13").options(transpose=True).value = project_a
	
	# ---是否入库---
	project_e= match("e1:e300",u"项目是否入库", wb1_sheet1)[0]
	wb2_sheet1.range("F12").options(transpose=True).value = project_e
	
	# ---是否验收---
	# project_f = match(u"项目是否入库", wb1_sheet1)[0]
	# wb2_sheet1.range("E12").options(transpose=True).value = project_f
	
	# ---是否已入库需要补充完善信息---
	project_f = match("f1:f300",u"是否已入库需要补充完善信息", wb1_sheet1)[0]
	wb2_sheet1.range("H12").options(transpose=True).value = project_f
	
	# ---项目区面积（亩）---
	project_h = match("h1:h300",u"项目区面积（亩）", wb1_sheet1)[0]
	wb2_sheet1.range("I12").options(transpose=True).value = project_h
	
	# ---高标准农田建成面积（亩---
	project_i = match("i1:i300",u"高标准农田建成面积（亩）", wb1_sheet1)[0]
	wb2_sheet1.range("J12").options(transpose=True).value = project_i
	
	# ---符合---
	project_j = match("j1:j300", [u"符合",u"建成高标准农田质量等级情况"], wb1_sheet1)[0]
	wb2_sheet1.range("K12").options(transpose=True).value = project_j
	
	# ---基本符合---
	project_k = match("k1:k300", u"基本符合", wb1_sheet1)[0]
	wb2_sheet1.range("L12").options(transpose=True).value = project_k
	
	# ---需要提质改造---
	project_l = match("l1:l300", u"需要提质改造", wb1_sheet1)[0]
	wb2_sheet1.range("M12").options(transpose=True).value = project_l
	
	# ---总投资---
	project_m = match("m1:m300",[u"总投资",u"项目投资情况（万元）"], wb1_sheet1)[0]
	wb2_sheet1.range("N13").options(transpose=True).value = project_m
	
	# ---中央资金---
	project_n = match("n1:n300", u"中央资金", wb1_sheet1)[0]
	wb2_sheet1.range("o12").options(transpose=True).value = project_n
	
	# ---地方资金---
	project_o = match("o1:o300", u"地方资金", wb1_sheet1)[0]
	wb2_sheet1.range("p12").options(transpose=True).value = project_o
	
	# ---社会资金---
	project_p = match("p1:p300", u"社会资金", wb1_sheet1)[0]
	wb2_sheet1.range("q12").options(transpose=True).value = project_p
	
	# ---是否明确管护主体---
	project_q = match("q1:q300", [u"是否明确管护主体",u"建成高标准农田管护情况"], wb1_sheet1)[0]
	wb2_sheet1.range("r13").options(transpose=True).value = project_q
	
	# ---是否落实管护经费---
	project_r = match("r1:r300", u"是否落实管护经费", wb1_sheet1)[0]
	wb2_sheet1.range("s12").options(transpose=True).value = project_r
	
	# ---种植情况良好---
	project_s = match("s1:s300", [u"种植情况良好",u"建成高标准农田后续利用情况"], wb1_sheet1)[0]
	wb2_sheet1.range("t13").options(transpose=True).value = project_s
	
	# ---种植情况一般---
	project_t= match("t1:t300", u"种植情况一般", wb1_sheet1)[0]
	wb2_sheet1.range("u12").options(transpose=True).value = project_t
	
	# ---种植情况较差---
	project_u = match("u1:u300", u"种植情况较差", wb1_sheet1)[0]
	wb2_sheet1.range("v12").options(transpose=True).value = project_u
	
	# ---是否存在撂荒---
	project_v = match("v1:v300", u"是否存在撂荒", wb1_sheet1)[0]
	wb2_sheet1.range("w12").options(transpose=True).value = project_v
	
	# ---是否存在建设占用---
	project_w = match("w1:w300", u"是否存在建设占用", wb1_sheet1)[0]
	wb2_sheet1.range("x12").options(transpose=True).value = project_w
	
	wb2.save()
	# wb2_sheet1.api.rows(1).delete  # 删除首行
	
	
	# 去除空白行
	# 获得range对象列表
	rows = wb2_sheet1.range("e13:e313")
	for ii in rows:
		# print ii.value
		if not ii.value:
			# print ii.address
			# wb2_sheet1.range(ii.address).api.EntireRow.clear()
			wb2_sheet1.range(ii.address).api.EntireRow.Delete()
			pass
		else:
			print ii.value
			ii.address
	print rows.address
	

		
			
	
	# wb2_sheet1.range(rows.address).api.EntireRow.Delete()
	# for row in rows:
	# 	print row.cell
		# if  row.value:
		# 	cell_to_del = row
		# 	wb2_sheet1.range(cell_to_del).api.EntireRow.Delete()
		# 	print row
	
	wb2_sheet1.range('A1:X150').columns.autofit()
	# wb2_sheet1.range("a10:a40").api.EntireRow.Delete()
	wb2.save()
	# sheet1.range("a1").api.EntireRow.Delete()  # 删除该单元格所在的行
	# sheet1.api.Rows(1).Insert()  # 插入一行
	# wb.save("new")
finally:
	app1.quit()
	print "\n close application"