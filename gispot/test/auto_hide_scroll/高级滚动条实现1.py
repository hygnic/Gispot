#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/19 22:04
# Reference:
"""
Description: 希望实现非点击状态下的移动滚动条和内容
目前只实现了移动滚动条
Usage:
"""
# ---------------------------------------------------------------------------
import ttk
import Tkinter as tk

root = tk.Tk()







	

	

def on_enter(widget):
	def inner(event):
		print "enter"
		print event.y
	widget.bind("<Enter>", inner)


def on_leave(widget):
	def inner(event):
		print "leave"
		print event.delta
	widget.bind("<Leave>", inner)
	
def mouse_up(widget):
	def inner(event):
		print "move"
		print event.delta # 向上滑是120，向下是-120
	widget.bind_all("<MouseWheel>", lambda e: y_move(widget, e))
	
def y_move(widget, event):
	widget.yview_scroll(-1*int(event.delta/120),'units')

frame = tk.Frame(root)
frame.pack()

"""____________________________________________________________________________"""
"""____________________________________________________________________________"""
on_enter(frame)
on_leave(frame)

"""____________________________________________________________________________"""
"""____________________________________________________________________________"""

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill="y")
txt = tk.Text(frame, yscrollcommand= scrollbar.set)
txt.insert("end", "this is tkinter\n"*50)
mouse_up(txt)
txt.pack()
scrollbar.configure(command=txt.yview)


	




root.mainloop()