#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/6 20:03
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk # global imports are bad
import ttk
from PIL import Image, ImageTk

root = tk.Tk()
nb = ttk.Notebook(root)
nb.pack(fill='both', expand=True)

f = tk.Frame(nb)
tk.Label(f, text="in frame").pack()

# must keep a global reference to these two
im = Image.open(r'G:\MoveOn\Gispot\GUIs\Icons\folder1.png')
ph = ImageTk.PhotoImage(im)

# note use of the PhotoImage rather than the Image
nb.add(f, text="profile", image=ph, compound=tk.LEFT) # use the tk constants

root.mainloop()