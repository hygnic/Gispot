# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/23

import Tkinter as tk
import time
import ttk
import threading
from multiprocessing import Process

songs = ['爱情买卖', '朋友', '回家过年', '好日子']
films = ['阿凡达', '猩球崛起',"心机穿越"]


class Application(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		
		self.createUI()
	
	# 生成界面
	def createUI(self):
		self.text = tk.Text(self)
		self.text.pack()
		
		tk.Button(self, text='音乐',
				  command=lambda: self.thread_it(self.music, songs)).pack(
			expand=True, side=tk.RIGHT)  # 注意lambda语句的作用！
		tk.Button(self, text='电影',
				  command=self.movie_t).pack(
			expand=True, side=tk.LEFT)
	
	
	# 逻辑：听音乐
	def music(self, songs):
		for x in songs:
			self.text.insert(tk.END, "听歌曲：%s \t-- %s\n" % (x, time.ctime()))
			print("听歌曲：%s \t-- %s" % (x, time.ctime()))
			time.sleep(2)
	
	
	# 逻辑：看电影
	def movie(self, films):
		for x in films:
			self.text.insert(tk.END, "看电影：%s \t-- %s\n" % (x, time.ctime()))
			print("看电影：%s \t-- %s" % (x, time.ctime()))
			time.sleep(2)
	
	# 逻辑：添加按键
	def add_button(self):
		while True:
			# ttk.Button(self,text="here am I").pack()
			tk.Button(self,text="here am I").pack()
			time.sleep(2)
	
	# 打包进线程（耗时的操作）
	@staticmethod
	def thread_it(func, *args):
		t = threading.Thread(target=func, args=args)
		t.setDaemon(True)  # 守护
		t.start()  # 启动

	
	def movie_t1(self):
		self.thread_it(self.movie, films)
		
	def movie_t(self):
		self.thread_it(self.add_button)
		
	
# t.join()          # 阻塞--会卡死界面！

if __name__ == '__main__':
	
	app = Application()
	app.mainloop()