# -*- coding:utf-8 -*-
# Created on: 2020/12/15 22:14

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk
try:
	import ttk
except ImportError:
	import tkinter.ttk as ttk

class AutoScroll(tk.Scrollbar):
	# def __init__(self, master):
	# 	ttk.Scrollbar.__init__(self, master)
	# 	self.master = master
	
	def __init__(self, master):
		tk.Scrollbar.__init__(self, master)
		self.master = master
	

	def frame(self):
		_frame = tk.Frame(self.master)
		_frame.pack(side="right", fill="y")
		
		
		
	def set(self, lo, hi):
		if float(lo) <= 0.0 and float(hi) >= 1.0:
			# grid_remove is currently missing from Tkinter!
			self.pack_forget()
		else:
			if self.cget("orient") == tk.HORIZONTAL:  # 将字符串转变为关键字
				self.pack(fill=tk.X)
			else:
				self.pack(side="right", fill="y")
		tk.Scrollbar.set(self, lo, hi)
		
		


root = tk.Tk()
root.geometry("200x300+500+600")
frame = tk.Frame(root, bg="SystemWindow")

frame.pack(side="right", fill="y")
hscrollbar = AutoScroll(frame)
hscrollbar.pack(side=tk.RIGHT, fill="y")

test_text = tk.Text(root, wrap=tk.NONE, yscrollcommand=hscrollbar.set)
test_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
print tk.Pack.__dict__.keys()

hscrollbar.config(command=test_text.xview)
poem_name = "Do Not Go Gentle into That Good Night.txt"
msg = "This is tkinter or Tkinter!\n"*50
test_text.insert(tk.END, msg)
# frame.update_idletasks()
root.mainloop()