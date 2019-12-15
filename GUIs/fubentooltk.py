# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21
# python2.7
"""所用工具和脚本都调用此GUI"""

import Tkinter as tk
import ttk
import tkFileDialog
import ScrolledText as stt
import os



# 导入配置包
from hyconf import luitils


# import sys
# # gisTKlists = ["../Gispot/ccarcpy"]
# for gisTKlist in gisTKlists:
# 	sys.path.append(gisTKlist)
# import export_jpeg
# import threading


class Tooltk(object):
	"""工具的GUI界面"""
	# 调用类变量也要加self
	block_list = []
	file_paths_ = []
	
	def __init__(self, window_name, help_path):
		"""
		:param window_name: 窗口名字
		:param help_path: 帮助文档的路径
		"""
		self.window = tk.Toplevel()
		self.window.title(window_name)
		self.helppath = help_path
		# self.window.overrideredirect(True)
		# 给Toplevel窗口设置透明度
		# self.window.attributes('-alpha',0.5)
		# 设置窗口置顶优先度
		# self.window.attributes('-topmost', 1)
		# self.window = tk.Tk()
		luitils.screen_cetre(self.window, width=800, height=660)
		# self.window.iconbitmap(default=os.path.dirname(__file__)+
		# 							   "/Icons/toolbox.ico")
		# 重新抓取设置，使Toplevel显示在最上面
		self.window.grab_set()
		# self.window.grab_release()
		# self.window.resizable(False, False)
		# self.input_str_1 = tk.StringVar()
		# self.input_str_2 = tk.StringVar()
		# self.input_int = tk.IntVar()
		self.color_mylife()  # 颜色
		self.icon_set()  # 配置图片
		self.create_frames()  # 配置框架
		self.create_button()  # 配置按钮
		self.read_help()
	
	def color_mylife(self):
		self.color1 = "#F1F1F1"  # 帮助栏颜色
		self.color5 = "Olive"  # 橄榄色，显示text
		self.color3 = "#F1F1F1"  # 主框的上半部分颜色 侧栏颜色
		# self.color4 = "Cornsilk" # 侧栏颜色
		self.color2 = "#E1E1E1"  # 茶色 较深
		self.color6 = '#EBEEEE'  # 底栏颜色
	
	def icon_set(self):
		dir_n = os.path.dirname(__file__)
		self.gif_text16 = tk.PhotoImage(file=
										os.path.join(dir_n,
													 r"Icons\Text_File16.gif"))
		# self.gif_text32 = tk.PhotoImage(file=r'GUIs\Icons\Text_File32.gif')
		self.gif_folder16 = tk.PhotoImage(file=os.path.join(dir_n,
													 r"Icons\Folder16.gif"))
		# self.gif_folder32 = tk.PhotoImage(file=r'GUIs\Icons\Folder32.gif')
		self.gif_close16 = tk.PhotoImage(file=os.path.join(dir_n,
													 r"Icons\Close16.gif"))
		# self.gif_close32 = tk.PhotoImage(file=r'GUIs\Icons\Close32.gif')
		self.gif_quit = tk.PhotoImage(file=os.path.join(dir_n,
													 r"Icons\Close16.gif"))
		self.gif_confirm = tk.PhotoImage(file=os.path.join(dir_n,
											 r"Icons\GenericCheckMarkGreen16.gif"))
		self.gif_help = tk.PhotoImage(
			file=os.path.join(dir_n, r"Icons\GenericInformationBubble16.gif"))
		# ph = tk.PhotoImage(file=r'GUIs\Icons\checked.gif')
		# self.gif_comfirm =  ph.zoom(x= 2,y = 2)
		# self.gif_comfirm =  ph.subsample(x= 40,y=40)
		
		"""
		使用pillow设置按键图标
		from PIL import Image, ImageTk
		self.gif_comfirm = ph
		# test
		im = Image.open(r"E:\move on move on\Gispot\GUIs\66.png")
		self.ph_im = ImageTk.PhotoImage(im)
		"""
		
	
	def create_frames(self):
		# 侧边栏
		self.frame_side_bar = tk.Frame(self.window,
									   width="500",
									   border=2, relief="groove")
		self.frame_side_bar.pack(side="right", anchor="e",
								 expand=False, fill="y")
		# 左边的主框
		self.frame_major = tk.Frame(self.window, height="310",
									width="400",
									border=2, relief="sunken")
		self.frame_major.pack(side="top", anchor="center",
							  expand=True, fill="both")
		# 主框下的底部栏
		self.frame_bottom_bar = tk.Frame(self.window, height="60",
										 bg=self.color6, border=2,
										 relief="raised")
		self.frame_bottom_bar.pack(side="top", anchor="center",
								   expand=False, fill="x")
		# expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
		# x轴（左右）方向上会拉伸
		# 主框中的帮助信息
		help_f = tk.LabelFrame(self.frame_major,
							   relief=tk.RIDGE, width="500",
							   text="____" * 80, bd=2, fg=self.color5)
		help_f.pack(side=tk.BOTTOM, anchor="center",
					expand=True, fill="both")
		# 设置带滚动条的text
		s_bar = tk.Scrollbar(help_f, relief="flat",
							 elementborderwidth=-15)
		s_bar.pack(side="right", fill="y")
		self.help_text = tk.Text(help_f, relief=tk.FLAT,
								 fg=self.color5, yscrollcommand=s_bar.set)
		
		self.help_text.pack(expand=True, fill="both")
		s_bar.config(command=self.help_text.yview)
		
		""""
			侧边框插入文本框，文本框分成上下两部分，上部分显示固定的信息，
		下半部分显示动态信息"""
		# 上栏
		self.text = stt.ScrolledText(self.frame_side_bar, height="10",
									 width="60")
		# 不起作用，将所用txt都标记了
		# self.text.tag_add("tag1","1.end","2.end")
		self.text.insert(tk.END,
						 "Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, "
						 "15:19:22) author: Liaochenchen") #,"tag1"
		# self.text.tag_config("tag1",underline = True,foreground = "Ivory")
		self.text.pack(side="top", anchor="n", expand=False,
					   padx=2)
		# 下栏 主要的动态信息显示栏
		s_bar = tk.Scrollbar(self.frame_side_bar, relief="flat",
							 elementborderwidth=-15)
		s_bar.pack(side="right", fill="y")
		self.text_majorMsg = tk.Text(self.frame_side_bar, height="10",
									 width="60", yscrollcommand=s_bar.set,
									maxundo = 15, undo =True)
									# 支持撤销操作，支持换行 wrap = "char"
		self.text_majorMsg.insert(tk.END,">>>"*20)
		self.text_majorMsg.pack(side="top", anchor="n", expand=True,
								fill=tk.Y, padx=2)
		s_bar.config(command=self.text_majorMsg.yview)
		
		# tk.Label(self.frame_right_side,
		# 		 text=u"处理详情",
		# 		 font=("Times",0,"bold"),
		# 		 bg = self.color4
		# 		 ).grid(row = 1)
		# tk.Label(self.frame_right_side,
		# 		 text=u"一大推处理结果方法辅导费多付多付多
		# 		 付多付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付付",
		# 		 wraplength = "100",
		# 		 height="0",
		# 		 width="0").grid(row = 1, sticky = "w")
		# expand = False, fill = None,
		
		return 1
	
	# 读取帮助信息并插入帮助框中
	def read_help(self):
		"""
		读取帮助信息并插入帮助框中
		:return:
		"""
		filename = self.helppath
		with open(filename, "r") as read_msgs:
			for read_line in read_msgs.readlines():
				self.help_text.insert(tk.END, read_line)
			# print read_line
	

	def create_button(self):
		
		
		self.button_confirm = tk.Button(self.frame_bottom_bar,
										image=self.gif_confirm)  # text=u'确认'
		self.button_help = ttk.Button(self.frame_bottom_bar,
									  image=self.gif_help)  # text=u'帮助详情',
		self.button_quit = ttk.Button(self.frame_bottom_bar,
									  image=self.gif_quit,
									  command=self.window.destroy)
		self.button_confirm.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E,
								 padx=5)
		self.button_help.pack(side=tk.LEFT, expand=tk.NO, anchor=tk.E, padx=5)
		self.button_quit.pack(side=tk.RIGHT, expand=tk.NO, anchor=tk.E, padx=5)
		# buttonttk["command"] = self.kk
		
		return 1
	
	def single_file_block(self, sfb_filetype, sfb_name):
		# sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		"""
		sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
		
		# 文件选取菜单
		def select_file():
			file_path = tkFileDialog.askopenfilename(filetypes=sfb_filetype)
			# 刷新normal_single_block() 中的Entry
			input_msg1.set(file_path)
		
		label_1 = tk.Label(self.frame_major, text=sfb_name)
		label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one,
										 text=u"选择", command=select_file,
										 image=self.gif_text16)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sfb = tk.Entry(frame_one, textvariable=input_msg1,
								  border=2, relief=tk.GROOVE)
		self.input_sfb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
							fill=tk.X, padx=15)
		# input_msg.set(one_file_path)
		return 1
	
	def savename_block(self, sfb_filetype, sfb_name):
		# sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		"""
		major-Frame中的功能块之一，该模块让用户选择文件的保存位置和名字
		
		sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		"""
		# 文件选取菜单
		def select_file():
			file_path = tkFileDialog.asksaveasfilename(filetypes=sfb_filetype)
			# 刷新normal_single_block() 中的Entry
			# lis = self.file_paths_.append(file_path)
			# print lis
			input_msg1.set(file_path)
			# return file_path
		
		label_1 = tk.Label(self.frame_major, text=sfb_name)
		label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one, image=self.gif_text16,
										 command=select_file, text=u"选择")
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sb = tk.Entry(frame_one, textvariable=input_msg1,
								 border=2, relief=tk.GROOVE)
		self.input_sb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
						   fill=tk.X, padx=15)
		return 1
	
	def single_dir_block(self, sdb_name):
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
		
		label_2 = tk.Label(self.frame_major, text=sdb_name)
		label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60",
							 width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = ttk.Button(frame_one, text=u"选择",
										 command=select_file,
										 image=self.gif_folder16)
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
		label_3 = tk.Label(self.frame_major, text=gib_name)
		label_3.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		self.addfile_button = ttk.Button(frame_one, text=u"选择", command=None)
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
	
	def single_int_block2(self, gib_name):
		"""
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
		label_ = tk.Label(self.frame_major, text=gib_name)
		label_.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		self.addfile_button = ttk.Button(frame_one, text=u"选择", command=None)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sib2 = tk.Entry(frame_one, textvariable=input_msg1, border=2,
								   relief=tk.GROOVE)
		# , state = "readonly"
		self.input_sib2.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							 padx=15)
		# input_msg.set(one_file_path)
		return 1
	
	def get_Entry_fromblock(self, *arg):
		"""
		获取Entry值，组成列表
		:param arg: 各个block的Entry模块组成的元组
		:return: self.block_list 返回 含有用户输入的各种因子的 列表
		"""
		self.block_list = []
		for i in arg:
			# 由于Entry输出纯英文数字时是str格式，为方便后续进行比较等操作
			# 将str转换为unicode
			msg = i.get()
			if type(msg) == type("str"):  # unicode
				msg = msg.decode("cp936")
				self.block_list.append(msg)
			else:
				# unicode格式的直接加进去
				self.block_list.append(msg)
			# 将信息显示到右上角
			self.text.insert("end", "\n  " + msg)
		return self.block_list
	
	# got_msg1 = arg[0].get()
	# # .decode("cp936")
	# got_msg2 = arg[1].get()
	# self.block_list.append(got_msg1)
	# self.block_list.append(got_msg2)


if __name__ == '__main__':
	class App(Tooltk):
		def __init__(self):
			super(App, self).__init__(u"本地实验", "docs/explode_mulitp.gc")
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
			self.get_Entry_fromblock(self.input_sfb, self.input_sdb)
			print "self.block_list: ", self.block_list
			for i in self.block_list:
				print i, " type: ", type(i)
			# 重置
			self.block_list = []
			"""
			文件
			filedialog: C:/Users/hygnic/Desktop/打开host.txt  type:  <type 'unicode'>
			filedialog: C:/Users/hygnic/Desktop/204863.txt  type:  <type 'str'>
			文件夹
			filedialog+手动: E:/move on move on/是多少  type:  <type 'unicode'>
			手动: G:\软件包  type:  <type 'unicode'>
			手动: G:\music  type:  <type 'str'>
			filedialog: E:/move on move on/Gispot/bin  type:  <type 'str'>
			filedialog: E:/move on move on/公示图  type:  <type 'unicode'>
			结论:
			"""
	
	
	app = App()
	app.window.mainloop()
# print app.block_list
