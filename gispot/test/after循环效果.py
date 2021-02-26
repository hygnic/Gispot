#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/6 19:23
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import time
import Tkinter as tk

def __writeText():
    text.insert(tk.END, str(time.time())+'\n')
    root.after(1000, __writeText)  # again forever

root = tk.Tk()
text = tk.Text(root)
text.pack()
root.after(1000, __writeText)
root.mainloop()