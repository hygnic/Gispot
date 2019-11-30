# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/28
"""
tool_entrance和tooltk都需要的功能
"""


# import Tkinter as tk


def screen_cetre(master, width=None, height=None):
	# 窗口居中
	screenwidth = master.winfo_screenwidth()
	screenheight = master.winfo_screenheight()
	if width is None:
		width, height = 800,660
	geometry_size = "{}x{}+{}+{}".format(width, height,
										 (screenwidth - width) / 2,
										 (screenheight - height) / 2)
	master.geometry(geometry_size)
	# geometry = '%dx%d+%d+%d' % (
	# width, height, (screenwidth - width) / 2, (screenheight - height) / 2)