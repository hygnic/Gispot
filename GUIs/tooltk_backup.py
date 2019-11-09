# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21

"""所用工具和脚本都调用此GUI"""

import Tkinter as tk
import ttk
import tkFileDialog
import sys
gisTKlists = ["../GisCat/HyMap"]
for gisTKlist in gisTKlists:
	sys.path.append(gisTKlist)
import export_jpeg
import threading

def fun():
	print " I'm ok"

class Tooltk(object):
	"""工具的GUI界面"""
	filepaths = []
	tooltk_variable1 = ""
	
	def __init__(self):
		# 效果未知
		# self.frame_ma.bell(displayof=self.window)
		self.window = tk.Tk()
		self.window.title("Tools")
		self.window.geometry("900x560")
		self.window.iconbitmap(default=r"Icons/toolbox.ico")
		self.input_str_1 = tk.StringVar()
		self.input_str_2 = tk.StringVar()
		self.input_int = tk.IntVar()
		
		self.color_mylife() # 颜色
		self.create_frames() # 配置框架
		self.create_button() # 配置按钮
		# self.other_config() # 其他配置，暂时不摆放
	
	def color_mylife(self):
		self.color1 = "Silver"
		self.color2 = "LemonChiffon"
		self.color3 = "Wheat"
		self.color4 = "Cornsilk"
		self.color5 = "Tea"
	
	def create_frames(self):
			self.frame_side_bar = tk.Frame(height ="560", width ="300",
								   bg=self.color4,border =2 ,relief = "sunken")
			self.frame_major = tk.Frame(height ="310", width ="600",
									bg=self.color3,border =2 ,relief = "sunken")
			# self.frame_middle_bar = tk.Frame(height ="190", width ="700",
			# 						bg='SkyBlue', border =2 ,relief = "sunken")
			self.frame_bottom_bar = tk.Frame(height ="60", width ="700",
									 bg='Beige', border =2 ,relief = "raised")
			self.frame_side_bar.pack(side="right", anchor="e", expand=False, fill="y")
			self.frame_major.pack(side="top", anchor="center",expand=True, fill ="both")
			# self.frame_middle_bar.pack(side="top", anchor="center",expand=True, fill ="both")
			self.frame_bottom_bar.pack(side="top", anchor="center",
									   expand=False, fill ="x")
				# expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
					# x轴（左右）方向上会拉伸
			return 1


	def create_button(self):
		"""三个基础按键配置 确认，帮助详情和退出"""
		# self.characterFont1 = tkFont.Font(family="微软雅黑", size=14,
		# 						weight=tkFont.BOLD)
		# self.characterFont2 = tkFont.Font(family="微软雅黑", size=10)
		# self.button1 = tk.Button(self.window, text="confirm", bg=self.bg,
		# 	command= self.getvalue, font=self.characterFont2, height=1,
		# 	fg="black", width=10)
		# self.buttonttk = ttk.Button(self.window, text=u'我的按钮')
		# Entry
		# self.inputbox1 = tk.Entry(self.frame_major, show = None,
		# 						  font =self.characterFont2, width = 300)
		# self.inputbox2 = tk.Entry(self.frame_major, show = None,
		# 						  font =self.characterFont2, width = 100)
		# self.exportGUI(fun)
		self.button_confirm = ttk.Button(self.frame_bottom_bar, text=u'确认')
		self.button_help = ttk.Button(self.frame_bottom_bar, text=u'帮助详情')
		self.button_quit = ttk.Button(self.frame_bottom_bar, text=u'退出',
									  command=self.window.quit)
		self.button_confirm.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E, padx=5)
		self.button_help.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E, padx=5)
		self.button_quit.pack(side=tk.RIGHT, expand=tk.NO, anchor=tk.E, padx=5)
		# buttonttk["command"] = self.kk
		return 1
	
	


	
	def normal_single_block(self):
		"""主Frame中的功能块"""
		

			
		self.label_1 = tk.Label(self.frame_major, text="label one",
								bg=self.color3)
		self.label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
			# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major,height ="60", width ="700",
							 bg=self.color3, pady = 4) # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center",expand=False, fill ="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one, text = u"选择",
									command = self.select_file)
		self.addfile_button.pack(side=tk.RIGHT,anchor=tk.CENTER, padx=10)
		# Entry
			# 也可以将input_msg设置成类属性，方便在select_file中刷新
		# input = "msg"+str(block_num)
		self.input_box1 = tk.Entry(frame_one, textvariable=self.input_str_1, text = "input_box1",
							   border = 2,relief = tk.GROOVE)
		self.input_box1.pack(side=tk.LEFT,anchor=tk.W, expand= True,
						fill = tk.X, padx=15)
		# input_msg.set(one_file_path)
		return 1

	# @staticmethod
	def select_file(self):
		# global tooltk_variable1
		tooltk_variable1 = tkFileDialog.askopenfilename(filetypes=
						 [(u'文本文档', '*.txt'),('All Files', '*')])
		# 刷新normal_single_block() 中的Entry
		self.input_str_1.set(tooltk_variable1)
		# print(one_file_path)


		# 确认按钮
		# button = tk.Button(self.rootwindow, text="confirm", bg=self.bg,
	    # command=getvalue,font=self.characterFont2, height=1, fg="black", width=10)
		# button1.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		
		
		# self.rootwindow.mainloop()
		# return [path, resolution]
	

		
# if __name__ == '__main__':
# 	app = Tooltk()
# 	# app.create_button().button_help["command"] = app.openfile
# 	# app.GUIexport()
# 	app.window.mainloop()
# 	# app.rootwindow.mainloop()

# if __name__ == '__main__':
# 	app = Tooltk()
# 	app.rootwindow.mainloop()

if __name__ == '__main__':
	class App(Tooltk):
		def __init__(self):
			super(App, self).__init__()
			self.window.title(u"两区公示图命名规范化")
			
		# def create_button(self):
			self.normal_single_block()
			self.label_1["text"] = u"文本文档"
			
			# block2
			self.normal_single_block()
			self.input_box1["textvariable"] = self.input_str_2
			
			
			self.label_1["text"] = u"图片文件夹"
			# self.addfile_button["state"] = "disabled"
			# self.addfile_button.pack_forget() # 隐藏模块
			# self.addfile_button.destroy()	# 隐藏模块
			
			
	app = App()
	app.window.mainloop()











# 	def GUIexport(self, *arg):
# 		"""使用export_function方法将输入的mxd文档导出为图片 """
#
# 		# 信息输入框
# 		# inputbox1 = tk.Entry(self.rootwindow, show = None,
# 		# 				 font =self.characterFont2, width = 300)
# 		# path = inputbox1.get()
# 		# inputbox2 = tk.Entry(self.rootwindow, show = None,
# 		# 			 font =self.characterFont2, width = 100)
# 		def getvalue():
# 			"""按下button触发才会该方法"""
# 			path = self.inputbox1.get()
# 			resolution = self.inputbox2.get()
# 			resolution = int(resolution)
# 			print path, resolution
# 			# self.thread_it(export(path, resolution))
# 			export_jpeg.export(path, resolution)
#
# # button1 = tk.Button(self.window, text="confirm", bg=self.bg,
# # 						 command=getvalue,
# # 						 font=self.characterFont2, height=1, fg="black",
# # 						 width=10)
#
# # self.inputbox1.pack()
# # self.inputbox2.pack()