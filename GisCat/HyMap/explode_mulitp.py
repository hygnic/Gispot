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
def outer(queue, func, *args):
	"""
	装饰函数，将我们的功能函数放进去
	:param queue: 指向队列multiprocessing.Queque的实例
	:param func: 主要的功能函数
	:param args: 地址的集合
	:return:
	"""
	info1 = u"多部件拆分...\n"
	queue.put(info1)
	func(args[0], args[1])
	info2 = u"多部件已拆解"
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
								  "docs/explode_mulitp.gc")
		# s = self.window.winfo_children()
		# for i in s:
		# 	print type(i) # <type 'instance'>
		self.single_file_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							   u"选择待处理shp文件")
		self.savename_block([(u'shapefile', '*.shp'), ('All Files', '*')],
							u"选择保存地址")
		self.button_confirm["command"] = self.confirm_method_q
		self.window.mainloop()
		
	def process_communication(self):
		
		while True:
			i = self.q.get()
			self.text_majorMsg.insert("end", i+"\n")
			# self.text_majorMsg.insert("end", u"多部件已拆解")
	
	def confirm_method_q(self):
		# 获取列表
		v = self.get_Entry_fromblock(self.input_sfb, self.input_sb)
		p = Process(target=outer, args=(self.q,explode_m,v[0], v[1],))
		# self.text_majorMsg.insert("end", u"多部件拆分...\n")
		p.start()
		print self.q
		print self.q.qsize()
		print self.q.empty()
		print u"t begin"
		t = Thread(target=self.process_communication)
		t.start()
		
		# explode_m(v[0], v[1])
	
		# t = Thread(target=explode_m,args=(v[0], v[1]))
		# t.setDaemon(True)
		# t.start()
		# self.text_majorMsg.insert("end", u"多部件已拆解")

if __name__ == '__main__':
	path1 = raw_input(u"待输入处理数据：")
	path2 = raw_input(u"保存位置")
	print u"多部件拆分..."
	explode_m(path1, path2)
	print u"多部件已拆解"
