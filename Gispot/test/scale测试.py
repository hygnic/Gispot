# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/27
import Tkinter as tk
import ttk


class Tooltk(object):
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Tools")
		self.window.geometry("300x400")
		self.bt = ttk.Button(text="confirm")\
			.pack(expand = True)
		
		# tk.Scale(
		# 	from_=-400,  # 设置最小值
		# 	to=500,  # 设置最大值
		# 	resolution=5,  # 设置步距值
		# 	orient=tk.HORIZONTAL,  # 设置水平方向
		#
		# 	  ).pack()
		self.numin= tk.IntVar()
		
		tk.Scale(
			from_=2,  # 设置最小值
			to=12,  # 设置最大值
			orient=tk.HORIZONTAL, # 设置水平方向
			variable=self.numin,
			resolution=1,
			# relief = tk.FLAT,
			# sliderrelief = tk.FLAT,
			sliderlength = 10,
			# borderwidth=0,
			# tickinterval=7 数字刻度
			# digits =5 小数
			foreground = "Olive"
		
			
			
		).pack()
		
		ss =ttk.Scrollbar().pack()
		ttk.Style()
		
		en =tk.Entry(textvariable = self.numin ).pack()
		
# {"q": 1, "w": 2}

app = Tooltk()
app.window.mainloop()