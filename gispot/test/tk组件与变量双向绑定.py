# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/23


from Tkinter import *
# 导入ttk
import ttk

class App(object):
	def __init__(self, master):
		self.master = master
		self.st = StringVar()
		self.initWidgets()
	def initWidgets(self):
		# 创建Entry组件，将其textvariable绑定到self.st变量
		ttk.Entry(self.master, textvariable=self.st,
				  width=24,
				  font=('StSong', 20, 'bold'),
				  foreground='red').pack(fill=BOTH, expand=YES)
		# 创建Frame作为容器
		f = Frame(self.master)
		f.pack()
		# 创建两个按钮，将其放入Frame中
		ttk.Button(f, text='改变', command=self.change).pack(side=LEFT)
		ttk.Button(f, text='获取', command=self.get).pack(side=LEFT)
	def change(self):
		books = ('疯狂Python讲义', '疯狂Kotlin讲义', '疯狂Swift讲义')
		import random
		# 改变self.st变量的值，与之绑定的Entry的内容随之改变
		self.st.set(books[random.randint(0, 2)])
	def get(self):
		from tkinter import messagebox
		# 获取self.st变量的值，实际上就是获取与之绑定的Entry中的内容
		# 并使用消息框显示self.st变量的值
		messagebox.showinfo(title='输入内容', message=self.st.get() )
root = Tk()
root.title("variable测试")
App(root)
root.mainloop()

