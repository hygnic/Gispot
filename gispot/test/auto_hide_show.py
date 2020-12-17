#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/6 20:03
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk


class AutoScrollbar(tk.Scrollbar):
	"""Create a scrollbar that hides iteself if it's not needed. Only
	works if you use the pack geometry manager from tkinter.
	"""
	
	def set(self, lo, hi):
		if float(lo) <= 0.0 and float(hi) >= 1.0:
			self.pack_forget()
		else:
			if self.cget("orient") == tk.HORIZONTAL:
				self.pack(fill=tk.X, side=tk.BOTTOM)
			else:
				self.pack(fill=tk.Y, side=tk.RIGHT)
		tk.Scrollbar.set(self, lo, hi)
	
	def grid(self, **kw):
		raise tk.TclError("cannot use grid with this widget")
	
	def place(self, **kw):
		raise tk.TclError("cannot use place with this widget")


class AutoS(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self)
		vscrollbar = AutoScrollbar(master)
		canvas = tk.Canvas(master, yscrollcommand=vscrollbar.set)
		canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		vscrollbar.config(command=canvas.yview)
		frame = tk.Frame(canvas)
		canvas.create_window(0, 0, anchor=tk.NW, window=frame)
		
		frame.update_idletasks()
		canvas.config(scrollregion=canvas.bbox("all"))



if __name__ == '__main__':
	
	root = tk.Tk()
	
	
	
	ss=AutoS(root)
	label = tk.Label(ss, text="text", font=("Arial", "512"))
	label.pack()
	
	root.mainloop()