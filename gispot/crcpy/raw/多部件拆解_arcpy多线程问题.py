# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
"""
拆分多部件
使用了多线程技术 牛逼！！！！！！！！！
"""

import arcpy
# from threading import Thread
import tooltk

def explode_m(shp_p, new_shp):
	"""
	:param shp_p: 需要拆分多部件的shp文件地址
	:param new_shp: 保存地址
	:return:
	"""
	arcpy.env.overwriteOutput = True
	# import time
	# time.sleep(10)
	# arcpy.env.workspace = r"E:\move on move on\aaa"
	base = "base.shp"
	print arcpy.Exists(shp_p)
	print shp_p,type(shp_p),"\n",new_shp,type(new_shp)
	arcpy.MakeFeatureLayer_management(shp_p, base)
	print u"多部件拆分..."
	arcpy.MultipartToSinglepart_management(base, new_shp)
	print u"多部件已拆解"

class App(tooltk.Tooltk):
	"""
	该功能的调用窗口
	"""
	def __init__(self):
		super(App, self).__init__(u"拆分多部件",
								  "docs/explode.gc")
		# s = self.window.winfo_children()
		# for i in s:
		# 	print type(i) # <type 'instance'>
		self.single_file_block( [(u'shapefile', '*.shp'), ('All Files', '*')],
								u"选择待处理shp文件")
		self.save_path_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							   u"选择保存地址")
		self.button_confirm["command"] = self.confirm_method_q
		
	def confirm_method_q(self):
		# 获取列表
		v = self.get_blockvalue(self.input_sfb, self.input_sb)
		# t = Thread(target=explode_m, args=(v[0], v[1]))
		# t = Thread(target=explode_m, args=(self.block_list[0], self.block_list[1]))
		# print v[0],type(v[0])
		# print v[1],type(v[1])
		# t.setDaemon(True)  # 就是设置子线程随主线程的结束而结束
		# t.start()
		explode_m(v[0], v[1])


if __name__ == '__main__':
	path1 = r"E:\move on move on\正安县\正安数据\CJQY5203242019.shp"
	# path2 = r"G:\test\市中区\output\12.shp"
	path2 = r"E:\move on move on\正安县\正安数据\CJdd.shp"
	explode_m(path1, path2)