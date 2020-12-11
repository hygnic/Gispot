# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19

"""
*************************************该工具的主体界面****************************
********************************************************************************
*************************************CLASS: AppEntrance*************************
*************************************MAIN FEATURES:*****************************
                                menu: menu
                                run_toolbar_viewer: Toolbar
                                
********************************************************************************
********************************************************************************
"""
import os
import Tkinter as tk
import sys
import ttk
import tkMessageBox
from webbrowser import open as weberopen
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

# 获取当前的文件位置
# E:\move on move on\gispot\GUIs\entrance.py
realp = os.path.abspath(sys.argv[0])
print "os.path.abspath(sys.argv[0]):",os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# 该文件所处的文件夹绝对路径
realp_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = os.path.abspath(os.path.dirname(realp_dir))
print "os.path.dirname(sys.argv[0]):", os.path.dirname(sys.argv[0])
print "root_base:",root_base
# E:\move on move on\gispot\gispot
rb_GisCat = os.path.join(root_base, "gispot")
# E:\move on move on\gispot\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\gispot\GUIs\Icons
rbg_Icons = os.path.join(rb_GUIs, "Icons")
rbdoc = os.path.join(root_base, "docs")
rb_bin = os.path.join(root_base, "bin")
rb_libs = os.path.join(root_base, "Lib")
rb_GUIconfig = os.path.join(rb_libs, "GUIconfig")

giscat_paths = (root_base,
				rb_GisCat,
				rb_GUIs,
				rbg_Icons,
				rbdoc,
				rb_bin,
				rb_libs,
				rb_GUIconfig)
for giscat_path in giscat_paths:
	sys.path.append(giscat_path)

# print "sys.path:",sys.path

# import LQHD # 识别不了gstrename
# from gispot.LQHD import gstrename
# from gispot.crcpy import multip_ejpg
# from gispot.crcpy import explode_mulitp
# from gispot.crcpy import task_dispatch


# 界面模块导入
import interface
# 功能模块导入
import gstrename
import crcpy.multiplexport
import crcpy.explode
import crcpy.task_dispatch
import crcpy.ZLDJ
# 配置包导入
from GUIconfig import newGUI,hyini
from GUIconfig import gispotpath

# Gispot图标
icon = gispotpath.PngIcon.icon

import Tix


def kill_pid(pid):
	# 本函数用于中止传入pid所对应的进程
	if os.name == 'nt':
		# Windows系统
		cmd = 'taskkill /pid ' + str(pid) + ' /f'
		try:
			os.system(cmd)
			print(pid, 'killed')
		except Exception as e:
			print(e)
	elif os.name == 'posix':
		# Linux系统
		cmd = 'kill ' + str(pid)
		try:
			os.system(cmd)
			print(pid, 'killed')
		except Exception as e:
			print(e)
	else:
		print('Undefined os.name')


class AppEntrance(object):
	"""进行打包的可视化外壳"""
	prograss_int = 0
	
	def __init__(self):
		self.rootwindow = tk.Tk()
		# self.rootwindow = ThemedTk(theme="arc")
		self.rootwindow.title("")
		# self.rootwindow.title("GISPOT")
		# self.rootwindow.update_idletasks()
		# self.rootwindow.overrideredirect(True)
		# self.rootwindow.tk_setPalette(background="#f5f6f7") # 一次性修改所有背景颜色
		newGUI.screen_cetre(self.rootwindow, width=hyini.width, height=hyini.height)
		self.rootwindow.iconbitmap(default=icon)
		self.rootwindow.resizable(1, 1)
		self.menu()
		# bt.pack(side='left')
		# self.rootwindow.attributes('-topmost', 0)
		self.gradient_bar()
		self.upgrade_from_github()
		# -------------------------------------
		# 主界面左侧图标工具栏
		# Frame的实际大小不仅仅受width控制，如果其中有其它部件，
		# 以其它部件大小为准
		self.main_face = tk.Frame(self.rootwindow, relief="sunken" ,width= 55, height = 600,bd =1)
		self.main_face.pack(side="left", fill="both", expand=True)
		# self.toolbar.place(x=0,y=0)
		# 初始界面右侧的交互界面的框架 interface_frame
		# self.interface_frame = tk.Frame(self.rootwindow, relief="groove",width= 900, height = 600)
		# self.interface_frame.pack(side="right", expand=True, fill="both")
		# self.interface_frame.place(x=55,y=0)
		
		# 绑定退出弹窗与退出功能，实现退出功能
		self.rootwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
		# 界面
		# self.run_menu()
		# self.run_toolbar_viewer()
		tnb = interface.ttknotebook(self.main_face)
		interface.ToolSet(tnb.notebook2)
	
	
	def gradient_bar(self):
		self.gradient_canv = newGUI.GradientCanvas(
			self.rootwindow, "#ffc851", "#808000", relief="flat")
		self.gradient_canv.pack(side="bottom", anchor=tk.SE, fill="x")
		self.gradient_canv.create_text(32, 10, text="gispot 1")
	
	def upgrade_from_github(self):
		def open_u():
			update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
			weberopen(update_url, new=0, autoraise=True)
		# self.image_octacat = tk.PhotoImage(file=gispotpath.PngIcon.github)
		self.image_octacat = ImageTk.PhotoImage(
			Image.open(gispotpath.PngIcon.github))
		ap_button = newGUI.HoverButton(master=self.gradient_canv,
									   command=open_u, bd=2,
									   image=self.image_octacat,
									   width=15, height=15)
		# ap_button = ttk.Button(master=self.gradient_canv,
		# 							   command=open_u,
		# 							   image=self.image_octacat)
		ap_button.pack(side='top', expand='yes', anchor="se")
	
	def menu(self):
		"""设置置顶菜单栏"""
		self.menubar = tk.Menu(self.rootwindow)
		# 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，# Exit功能项）
		self.menubar_file = tk.Menu(self.menubar, tearoff=0)
		# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
		self.menubar.add_cascade(label='File', menu=self.menubar_file)
		# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，
		# 每一个小菜单对应命令操作。
		self.menubar_file.add_command(label='New', command=None)
		self.menubar_file.add_command(label='Open', command=None)
		self.menubar_file.add_command(label='Save', command=None)
		self.menubar_file.add_command(label='Prograss Bar',
									  command=None)
		self.menubar_file.add_separator()  # 分隔线
		self.menubar_file.add_command(
			label='Exit', command=self.rootwindow.quit)  # 用tkinter里面自带的quit()函数
		submenu = tk.Menu(self.menubar_file)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
		# 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
		submenu.add_command(
			label='Submenu_1', command=None)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
		# 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
		# 创建第二级菜单，即菜单项里面的菜单
		self.menubar_file.add_cascade(
			label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import
		# edit菜单栏
		self.menubar_edit = tk.Menu(self.menubar, tearoff=0)
		# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
		self.menubar.add_cascade(label='Edit', menu=self.menubar_edit)
		self.menubar_edit.add_command(label='Cut', command=None)
		self.menubar_edit.add_command(label='Copy', command=None)
		self.menubar_edit.add_command(label='Paste', command=None)
		
		# 两区公示图 菜单栏
		self.menubar_gst = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="两区公示图", menu=self.menubar_gst)
		self.menubar_gst.add_command(
			label='公示图命名规范化', command=self.open_GSTrename)
		
		# 制图mapping菜单栏
		self.menubar_map = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label=u"制图", menu=self.menubar_map)
		self.menubar_map.add_command(
			label=u'多进程批量出图(JPEG)', command=self.open_Multip_exp)
		self.menubar_map.add_command(label='拆分多部件',
									 command=self.explode_mulitp)
		self.menubar_map.add_command(label='任务分配',
									 command=self.start_dispatch_task)
		
		# 高标准农田
		self.menubar_GBZ = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="高标准农田", menu=self.menubar_GBZ)
		self.menubar_GBZ.add_command(label='修改质量等级',
									 command=self.start_ZLDJ)
		
		# 关于 栏
		self.menubar_about = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="关于", menu=self.menubar_about)
		self.menubar_about.add_command(
			label='获取更新', command=self.upgrade_from_github)
	
	# 配置安放菜单栏，写成方法便于调控纯程序
	def run_menu(self):
		self.rootwindow.config(menu=self.menubar)
	
	# def trans_name(self):
	#     """
	#     之前要将四川标准的图片名称改为国家标准的名称，
	#     没用上，以后也没有用了
	#     """
	#     def open_gst_trans():
	#         from LQHD import gst_trans
	#         open_gst_trans = gst_trans.App()
	#         open_gst_trans.window.mainloop()
	#
	#     def open_fbt_trans():
	#         from LQHD import fbt_trans
	#         open_fbt_trans = fbt_trans.App()
	#         open_fbt_trans.window.mainloop()
	#
	#     # 图件命名转换 菜单栏
	#     self.menubar_trans = tk.Menu(self.menubar, tearoff=0)
	#     self.menubar.add_cascade(label=u"两区图件名称装换", menu=self.menubar_trans)
	#     self.menubar_trans.add_command(label=u'公示图名称',
	#                               command=open_gst_trans)
	#     self.menubar_trans.add_command(label=u'分布图名称',
	#                               command=open_fbt_trans)
	#     # self.menubar_trans.add_command(label=u'标志牌名称'）
	#
	#     # 创建菜单栏完成后，配置让菜单栏self.menubar显示出来
	#     self.rootwindow.config(menu=self.menubar)
	
	# ----------------------------------------
	"""
	全是一些按键的command指令，放在这里方便添加修改一些自定义功能
	使用的各种函数方法说明：
		newidgets.destroy_child(self.main_f): 在打开一个功能的GUI界面时，销毁覆盖
			之前存在的GUI界面
	"""
	def open_GSTrename(self):
		newGUI.destroy_child(self.interface_frame)
		# gstrename.App(self.main_f)
		gstrename.App(self.interface_frame)
	
	def open_Multip_exp(self):
		newGUI.destroy_child(self.interface_frame)
		# multip_ejpg.MultipExp(self.main_f)
		crcpy.multiplexport.MultipExp(self.interface_frame)
	
	# 多进程导出JPEG图片
	def explode_mulitp(self):
		newGUI.destroy_child(self.interface_frame)
		# explode_mulitp.App(self.main_f)
		crcpy.explode.App(self.interface_frame)
	
	def start_dispatch_task(self):
		newGUI.destroy_child(self.interface_frame)
		# task_dispatch.StartApp(self.main_f)
		crcpy.task_dispatch.StartApp(self.interface_frame)
	
	def start_ZLDJ(self):
		# pool_list = MuCation.submultiprocess
		# while pool_list:
		#     print dead_p
		#     dead_p =pool_list.pop()
		#     kill_pid(dead_p)
		newGUI.destroy_child(self.interface_frame)
		# task_dispatch.StartApp(self.main_f)
		crcpy.ZLDJ.AppGUI(self.interface_frame)
	
	# ----------------------------------------
	
	def run_toolbar_viewer(self):
		# 使程序主要面板运行起来
		# return 1
		# toolbar_viewer就是建立在input_interface上的
		button1 = interface.ttknotebook(
			self.toolbar, self.interface_frame)
		# button1.config()
	
	def button_config(self):
		def open_u():
			import webbrowser
			update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
			webbrowser.open(update_url, new=0, autoraise=True)
		ap_button = ttk.Button(text=u"获取更新",command=open_u)
		ap_button.pack(side='top', expand='yes', anchor="se")
	
	def on_closing(self):
		# 退出确认功能，防止误触发
		if tkMessageBox.askokcancel("Quit", "   Do you want to quit?"):
			self.rootwindow.destroy()

if __name__ == '__main__':
	class AppEntrance2(object):
		"""进行打包的可视化外壳"""
		prograss_int = 0
		
		def __init__(self):
			# self.rootwindow = tk.Tk()
			self.rootwindow = ThemedTk(theme="arc")
			self.rootwindow.title("GISPOT")
			# self.rootwindow.tk_setPalette(background="#f5f6f7") # 一次性修改所有背景颜色
			newGUI.screen_cetre(self.rootwindow, width=hyini.width,
								height=hyini.height)
			self.rootwindow.iconbitmap(default=icon)
			self.rootwindow.resizable(0, 0)
			# bt.pack(side='left')
			# self.rootwindow.attributes('-topmost', 0)
			# self.gradient_bar()
			# self.upgrade_from_github()
			# -------------------------------------
			# 主界面左侧图标工具栏
			# Frame的实际大小不仅仅受width控制，如果其中有其它部件，
			# 以其它部件大小为准
			self.toolbar = tk.Frame(self.rootwindow, relief="sunken", width=45,bg="red",
									height=600, bd=1)
			# self.toolbar.pack(side="left", fill="both", expand=False)
			self.toolbar.place(x=0, y=0)
			# 初始界面右侧的交互界面的框架 interface_frame
			self.interface_frame = tk.Frame(self.rootwindow, relief="groove",
											width=900, height=600,bg="blue")
			# self.interface_frame.pack(side="right", expand=True, fill="both")
			self.interface_frame.place(x=45, y=0)
	
	app = AppEntrance2()
	app.rootwindow.mainloop()