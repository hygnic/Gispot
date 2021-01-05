# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2020/3/17
# python2 arcgis10.6

import os
import Tkinter as tk
from gpconfig import newGUI
from gpconfig import gppath
from teminal import export


"""viewer items
配置位于主界面右边的toolbar viewer中的部件"""

# ----------------------------------------------------
# 可运行


# 单进程导出图片JPEG(适用于文件夹和单个mxd文件)
def export_s(master):
	frame = newGUI.ButtonFrame(
		master,
		tk.PhotoImage(file=gppath.GifPath.confirm),
		"导出图片",command=export.func)
	frame.pack(side="left", anchor="nw", fill=None, expand=False)
	
# ----------------------------------------------------
# 仅查看


# 根据文件的后缀匹配图标 仅查看
class Filter(object):
	def __init__(self, master):
		path = ur"G:\MoveOn\Gispot\Lib\cpt"
		self.master = master
		self.flag1 = 0
		for item in os.listdir(path):
			aa, suffi = os.path.splitext(item)
			self.name = os.path.basename(aa)
			# print self.name
			# print suffi
			suffi = suffi.lower()
			if suffi == ".py":
				self.flag1 = 1
			elif suffi == "tbx":
				self.flag1 = 2
			# print self.flag1
			self.icon_selector()
	
	def icon_selector(self):
		if self.flag1 == 1:
			newGUI.ButtonFrame(
				self.master, tk.PhotoImage(file=gppath.GifPath.python),
				self.name, command=None)
		elif self.flag1 == 2:
			newGUI.ButtonFrame(
				self.master, tk.PhotoImage(file=gppath.GifPath.python),
				self.name, command=None)
	
			
if __name__ == '__main__':
	# 	path = ur"G:\MoveOn\Gispot\Lib\misc"
	#
	# 	for i1 in os.listdir(path):
	# 		aa, suffi = os.path.splitext(i1)
	# 		name = os.path.basename(aa)
	# 		print name
	# 		print suffi
	class Filter(object):
		def __init__(self, master):
			path = ur"G:\MoveOn\Gispot\Lib\cpt"
			self.master = master
			for item in os.listdir(path):
				aa, suffi = os.path.splitext(item)
				self.name = os.path.basename(aa)
				print self.name
				print suffi
				suffi = suffi.lower()
				if suffi == ".py":
					self.flag1 = 1
				elif suffi == "tbx":
					self.flag1 = 2
				print self.flag1
