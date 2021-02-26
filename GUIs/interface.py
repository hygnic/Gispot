#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# python2 arcgis10.6
"""
# Author: LiaoChenchen
# Created on: 2020/3/5
# Reference:
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description:……………………………………………………………………………………
程序打开的初始界面
	包含：
	1.toolbar 左侧工具栏
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description………………………………………………………………………………………
Usage:
# ---------------------------------------------------------------------------
"""
from __future__ import absolute_import
import Tkinter as tk
import ttk
from PIL import ImageTk, Image
from os.path import join

from gpconfig import newGUI, hyini
from gpconfig.gppath import PngIcon, GifPath
import gpconfig.gppath as gpath
import vitems
from crcpy import save_acopy
from crcpy import txt2shp
from crcpy import multiplexport
from crcpy import ZLDJ
from crcpy import area_cal
from crcpy import zldj_cal
from crcpy import cal_real_area


# class MyImG(object):
# 	def __init__(self):
# 		self.img_tab2 = Image.open(join(gpath.base_icons_path, "toolbox-45.png"))
#
# 		# img_tab2=img_tab2.resize((40, 40))
# 		self.tb2 = ImageTk.PhotoImage(self.img_tab2)
#
# mi=MyImG()



class ttknotebook(object):
	"""
	主界面的Notebook
	"""
	def __init__(self, master):
		self.image() # 引入toolbar中的图标
		self.window = master
		style = ttk.Style(self.window)
		style.configure('lefttab.TNotebook', tabposition='wn')
		
		"""-----------------------------------------------------------"""
		"""----------------------NoteBook-----------------------------"""
		# para
		self.padding = 0 # notebook padding
		# para
		self.mian_notebook = ttk.Notebook(self.window, style='lefttab.TNotebook')
		self.mian_notebook.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
		self.mian_notebook.configure(takefocus="")
		"""____________________________image__________________________________"""
		#TODO:
			# 问题 在这里使用图片才行，不然报错:
								# Too early to create image
			# 或者直接不显示图片
		global img_tab2, img_tab3, img_tab1, img_tab4, img_tab5
		self.resize = (20,20) # 缩放大小
		
		img1 = Image.open(join(gpath.base_icons_path, "home20.png"))
		img_tab1 = ImageTk.PhotoImage(img1.resize(self.resize))
		img2 = Image.open(join(gpath.base_icons_path, "toolbox-20.png"))
		img_tab2 = ImageTk.PhotoImage(img2.resize(self.resize))
		img3 = Image.open(join(gpath.base_icons_path, "folder1.png"))
		img_tab3 = ImageTk.PhotoImage(img3.resize(self.resize))
		img4 = Image.open(join(gpath.base_icons_path, "option20.png"))
		img_tab4 = ImageTk.PhotoImage(img4.resize(self.resize))
		img5 = Image.open(join(gpath.base_icons_path, "logo_20.png"))
		img_tab5 = ImageTk.PhotoImage(img5.resize(self.resize))
		"""____________________________image__________________________________"""
		# first tab
		self.notebook_1 = ttk.Frame(self.mian_notebook)
		self.mian_notebook.add(self.notebook_1, padding=self.padding, image=img_tab1)
		self.mian_notebook.tab(0, text="首页", compound="left")
		# second tab
		self.notebook_2 = ttk.Frame(self.mian_notebook)
		self.mian_notebook.add(self.notebook_2, padding=self.padding, image=img_tab2)
		self.mian_notebook.tab(1, text="工具", compound="left", underline="-1")
		# third tab
		self.notebook_3 = ttk.Frame(self.mian_notebook)
		self.mian_notebook.add(self.notebook_3, padding=self.padding, image=img_tab3)
		self.mian_notebook.tab(2, text="文档", compound="left", underline="-1")
		# 4th tab
		self.notebook_4 = ttk.Frame(self.mian_notebook)
		self.mian_notebook.add(self.notebook_4, padding=self.padding, image=img_tab4)
		self.mian_notebook.tab(3, text="选项", compound="left", underline="-1")
		# 5th tab
		self.notebook_5 = ttk.Frame(self.mian_notebook)
		self.mian_notebook.add(self.notebook_5, padding=self.padding, image=img_tab5)
		self.mian_notebook.tab(4, text="关于", compound="left", underline="-1")
		"""----------------------NoteBook-----------------------------"""
		"""-----------------------------------------------------------"""
		
	@property
	def notebook1(self):
		return self.notebook_1
	
	@property
	def notebook2(self):
		return self.notebook_2
	
	@property
	def notebook3(self):
		return self.notebook_3
	
	@property
	def notebook4(self):
		return self.notebook_4
	
	@property
	def notebook5(self):
		return self.notebook_5
	
	def image(self):
		"""notebook tab image
		初始界面左侧的 toolbar 图标；tk.PhotoImage必须加入file（arcgis10.6）"""
		# <PIL>
		self.icon_dos = tk.PhotoImage(file = GifPath.dos)
		# 对应second_viewer
		self.icon_editor = tk.PhotoImage(file=GifPath.editor)
		# self.icon_tool = tk.PhotoImage(file=paths.GifPath.tool)
		self.icon_tool = ImageTk.PhotoImage(Image.open(PngIcon.toolbox_45))
		self.icon_home = ImageTk.PhotoImage(Image.open(PngIcon.home))
		# dd = paths.PngIcon()
		# self.circle= dd.circle_icon_fun()
	
	# toolbar第yi个图标(一个查看器)打开的物品集 browser
	# 查看器，不可运行
	def first_viewer(self):
		newGUI.destroy_child(self.window2)
		pass
		# vitems.Filter(self.window2)
	
	def second_viewer(self):
		"""放置可运行的
		界面右侧的viewer,放置一个一个的图标
		master2  interface_frame
		master2
		newidgets.destroy_child(master1)"""
		newGUI.destroy_child(self.window2)
		vitems.export_s(self.window2)
	
	def open_viewer3(self):
		"""调用Third_Viewer类"""
		newGUI.destroy_child(self.window2)
		ToolSet(self.window2)
		# Third_Viewer(self.window2, self.circle)
	
	# -------------------------
	# 将带有参数的类变成方法和button绑定
	# def show_first_viewer(self):

# def func1():
#     # name: 坐标系转换
#     print "func1"
#
# def func2():
#     # name: Excel转shp
#     print "func2"
#
#
# def func3():
#     # name: 坐标系转换
#     print "func1"
#
#
# def func4():
#     # name: Excel转shp
#     print "func2"
#
# func_name = {
# 	u"顺序":(
# 		u"转换工具",u"高标准农田"
# 	),
#     u"转换工具":(
#         (func1,u"坐标系转换"),
#         (func2,u"Excel转shp")
#     ),
#     u"高标准农田":(
#         (func3,u"坐标系转换2"),
#         (func4,u"Excel转shp2")
#     )
# }

# func_name2 = OrderedDict()
# func_name2[u"转换工具"] = (
#         (func1,u"坐标系转换"),
#         (func2,u"Excel转shp")
#     )
# func_name2[u"高标准农田"] =  (
#         (func3,u"坐标系转换2"),
#         (func4,u"Excel转shp2")
#     )
# # func_name2 = (u"转换工具",((func1,u"坐标系转换"),(func2,u"Excel转shp")),u"高标准农田",((func3,u"坐标系转换2"),(func4,u"Excel转shp2")))
#
# for k,v in func_name2.items():
#     print k,v


class ToolSet(object):
	"""
	用于显示工具箱button中的内容
	点击工具箱启动该类
	"""
	def __init__(self, master):
		self.master = master
		self.light_white = hyini.light_white
		self.cav_color=hyini.light_blue3 # canve长条的颜色
		self.padding2 = 3 #水平 tab 栏
		self.notebok()
		self.main_widget(self.make_test_dict())  # 工具栏 子部件 依附于 self.notebok()
		
	def notebok(self):
		# para
		# self.master["pady"] = 4
		# self.master["padx"] = 4
		# para
		_img = Image.open(join(gpath.base_icons_path, "Utilities-circle30.png"))
		"""______________________________notebook_____________________________"""
		self.padding=0
		self.tool_notebook = ttk.Notebook(self.master)
		# self.tool_notebook.place(relx=0.0, rely=0.0, relheight=1.0,relwidth=1.0)
		self.tool_notebook.pack(expand=True, fill="both")
		
		self.notebook_1 = ttk.Frame(self.tool_notebook)
		self.notebook_1.configure(relief="flat")
		self.tool_notebook.add(self.notebook_1, padding=self.padding)
		self.tool_notebook.tab(0, text="toolbar", compound="left", underline="-1")
		# second tab
		# self.notebook_2 = ttk.Frame(self.tool_notebook)
		# self.tool_notebook.add(self.notebook_2, padding=self.padding)
		# self.tool_notebook.tab(1, text="其它", compound="left", underline="-1")
		"""______________________________notebook_____________________________"""
		# self.icon = ImageTk.PhotoImage(_img.resize((30, 30)))
		self.icon = ImageTk.PhotoImage(_img)

	def make_canve(self, color):
		# cav = tk.Canvas(self.master,height =20,width =20)
		width = 100
		height = 10
		cav = tk.Canvas(self.notebook_1, width=width, height=height, bd=0)
		cav.pack(fill="x")
		for i in xrange(hyini.width):
			# cav.create_line(0, 70, 70, 90, fill="red", ) # dash=(4, 4)
			cav.create_line(i, 0, i, height, fill=color, )  # dash=(4, 4)
			# cav.create_line(height=4, fill="#5294e2") #  tags=("gradient",),
	
	def main_widget(self, funcs):
		"""
		 funcs(Dict): a function which return a dictionary containing feature widget(function)
		 such as :
			def make_test_dict(self):
				func_name = {
					u"顺序": (
						u"转换工具", u"高标准农田"
					),
					u"转换工具": (
						(self.test_func1, u"坐标系转换"),
						(self.test_func2, u"Excel转shp")
					),
					u"高标准农田": (
						(self.test_func3, u"坐标系转换2"),
						(self.test_func4, u"Excel转shp2")
					)
				}
				return func_name
		:return:
		"""
		# label_spec.pack(anchor="nw", fill="x")
		# The order of tool frame type:List
		frame_order = funcs[u"顺序"]
		
		for i in frame_order:
			feature_set = funcs[i]  # ((func3, u"坐标系转换2"),(func4, u"Excel转shp2"))
			# font=('Times',10,'bold','italic') # ,bg="#5294e2"
			# tk.Frame; newidgets.NeewwFrame
			big_frame = tk.Frame(
				self.notebook_1, relief="flat", height=20,
				borderwidth=4, background=self.light_white,
			)
			big_frame.pack(anchor="nw", fill="x")
			name_label = ttk.Label(
				big_frame, text =i, background=self.light_white,relief="flat")
			name_label.configure(font="-family {Microsoft YaHei UI} -size 9 -weight bold")
			name_label.pack(anchor="nw", fill=None)
			self.make_canve(hyini.light_blue)
			
			# A SET OF BUTTONS**************************************************
			for a_feature in feature_set:
				tool_func = a_feature[0]
				# print "tool_func:",tool_func
				tool_name = a_feature[1]
				
				frame = ttk.Frame(big_frame)
				frame.pack(anchor = "w",side="left") # 保证横向排列
				# self.PNotebook1 = ttk.Notebook(self.master, style='lefttab.TNotebook')
				# self.style.configure('lefttab.TNotebook', tabposition='wn')
				
				# button1_1 = ttk.Button(frame, text=tool_name, command=tool_func)
				button1_1 = newGUI.HoverButton(frame, text=tool_name, command=tool_func,
											   background=self.light_white,
											   width=80)
				button1_1.configure(image=self.icon)
				button1_1.configure(compound='top')
				button1_1.pack(side="top", anchor="center")
			# *******************************************************************
	
		
	def make_tab(self,func):
		"""
		点击每一个工具都会生成一个tab
		:param func: {Class} 工具的类
		:return: None
		"""
		"""_____________________________create tab____________________________"""
		tab = ttk.Frame(self.tool_notebook)
		tab.configure(relief="flat")
		"""________________________place tool gui at tab______________________"""
		f = func(tab)  # txt2shp.Txt2shp(self.master)
		name = f.name # tab's name
		"""________________________place tool gui at tab______________________"""
		
		self.tool_notebook.add(
			tab, text=name, padding=self.padding2, compound="left",
			underline="-1")
		tab_count = self.tool_notebook.index('end')  # tab数量
		self.tool_notebook.select(tab_count - 1) # focus new tab
	
	
	# # 主要将国土土地报备坐标txt文本处理生成shp文件
	# def txt2shp_1(self):
	# 	newGUI.destroy_child(self.master)
	# 	txt2shp.Txt2shp(self.master)
	#
	# # 将高版本mxd文件转换为低版本的
	# def to_other_version(self):
	# 	newGUI.destroy_child(self.master)
	# 	save_acopy.SaveACopyFunction(self.master)
	#

	# def txt2shp_1(self):
	#
	# 	# self.tool_notebook = ttk.Notebook(self.master)/
	# 	# self.tool_notebook.place(relx=0.0, rely=0.0, relheight=1.0,relwidth=1.0)
	# 	# self.tool_notebook.pack(expand=True, fill="both")
	#
	# 	tab = ttk.Frame(self.tool_notebook)
	# 	tab.configure(relief="flat")
	# 	# self.tool_notebook.add(tab, padding=self.padding)
	# 	# self.tool_notebook.tab(1, text="toolbar", compound="left", underline="-1")
	#
	# 	self.tool_notebook.add(
	# 		tab, text="toolbar", padding=self.padding, compound="left", underline="-1")
	# 	# print self.tool_notebook.select()
	# 	# print self.tool_notebook.index(self.tool_notebook.select())
	# 	# print self.tool_notebook.index('current')
	# 	tab_count = self.tool_notebook.index('end') # tab数量
	# 	self.tool_notebook.select(tab_count-1)
	#
	# 	# self.tool_notebook
	# 	# newGUI.destroy_child(self.master)
	# 	ss=txt2shp.Txt2shp(tab)
		
	
	def make_test_dict(self):
		# 工具列的显示顺序
		func_name = {
			u"顺序": (
				u"转换工具", u"高标准农田", "ArcGIS"
			),
			u"转换工具": (
				(None, u"坐标系转换"),
				(None, u"Excel转shp"),
				(lambda:self.make_tab(txt2shp.Txt2shp), u"TXT转shp"),
				(lambda:self.make_tab(save_acopy.SaveACopyFunction), u"版本降低")
			),
			u"高标准农田": (
				(lambda:self.make_tab(ZLDJ.ZLDJGui), u"质量等级"),
				(lambda: self.make_tab(area_cal.AreaCalGui), u"计算地类面积"),
				(lambda: self.make_tab(zldj_cal.ZLDJCalGui), u"计算质量等级"),
				(lambda: self.make_tab(cal_real_area.MainGUI), u"计算真实面积")
			),
			
			"ArcGIS": (
				(lambda:self.make_tab(multiplexport.MultipExp), u"多进程批量导图"),
				(None, "test")
			)
		}
		return func_name
	

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
	widget = event.widget
	element = widget.identify(event.x, event.y)
	if "close" in element:
		index = widget.index("@%d,%d" % (event.x, event.y))
		widget.state(['pressed'])
		widget._active = index

def _button_release(event):
	widget = event.widget
	if not widget.instate(['pressed']):
			return
	element = widget.identify(event.x, event.y)
	try:
		index = widget.index("@%d,%d" % (event.x, event.y))
	except TclError:
		pass
	if "close" in element and widget._active == index:
		widget.forget(index)
		widget.event_generate("<<NotebookTabClosed>>")

	widget.state(['!pressed'])
	widget._active = None

def _mouse_over(event):
	widget = event.widget
	element = widget.identify(event.x, event.y)
	if "close" in element:
		widget.state(['alternate'])
	else:
		widget.state(['!alternate'])