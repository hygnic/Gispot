# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/18



"""
file：window.py.py
create time:2019/6/27 14:54
author:Loong Xu
desc: 窗口
"""
import Tkinter as tk
# from tkinter import filedialog, dialog
import tkFileDialog as filedialog
import Dialog as dialog
import os

window = tk.Tk()
window.title('窗口标题')  # 标题
window.geometry('500x500')  # 窗口尺寸

file_path = ''

file_text = ''

text1 = tk.Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()


def open_file():
	'''
	打开文件
	:return:
	'''
	global file_path
	global file_text
	file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(
		os.path.expanduser('H:/')))
	print('打开文件：', file_path)
	if file_path is not None:
		with open(file_path, mode='r+') as file:
			file_text = file.read()
		text1.insert('insert', file_text)


def save_file():
	global file_path
	global file_text
	file_path = filedialog.asksaveasfilename(title=u'保存文件')
	print('保存文件：', file_path)
	file_text = text1.get('1.0', tk.END)
	if file_path is not None:
		with open(file_path, mode='a+') as file:
			file.write(file_text)
		text1.delete('1.0', tk.END)
		dialog.Dialog(None, {'remove_sth': 'File Modified', 'text': '保存完成',
							 'bitmap': 'warning', 'default': 0,
							 'strings': ('OK', 'Cancle')})
		print('保存完成')


bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
bt1.pack()
bt2 = tk.Button(window, text='保存文件', width=15, height=2, command=save_file)
bt2.pack()

window.mainloop()  # 显
