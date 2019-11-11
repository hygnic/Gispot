# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19

import os
import Tkinter as tk
import sys
# 获取程序当前的文件夹位置
# E:\move on move on\GisCat\bin\appenter.py
realp = os.path.abspath(__file__)
# 上级 绝对路径
# E:\move on move on\GisCat
root_base = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# E:\move on move on\GisCat\GisCat
rb_GisCat = os.path.join(root_base, "GisCat")
# E:\move on move on\GisCat\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\GisCat\GUIs\Icons
rbg_Icons = os.path.join(rb_GUIs, "Icons")
rbdoc = os.path.join(root_base, "docs")
giscat_paths = [root_base,rb_GisCat,rb_GUIs,rbg_Icons,rbdoc]
for giscat_path in giscat_paths:
	sys.path.append(giscat_path)
from nonArcGIS import gstrename
from HyMap import multip_ejpg
# from threading import Thread


class AppEntrance(object):
	"""进行打包的可视化外壳"""
	def __init__(self):
		self.rootwindow = tk.Tk()
		self.rootwindow.title(u"主界面")
		self.rootwindow.geometry("700x500")
		self.rootwindow.iconbitmap(default=os.path.join(rbg_Icons,"cpt2.ico"))
		# self.rootwindow.attributes('-topmost', 0)
		
	def menu(self):
		"""设置置顶菜单栏"""
		# window = tk.Tk()
		# window.title('My Window')
		# window.geometry('500x300')
		label_uesless = tk.Label(self.rootwindow, text='       ', bg='olive')
		label_uesless.pack(side = "bottom",anchor = tk.SE)
		
		def do_job():
			# global counter
			counter = 0
			label_uesless.config(text='do ' + str(counter))
			counter += 1
		# 创建菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
		menubar = tk.Menu(self.rootwindow)
		# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，
			# Exit功能项）
		menubar_file = tk.Menu(menubar, tearoff=0)
		# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
		menubar.add_cascade(label='File', menu=menubar_file)
		# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，
			# 每一个小菜单对应命令操作。
		menubar_file.add_command(label='New', command=do_job)
		menubar_file.add_command(label='Open', command=do_job)
		menubar_file.add_command(label='Save', command=do_job)
		menubar_file.add_separator()  # 添加一条分隔线
		menubar_file.add_command(label='Exit',
								 command=self.rootwindow.quit)  # 用tkinter里面自带的quit()函数
		submenu = tk.Menu(menubar_file)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
		# 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
		submenu.add_command(label='Submenu_1',
							command=do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
		# 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
		# 创建第二级菜单，即菜单项里面的菜单
		menubar_file.add_cascade(label='Import', menu=submenu,
								 underline=0)  # 给放入的菜单submenu命名为Import
		# edit菜单栏
		menubar_edit = tk.Menu(menubar, tearoff=0)
		# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
		menubar.add_cascade(label='Edit', menu=menubar_edit)
		# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元,
			# 就会触发do_job的功能
		menubar_edit.add_command(label='Cut', command=do_job)
		menubar_edit.add_command(label='Copy', command=do_job)
		menubar_edit.add_command(label='Paste', command=do_job)
		
		# 制图mapping菜单栏
		menubar_gst = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label = u"两区公示图", menu=menubar_gst)
		menubar_gst.add_command(label=u'公示图命名规范化',
								command=self.open_GSTrename)
		# 创建菜单栏完成后，配置让菜单栏menubar显示出来
		
		# self.root.mainloop()
		
		menubar_map = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label=u"制图", menu=menubar_map)
		menubar_map.add_command(label=u'多进程导图JPEG',
								command=self.open_Multip_exp)
		
		# 创建菜单栏完成后，配置让菜单栏menubar显示出来
		self.rootwindow.config(menu=menubar)
	
	
	@staticmethod
	def open_GSTrename():
		GST_app = gstrename.App()
		GST_app.window.mainloop()
	
	@staticmethod
	def open_Multip_exp():
		mul_app = multip_ejpg.MultipExp()
		mul_app.window.mainloop()
	
# if __name__ == '__main__':
# 	AppEntrance().menu()


# if __name__ == '__main__':
# 	app = AppEntrance()
# 	app.root.mainloop()

if __name__ == '__main__':
	app = AppEntrance()
	app.menu()
	app.rootwindow.mainloop()