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
		
		tk.Scale(
			  from_=-400,  # 设置最小值
			  to=500,  # 设置最大值
			  resolution=5,  # 设置步距值
			  orient=tk.HORIZONTAL  # 设置水平方向
			  ).pack()
		
		ttk.Scale(
			from_=-400,  # 设置最小值
			to=500,  # 设置最大值
			orient=tk.HORIZONTAL, # 设置水平方向
			
		).pack()
		

# {"q": 1, "w": 2}

app = Tooltk()
app.window.mainloop()