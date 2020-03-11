# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

# !/usr/bin/python3.5
# -*- coding: UTF-8 -*-

import  Tkinter  # 导入 Tkinter 库
import tkMessageBox  # 导入消息框库
import os  # 导入OS库
import subprocess


def show_something():
	tkMessageBox.showinfo("Python", "Hello everyone")


def show_while():
	if button3['text'] == 'WHILE_run':
		button3['text'] = 'WHILE_close'
	else:
		button3['text'] = 'WHILE_run'
	data = subprocess.Popen('./a.out', stdout=subprocess.PIPE,
							stdin=subprocess.PIPE, shell=True)
	while True:
		'''
		与子进程通信，给它输入
		data.stdin.write(("abcdf\n").encode())
	 data.stdin.flush()
		'''
		t1.config(state='normal')  # 设置为可编辑
	# t1.delete('1.0','end') #清空文本框
		t1.insert('end', data.stdout.readline())
		t1.see('end')  # 设置显示最末尾的数据
		t1.update()
		t1.config(state='disabled')  # 设置为无法编辑


def show_ls():
	t2.config(state='normal')  # 设置为可编辑
	t2.delete('1.0', 'end')  # 清空文本框
	t2.insert('end', os.popen('ls').read())
	t2.config(state='disabled')  # 设置为无法编辑


# ---创建窗口对象---
root_window = Tkinter.Tk()
root_window.title('TEST BY FC')
root_window.geometry('500x500')

# ---创建容器---
main_frame = Tkinter.Frame(root_window)
main_frame.pack()

# ---创建列表---
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# ---创建两个列表组件---
listb = Tkinter.Listbox(root_window)
# ---给小部件插入数据---
for __getall_items in li:
	listb.insert(0, __getall_items)
listb.pack()

# ---创建子容器，在子容器上创建Label---
frm1 = Tkinter.Frame(main_frame)
frm1.pack()
Tkinter.Label(frm1, text='hello', bg='green', width=10, height=2).pack(
	side='left')
frm2 = Tkinter.Frame(main_frame)
frm2.pack()
Tkinter.Label(frm1, text=' world', bg='yellow', width=10, height=2).pack(
	side='right')

# 创建按钮
button_frm = Tkinter.Frame(root_window)
button_frm.pack()
button1 = Tkinter.Button(button_frm, text="确定", bg='red', fg='white', width=10,
						 height=2, command=show_something)
button1.pack()
button2 = Tkinter.Button(button_frm, text="LS", bg='blue', fg='white', width=10,
						 height=2, command=show_ls)
button2.pack()
button3 = Tkinter.Button(button_frm, text="WHILE_run", bg='green', fg='white',
						 width=10, height=2, command=show_while)
button3.pack()

# 创建滚动条
s1 = Tkinter.Scrollbar()
s1.pack(side='right', fill='y')  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充

# 创建文本显示框
t1 = Tkinter.Text(bg='lightgreen', width=30, height=10, state='disabled',
				  yscrollcommand=s1.set)  # 设置为无法编辑
t1.pack()
s1.config(command=t1.yview)
t2 = Tkinter.Text(bg='lightblue', width=10, height=2,
				  state='disabled')  # 设置为无法编辑
t2.pack()

# t2.config(yscrollcommand=s1.set)

# ---进入消息循环---
root_window.mainloop()