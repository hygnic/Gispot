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

# import arcpy
from multiprocessing import Process
# from threading import Thread
from GUIconfig import multication
import tooltk
from GUIconfig import paths
# import subprocess

em_path = paths.DocPath.doc_em

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
		print info
	qq.put(info)


class App(tooltk.Tooltk):
	commu = multication.MuCation()
	"""
	main-function's GUI
	"""
	def __init__(self,master_eem):
		"""
		:param master_eem: mian_f, a widget from entrance.py
		"""
		super(App, self).__init__(master_eem,
								  em_path,
								  self.confirm_method_e)
		# s = self.window.winfo_children()
		# for i in s:
		# 	print type(i) # <type 'instance'>
		self.single_file_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							   u"选择待处理shp文件")
		self.save_path_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							u"选择保存地址")
		self.window.mainloop()
		
	def confirm_method_e(self):
		# 获取列表
		v = self.get_blockvalue(self.input_sfb, self.input_sb)
		# p = Process(target=self.commu.decor, args=( explode_m, v[0], v[1],))
		p = Process(target=self.commu.decor, args=(self.commu.que,
												   explode_m, v[0], v[1],))
		p.start()
		print "process_communication begin"
		# t = Thread(target=self.process_communication)
		# t.start()
		self.commu.process_communication(self.text_major_msg)
		# self.process_communication(self.q)
		# explode_m(v[0], v[1])
	
		# t = Thread(target=explode_m,args=(v[0], v[1]))
		# t.setDaemon(True)
		# t.start()
		# self.text_major_msg.insert("end", u"多部件拆分...\n")
		# self.text_major_msg.insert("end", u"多部件已拆解")

# if __name__ == '__main__':
# 	path1 = raw_input(u"待输入处理数据：")
# 	path2 = raw_input(u"保存位置")
# 	print u"多部件拆分..."
# 	explode_m(path1, path2)
# 	print u"多部件拆解完成"
