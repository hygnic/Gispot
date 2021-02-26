# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/16
# Python2

from tkinter import *
import tkinter.messagebox as messagebox


class A:
	"""
	使用StringVar() 和 textvariable
	对Button进行绑定
	实现Button对数据进行操作
	解决Button传参问题
	StringVar()的数需要使用.get()获取值
	"""
	
	def __init__(self, master):
		self.root = Frame(master)
		self.num1 = StringVar()  # 第一个数字
		self.num2 = StringVar()  # 第一个数字
		self.createpage()
	
	def createpage(self):
		self.root.pack()
		Label(self.root, text='num1').grid(row=0, column=0, stick=W, pady=10)
		# textvariable和StringVar的num1绑定
		Entry(self.root, textvariable=self.num1).grid(row=0, column=1, stick=E)
		Label(self.root, text='num2').grid(row=1, column=0, stick=W, pady=10)
		# textvariable和StringVar的num2绑定
		Entry(self.root, textvariable=self.num2).grid(row=1, column=1, stick=E)
		# Button传递参数
		Button(
			self.root, text='加', command=self.btn_def
		).grid(row=2, column=0, stick=W)
		Button(self.root, text='减').grid(row=2, column=1, stick=E)
		Label(self.root, text='说明').grid(row=3, column=0, stick=W, pady=10)
		Label(self.root, text='只写了加法(请输入简单数字测试button传参)').grid(
			row=3, column=1, stick=E
		)
	
	def btn_def(self):
		# 使用.get()获取值
		num = int(self.num1.get()) + int(self.num2.get())
		messagebox.showinfo('结果', '%d' % num)


if __name__ == '__main__':
	root = Tk()
	root.title('Demo2')
	root.geometry('400x150')
	A(root)
	root.mainloop()