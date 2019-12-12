# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/28
"""
完善主窗口（tool_entrance）的功能：
	窗口居中
	清楚父部件中的子部件
	

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
	
	
def destroy_chird(master):
	"""
	监测一个部件内部是否有子部件，如果有，
	那么删除子部件
	:param master: 父部件
	:return:
	"""
	widget_set = master.winfo_children()
	if widget_set:
		for i in widget_set:
			i.destroy()