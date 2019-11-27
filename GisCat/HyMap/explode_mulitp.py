# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
"""拆分多部件"""

import arcpy
import tooltk

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

class App(tooltk.Tooltk):
	"""
	该功能的调用窗口
	"""
	def __init__(self):
		super(App, self).__init__(u"拆分多部件",
								  "docs/explode_mulitp")
		self.single_file_block( [(u'shpfile', '*.shp'), ('All Files', '*')],
								u"选择待处理shp文件")
		self.savename_block([(u'shpfile', '*.shp'), ('All Files', '*')],
							   u"选择保存地址")
		self.button_confirm["command"] = self.confirm_method
		
	def confirm_method(self):
		# 获取列表
		v = self.get_Entry_fromblock(self.input_sfb, self.input_sfb2)
		explode_m(v[0], v[1])





		
if __name__ == '__main__':
	path1 = r"G:\test\市中区\矢量数据\LQDK5110022019.shp"
	path2 = r"G:\test\市中区\output\12.shp"
	explode_m(path1, path2)