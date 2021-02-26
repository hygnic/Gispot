# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/27
"""
测试Tkinter 中的tkFileDialog的作用和用法
"""
import Tkinter as tk
import tkFileDialog

window = tk.Tk()
window.title()
window.geometry("300x200")

def diag():
	file_path = tkFileDialog.asksaveasfilename()
	print file_path

bt = tk.Button(text = "1212",command = diag).pack()

window.mainloop()
