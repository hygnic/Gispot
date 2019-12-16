# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21
# python2.7
"""所用工具和脚本调用此GUI"""

import Tkinter as tk
import tkFileDialog
import ScrolledText as stt

# 导入配置包、地址包
from hyconf import luitils
from hyconf import gispotpath


class Tooltk(object):
	"""工具的GUI界面"""
	# button's width and height
	_button_size = 24
	
	# 调用类变量也要加self
	def __init__(self, master, help_path, confirm_method):
		"""
		:param master:
		:param help_path: 帮助文档的路径
		:param confirm_method: 按下确认键后的响应事件
		"""
		self.block_list = []
		self.window = master
		# self.window.title(window_name)
		self.helppath = help_path
		self.confirm_method = confirm_method
		# self.window.overrideredirect(True)
		# 给Toplevel窗口设置透明度
		# self.window.attributes('-alpha',0.5)
		# 设置窗口置顶优先度
		# self.window.attributes('-topmost', 1)
		# self.window = tk.Tk()
		# GUIutils.screen_cetre(self.window, width=800, height=660)
		# self.window.iconbitmap(default=os.path.dirname(__file__)+
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
		self.create_frames()  # 配置框架
		self.create_button()  # 配置按钮
		# color   "SystemHighlight","SystemMenuText"
		self.read_help()
	
	def color_mylife(self):
		self.color1 = "#F1F1F1"  # 帮助栏颜色
		self.color5 = "Olive"  # 橄榄色，显示text
		self.color3 = "#F1F1F1"  # 主框的上半部分颜色 侧栏颜色
		# self.color4 = "Cornsilk" # 侧栏颜色
		self.color2 = "#E1E1E1"  # 茶色 较深
		self.color6 = '#EBEEEE'  # 底栏颜色
	
	def icon_set(self):
		self.gif_text = tk.PhotoImage(file=gispotpath.GifPath.gif_textfile)
		self.gif_addfile = tk.PhotoImage(file=gispotpath.GifPath.gif_add_file)
		
		self.gif_folder = tk.PhotoImage(file=gispotpath.GifPath.gif_folder)
		self.gif_close = tk.PhotoImage(file=gispotpath.GifPath.gif_close)
		self.gif_quit = tk.PhotoImage(file=gispotpath.GifPath.gif_close)
		self.gif_help = tk.PhotoImage(file=gispotpath.GifPath.gif_info)
		self.gif_confirm = tk.PhotoImage(file=gispotpath.GifPath.gif_confirm)
		
		self.gif_empty_1 = tk.PhotoImage(file=gispotpath.GifPath.gif_empty1)
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
	
	def create_frames(self):
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
		# 里面 的 上部分
		self.frame_major = tk.Frame(self.frame_left_side, width=696,
									relief="flat")
		self.frame_major.pack(
			expand=True, fill="both")
		# 主框下的底部栏
		self.frame_bottom_bar = tk.Frame(self.frame_left_side, height="60",
										 bg=self.color6, border=2,
										 relief="groove")  # ffc851
		self.frame_bottom_bar.pack(
			expand=False, fill="both")
		# expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
		# x轴（左右）方向上会拉伸
		# 左边主框中的帮助信息
		help_f = tk.Frame(self.frame_major, width=696,
							   relief=tk.RIDGE,
							   bd=2)
		help_f.pack(side=tk.BOTTOM, anchor="s",
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
			右边主框插入文本框，文本框分成上下两部分，上部分显示固定的信息，
		下半部分显示动态信息"""
		# 上栏
		self.text = stt.ScrolledText(self.frame_right_side, height="10",
									 width="90")
		# 不起作用，将所用txt都标记了
		# self.text.tag_add("tag1","1.end","2.end")
		self.text.insert(tk.END,
						 "Python 2.7.12 (v2.7.12:d33e0cf91556,Jun 27 2016, "
						 "15:19:22) author: Liaochenchen 2019#00#00")  # ,"tag1"
		# self.text.tag_config("tag1",underline = True,foreground = "Ivory")
		self.text.pack(side="top", anchor="n", expand=True, fill="both",
					   padx=2)
		# 下栏 主要的动态信息显示栏
		s_bar = tk.Scrollbar(self.frame_right_side, relief="flat",
							 elementborderwidth=-15)
		s_bar.pack(side="right", fill="y")
		self.text_majorMsg = tk.Text(self.frame_right_side, height="60",
									  yscrollcommand=s_bar.set,
									 maxundo=15, undo=True)
		# 支持撤销操作，支持换行 wrap = "char"
		self.text_majorMsg.insert(tk.END, ">>>" * 20)
		self.text_majorMsg.pack(side="top", anchor="n", expand=True,
								fill="both", padx=2)
		s_bar.config(command=self.text_majorMsg.yview)
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
			self.help_text["state"] = "disabled"
	
	# print read_line
	
	def create_button(self):
		"""
		create second window button
		"""
		
		# self.confirm_method 确认按键所触发的方法
		self.button_confirm = luitils.HoverButton(self.frame_bottom_bar,
												  image=self.gif_confirm,
												  command=self.confirm_method,
												  width =self._button_size,
												  height =self._button_size)
		# print "tooltk.py>>Border:", self.button_confirm["borderwidth"] # 2
		# height = 18, width = 18,
		self.button_help = luitils.HoverButton(self.frame_bottom_bar,
											   image=self.gif_help,
											   width=self._button_size,
											   height=self._button_size)
		
		def inner_quit():
			"""
			使用该方法来删除main_f下的子部件，如果直接使用
			command=self.windows.destory ,会删除掉main_f，
			导致打开其他功能时找不到main_f而报错
			:return:
			"""
			luitils.destroy_chird(self.window)
		
		self.button_quit = luitils.HoverButton(self.frame_bottom_bar,
											   image=self.gif_quit,
											   command=inner_quit,
											   width=self._button_size,
											   height=self._button_size)
		self.button_confirm.pack(side=tk.LEFT, anchor=tk.E,
								 padx=5)
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
		label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
	
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sfb = tk.Entry(frame_one, textvariable=input_msg1,border=0)
		self.input_sfb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
							fill=tk.X, padx=10)
		self.addfile_button = luitils.HoverButton(frame_one, text=u"选择",
												  command=select_file,
												  image=self.gif_addfile,
												  width=self._button_size,
												  height=self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def save_path_block(self, sfb_filetype, sfb_name):
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
		
		name_label = tk.Label(self.frame_major, text=sfb_name)
		name_label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = luitils.HoverButton(frame_one, image=self.gif_addfile,
												  command= select_file,
												  width= self._button_size,
												  height = self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sb = tk.Entry(frame_one, textvariable=input_msg1,
								 border=2, relief=tk.FLAT)
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
		label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sdb = tk.Entry(frame_one, textvariable=input_msg1,bd = 0)
		self.input_sdb.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							padx=10)
		# input_msg.set(one_file_path)
		self.addfile_button = luitils.HoverButton(frame_one,
												  command=select_file,
												  image=self.gif_folder,
												  width = self._button_size,
												  height = self._button_size)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def single_int_block(self, gib_name):
		"""
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
		label_3 = tk.Label(self.frame_major, text=gib_name)
		label_3.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sib = tk.Entry(frame_one, textvariable=input_msg1, border=0)
		self.input_sib.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							padx=10)
		# input_msg.set(one_file_path)
		# 按钮
		int_button_1 = luitils.HoverButton(frame_one, image=self.gif_empty_1,
										   state = "disabled",
										   width = self._button_size,
										   height = self._button_size)
		int_button_1.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		return 1
	
	def single_int_block2(self, gib_name):
		"""
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
		label_ = tk.Label(self.frame_major, text=gib_name)
		label_.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		int_button_2 = luitils.HoverButton(frame_one,state = "disabled",
										   image=self.gif_empty_1,
										   width = self._button_size,
										   height = self._button_size)
		int_button_2.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sib2 = tk.Entry(frame_one, textvariable=input_msg1, border=0)
		# , state = "readonly"
		self.input_sib2.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
							 padx=10)
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
			super(App, self).__init__(u"本地实验", "docs/explode_mulitp.gc",
									  self.confirm_method)
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