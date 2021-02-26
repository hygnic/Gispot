# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/5

# 卡死示例
"""
import Tkinter as tk
import ttk
import time

class Tooltk(object):
	def __init__(self):
		self.window = tk.Tk()
		self.window.remove_sth("Tools")
		self.window.geometry("900x800")
		self.bt = ttk.Button(text = "confirm", command = self.bar).pack()
		
	
	def bar(self):
		time.sleep(10)
		

app = Tooltk()
app.window.mainloop()

"""

"""
睡眠10秒
"""


import Tkinter as tk
import ttk
import time
from threading import Thread

class Tooltk(object):
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Tools")
		self.window.geometry("300x400")
		self.bt = ttk.Button(text="confirm", command=self.th)\
			.pack(expand = True)
	
	def func_sleep(self):
		time.sleep(10)

	def th(self):
		# 就是生成的子线程
		t = Thread(target=self.func_sleep)
		t.setDaemon(True)  # 就是设置子线程随主线程的结束而结束
		t.start()
		# t.join()  #
		print "ok"
app = Tooltk()
app.window.mainloop()