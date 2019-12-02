# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
"""
main function: make multiple-parts to single.
因为我的电脑arcgis经常在进行多部件拆解的时候卡死，
所以自己弄了一个拆解小程序。
使用了多线程技术 牛逼！！！！！！！！！
"""

import arcpy
from multiprocessing import Process,Queue
# from threading import Thread
from hyconf import multication
import tooltk
# import subprocess


def explode_m(shp_p, new_shp):
	"""
	main function, make multiple-parts to single.
	:param shp_p: shp path which we need to deal with.
	:param new_shp: shp path which saves our result.
	:return:
	"""
	arcpy.env.overwriteOutput = True
	# import time
	# time.sleep(10)
	base = "base.shp"
	arcpy.env.workspace = r"E:\move on move on\ffff"
	if arcpy.Exists(shp_p):
		arcpy.MakeFeatureLayer_management(shp_p, base)
		arcpy.MultipartToSinglepart_management(base, new_shp)
		print "complete"
	else:
		print u"无法识别文件，请检查文件名和路径是否正确；\n" \
			  u"或者重启程序。"

# 装饰函数
# def decor(queue, func, *args):
# 	"""
# 	the function has two features:
# 	1:
# 		as a decortor, put out main function inside,
# 		and repalce our main function, then run it by child process.
# 	2:
# 		we can put some message in multiprocessing.Queque, like End message.
# 	question:
# 		can't put this Funtion behide main block, error occur.
# 		due to windows, I can only setup multiprocessing.Queque after main block.
# 	:param queue:  ponit to multiprocessing.Queque's instance.
# 	:param func: main Function (explode_m)
# 	:param args: the set of paths
# 	:return:
# 	"""
# 	info1 = u"多部件拆分...\n"
# 	queue.put(info1)
# 	print queue
# 	print queue.qsize() # 1
# 	print queue.empty() # Ture
# 	func(*args)
# 	info2 = u"多部件拆解完成"
# 	queue.put(info2)
	# while True:
	# 	print q.get() # 多部件拆分...
				  # 多部件已拆解
				  

	
class App(tooltk.Tooltk):
	
	commu = multication.MuCation()
	"""
	main-function's GUI
	"""
	
	def __init__(self):
		super(App, self).__init__(u"拆分多部件",
								  "../docs/explode_mulitp.gc")
		# s = self.window.winfo_children()
		# for i in s:
		# 	print type(i) # <type 'instance'>
		self.single_file_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							   u"选择待处理shp文件")
		self.savename_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							u"选择保存地址")
		self.button_confirm["command"] = self.confirm_method_e
		# self.text_majorMsg.insert("end", "jkjkjkjkkjkk" + "\n")
		# self.text_majorMsg.insert("end", "jkjkjkjkkjkk" + "\n")
		self.window.mainloop()
		

		
	def confirm_method_e(self):
		# 获取列表
		v = self.get_Entry_fromblock(self.input_sfb, self.input_sb)
		# p = Process(target=self.commu.decor, args=( explode_m, v[0], v[1],))
		p = Process(target=self.commu.decor, args=(self.commu.que,
												   explode_m, v[0], v[1],))
		p.start()
		
		print "process_communication: begin"
		# t = Thread(target=self.process_communication)
		# t.start()
		self.commu.process_communication(self.text_majorMsg)
		# self.process_communication(self.q)
		# explode_m(v[0], v[1])
	
		# t = Thread(target=explode_m,args=(v[0], v[1]))
		# t.setDaemon(True)
		# t.start()
		# self.text_majorMsg.insert("end", u"多部件拆分...\n")
		# self.text_majorMsg.insert("end", u"多部件已拆解")

# if __name__ == '__main__':
# 	path1 = raw_input(u"待输入处理数据：")
# 	path2 = raw_input(u"保存位置")
# 	print u"多部件拆分..."
# 	explode_m(path1, path2)
# 	print u"多部件拆解完成"
