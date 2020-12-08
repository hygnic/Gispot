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
from Tkinter import *
import ttk

root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame_main = Frame()
frame_profile = Frame()

prof_img = PhotoImage(file=r'G:\MoveOn\Gispot\GUIs\Icons\file3.gif')

notebook.add(frame_main, text='Main')
notebook.add(frame_profile, text='Profile', image=prof_img, compound=TOP)

root.mainloop()