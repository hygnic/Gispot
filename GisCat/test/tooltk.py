# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21

"""所用工具和脚本都调用此GUI"""

import Tkinter as tk
import tkFont
import ttk
import sys
sys.path.append("../GisCat/HyMap")


def fun():
	print " I'm ok"

class Tooltk(object):
	"""工具的GUI界面"""
	def __init__(self):
		self.rootwindow = tk.Tk()
		self.rootwindow.title("Tools")
		self.rootwindow.geometry("500x300")
		self.bg = "Silver"
		self.characterFont1 = tkFont.Font(family="微软雅黑", size=14,
								weight=tkFont.BOLD)
		self.characterFont2 = tkFont.Font(family="微软雅黑", size=10)
		self.button1 = tk.Button(self.rootwindow, text="confirm", bg=self.bg,
			command= self.getvalue , font=self.characterFont2, height=1, fg="black", width=10)
		
		self.buttonttk = ttk.Button(self.rootwindow, text=u'我的按钮')
		# Entry
		self.inputbox1 = tk.Entry(self.rootwindow, show = None,
						  font =self.characterFont2, width = 300)
		self.inputbox2 = tk.Entry(self.rootwindow, show = None,
					      font =self.characterFont2, width = 100)
		# self.exportGUI(fun)

	# def bar(self):
	# 	inputbox = tk.Entry(self.rootwindow, show = None).pack()
	# 	self.rootwindow.mainloop()
	# if __name__ == '__main__':
	# 	Tooltk(fun).bar()
	
	
	def getvalue(self):
		"""按下button触发才会该方法"""
		path = self.inputbox1.get()
		resolution = self.inputbox2.get()
		resolution = int(resolution)
		print path,resolution
		# return [path, resolution]
	
	def GUIexport(self):
		"""使用export_function方法将输入的mxd文档导出为图片 """
		# 信息输入框
		# inputbox1 = tk.Entry(self.rootwindow, show = None,
		# 				 font =self.characterFont2, width = 300)
		# path = inputbox1.get()
		# inputbox2 = tk.Entry(self.rootwindow, show = None,
		# 			 font =self.characterFont2, width = 100)
		self.inputbox1.pack()
		self.inputbox2.pack()

		
		# 确认按钮
		# button = tk.Button(self.rootwindow, text="confirm", bg=self.bg,
	    # command=getvalue,font=self.characterFont2, height=1, fg="black", width=10)
		self.button1.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		self.buttonttk.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		
		# self.rootwindow.mainloop()
		# return [path, resolution]
		
if __name__ == '__main__':
	app = Tooltk()
	app.GUIexport()
	app.rootwindow.mainloop()
	# app.rootwindow.mainloop()

# if __name__ == '__main__':
# 	app = Tooltk()
# 	app.rootwindow.mainloop()