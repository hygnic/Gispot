#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/20 16:50
# Reference:
"""
Description: 快速处理 “十二五”以来高标准农田建设评估复核修正统计表
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
from shutil import copyfile
import os
from multiprocessing import Process
from hybag import ezarcpy
from hybag import hybasic
import tooltk
from gpconfig import multication


arcpy.env.overwriteOutput =True
get_value = []
scratch_path, scratch_gdb = ezarcpy.InitPath()
# scratch_path = ezarcpy.initialize_environment()[0]
# scratch_gdb = ezarcpy.initialize_environment()[1]
arcpy.env.workspace = scratch_gdb




def rename(dirnames, rules):
	
	"""重命名文件夹中的所有文件，替换文件中的 “ ” 符号
	rename(gbz_shp, [u'”', "#2#", u'“', "#1#"])
	:param dirnames: 文件夹
	:param rules:
	:return:
	"""
	# gbz_shp_rename = []
	for a_dir in dirnames:
		# print "a_dir:",a_dir
		for f in os.listdir(a_dir):
			print f # XM2015511827GT陇东镇崇兴村“4.20”地震轻微毁损农用地复垦项目YS.shx
			whole_path = os.path.join(a_dir, f)
			print whole_path
			new1 = f.replace(rules[0], rules[1])
			new2 = new1.replace(rules[2], rules[3])
			new_path = os.path.join( a_dir, new2)
			# gbz_shp_rename.append(new_path)
			# print "new_path:", new_path
			# print "whole_path", whole_path
			if new_path!=whole_path:
				
				os.rename(whole_path, new_path)  # 重命名
	

def copy(name_list, new_dir):
	for name in name_list:
		dirr = os.path.dirname(name)
		file_name = os.path.basename(name)
		sufs = [".dbf", ".prj", ".shx"]
		copyfile(name, os.path.join(new_dir,file_name)) # 将shp先复制过去
		print name
		print "os.path.join(new_dir,file_name):",os.path.join(new_dir,file_name)
		for suf in sufs:
			name= name.replace(".shp", suf)
			copyfile(name, os.path.join(new_dir, file_name.replace(".shp", suf)))


# os.rename(i, os.path.join(dirr, new))


def handle_shp(inputs, dltb):
	all_shp = hybasic.getfiles(inputs, "shp")
	gbz_shp = hybasic.HBfilter(all_shp, "GBZ")
	hybasic._getall_items = []
	
	
	# gbz_shp_dir = [os.path.dirname(x) for x in gbz_shp]
	# gbz_shp_rename = rename(gbz_shp_dir, [u'”', "#2#", u'“', "#1#"])
	#
	# copy_to = scratch_path
	# copy(gbz_shp_rename, copy_to)
	#
	
	# 测试是否可以重命名为 “ ”
	# arcpy.Rename_management(
	# 	ur"G:\MoveOn\Gispot\Local\test_name\510000高标准农田建设上图入库数据20200114\510000GT2012511827宝兴县穆坪镇新光村土地开发复垦整理综合项目YS\GBZ2012511827GT宝兴县穆坪镇新光村土地开发复垦整理综合项目Y222S.shp",
	# 	ur"G:\MoveOn\Gispot\Local\test_name\510000高标准农田建设上图入库数据20200114\510000GT2012511827宝兴县穆坪镇新光村土地开发复垦整理综合项目YS\GBZ2012511827GT宝兴县穆坪镇新光村土地开发“复垦”整理综合项目Y222S.shp")
	
	
	
	count = len(gbz_shp)
	get_value.append(count) # 获取项目数量
	
	# 合并图层
	merge_layer = scratch_gdb + "/merge"
	# arcpy.Delete_management(merge_layer)
	arcpy.Merge_management(gbz_shp, output=merge_layer)
	# 返回面积
	gross_areas = 0
	with arcpy.da.SearchCursor(merge_layer, ["SHAPE@AREA"]) as cursor:
		for row in cursor:
			gross_areas+=row[0]
	gross_areas = round(gross_areas*0.0015, 4)
	print u"总面积（亩）：", gross_areas
	get_value.append(gross_areas) # 获取清查面积
	

	
	# 完全融合一个图层
	dissolve_layer=ezarcpy.merger_all(merge_layer)
	areas_no_dup = 0
	with arcpy.da.SearchCursor(dissolve_layer, ["SHAPE@AREA"]) as cursor:
		for row in cursor:
			areas_no_dup+=row[0]
	
	overlap_area = round((gross_areas - areas_no_dup*0.0015), 4)
	print "重叠面积（亩）：", overlap_area
	get_value.append(overlap_area) # 获取重叠面积
	
	# 标识
	identity_dltb = scratch_gdb + "/identity_dltb"
	arcpy.Identity_analysis(
		in_features=dissolve_layer, identity_features=dltb, out_feature_class=identity_dltb)
	
	identity_dltb_fields = arcpy.ListFields(identity_dltb)
	identity_dltb_name = [i.name for i in identity_dltb_fields]
	if u"地类编码" in identity_dltb_name:
		name = u"地类编码"
	else:
		name = "DLBM" # 大小写是否有影响？
	print "DLTB_NAME:", name
	print u"标识完成"
	
	gd_area = 0 # 耕地面积
	zzyd_area = 0 # 种植用地面积
	ld_area = 0 # 林地面积
	cd_area = 0 # 草地面积
	qt_area = 0 # 其它面积
	jsyd_area =  0 # 建设面积
	
	with arcpy.da.SearchCursor(identity_dltb, [name, "SHAPE@AREA"]) as cursor:
		for row in cursor:
			dlbm = row[0]
			area = row[-1]
			if dlbm in ("011", "012", "013"):
				gd_area += area
			elif dlbm.startswith("02"): # 种植用地面积
				zzyd_area += area
			elif dlbm.startswith("03"): # 林地面积
				ld_area += area
			elif dlbm.startswith("04"): # 草地面积
				cd_area += area
			elif dlbm in ("121", "122", "123", "124", "125", "126", "127"): # 其它面积
				qt_area += area
			else:
				jsyd_area += area
	
	get_value.append(round((zzyd_area+ld_area+cd_area+qt_area+jsyd_area)*0.0015, 4)) # 获取非耕地面积
	get_value.append(round(ld_area*0.0015,4)) # 林地
	get_value.append(round(cd_area*0.0015, 4)) # 草地
	get_value.append(round(zzyd_area*0.0015, 4)) # 种植用地面积
	get_value.append(round(jsyd_area*0.0015,4)) # 建设用地
	get_value.append(round(qt_area*0.0015, 4)) # 其它用地
	
	# def gd_intersect_layer():
	# 	"""合并图层（非融合）和 耕地进行相交"""
	# 	arcpy.MakeFeatureLayer_management(dltb_path, "dltb_lyr")
	# 	arcpy.SelectLayerByAttribute_management("dltb_lyr", "NEW_SELECTION", name+" LIKE '01%' ")
	# 	arcpy.CopyFeatures_management("dltb_lyr", "dltb_lyr_gd")
	# 	out_feature_class = scratch_gdb+"/intersect_layer"
	# 	arcpy.Intersect_analysis([merge_layer, "dltb_lyr"], out_feature_class)
	#
	# gd_intersect_layer()
	print "______________________________________________"
	print "______________________________________________"
	print "______________________________________________"
	for i in get_value:
		print i
	
	return get_value


# def handle_shp2(inputs):
# 	"""获取第二次复核的矢量图层和国土返回的shp文件"""
# 	all_shp = hybasic.getfiles(inputs, "shp")
# 	gbz_shp = hybasic.HBfilter(all_shp, "GBZ", size_limit=100)
# 	count = len(gbz_shp)
# 	get_value.append(count)  # 获取项目数量
#
# 	# 合并图层
# 	merge_layer = scratch_gdb + "/merge2"
# 	arcpy.Merge_management(gbz_shp, output=merge_layer)
# 	"""______________________________________________________________________"""
# 	"""___________________merge all shp, return gross area___________________"""
# 	# 返回清查总面积
# 	gross_areas = 0
# 	with arcpy.da.SearchCursor(merge_layer, ["SHAPE@AREA"]) as cursor:
# 		for row in cursor:
# 			gross_areas += row[0]
# 	gross_areas = round(gross_areas * 0.0015, 4)
# 	print u"总面积（亩）：", gross_areas
# 	get_value.append(gross_areas)  # 获取清查面积
# 	"""___________________merge all shp, return gross area___________________"""
# 	"""______________________________________________________________________"""
#
# 	"""______________________________________________________________________"""
# 	"""_________________dissolve totally, return overlap area________________"""
# 	dissolve_layer = ezarcpy.merger_all(merge_layer)
# 	areas_no_dup = 0
# 	with arcpy.da.SearchCursor(dissolve_layer, ["SHAPE@AREA"]) as cursor:
# 		for row in cursor:
# 			areas_no_dup += row[0]
#
# 	overlap_area = round((gross_areas - areas_no_dup * 0.0015), 4)
# 	print "重叠面积（亩）：", overlap_area
# 	get_value.append(overlap_area)  # 获取重叠面积
# 	"""_________________dissolve totally, return overlap area________________"""
# 	"""______________________________________________________________________"""
#
# 	return get_value

def write_excel(inputs, fill_value, range_cell):
	import xlwings as xw
	try:
		print "\n"
		app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
		app1.display_alerts = False  # 关闭Excel的提示和警告信息
		app1.screen_updating = False  # 不更新屏幕显示
		# app1.screen_updating = True
		# 打开清理统计表
		wb1 = app1.books.open(inputs)
		ws1 = wb1.sheets[0]
		# v1 = sheet1.range("a1:a7").value
		# v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
		wbs1_rowcount = ws1.api.UsedRange.Rows.count
		#
		targe_cells = ws1.range(range_cell)
		targe_cells.value = fill_value
		# # 项目名字
		# XMMC = ws1.range("C1:C" + str(wbs1_rowcount))
		# ZLDJ = ZLDJ.value
		# XMMC = XMMC.value
		# XMMC_ZLDJ= list(zip(XMMC, ZLDJ)) # [(荣县2011年国家农业综合开发高标准农田建设示范工程,需要提质改造),...]
		# for ii in XMMC_ZLDJ:
			# for i in ii:
			# 	print i
		wb1.save()
	finally:
		app1.quit()
		print "\n close application"




def run_funtion(qq_pip, folder_path2, dltb_path2,excel_path2):
	# 处理shp数据
	result = handle_shp(folder_path2, dltb_path2)
	# 写出数据到excel
	write_excel(excel_path2, result, "J7:R7")


class AreaCalGui(tooltk.Tooltk):
	commu = multication.MuCation()
	
	def __init__(self, master1):
		super(AreaCalGui, self).__init__(master1,
									  "area_cal.gc",
									  self.confirm)
		self.name = "计算地类面积"
		frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
		# block1
		self.block1 = tooltk.blockDIR_in(frame, u"数据文件地址")
		self.block2 = tooltk.blockShp_in(frame, u"DLTB图层")
		self.block3 = tooltk.blockSheet(frame, u"复核表")
	
	def confirm(self):
		_folder, _shp, _sheet = [self.block1.get(), self.block2.get(),  self.block3.get()]
		p = Process(target=self.commu.decor, args=(run_funtion, _folder, _shp, _sheet))
		# p.deamon = True
		p.start()
		# 将信息输出到右下方的动态信息栏
		self.commu.process_communication(self.major_msgframe)

# if __name__ == '__main__':
# 	"""———————————————————————————————para———————————————————————————————————————"""
# 	"""———————————————————————————————para———————————————————————————————————————"""
# 	# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
# 	# 测试路径
# 	# folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\test"
# 	folder_path = ur"F:\李恩东\跑模板\广元\剑阁-肖\新建文件夹\510000高标准农田建设上图入库数据20201221"
# 	# 测试路径
# 	dltb_path = ur"F:\李恩东\跑模板\广元\剑阁-肖\底图数据\DLTB.shp"
# 	excel_path = ur"F:\李恩东\跑模板\广元\剑阁-肖\新建文件夹\附表：“十二五”以来高标准农田建设评估复核修正统计表.xlsx"
# 	"""———————————————————————————————para———————————————————————————————————————"""
# 	"""———————————————————————————————para———————————————————————————————————————"""
# 	# 处理shp数据
# 	result_values = handle_shp(folder_path, dltb_path)
# 	# 写出数据到excel
# 	print "excel_path:",excel_path
# 	print "result_values:",result_values
# 	write_excel(excel_path, result_values, "J7:R7")
#
# 	# 处理shp数据
# 	# result_values = handle_shp(folder_path, dltb_path)
# 	# 写出数据到excel
# 	# write_excel(excel_path, result_values)