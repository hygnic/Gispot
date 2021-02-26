# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/10

import Tkinter as tk





class Block(tk.Frame):
	
	def __init__(self,master,name,**kw):
		tk.Frame.__init__(self,master,**kw)
		self.master = master
		# master1.rowconfigure(0, weight=1)
		# master1.columnconfigure(0, weight=1)
		# self.grid(row=0, column=0, sticky=tk.NSEW)
		# self.rowconfigure(1, weight=1)
		# self.rowconfigure(0, weight=1)
		# self.columnconfigure(1, weight=1)
		# self.columnconfigure(0, weight=1)
		
		self.pack(expand = True,fill = "both")
		label = tk.Label(self,text = name)
		label.grid(row = 0,sticky="nw",padx = 10)
		entry = tk.Entry(self,relief = "flat")
		entry.grid(row = 1,sticky="nwes",padx = 10)
		button = tk.Button(self,text = "oo")
		button.grid(row = 1,column = 1,sticky="e",padx = 10)
		
		# entry.rowconfigure(0, weight=2)
		# entry.rowconfigure(1, weight=1)
		
		# self.rowconfigure(0, weight=2)
		# self.rowconfigure(1, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(0, weight=20)
rooot = tk.Tk()
rooot.geometry("600x300")
mmm = Block(rooot,u"打开文件夹",bg = "green")
mmm.mainloop()













# root = tk.Tk()
#
# class Block(tk.Frame):
# 	def __init__(self,master1,name,**kw):
# 		tk.Frame.__init__(self,master1,**kw)
# 		self.master1 = master1
#
# 		tk.Label(self,text = name).pack(anchor = "w",  pady=10)
#
# 		self.block1 = tk.Frame(self)
# 		self.block1.pack()
# 		print self.block1.winfo_geometry()
#
# 		tk.Entry(self.block1,relief = "flat",width = 40).pack(side = "left")
# 		tk.Button(self.block1,text = "oo").pack(side = "right")
# 		# print args
# 		# print args
# #
#
#
# bba = Block(root,u"文件夹",bd = 20,bg = "blue")
# # , width=10,height = 10
# bba.pack()
#
# root.mainloop()
class te1(object):
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("600x600")
		
		self.f1 = tk.Frame(root,bg = "blue",width = 300,height = 100)
		self.f1.pack(side = "left",fill = "both",expand = True)
		self.f2 = tk.Frame(root,bg = "green",width = 300,height = 100)
		self.f2.pack(side = "right", fill = "both",expand = True)

		self.root.mainloop()
		
		
class te2(object):
	def __init__(self):
		self.window = tk.Tk()
		self.window.geometry("1192x650")
		
		self.frame_side_bar = tk.Frame(self.window, width=496,
									   border=2, relief="flat",bg = "blue")
		self.frame_side_bar.pack(side="right",
								 expand=True, fill="both")
		self.frame_side_bar.propagate(True)
		# 左边的主框
		self.frame_left_side = tk.Frame(self.window, width=696,
										border=2, relief="flat")
		self.frame_left_side.pack(side="left",
								  expand=True, fill="both")
		
		
		self.frame_major = tk.Frame(self.frame_left_side, width=696,
									 relief="flat",bg = "green")
		self.frame_major.pack(
							  expand=True, fill="both")
		# 左边主框下的底部栏
		self.frame_bottom_bar = tk.Frame(self.frame_left_side, height="60",
										 border=2,
										 relief="groove")  # ffc851
		self.frame_bottom_bar.pack(
								   expand=False, fill="both")
		
		help_f = tk.LabelFrame(self.frame_major, width=696,
							   relief=tk.RIDGE, text="____" * 80,
							   bd=2)
		help_f.pack(anchor = "s",
					expand=True, fill="both")
		# 设置带滚动条的text
		s_bar = tk.Scrollbar(help_f, relief="flat",
							 )
		s_bar.pack(side="right", fill="y")
		self.help_text = tk.Text(help_f, relief=tk.FLAT, width=696,
								 yscrollcommand=s_bar.set)
		
		self.help_text.pack(expand=True, fill="both")
		s_bar.config(command=self.help_text.yview)
		
		
		self.window.mainloop()
		

# bbb = te2()