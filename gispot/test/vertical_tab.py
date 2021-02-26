#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/10 13:46
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
import ttk
from ttkthemes import ThemedTk

# root = tk.Tk()
root = ThemedTk(theme="arc")

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=200, height=200)
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)

notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')

notebook.grid(row=0, column=0, sticky="nw")

root.mainloop()