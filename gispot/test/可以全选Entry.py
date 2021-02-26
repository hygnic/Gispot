# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/19

import Tkinter as tk

# def callback(event):
#
#     # select text
#     event.widget.select_range(0, 'end')
#     # move cursor to the end
#     event.widget.icursor('end')
#     #stop propagation
#     return 'break'
#
# root = tk.Tk()
#
# e = tk.Entry(root)
# e.pack()
# e.bind('<Control-a>', callback)
#
# root.mainloop()
class TTTT(object):

	def __init__(self):
		self.root = tk.Tk()
		self.txt = tk.Text(self.root)
		self.txt.pack()
		self.txt.bind_class("Text","<Control-a>", self.selectall)
	
	def selectall(self, event):
		event.widget.tag_add("sel","1.0","end")
		
TTTT().root.mainloop()

# root = tk.Tk()
# txt_text = tk.Text(root)
# txt_text.pack()
# def ctext_selectall(txt):
#     """Select all text in the text widget"""
#     txt_text.tag_add('sel', '1.0', 'end')
#
# txt_text.bind('<Control-a>', ctext_selectall)
#
# root.mainloop()