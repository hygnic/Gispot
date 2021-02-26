#!/usr/bin/env python
# -*- coding:utf8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/9 10:14
# Reference:
"""
Description:
	将附件三（XX县“十二五”以来高标准农田建设清理检查数据统计表.xlsx）的主要信息填入到指定模板中，
	可以对单个附件三进行转换，也可以对文件夹中的所有附件三进行转换
Usage:
"""
# ---------------------------------------------------------------------------
import os
try:
	import xlwings as xw
except ImportError as e:
	print e


def cellvalue_geter(rrange, col_name, sheet):
	"""
	<Python Package: xlwings>
	获取woeksheet某行（列）的数据并
	:param rrange: 行（列）的范围
	:param col_name: 列名称，方便识别
	:param sheet: woeksheet
	:return: 返回列表[值,值的个数]
	"""
	cells_value = sheet.range(rrange).value
	# cells_value = wbs1.range("d1:d300").value
	print "col_name:",col_name
	cells_value = cells_value[3:]
	num = sheet.api.UsedRange.Rows.count
	# num = len(cells_value)
	return [cells_value, num]

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


# num = row-8
def order_code(sheet, rrange, num, head_code=1):
	"""
	添加顺序码
	order_code(wbs2, "A8", wbs2_rowcount - 7)
	:param sheet: worksheet
	:param rrange: 范围
	:param num:
	:param head_code: 顺序起始码
	:return:
	"""
	# print "---------------"
	# print sheet.api.UsedRange.Rows.count
	# print sheet.range(rrange).row
	code_list = [x for x in xrange(head_code, num)]
	code_cell = sheet.range(rrange).options(
		transpose=True).value = code_list
	
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

def Excel_match_05(infile,mathfile,output,XZQ):
	"""
	匹配两张表格
	:param infile: 清理检查数据统计表.
	:param mathfile:评估复核统计表模板
	:param output: 输出目录
	:param XZQ: 市州行政区名字
	:return:
	"""
	try:
		print "\n"
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		# app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(infile)
		wbs1 = wb1.sheets[0]
		# v1 = sheet1.range("a1:a7").value
		# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
		
		wbs1_rowcount = wbs1.api.UsedRange.Rows.count
		# 将有合并单元格的列复制到空白列
		project_time = wbs1.range("A1:A" + str(wbs1_rowcount)).value
		wbs1.range("AA1:AA" + str(wbs1_rowcount)).options(
			transpose=True).value = project_time
		project_department = wbs1.range("B1:B" + str(wbs1_rowcount)).value
		wbs1.range("AB1:AB" + str(wbs1_rowcount)).options(
			transpose=True).value = project_department
		autofill(wbs1, "AA1:AA" + str(wbs1_rowcount))
		autofill(wbs1, "AB1:AB" + str(wbs1_rowcount))
		project_name, wbs1_excel_num = cellvalue_geter("d1:d300", u"项目名称", wbs1)
		
		
		wb2 = app1.books.open(mathfile)
		wbs2 = wb2.sheets[0]
		wbs2_rowcount = wbs2.api.UsedRange.Rows.count
		# 添加行
		for one_1 in xrange(wbs1_excel_num):
			wbs2.api.Rows(12).Insert()
		
		wbs2.range("E12").options(transpose=True).value = project_name
		
		# ---项目主管部门---
		project_b = cellvalue_geter("AB1:AB300", None, wbs1)[0]
		wbs2.range("d12").options(transpose=True).value = project_b
		
		# ---高标准农田建设任务所属年度---
		project_a = cellvalue_geter("AA1:AA300", None, wbs1)[0]
		wbs2.range("c12").options(transpose=True).value = project_a
		
		# ---是否入库---
		project_e= cellvalue_geter("e1:e300", u"项目是否入库", wbs1)[0]
		wbs2.range("F12").options(transpose=True).value = project_e
		
		# ---是否验收---
		# project_f = match(u"项目是否入库", wbs1)[0]
		# wbs2.range("E12").options(transpose=True).value = project_f
		
		# ---是否已入库需要补充完善信息---
		project_f = cellvalue_geter("f1:f300", u"是否已入库需要补充完善信息", wbs1)[0]
		wbs2.range("H12").options(transpose=True).value = project_f
		
		# ---项目区面积（亩）---
		project_h = cellvalue_geter("h1:h300", u"项目区面积（亩）", wbs1)[0]
		wbs2.range("I12").options(transpose=True).value = project_h
		
		# ---高标准农田建成面积（亩---
		project_i = cellvalue_geter("i1:i300", u"高标准农田建成面积（亩）", wbs1)[0]
		wbs2.range("J12").options(transpose=True).value = project_i
		
		# ---符合---
		project_j = cellvalue_geter("j1:j300", [u"符合", u"建成高标准农田质量等级情况"], wbs1)[0]
		wbs2.range("K12").options(transpose=True).value = project_j
		
		# ---基本符合---
		project_k = cellvalue_geter("k1:k300", u"基本符合", wbs1)[0]
		wbs2.range("L12").options(transpose=True).value = project_k
		
		# ---需要提质改造---
		project_l = cellvalue_geter("l1:l300", u"需要提质改造", wbs1)[0]
		wbs2.range("M12").options(transpose=True).value = project_l
		
		# ---总投资---
		project_m = cellvalue_geter("m1:m300", [u"总投资", u"项目投资情况（万元）"], wbs1)[0]
		wbs2.range("N12").options(transpose=True).value = project_m
		
		# ---中央资金---
		project_n = cellvalue_geter("n1:n300", u"中央资金", wbs1)[0]
		wbs2.range("o12").options(transpose=True).value = project_n
		
		# ---地方资金---
		project_o = cellvalue_geter("o1:o300", u"地方资金", wbs1)[0]
		wbs2.range("p12").options(transpose=True).value = project_o
		
		# ---社会资金---
		project_p = cellvalue_geter("p1:p300", u"社会资金", wbs1)[0]
		wbs2.range("q12").options(transpose=True).value = project_p
		
		# ---是否明确管护主体---
		project_q = cellvalue_geter("q1:q300", [u"是否明确管护主体", u"建成高标准农田管护情况"], wbs1)[0]
		wbs2.range("r12").options(transpose=True).value = project_q
		
		# ---是否落实管护经费---
		project_r = cellvalue_geter("r1:r300", u"是否落实管护经费", wbs1)[0]
		wbs2.range("s12").options(transpose=True).value = project_r
		
		# ---种植情况良好---
		project_s = cellvalue_geter("s1:s300", [u"种植情况良好", u"建成高标准农田后续利用情况"], wbs1)[0]
		wbs2.range("t12").options(transpose=True).value = project_s
		
		# ---种植情况一般---
		project_t= cellvalue_geter("t1:t300", u"种植情况一般", wbs1)[0]
		wbs2.range("u12").options(transpose=True).value = project_t
		
		# ---种植情况较差---
		project_u = cellvalue_geter("u1:u300", u"种植情况较差", wbs1)[0]
		wbs2.range("v12").options(transpose=True).value = project_u
		
		# ---是否存在撂荒---
		project_v = cellvalue_geter("v1:v300", u"是否存在撂荒", wbs1)[0]
		wbs2.range("w12").options(transpose=True).value = project_v
		
		# ---是否存在建设占用---
		project_w = cellvalue_geter("w1:w300", u"是否存在建设占用", wbs1)[0]
		wbs2.range("x12").options(transpose=True).value = project_w
		
		
		
		wbs2.range("B8").value = XZQ
		if  wbs1.range("a1").value[:2] == u"附件":
			XJQY = wbs1.range("a2").value.strip(u"（市、区、旗、团场）“十二五”以来高标准农田建设清理检查数据统计表")
			XJQY =XJQY.strip()
		else:
			XJQY = wbs1.range("a1").value.strip(u"（市、区、旗、团场）“十二五”以来高标准农田建设清理检查数据统计表")
			XJQY = XJQY.strip()
		wbs2.range("B11").value = XJQY
		wbs2_rowcount = wbs2.api.UsedRange.Rows.count
		"-----------------------"
		# 去除空白行
		# 获得range对象列表
		row_list = []
		rows = wbs2.range("E12:E" + str(wbs2_rowcount))
		for ii in rows:
			# print ii.value
			if not ii.value:
				pass
				# print ii.address
				# row_d = wbs2.range(ii.address).row
				# print row_d
				# print "00000000000000000000000"
				# wbs2.api.rows(row_d).delete
				# print ii.value
				#TODO 无法删除，不知为什么
				# wbs2.api.rows(1).delete
				# wbs2.range(ii.address).api.EntireRow.Delete()
			else:
				row_d = wbs2.range(ii.address).row
				# 目标 行数据 组成的列表
				row_list.append(wbs2.api.Rows(row_d).value)
				# print ii.value
				# print ii.address
			target_count = len(row_list)
		"-----------------------"
		# 删除空白行，保留目标行
		# 删除范围，多保留一条空行，方便后续插入的空白行能保持相同的格式，如表格框等
		del_range = "a12:a" + str(wbs2_rowcount - 2)
		# 添加空白行的位置和数量 TODO 忘记为什么是11了
		inser_range = 'A12:A' + str(11 + target_count-1)
		delete_blank_row(wbs2,row_list,del_range,inser_range,12)
		
		# all_row = []
		# for i1 in row_list:
		# 	entire_row =  wbs2.api.Rows(i1).value
		# 	# print entire_row
		# 	all_row.append(entire_row)
		# # 删除行
		# wbs2.range("a12:a"+str(wbs2_rowcount-2)).api.EntireRow.Delete()
		# # 清除内容保留格式
		# # wbs2.range("a12:al"+str(wbs2_rowcount-1)).clear_contents()
		# add_row = len(all_row)-1
		#
		# # 添加行
		# # method 1
		# # for one_1 in xrange(wbs1_excel_num):
		# # 	wbs2.api.Rows(12).Insert()
		# # method 2
		# # wbs2.range('A12:A' + str(11+add_row)).api.EntireRow.insert
		# wbs2.range('A12:A' + str(11+add_row)).api.EntireRow.Insert()
		# count =12
		# for a_row in all_row:
		# 	wbs2["A"+str(count)].value = a_row
		# 	count+=1
		
		# print wbs2.api.Rows(row_list[0]).value
		# wbs2.range("A56").value = wbs2.api.Rows(row_list[0]).value
		"-----------------------"
		# 排序
		new_wbs2_rowcount = wbs2.api.UsedRange.Rows.count
		order_code(wbs2, "A12", new_wbs2_rowcount - 7-4)
		"-----------------------"
		
		wbs2.range('A1:AL'+str(wbs2_rowcount)).columns.autofit()
		# wbs2.range('A1:AL300').columns.autofit()
		file_name = XJQY+u"“十二五”以来高标准农田建设评估复核统计表.xlsx"
		save_path = os.path.join(output,file_name)
		wb2.save(save_path)
		# sheet1.range("a1").api.EntireRow.Delete()  # 删除该单元格所在的行
		
	except Exception as e:
		print e.message
		# print "error"
		# # now = datetime.datetime.now()
		# # now_time = now.strftime('%d%H%M%S')
		# log_file = open(os.path.join(output,"error.log"),"a")
		# log_file.write(wb.name.encode("cp936")+"\n")
		# log_file.close()
		
	finally:
		app1.quit()
		print "\n close application"
		
if __name__ == '__main__':
	# inn= raw_input("input infile:")
	# temp = raw_input("input matcfile:")
	# out_put = raw_input("output dir:")
	#
	# name = raw_input("XZQ:")
	
	# Excel_match_05(
	# 	ur"甘孜县“十二五”以来高标准农田建设清理检查数据统计表 - 副本.xlsx",
	# 	ur"附件：“十二五”以来高标准农田建设评估复核统计表（以此为准） - 副本.xlsx",
	# 	ur"G:\高标准农田\新建文件夹",
	# 	u"甘孜州")
	# os.chdir(ur"G:\高标准农田\复核\其它")
	# dir_p= ur"G:\高标准农田\复核\甘孜州\乡城县“十二五”以来高标准农田建设清理检查数据统计表.xlsx"
	dir_p= ur"G:\高标准农田\复核\清理统计表\新建文件夹"
	XJXZQ_name = u"**"
	out = ur"G:\高标准农田\复核\清理统计表\新建文件夹 (2)"
	if os.path.isdir(dir_p):
		dirrs = os.listdir(dir_p)
		for dirr in dirrs:
			if not os.path.isdir(os.path.join(dir_p,dirr)):
				rrrnew_path = os.path.join(dir_p,dirr)
		# inn = ur"巴塘县“十二五”以来高标准农田建设清理检查数据统计表.xls"
		# inn = ur"白玉县“十二五”以来高标准农田建设清理检查数据统计表.xlsx"
		# inn = ur"G:\高标准农田\复核\其它\罗江区“十二五”以来高标准农田建设清理检查数据统计表.xls"
		
		
			inn = rrrnew_path
			temp = ur"G:\高标准农田\复核\附件：“十二五”以来高标准农田建设评估复核统计表（以此为准）.xlsx"
			Excel_match_05(inn, temp,
						   out,
						   XJXZQ_name)
	else:
		inn = dir_p
		temp = ur"G:\高标准农田\复核\附件：“十二五”以来高标准农田建设评估复核统计表（以此为准）.xlsx"
		Excel_match_05(inn, temp,
					   out,
					   XJXZQ_name)