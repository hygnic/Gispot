# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
"""拆分多部件"""

import arcpy


def explode_m(shp_p, new_shp):
	"""
	:param shp_p: 需要拆分多部件的shp文件地址
	:param new_shp: 保存地址
	:return:
	"""
	arcpy.env.overwriteOutput = True
	base = "base.shp"
	arcpy.MakeFeatureLayer_management(shp_p, base)
	print u"拆分多部件..."
	arcpy.MultipartToSinglepart_management(base, new_shp)
	print u"多部件拆分完成!"

if __name__ == '__main__':
	path1 = r"G:\test\市中区\矢量数据\LQDK5110022019.shp"
	path2 = r"G:\test\市中区\output\12.shp"
	explode_m(path1, path2)