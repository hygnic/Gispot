# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
# python2.7
"""
main function: make multiple-parts to single.
因为我的电脑arcgis经常在进行多部件拆解的时候卡死，
所以自己弄了一个拆解小程序。
使用了多线程技术 牛逼！！！！！！！！！
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
# import arcpy
from multiprocessing import Process
from gpconfig import multication
import tooltk


def explode_m(qq, shp_p, new_shp):
	"""
	main function, make multiple-parts to single.
	:param qq: 就是queue
	:param shp_p: shp path which we need to deal with.
	:param new_shp: shp path which saves our result.
	:return:
	"""
	arcpy.env.overwriteOutput = True
	# import time
	# time.sleep(10)
	# print u"程序开始了"
	base = "base.shp"
	# arcpy.env.workspace = r"E:\move on move on\ffff"
	if arcpy.Exists(shp_p):
		infoo = u"开始拆除多部件！\n"
		qq.put(infoo)
		arcpy.MakeFeatureLayer_management(shp_p, base)
		arcpy.MultipartToSinglepart_management(base, new_shp)
		info =  "complete\n"
	else:
		info = u"无法识别文件，请检查文件名和路径是否正确；\n" \
			  u"或者重启程序。\n"
		print(info)
	qq.put(info)


class App(tooltk.Tooltk):
	"""
	main-function's GUI
	"""
	def __init__(self,master_eem):
		"""
		:param master_eem: mian_f, a widget from entrance.py
		"""
		super(App, self).__init__(master_eem,
								  "explode.gc",
								  self.confirm_method_e)
		frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
		# block1
		self.block1 = tooltk.blockShp_in(frame, u"添加SHP文件")
		# block2 取消按钮
		self.block2 = tooltk.blockShp_out(frame, u"选择保存路径")
		self.commu = multication.MuCation()
		
	def confirm_method_e(self):
		# 获取列表
		v =[self.block1.get(),self.block2.get()]
		p = Process(target=self.commu.decor, args=(explode_m, v[0], v[1],))
		p.daemon = True
		p.start()
		self.commu.process_communication(self.major_msgframe)


# if __name__ == '__main__':
# 	path1 = raw_input(u"待输入处理数据：")
# 	path2 = raw_input(u"保存位置")
# 	print u"多部件拆分..."
# 	explode_m(path1, path2)
# 	print u"多部件拆解完成"
