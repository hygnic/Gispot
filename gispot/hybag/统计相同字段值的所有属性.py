# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/19
# python2 arcgis10.6

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
def getvalue_from_attribute(area,name):
	# 获取shp属性表中所有相同值的和，比如获取不同乡镇的高标准建成区面积
	"""
	area: 统计面积  name: 名称
	"""
	field_list = [area,name]
	mxd1 = arcpy.mapping.MapDocument("CURRENT")
	layer = arcpy.mapping.ListLayers(mxd1)[-2]
	with arcpy.da.UpdateCursor(layer,field_list) as cursor:
		name=None
		name_list=[]
		# get the names with list format
		for row in cursor:
			if row[1] not in name_list:
				name_list.append(row[1])
		cursor.reset()
		for name in name_list:
			mj = 0
			# cursor 只能遍历一次
			for roww in cursor:
				if name == roww[1]:
					tbdlmj = float(roww[0])
					mj += round(tbdlmj * 0.0015, 4)
					# mj+=roww[0]
			cursor.reset()
			print name,mj,round(mj * 0.0015, 4)
			
if __name__ == '__main__':
	getvalue_from_attribute("TBDLMJ","MC")