# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21
# python2.7
"""
GUI  所用工具和脚本用GUI"""
import os
import ttk
import Tkinter as tk
import tkFileDialog
import ScrolledText as stt
from PIL import Image, ImageTk

# 导入配置包、地址包
from GUIconfig import GUI
from GUIconfig import GUIpath
# from GUIconfig.paths import GifPath
from GUIconfig.GUIpath import PngIcon


class GIF(object):
	
	def __init__(self):
		self.text = tk.PhotoImage(file=GUIpath.GifPath.textfile)
		self.addfile = tk.PhotoImage(file=GUIpath.GifPath.add_file)
		
		self.folder = tk.PhotoImage(file=GUIpath.GifPath.folder)
		self.close = tk.PhotoImage(file=GUIpath.GifPath.close)
		self.quit = tk.PhotoImage(file=GUIpath.GifPath.close)
		self.help = tk.PhotoImage(file=GUIpath.GifPath.info)
		self.confirm = tk.PhotoImage(file=GUIpath.GifPath.confirm)
		self.empty_1 = tk.PhotoImage(file=GUIpath.GifPath.empty1)


# @staticmethod
# def dd():
# 	empty_1 = tk.PhotoImage(file=paths.GifPath.gif_empty1)


class Tooltk(object):
	"""工具的GUI界面"""
	# 如果是图片，表示 24 像素单位，否则不是
	_button_size = 24
	
	# 调用类变量也要加self
	def __init__(self, master, help_path, confirm_method):
		"""
		:param master:
		:param help_path: path of help information file（can be None）
		:param confirm_method: 按下确认键后的响应事件
		"""
		self.block_list = []
		self.window = master
		# self.window.remove_sth(window_name)
		self.helppath = help_path
		self.confirm_method = confirm_method
		# self.window.overrideredirect(True)
		# 给Toplevel窗口设置透明度
		# self.window.attributes('-alpha',0.5)
		# 设置窗口置顶优先度
		# self.window.attributes('-topmost', 1)
		# self.window = tk.Tk()
		# GUIutils.screen_cetre(self.window, width=800, height=660)
		# self.window.iconbitmap(default=os.path.dirname(sys.argv[0])+
		# 							   "/Icons/toolbox.ico")
		# 重新抓取设置，使Toplevel显示在最上面
		# self.window.grab_set()
		# self.window.grab_release()
		# self.window.resizable(False, False)
		# self.input_str_1 = tk.StringVar()
		# self.input_str_2 = tk.StringVar()
		# self.input_int = tk.IntVar()
		self.color_mylife()  # 颜色
		self.icon_set()  # 配置图片
		self.frames_initial()  # 配置框架
		self.create_button()  # 配置按钮
		# color   "SystemHighlight","SystemMenuText"
		self.read_help()
	
	@property
	def Frame(self):
		return self.block_frame
	
	# static information box(Upper right corner)
	@property
	def FrameStatic(self):
		return self.msgframe
	
	# dynamic information box(lower right corner)
	@property
	def FrameDynamic(self):
		return self.major_msgframe
	
	def color_mylife(self):
		self.color1 = "#F1F1F1"  # help bar
		self.color5 = "#808000"  # Olive,显示text
		self.color3 = "#F1F1F1"  # 主框的上半部分颜色 侧栏颜色
		# self.color4 = "Cornsilk" # 侧栏颜色
		self.color2 = "#E1E1E1"  # 茶色 较深
		self.color6 = '#EBEEEE'  # 底栏颜色
	
	def icon_set(self):
		# 必须加file参数，不然不显示图片（arcgis10.6）
		self.gif_text = tk.PhotoImage(file=GUIpath.GifPath.textfile)
		self.gif_addfile = tk.PhotoImage(file=GUIpath.GifPath.add_file)
		
		self.gif_folder = tk.PhotoImage(file=GUIpath.GifPath.folder)
		self.gif_close = tk.PhotoImage(file=GUIpath.GifPath.close)
		self.gif_quit = tk.PhotoImage(file=GUIpath.GifPath.close)
		self.gif_help = tk.PhotoImage(file=GUIpath.GifPath.info)
		self.gif_confirm = tk.PhotoImage(file=GUIpath.GifPath.confirm)
		
		self.gif_empty_1 = tk.PhotoImage(file=GUIpath.GifPath.empty1)
		# self.gif_empty_2 = tk.PhotoImage(file=gispotpath.GifPath.gif_empty2)
		
		# ph = tk.PhotoImage(file=gispotpath.GifPath.gif_confirm)
		# self.gif_check_green16 =  ph.zoom(x= 2,y = 2)
		# self.gif_check_green16 =  ph.subsample(x= 40,y=40)
		
		"""
		使用pillow设置按键图标
		from PIL import Image, ImageTk
		self.gif_comfirm = ph
		# test
		im = Image.open(r"E:\move on move on\Gispot\GUIs\66.png")
		self.ph_im = ImageTk.PhotoImage(im)
		"""
	
	def frames_initial(self):
		# 1192/2 = 596
		# 右边的主框
		self.frame_right_side = tk.Frame(self.window, width=496,
										 border=0, relief="flat")
		self.frame_right_side.pack(side="right",
								   expand=True, fill="both")
		# self.frame_right_side.propagate(False)
		# 左边的主框
		self.frame_left_side = tk.Frame(self.window, width=696,
										border=0, relief="flat")
		self.frame_left_side.pack(side="left",
								  expand=True, fill="both")
		# 上部分 用于盛放block模块
		self.block_frame = tk.Frame(self.frame_left_side, width=696,
									relief="flat")
		self.block_frame.pack(expand=True, fill="both")
		# 主框下的底部栏
		self.frame_bottom_bar = tk.Frame(self.frame_left_side, height="60",
										 bg=self.color6)  # ffc851
		# self.frame_bottom_bar.pack_propagate(0)
		self.frame_bottom_bar.pack(expand=False, fill="both")
		# expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
		# x轴（左右）方向上会拉伸
		# 左边主框中的帮助信息
		help_f = tk.Frame(self.block_frame, relief=tk.GROOVE, bd=2, padx=3)
		# help_f.pack_propagate(0)
		help_f.pack(side=tk.BOTTOM, anchor="s", expand=True, fill="both")
		# 设置带滚动条的text
		s_bar = tk.Scrollbar(help_f, relief="flat", elementborderwidth=-15)
		s_bar.pack(side="right", fill="y")
		self.help_text = GUI.NeewwText(
			help_f, relief=tk.FLAT, height=20,
			fg=self.color5, yscrollcommand=s_bar.set
		)
		
		self.help_text.pack(expand=True, fill="both")
		s_bar.config(command=self.help_text.yview)
		
		""""
			右边主框插入文本框，文本框分成上下两部分，上部分显示固定的信息，
		下半部分显示动态信息"""
		# 上栏
		self.msgframe = stt.ScrolledText(
			self.frame_right_side, height="10", width="90")
		# 不起作用，将所用txt都标记了
		# self.text.tag_add("tag1","1.end","2.end")
		self.msgframe.insert(
			tk.END,
			"Python 2.7.12 (v2.7.12:d33e0cf91556,Jun 27 2016, "
			"15:19:22) author: Liaochenchen 2019#00#00"
		)  # ,"tag1"
		# self.text.tag_config("tag1",underline = True,foreground = "Ivory")
		self.msgframe.pack(
			side="top", anchor="n", expand=True, fill="both", padx=2)
		# 下栏 主要的动态信息显示栏
		s_bar = tk.Scrollbar(
			self.frame_right_side, relief="flat", elementborderwidth=-15)
		s_bar.pack(side="right", fill="y")
		self.major_msgframe = GUI.NeewwText(
			self.frame_right_side, height="60", yscrollcommand=s_bar.set)
		# 配置字体颜色
		self.major_msgframe.tag_config(
			"tag_1", backgroun="yellow", foreground="red", )
		# 支持撤销操作，支持换行 wrap = "char"
		# self.text_major_msg.insert(tk.END, ">>>" * 80)
		self.major_msgframe.pack(
			side="top", anchor="n", expand=True, fill="both", padx=2)
		s_bar.config(command=self.major_msgframe.yview)
	
	# return self.frame_major
	
	# Read help information and insert in help box
	def read_help(self):
		if self.helppath is not None:
			filename = self.helppath
			with open(filename, "r") as read_msgs:
				for read_line in read_msgs.readlines():
					self.help_text.insert(tk.END, read_line)
				self.help_text["state"] = "disabled"
	
	def create_button(self):
		"""
		Make three button:
		 1.button_confirm: the main function start up button
		 2.button_quit: back button
		 3.button_help: jump to a website which shows help information (most unused)
		"""
		self.button_confirm = GUI.HoverButton(
			self.frame_bottom_bar, msg="OK",
			image=self.gif_confirm,
			command=self.confirm_method,
			width=self._button_size,
			height=self._button_size)
		
		# print "tooltk.py>>Border:", self.button_confirm["borderwidth"] # 2
		# height = 18, width = 18,
		# help button
		self.button_help = GUI.HoverButton(
			self.frame_bottom_bar, msg="Info",
			image=self.gif_help,
			width=self._button_size,
			height=self._button_size)
		
		def __quit_inner():
			"""
			使用该方法来删除main_f下的子部件，如果直接使用
			command=self.windows.destory ,会删除掉main_f,
			导致打开其他功能时找不到main_f而报错
			"""
			GUI.destroy_child(self.window)
		
		# Back button
		self.button_quit = GUI.HoverButton(
			self.frame_bottom_bar, msg="Cancel",
			image=self.gif_quit,
			command=__quit_inner,
			width=self._button_size,
			height=self._button_size)
		# pack
		self.button_confirm.pack(side=tk.LEFT, anchor=tk.E, padx=5)
		self.button_help.pack(side=tk.LEFT, anchor=tk.E, padx=5)
		self.button_quit.pack(side=tk.RIGHT, anchor=tk.E, padx=5)
		# buttonttk["command"] = self.kk
		# --------------- 获取部件的query_class
		# print self.button_confirm.winfo_class()
		# print self.button_help.winfo_class()
		# print self.button_quit.winfo_class()
		"""
		# 测试ttk.Style.layout()
		ttk.Style().layout("TButton",
				[('Button.button', {'children':
					[('Button.focus', {'children':
						[('Button.border', {'border':1,'children':
							[('Button.label', {'sticky': 'nswe'})],
						'sticky': 'nswe'})],
					'sticky': 'nswe'})],
				'sticky': 'nswe'})])
		ttk.Style().configure("TButton", foreground="#ffc851", background="blue")
		# padding = 10
		"""
		# print ttk.Style().layout('TButton')
		# 原版
		# [('Button.button',
		#   {'children': [(
		# 	  'Button.focus', {'children': [('Button.padding',{'children': [('Button.label',{'sticky': 'nswe'})],'sticky': 'nswe'})],'sticky': 'nswe'})],'sticky': 'nswe'})]
		"""
		"""
		# ---------------
		
		return 1
	
	def single_file_block(self, sfb_filetype, sfb_name):
		# __sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		"""
		__sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
		
		# 文件选取菜单
		def select_file():
			file_path = tkFileDialog.askopenfilename(filetypes=sfb_filetype)
			# 刷新normal_single_block() 中的Entry
			input_msg1.set(file_path)
		
		label_1 = tk.Label(self.block_frame, text=sfb_name)
		label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sfb = GUI.NeewwEntry(frame_one, textvariable=input_msg1,
										border=0)
		self.input_sfb.pack(
			side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=10)
		self.addfile_button = GUI.HoverButton(
			frame_one, text=u"选择",
			command=select_file,
			image=self.gif_addfile,
			width=self._button_size,
			height=self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def save_path_block(self, sfb_filetype, sfb_name):
		# __sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		"""
		major-Frame中的功能块之一，该模块让用户选择文件的保存位置和名字
		__sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		"""
		
		# 文件选取菜单
		def select_file():
			file_path = tkFileDialog.asksaveasfilename(filetypes=sfb_filetype)
			# 刷新normal_single_block() 中的Entry
			# lis = self.file_paths_.append(file_path)
			# print lis
			input_msg1.set(file_path)
		
		name_label = tk.Label(self.block_frame, text=sfb_name)
		name_label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = GUI.HoverButton(
			frame_one, image=self.gif_addfile,
			command=select_file,
			width=self._button_size,
			height=self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sb = GUI.NeewwEntry(
			frame_one, textvariable=input_msg1, border=2, relief=tk.FLAT)
		self.input_sb.pack(
			side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=15)
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
		
		label_2 = tk.Label(self.block_frame, text=sdb_name)
		label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sdb = GUI.NeewwEntry(
			frame_one, textvariable=input_msg1, bd=0)
		self.input_sdb.pack(
			side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=10)
		# input_msg.set(one_file_path)
		self.addfile_button = GUI.HoverButton(
			frame_one,
			command=select_file,
			image=self.gif_folder,
			width=self._button_size,
			height=self._button_size)
		
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def single_dir_block2(self, sdb_name):
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
		
		label_2 = tk.Label(self.block_frame, text=sdb_name)
		label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sdb2 = GUI.NeewwEntry(frame_one, textvariable=input_msg1, bd=0)
		self.input_sdb2.pack(
			side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=10)
		# input_msg.set(one_file_path)
		self.addfile_button = GUI.HoverButton(
			frame_one,
			command=select_file,
			image=self.gif_folder,
			width=self._button_size,
			height=self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def single_vari_block(self, gib_name, input_msg1):
		"""
		主Frame中的功能块之一，直接通过Entry获取变量值，
		其变量类型，可以根据需要灵活指定。
		:param input_msg1: # input_msg1 = tk.StringVar()
		:param gib_name: label name;ues to describe function
		:return:
		"""
		label_3 = tk.Label(self.block_frame, text=gib_name)
		label_3.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# Entry
		# input_msg1 = tk.StringVar()
		self.input_svb = GUI.NeewwEntry(
			frame_one, textvariable=input_msg1, border=0
		)
		self.input_svb.pack(side=tk.LEFT, anchor=tk.W,
							expand=True, fill=tk.X, padx=10)
		# input_msg.set(one_file_path)
		# 按钮
		int_button_1 = GUI.HoverButton(
			frame_one, image=self.gif_empty_1,
			state="disabled",
			width=self._button_size,
			height=self._button_size)
		int_button_1.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def single_int_block2(self, gib_name):
		"""
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
		_label = tk.Label(self.block_frame, text=gib_name)
		_label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.block_frame)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		int_button_2 = GUI.HoverButton(
			frame_one, state="disabled",
			image=self.gif_empty_1,
			width=self._button_size,
			height=self._button_size
		)
		int_button_2.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sib2 = GUI.NeewwEntry(
			frame_one,
			textvariable=input_msg1, border=0
		)
		# , state = "readonly"
		self.input_sib2.pack(
			side=tk.LEFT, anchor=tk.W,
			padx=10, expand=True, fill=tk.X
		)
		# input_msg.set(one_file_path)
		return 1
	
	def single_text_block(self, stb_name):
		"""
		text组件
		:param stb_name:
		:return:
		"""
		# 块名称
		tk.Label(self.block_frame, text=stb_name). \
			pack(side=tk.TOP, anchor=tk.NW, padx=40)
		frame_one = tk.Frame(self.block_frame)
		frame_one.pack(side="top", anchor="center",
					   expand=True, fill="both")
		# 右边障碍要素
		GUI.HoverButton(
			frame_one, state="disabled",
			image=self.gif_empty_1,
			width=60,
			height=self._button_size
		).pack(side=tk.RIGHT, padx=10)
		# 左边障碍要素
		GUI.HoverButton(
			frame_one, state="disabled",
			image=self.gif_empty_1,
			width=13,
			height=self._button_size
		).pack(side=tk.LEFT, padx=10)
		
		# frame_one.columnconfigure(0, weight=1)
		# frame_one.columnconfigure(1, weight=1)
		self.input_tb = GUI.NeewwText(frame_one, wrap="none",
									  relief="flat", height=10)
		self.input_tb.pack(expand=True, fill="both")
	
	# text.grid(column = 0,sticky = "nesw")
	
	def divider_bar_block(self, master, color11, color22):
		"""
		最下面的那个分隔栏
		:return:
		"""
		s = GUI.GradientCanvas(
			master, color11, color22,
			height=10, bd=0
		).pack(fill="x")
	
	def get_blockvalue(self, *arg):
		"""
		列表初始化
		获取Entry值，组成列表
		:param arg: 各个block的Entry模块组成的元组
		:return: self.block_list 返回 含有用户输入的各种因子的 列表
		"""
		self.block_list = []
		for i in arg:
			# 由于Entry输出纯英文数字时是str格式，为方便后续进行比较等操作
			# 将str转换为unicode
			msg = i.get()
			print "msg:", msg
			print "msg's type:", type(msg)
			if type(msg) == type("str"):  # unicode
				msg = msg.decode("cp936")
				print "msg:", msg
				print "msg's type:", type(msg)
				self.block_list.append(msg)
			else:
				# unicode格式的直接加进去
				self.block_list.append(msg)
			# 将信息显示到右上角
			self.msgframe.insert("end", "\n  " + msg)
		# print len(self.block_list)
		# print self.block_list[3]
		return self.block_list


class SingleFileBlock(object):
	"""单个文件选择功能块
	ss = tooltk.SingleFileBlock(frame, "添加文件",
									tkFileDialog.askopenfilename，[(u'文本文档', '*.txt'), ('All Files', '*')],
									"add_file")"""
	_button_pixel_size = 24
	
	def __init__(self, frames, name, tkFileDialogFunc, filetype, image):
		"""
		:param frames: {Tuple} GUI界面中几个主要框架
			*self.block_frame,self.msgframe,self.major_msgframe
			 self.block_frame 父组件，左上界面
			 self.msgframe 右上 静态信息界面
			 self.major_msgframe 右下 动态信息界面
			
		:param name: {String} 块（Block）名字
		
		:param tkFileDialogFunc: tkFileDialog 模块名称
			*tkFileDialog.askopenfilename: 获取单个文件的位置和名称
				file_path = tkFileDialog.askopenfilename([(u'文本文档', '*.txt'), ('All Files', '*')])
			*tkFileDialog.askdirectory:
				file_path = tkFileDialog.askdirectory()
		
		:param filetype: tkFileDialog {List} 文件选择类型
			*__sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
		
		:param image: {String} 按键图片名字，用于反射
			* "add_file"
		"""
		# 传入参数
		self.__master = frames[0]  # self.frame_major
		self.__static = frames[1]
		self.__dymnic = frames[2]
		self.__sfb_filetype = filetype
		self.dialoge_type = tkFileDialogFunc
		# self.tkFileDialog.askopenfilename = tkFileDialog.askopenfilename
		
		# 内部建立自用
		self.var = tk.StringVar()
		
		self.image(image)
		self.single_file_block(name)
	
	# 设置图片,使用了反射
	# 方案一：使用gif图片
	# def image(self,image):
	# 	# print "getattr(GifPath,image):",getattr(GifPath,image)
	# 	raw_p = getattr(GifPath,image)
	# 	# tk.PhotoImage需要设置成全局变量才生效，一个bug
	# 	global a_gif
	# 	a_gif = tk.PhotoImage(file=raw_p)
	# 	self.but_image = a_gif
	def image(self, image):
		# print "getattr(GifPath,image):",getattr(GifPath,image)
		raw_p = getattr(PngIcon, image)
		img = Image.open(raw_p)
		photo = ImageTk.PhotoImage(img)
		
		# tk.PhotoImage需要设置成全局变量才生效，一个bug
		# global a_gif
		# a_gif = tk.PhotoImage(file=raw_p)
		self.but_image = photo
	
	# 打开 文件/文件夹 选取窗口
	def dialog(self):
		file_path = self.dialoge_type(filetypes=self.__sfb_filetype)
		
		# file_path = tkFileDialog.askopenfilename(
		# 		[(u'文本文档', '*.txt'), ('All Files', '*')])
		# 刷新normal_single_block() 中的Entry
		self.var.set(file_path)
	
	def single_file_block(self, sfb_name):
		"""主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		__sfb_filetype: {List} tkFileDialog
		
		sfb_name: {String} label name;ues to describe function
		"""
		label_1 = tk.Label(self.__master, text=sfb_name)
		label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 整齐排列Entry和按钮
		frame_one = tk.Frame(self.__master)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		
		# Entry
		self.__newEntry = GUI.NeewwEntry(
			frame_one, textvariable=self.var, border=0)
		self.__newEntry.pack(
			side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=10)
		self.__button = GUI.HoverButton(
			frame_one, text=u"选择",
			command=self.dialog,
			image=self.but_image,
			width=self._button_pixel_size,
			height=self._button_pixel_size)
		self.__button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
	
	# 点击确认键的时候获取Entry中的值
	def get(self):
		block_list = []
		# 由于Entry输出纯英文数字时是str格式，为方便后续进行比较等操作
		# 将str转换为unicode
		msg = self.__newEntry.get()
		frame = self.__static
		print "msg", msg
		print "msg's type", type(msg)
		if type(msg) == type("str"):  # unicode
			msg = msg.decode("cp936")
			# block_list.append(msg)
			# self.text.insert("end", "\n  " + msg)
			frame.insert("end", "\n  " + msg)
			# print "msg1", msg
			# print "msg's type1", type(msg)
			return msg
		else:
			# unicode格式的直接加进去
			frame.insert("end", "\n  " + msg)
			# print "msg2", msg
			# print "msg's type2", type(msg)
			# print os.path.isdir(msg)
			return msg
	
	# def get(self):
	# 	_value = _handlevalue(self.__newEntry, self.__static)
	# 	return _value
	
	@property
	def button(self):
		return self.__button
	
	@property
	def entry(self):
		return self.__newEntry


# 文件夹模块
def blockDIR_in(frames, name):
	return SingleFileBlock(
		frames, name, tkFileDialog.askdirectory, None, "folder1")


def blockSheet(frames, name):
	return SingleFileBlock(
		frames, name, tkFileDialog.askopenfilename,
		[(u'工作簿', '*.xlsx'), (u'工作簿', '*.xls'),
		('All Files', '*')], "add_file"
	)


def blockDIR_out(frames, name):
	return SingleFileBlock(
		frames, name, tkFileDialog.askdirectory, None, "folder2")


# 数字输入模块（没有button）
def blockValue(frames, name):
	inner = SingleFileBlock(frames, name, tkFileDialog.askdirectory, None ,"empty")
	# inner.block_button["state"] ="disabled"  #不行
	# inner.block_button.config(state ="disabled") # 不行
	# 解除绑定
	inner.button.close()  # state = "disabled",  normal,active
	return inner


if __name__ == '__main__':
	
	class TstApp(Tooltk):
		def __init__(self):
			master = tk.Tk()
			# master = ThemedTk(theme="arc")
			super(TstApp, self).__init__(master, None,
										 self.confirm_method)
			self.button_confirm["command"] = self.confirm_method
			# block 1
			self.single_file_block([(u'文本文档', '*.txt'), ('All Files', '*')],
								   u"文本文档")
			# block2
			self.single_dir_block(u"图片文件夹")
			frame = (self.block_frame, self.msgframe, self.major_msgframe)
			SingleFileBlock(frame, u"TEST",
							tkFileDialog.askopenfilename, [(u'文本文档', '*.txt'),
														   ('All Files', '*')],
							"add_file")
		
		# self.addfile_button["state"] = "disabled"
		# self.addfile_button.pack_forget() # 隐藏模块
		# self.addfile_button.destroy()	# 隐藏模块
		# 触发命令获取Entry的值
		
		def confirm_method(self):
			self.get_blockvalue(self.input_sfb, self.input_sdb)
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
			filedialog: E:/move on move on/gispot/bin  type:  <type 'str'>
			filedialog: E:/move on move on/公示图  type:  <type 'unicode'>
			结论:
			"""
	
	
	app = TstApp()
	app.window.mainloop()
