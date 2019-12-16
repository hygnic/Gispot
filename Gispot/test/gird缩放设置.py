# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/15
import Tkinter  as tk
import tkFileDialog
import ttk

# root = Tk()
#
# content = ttk.Frame(root, padding=(3,3,12,12))
# frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)
#
# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()
#
# onevar.set(True)
# twovar.set(False)
# threevar.set(True)
#
# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")
#
# content.grid(column=0, row=0, sticky=(N, S, E, W))
# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)
#
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# content.columnconfigure(0, weight=3)
# content.columnconfigure(1, weight=3)
# content.columnconfigure(2, weight=3)
# content.columnconfigure(3, weight=1)
# content.columnconfigure(4, weight=1)
# content.rowconfigure(1, weight=1)
#
# root.mainloop()
def bar():
	
	root = tk.Tk()
	root.columnconfigure(0, weight=1)
	s_bar = tk.Scrollbar(root, relief="flat",
						 elementborderwidth=-15)
	text_1 = tk.Text(root, yscrollcommand = s_bar.set)
	text_1.grid(row=0, column=0, sticky="nsew")
	s_bar.grid(row=0,column=1,sticky = "ns")
	s_bar.config(command=text_1.yview)
	root.mainloop()

bar()
class main(object):
	def __init__(self):
		self.frame_major = tk.Tk()
		self.setting()
		# self.frame_right_side = tk.Frame(self.window, width=496,
		# 								 border=2, relief="flat",bg = "green")
		# self.frame_right_side.grid(stick="nsew")
		# # self.frame_right_side.propagate(False)
		# # 左边的主框
		# self.frame_left_side = tk.Frame(self.window, width=696,
		# 								border=2, relief="flat",bg = "olive")
		# self.frame_left_side.grid(column=1, stick="nsew")
		# # 里面 的 上部分
		# # self.frame_major = tk.Frame(self.frame_left_side, width=696,
		# # 							relief="flat")
		# # self.frame_major.pack(
		# # 	expand=True, fill="both")
		# # 主框下的底部栏
		# self.frame_bottom_bar = tk.Frame(self.frame_left_side, height="60",
		# 								 bg="blue", border=2,
		# 								 relief="groove")  # ffc851
		# self.frame_bottom_bar.grid(row=1, column=0, stick="nsew")
	def setting(self):
		def select_file():
			file_path = tkFileDialog.asksaveasfilename(filetypes=
													   [(u'文本文档', '*.txt'), ('All Files', '*')])
			# 刷新normal_single_block() 中的Entry
			# lis = self.file_paths_.append(file_path)
			# print lis
			input_msg1.set(file_path)
		
		# return file_path
		sfb_name = "ok"
		name_label = tk.Label(self.frame_major, text=sfb_name)
		name_label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
		# 块一
		# 将Entry和按钮整齐的放到一起
		frame_one = tk.Frame(self.frame_major, height="60", width="700",
							 pady=4)  # , border =1 ,relief = "raised"
		frame_one.pack(side="top", anchor="center", expand=False, fill="x")
		# 按钮
		# photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
		self.addfile_button = tk.Button(frame_one,text = u"按键",
										  command=select_file, width=24)
		self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
		# Entry
		input_msg1 = tk.StringVar()
		self.input_sb = tk.Entry(frame_one, textvariable=input_msg1,
								 border=2, relief=tk.FLAT)
		self.input_sb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
						   fill=tk.X, padx=15)
		return 1
		
# main().frame_major.mainloop()