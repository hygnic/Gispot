# -*- coding:cp936 -*-
# User: liaochenchen
# Date: 2020/3/19
# python2 arcgis10.6
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import arcpy
"""
遍历shp表格
	获取名字列表
	重置游标
for 名字列表
	遍历shp表格
	if 名称匹配上
		值相加
	重置游标

打印 名字 XX
"""

def allget():
	print "ok1"
	mxd0 = arcpy.mapping.MapDocument("CURRENT")
	XM = arcpy.mapping.ListLayers(mxd0,"XM")[0]
	DLTB2 = arcpy.mapping.ListLayers(mxd0,"DLTB_lcc")[0]
	print XM,DLTB2
	name_list1 = []
	cursor= arcpy.da.UpdateCursor(XM, ["XMMC"])
	for row in cursor:
		xx1 = row[0]
		if xx1 not in name_list1:
			name_list1.append(xx1)
	print "ok2"
	print name_list1
	for name1 in name_list1:
		print "ok3"
		XM.definitionQuery = ""
		XM.definitionQuery = '"' + 'XMMC' + '"' + ' = ' + "'" + name1 + "'"
		arcpy.SelectLayerByLocation_management(XM, "WITHIN", DLTB2,
											   "", "NEW_SELECTION",
											   "NOT_INVERT")
		getvalue_from_attribute("TBDLMJ", "MC",name1)


def getvalue_from_attribute(mxd_document, static, name, xx):
	# 获取shp属性表中所有相同值的和，比如获取一个同一个乡镇下，所有TBDLMJ的和
	"""
	area: 统计面积  name: 名称
	"""
	mxd1 = mxd_document
	field_list = [static, name]
	layer = arcpy.mapping.ListLayers(mxd1)[-2]
	with arcpy.da.UpdateCursor(layer,field_list) as cursor:
		name=None
		value_list=[]
		# get the names with list format
		for row in cursor:
			if row[1] not in value_list:
				value_list.append(row[1])
		cursor.reset()
		for name in value_list:
			mj = 0
			# cursor 只能遍历一次
			for roww in cursor:
				if name == roww[1]:
					tbdlmj = float(roww[0])
					mj += round(tbdlmj * 0.0015, 4)
					# mj+=roww[0]
			cursor.reset()
			# mian ji dan wei   mu
			msgg =  name+","+str(mj)+xx+"\n"
			print msgg
			f=open(ur"G:\高标准分布图\511302顺庆区\123321.txt","a",)
			f.write(msgg)
		f.write("\n")
		f.close()


if __name__ == '__main__':
	mxd = arcpy.mapping.MapDocument("CURRENT")
	getvalue_from_attribute(mxd,"TBDLMJ","MC"," ")
	# allget()


# def getvalue_from_attribute(area, name, xx):
# 	# 获取shp属性表中所有相同值的和，比如获取不同乡镇的高标准建成区面积
# 	"""
# 	area: 统计面积  name: 名称
# 	"""
# 	mxd1 = arcpy.mapping.MapDocument("CURRENT")
# 	field_list = [area, name]
#
# 	layer = arcpy.mapping.ListLayers(mxd1)[-2]
# 	with arcpy.da.UpdateCursor(layer, field_list) as cursor:
# 		name = None
# 		name_list = []
# 		# get the names with list format
# 		for row in cursor:
# 			if row[1] not in name_list:
# 				name_list.append(row[1])
# 		cursor.reset()
# 		for name in name_list:
# 			mj = 0
# 			# cursor 只能遍历一次
# 			for roww in cursor:
# 				if name == roww[1]:
# 					tbdlmj = float(roww[0])
# 					mj += round(tbdlmj * 0.0015, 4)
# 			# mj+=roww[0]
# 			cursor.reset()
# 			# mian ji dan wei   mu
# 			msgg = name + "," + str(mj) + xx + "\n"
# 			print msgg
# 			f = open(ur"G:\高标准分布图\511302顺庆区\123321.txt", "a", )
# 			f.write(msgg)
# 		f.write("\n")
# 		f.close()

