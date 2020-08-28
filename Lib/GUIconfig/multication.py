#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author: liaochenchen, hygnic
# Created on: 2019/12/1
# python2.7
"""
Description:
	multiprocess communication两个单词的组合  !!!
	The class contains some fuctions about a GUI how to coummnication with
	we feature function. Mostly use Queue to comply.
"""

from multiprocessing import Queue
from threading import Thread
import os


class MuCation(object):
	"""
	功能一：新开一个进程执行指定的方法
	功能二：进程之间的通信
	"""
	# instance of multiprocessing.Queue()
	# _q = Queue()
	# @property
	# def que(self):
	# 	return self._q
	def __init__(self):
		self.que = Queue()
	
	def decor(self, func, *args):
		"""
		新开一个进程执行指定的方法
		the function has two features:
		1:
			as a decortor, put out main_function inside,
			and repalce our main_function, then run it by child process.
		2:
			we can put some message in multiprocessing.Queque, like End message.
		question:
			1.can't put this Funtion behide main block, error occur.
			2.due to windows, I can only setup multiprocessing.Queque after main
			block.
			3.staticmethod not support
		:param func: main Function (explode_m)
		:param args:
		:return:
		"""
		info1 = "<ProcessID: {}> BEGIN\n".format(os.getpid())
		# self.que.put("\n")
		self.que.put(info1)
		# queue.put(information)
		# print queue
		# print queue.qsize()  # 1
		# print queue.empty()  # Ture
		func(self.que, *args)
		info2 = "<ProcessID: {}> CLOSE\n".format(os.getpid())
		self.que.put("\n")
		self.que.put(info2)
	
	
	def process_communication(self, output_window):
		"""
		sharing messages with some Process.
		The main process starts a child thread to get messages from another
		(child process)
		:param output_window: Tkinter.text  我们使用的这个 self.major_msgframe
		:return:
		"""
		def inner():
			# 因为是阻塞操作，另起一子线程循环监听Queue，否则会导致GUI界面卡死。
			while True:
				i = self.que.get()
				# 给带有 "<ProcessID" 字符的行整上颜色
				if i.startswith("<ProcessID"):
					# tag_1 在 major_msgframe 处已经配置
					output_window.insert("end", " " + i,"tag_info")
					output_window.see("end")
					# "\n  " + 反而会冒出一个空行
				else:
					output_window.insert("end", " " + i)
					output_window.see("end")
		t = Thread(target=inner)
		t.start()

	
