# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21

"""所用工具和脚本都调用此GUI"""

import Tkinter as tk
import os
import ttk
import tkFileDialog
# import sys
# # gisTKlists = ["../GisCat/HyMap"]
# for gisTKlist in gisTKlists:
# 	sys.path.append(gisTKlist)
# import export_jpeg
# import threading


class Tooltk(object):
	"""工具的GUI界面"""
	# 调用类变量也要加self
	block_list = []
	file_path_ = "23"
	
	def __init__(self, window_name):
		# 效果未知
		# self.frame_ma.bell(displayof=self.window)
		self.window = tk.Toplevel()
		self.window.title(window_name)
		# 给Toplevel窗口设置透明度
		# self.window.attributes('-alpha',0.5)
		# 设置窗口置顶优先度
		# self.window.attributes('-topmost', 1)
		# self.window = tk.Tk()
		self.window.geometry("800x660")
		# self.window.iconbitmap(default=os.path.dirname(__file__)+
		# 							   "/Icons/toolbox.ico")
		# 重新抓取设置，使Toplevel显示在最上面
		self.window.grab_set()
		# self.window.resizable(False, False)
		# self.input_str_1 = tk.StringVar()
		# self.input_str_2 = tk.StringVar()
		# self.input_int = tk.IntVar()
		self.color_mylife() # 颜色
		self.create_frames() # 配置框架
		self.create_button() # 配置按钮
		
	def color_mylife(self):
		self.color1 = "Silver"
		self.color2 = "LemonChiffon"
		self.color3 = "Wheat"
		self.color4 = "Cornsilk"
		self.color5 = "Tea"
	
	def create_frames(self):
			self.frame_side_bar = tk.LabelFrame(self.window,
												width ="500",bg=self.color4,
												border =2 ,relief = "groove")
			self.frame_major = tk.Frame(self.window, height ="310", width = "400"
										,bg=self.color3, border =2, relief =
										"sunken")
			# self.frame_middle_bar = tk.Frame(self.window,height ="190", width ="700",
			# 						bg='SkyBlue', border =2 ,relief = "sunken")
			self.frame_bottom_bar = tk.Frame(self.window,height ="60",
									 bg='Beige', border =2 ,relief = "raised")
			self.frame_side_bar.pack(side="right", anchor="e", expand = False,
									 fill="y")
			self.frame_major.pack(side="top", anchor="center",
								  expand=True, fill="both")
			# self.frame_middle_bar.pack(side="top", anchor="center",expand=True, fill ="both")
			self.frame_bottom_bar.pack(side="top", anchor="center",
									   expand=False,fill ="x")
				# expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
					# x轴（左右）方向上会拉伸
			self.text = tk.Text(self.frame_side_bar,
								width = "50",bg = "Tan")
			self.text.insert(tk.END,"okokokokoy7")
			self.text.pack(expand = True, fill = "y",padx=2)
			# tk.Label(self.frame_side_bar,
			# 		 text=u"处理详情",
			# 		 font=("Times",0,"bold"),
			# 		 bg = self.color4
			# 		 ).grid(row = 1)
			# tk.Label(self.frame_side_bar,
			# 		 text=u"一大推处理结果方法辅导费多付多付多
			# 		 付多付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付",
			# 		 wraplength = "100",
			# 		 height="0",
			# 		 width="0").grid(row = 1, sticky = "w")
			# expand = False, fill = None,
			return 1

	def create_button(self):
		self.button_confirm = ttk.Button(self.frame_bottom_bar, text=u'确认')
		self.button_help = ttk.Button(self.frame_bottom_bar, text=u'帮助详情')
		self.button_quit = ttk.Button(self.frame_bottom_bar, text=u'退出',
									  command=self.window.destroy)
		self.button_confirm.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E,
								 padx=5)
		self.button_help.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E, padx=5)
		self.button_quit.pack(side=tk.RIGHT, expand=tk.NO, anchor=tk.E, padx=5)
		# buttonttk["command"] = self.kk
		return 1
	
	def single_file_block(self,sfb_filetype,sfb_name):
		# sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		"""
		sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
		# 文件选取菜单
		def select_file():
			# global file_path
			file_path = tkFileDialog.askopenfilename(filetypes=sfb_filetype)
			# 刷新normal_single_block() 中的Entry
			# self.block_list.append(file_path)
			input_msg1.set(file_path)
			
		self.label_1 = tk.Label(self.frame_major, text= sfb_name,
								bg=self.color3)
		self.label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
			# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major,height ="60", width ="700",
							bg=self.color3, pady = 4) # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center",expand=False, fill ="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one, text = u"选择",command =
										select_file)
		self.addfile_button.pack(side=tk.RIGHT,anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sfb = tk.Entry(frame_one, textvariable=input_msg1,
								  border = 2, relief = tk.GROOVE)
		self.input_sfb.pack(side=tk.LEFT, anchor=tk.W, expand= True,
							fill = tk.X, padx=15)
		# input_msg.set(one_file_path)
		return 1
	
	def single_dir_block(self,sdb_name):
		"""
		sdb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件夹  传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
		
		def select_file():
			# global file_path
			file_path = tkFileDialog.askdirectory()
			# 刷新normal_single_block() 中的Entry
			input_msg1.set(file_path)
		
		self.label_2 = tk.Label(self.frame_major, text=sdb_name,
								bg=self.color3)
		self.label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 bg=self.color3,
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one, text=u"选择", command=
		select_file)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sdb = tk.Entry(frame_one, textvariable=input_msg1, border=2,
								  relief=tk.GROOVE)
		self.input_sdb.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							padx=15)
		# input_msg.set(one_file_path)
		return 1
	
	def single_int_block(self, gib_name):
		"""
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
		self.label_3 = tk.Label(self.frame_major, text=gib_name,
								bg=self.color3)
		self.label_3.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 bg=self.color3, pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		self.addfile_button = ttk.Button(frame_one, text=u"选择", command=
		None)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sib = tk.Entry(frame_one, textvariable=input_msg1, border=2,
								  relief=tk.GROOVE)
		# , state = "readonly"
		self.input_sib.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							padx=15)
		# input_msg.set(one_file_path)
		return 1

	def get_Entry_fromblock(self,*arg):
		"""
		获取Entry值，组成列表
		:param arg: 各个block的Entry模块组成的元组
		:return:
		"""
		for i in arg:
			# 由于Entry输出纯英文数字时是str格式，为方便后续进行，
				# 将str转换为unicode
			msg = i.get()
			if type(msg) == type("str"):
				msg = msg.decode("cp936")
				self.block_list.append(msg)
			else:
				# unicode格式的直接加进去
				self.block_list.append(msg)
		# got_msg1 = arg[0].get()
		# # .decode("cp936")
		# got_msg2 = arg[1].get()
		# self.block_list.append(got_msg1)
		# self.block_list.append(got_msg2)


if __name__ == '__main__':
	class App(Tooltk):
		def __init__(self):
			super(App, self).__init__(u"本地实验")
			self.button_confirm["command"] = self.confirm_method
			# block 1
			self.single_file_block([(u'文本文档', '*.txt'), ('All Files', '*')],
								   u"文本文档")
			# block2
			self.single_dir_block(u"图片文件夹")
			# self.addfile_button["state"] = "disabled"
			# self.addfile_button.pack_forget() # 隐藏模块
			# self.addfile_button.destroy()	# 隐藏模块
			# 触发命令获取Entry的值
		
			
		def confirm_method(self):
			self.get_Entry_fromblock(self.input_sfb,self.input_sdb)
			print "self.block_list: ",self.block_list
			for i in self.block_list:
				print i," type: ",type(i)
			#重置
			self.block_list = []
			"""
			文件
			filedialog: C:/Users/hygnic/Desktop/打开host.txt  type:  <type 'unicode'>
			filedialog: C:/Users/hygnic/Desktop/204863.txt  type:  <type 'str'>
			文件夹
			filedialog+手动: E:/move on move on/是多少  type:  <type 'unicode'>
			手动: G:\软件包  type:  <type 'unicode'>
			手动: G:\music  type:  <type 'str'>
			filedialog: E:/move on move on/GisCat/bin  type:  <type 'str'>
			filedialog: E:/move on move on/公示图  type:  <type 'unicode'>
			结论:
			"""
			
	app = App()
	app.window.mainloop()
	# print app.block_list
