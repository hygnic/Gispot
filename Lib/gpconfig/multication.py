#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author: liaochenchen, hygnic
# Created on: 2019/12/1
# python2.7
# Reference:
# Python multiprocessing redirect stdout of a child process to a Tkinter Text
# https://stackoverflow.com/questions/23947281/python-multiprocessing-redirect-stdout-of-a-child-process-to-a-tkinter-text
	
"""
Description:
	multiprocess communication两个单词的组合  !!!
	The class contains some fuctions about a GUI how to coummnication with
	we feature function. Mostly use Queue to comply.
"""
from __future__ import absolute_import
from multiprocessing import Queue
from threading import Thread
import threading
import os
import sys

from hybag import hybasic

hyt = hybasic.HyTime()

class StdoutQueue(object):
	"""
	TypeError: Error when calling the metaclass bases
	function() argument 1 must be code, not str
	"""
	# singleton pattern
	_instance_lock = threading.Lock()
	def __new__(cls, *args, **kwargs):
		if not hasattr(StdoutQueue, "_instance"):
			with StdoutQueue._instance_lock:
				if not hasattr(StdoutQueue, "_instance"):
					StdoutQueue._instance = object.__new__(cls)
		return StdoutQueue._instance
	
	def __init__(self,*args,**kwargs):
		# ctx = multiprocessing.get_context()
		self.inner_que = Queue()
		
	def write(self, msg):
		self.inner_que.put(msg)
		
	def put(self,msg):
		self.inner_que.put(msg)
	
	# 可传输tag内容
	# def append_tag(self,msg,tag):
	# 	self.inner_que.put(msg)
	# 	self.inner_que.put(tag)
	
	def append(self, msg):
		self.inner_que.put(msg)
		
	def get(self):
		return self.inner_que.get()
	
	# def get_tag(self):
	# 	msg = self.inner_que.get()
	# 	tag = self.inner_que.get()
	# 	return msg,tag
		
	def flush(self):
		sys.__stdout__.flush()
	
	def close(self):
		self.inner_que.close()
		

# import traceback
# def except_hook_func(tp, val, tb):
# 	trace_info_list = traceback.format_exception(tp, val, tb)
# 	trace_str = ' '.join(trace_info_list)
# 	info1 = 'sys.excepthook'
# 	f = open("D:\\1.txt", "a")
# 	f.write(info1)
# 	f.write(trace_str)
# 	sys.stderr.write(info1)
# 	sys.stderr.write(trace_str)
# 	f.close()


class MuCation(object):
	"""
	功能一：新开一个进程执行指定的方法
	功能二：进程之间的通信
	"""
	submultiprocess = []  # 子进程的列表
	
	# singleton pattern
	_instance_lock = threading.Lock()
	def __new__(cls, *args, **kwargs):
		if not hasattr(MuCation, "_instance"):
			with MuCation._instance_lock:
				if not hasattr(MuCation, "_instance"):
					MuCation._instance = object.__new__(cls)
		return MuCation._instance
	
	def __init__(self):
		# self.que = Queue()
		self.que = StdoutQueue()
		# sys.stdout = self.que
		# If we redirect stdout to Tkinter text, some errors occur and i
		# don't know why at all
		# 1.issue
		# Sometime, after standalone windows program run a function finished or
		# error occur, the GUI interface disapper immediately.
		# 2.issue
		# Sometime, it just errors occur when I run a function(with standalone
		# windows program) which I have never encountered before
	
		# aa = "ssssdddd"  # TODO 运行程序时为什么会重复打印4次？
		# print aa
		# print id(self.que)
	
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
		pid = os.getpid()
		begin_info1 = "<ProcessID: {}> Running\n".format(pid) # BEGIN\n
		begin_time = hyt.time_now
		begin_info2 = "<ProcessID: {}> Begin time: {}\n".format(pid,begin_time[1])
		self.que.put(begin_info1)
		self.que.put(begin_info2)
		self.que.put("\n")
		# queue.put(information)
		# print queue
		# print queue.qsize()  # 1
		# print queue.empty()  # Ture
		func(self.que, *args)
		end_time = hyt.time_now
		end_info = "<ProcessID: {}> CLOSE\n".format(pid)
		end_info2 = "<ProcessID: {}> End time: {}\n".format(pid,end_time[1])
		self.que.put("\n")
		self.que.put(end_info)
		self.que.put(end_info2)
		elapsed_time = hyt.elapsed_time(begin_time[0], end_time[0])
		end_info3 = "<ProcessID: {}> {}\n".format(pid, elapsed_time)
		self.que.put(end_info3)
		
		self.submultiprocess.append(os.getpid()) # 将已结束进程的进程号加入列表
		
	def process_communication(self, output_window):
		"""
		sharing messages with some Process.
		The main process starts a child thread to get messages from another
		(child process)
		output_window(): Tkinter.text  我们使用的这个 self.major_msgframe
		"""
		
		def inner():
			# 因为是阻塞操作，另起一子线程循环监听Queue，否则会导致GUI界面卡死。
			while True:
				i = self.que.get()
				# 给带有 "<ProcessID" 字符的行整上颜色
				if i.startswith("<ProcessID"):
					# tag_1 在 major_msgframe 处已经配置
					output_window.insert("end", " "+i, "tag_info")
					output_window.see("end")
				# "\n  " + 反而会冒出一个空行
				else:
					output_window.insert("end", " "+i)
					output_window.see("end")
		
		t = Thread(target=inner)
		t.setDaemon(True)  # TODO 如果主进程结束，queue管道中尚且有值就被关闭了
		t.start()
		# t.join() # 主-子线程同步，开启后会使GUI界面阻塞

	
if __name__ == '__main__':
	MuCation()