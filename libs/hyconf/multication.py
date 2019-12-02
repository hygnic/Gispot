# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/1
"""
multiprocess communication两个单词的组合  > _ < !!!
The class contains some fuctions about a GUI how to coummnication with
we feature function. Mostly use Queue to comply.
"""

from multiprocessing import Process,Queue
from threading import Thread
import os


class MuCation(object):
	
	"""
	multiprocess communication
	"""
	# instance of multiprocessing.Queue()
	_q = Queue()
	@property
	def que(self):
		return self._q
	
	
	def decor(self, queue,  func, *args):
		
		"""
			这里必须传入参数queue，因为multiprocessing.Queue只能在mian下建立
		才能实现它的功能（数据交流），设置该参数，让他在被调用时，重伸一下Queue，
		且是在main块下被调用的，这样就能实现功能。如果不这样的话，queue.get()
		获取不到值。
		
		the function has two features:
		1:
			as a decortor, put out main function inside,
			and repalce our main function, then run it by child process.
		2:
			we can put some message in multiprocessing.Queque, like End message.
		question:
			can't put this Funtion behide main block, error occur.
			due to windows, I can only setup multiprocessing.Queque after main
			block.
		:param queue: point to multiprocessing.Queue()
		:param information:
		:param func: main Function (explode_m)
		:param args: the set of paths
		:return:
		"""
		info1 = u"<ProcessID: {}> 任务开始...\n".format(os.getpid())
		queue.put(info1)
		# queue.put(information)
		print queue
		print queue.qsize()  # 1
		print queue.empty()  # Ture
		func(queue,*args)
		info2 = u"<ProcessID: {}> 任务结束。\n".format(os.getpid())
		queue.put(info2)
	
	
	def process_communication(self, text):
		
		"""
		sharing messages with some Process.
		The main process starts a child thread to get messages from another
		(child process)
		:param text: Tkinter.text  我们使用的这个 self.text_majorMsg
		:return:
		"""
		def inner():
			# 因为是阻塞操作，另起一子线程循环监听Queue，否则会导致GUI界面卡死。
			while True:
				i = self.que.get()
				
				if i.startswith("<ProcessID"):
					text.tag_config("tag_1", backgroun="yellow",
									foreground="red")
					text.insert("end", " " + i,"tag_1")
					# "\n  " + 反而会冒出一个空行
				else:
					text.insert("end", " " + i)
		
		t = Thread(target=inner)
		t.start()

	
