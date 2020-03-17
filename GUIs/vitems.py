# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2020/3/17
# python2 arcgis10.6

import tkinter as tk
from TkGUIconfig import newidgets
from TkGUIconfig import paths
from ccmd import export


"""viewer items
配置位于主界面右边的toolbar viewer中的部件"""

# ----------------------------------------------------
# 可运行

# 单进程导出图片JPEG(适用于文件夹和单个mxd文件)
def export_s(master):
	newidgets.ButtonFrame(
		master,
		tk.PhotoImage(file=paths.GifPath.gif_python),
		"导出图片",command=export.func
	)
	
	
# ----------------------------------------------------
# 仅查看

def itme_1(master):
	newidgets.ButtonFrame(
		master,
		tk.PhotoImage(file=paths.GifPath.gif_python),
		"自动计算面积", command=export.func
	)