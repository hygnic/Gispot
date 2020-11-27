#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# User: liaochenchen
# Date: 2020/3/19
# python2 arcgis10.6
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import arcpy
import codecs
"""
遍历图层
	按位置选择
	属性表读取模块
	写出
"""


def getvalue_from_attribute(layer, txt_output, strrr, class_field, value_field):
	# 获取layer图层属性表中所有相同值的和，比如获取一个同一个乡镇下，所有TBDLMJ的和
	"""
	:param layer:  图层
	:param txt_output:  输出TXT路径
	:param strrr:
	:param class_field: 用于分类的字段 如 CJQYMC
	:param value_field: 我们需要的数据的字段，比如面积字段 "SHAPE@AREA" 等
	:return:
	"""
	field_list = [class_field, value_field]
	with arcpy.da.UpdateCursor(layer, field_list) as cursor:
		name = None
		class_field_list = []
		# get the names with list format
		for row in cursor:
			if row[0] not in class_field_list:
				class_field_list.append(row[0])
		cursor.reset()
		for name in class_field_list:
			mjm = 0
			mj = 0
			# cursor 只能遍历一次
			for roww in cursor:
				if name == roww[0]:
					tbdlmj = float(roww[1])
					mj += tbdlmj
					mjm += round(tbdlmj * 0.0015, 4)
					# mj+=roww[0]
			cursor.reset()
			# mian ji dan wei   mu
			msgg = "," + name + "," + str(mjm) + "\n"
			print msgg
			f11 = codecs.open(txt_output, "a", "utf8")
			# f=open(txt_output,"a")
			f11.write(strrr)
			f11.write(msgg)
		f11.write("\n")
		f11.close()


"""__________________________________________________________________________"""
if __name__ == '__main__':
	# 注意：GBZ农田不能是空表 空表报以下错，以后再解决
	"""
	Runtime error
	Traceback (most recent call last):
	File "<string>", line 84, in <module>
	File "<string>", line 64, in getvalue_from_attribute
		UnboundLocalError: local variable 'f11' referenced before assignment
	"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	txt_path = ur"G:\121.txt" # 将 G:\121.txt 替换成你需要保存的txt地址（会自动创建TXT文件）
	mxd = arcpy.mapping.MapDocument("CURRENT")
	layer_dltb = arcpy.mapping.ListLayers(mxd, "DLTB")[0]
	layer_GBZ = arcpy.mapping.ListLayers(mxd, "GBZ*")  # [...,"GBZ2018510604GT德阳市罗江县鄢家镇高垭村土地整理项目SS",...]
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	
	print "GBZ_count:", len(layer_GBZ)
	for i in layer_GBZ:
		print "GBZ_name:", i.name
		real_name = i.name[15:-2]
		try:
			arcpy.SelectLayerByLocation_management(
				layer_dltb, "WITHIN", i, "", "NEW_SELECTION")  # 10.1只有五个要素
		except arcpy.ExecuteError as e:
			print e.message
			continue
		# 需要对DLTB做空间连接 赋予行政区名字属性
		getvalue_from_attribute(layer_dltb, txt_path, real_name, "XZQMC", "TBDLMJ")
		# getvalue_from_attribute(layer_dltb, txt_path,real_name,"MC_new", "TBDLMJ")
