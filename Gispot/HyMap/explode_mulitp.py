# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/20
"""
拆分多部件
使用了多线程技术 牛逼！！！！！！！！！
"""

import arcpy
from multiprocessing import Process,Queue
from threading import Thread
import tooltk
# import subprocess


def explode_m(shp_p, new_shp):
	"""
	主功能函数，实现多部件的拆分
	:param shp_p: 需要拆分多部件的shp文件地址
	:param new_shp: 保存地址
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
def decor(queue, func, *args):
	"""
	该函数有两个功能：
	一：
		装饰函数，将我们的功能函数放进去，
		并且会代替原功能函数，被子进程执行。
	二：
		将需要的信息装进multiprocessing.Queque中,比如结束信息。
	问题：
		不能把该函数放到mian块中，会报错。
		不能把multiprocessing.Queque创建在main，会报错，这是Windows的问题
	:param queue: 指向队列multiprocessing.Queque的实例
	:param func: 主要的功能函数
	:param args: 地址的集合
	:return:
	"""
	info1 = u"多部件拆分...\n"
	queue.put(info1)
	print queue
	print queue.qsize() # 1
	print queue.empty() # Ture
	func(*args)
	info2 = u"多部件拆解完成"
	queue.put(info2)
	# while True:
	# 	print q.get() # 多部件拆分...
				  # 多部件已拆解
				  

	
class App(tooltk.Tooltk):
	q = Queue()
	"""
	该功能的GUI调用窗口
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
		self.window.mainloop()
		
	def process_communication(self):
		"""进程数据共享
		主进程开始一个子线程来获取另一个（子进程）的数据
		"""
		while True:
			i = self.q.get()
			self.text_majorMsg.insert("end", i+"\n")
	
	def confirm_method_e(self):
		# 获取列表
		v = self.get_Entry_fromblock(self.input_sfb, self.input_sb)
		p = Process(target=decor, args=(self.q, explode_m, v[0], v[1],))
		p.start()
		
		print "process_communication: begin"
		t = Thread(target=self.process_communication)
		t.start()
		
		# explode_m(v[0], v[1])
	
		# t = Thread(target=explode_m,args=(v[0], v[1]))
		# t.setDaemon(True)
		# t.start()
		# self.text_majorMsg.insert("end", u"多部件拆分...\n")
		# self.text_majorMsg.insert("end", u"多部件已拆解")

if __name__ == '__main__':
	path1 = raw_input(u"待输入处理数据：")
	path2 = raw_input(u"保存位置")
	print u"多部件拆分..."
	explode_m(path1, path2)
	print u"多部件拆解完成"
