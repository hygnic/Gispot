#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/11 15:13
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
import ttk
root=tk.Tk()
s = ttk.Style()
s.theme_use('classic')
s.configure('zc.TButton',borderwidth='0')
# s.configure('zc.TButton',highlightthickness='10')
s.configure('zc.TButton',highlightthickness='1')
s.configure('zc.TButton',highlightcolor='pink')
# s.map('zc.TButton',background=[('active', 'pressed', 'yellow'),('!active','green'), ('active','!pressed', 'cyan')])
s.map('zc.TButton',background=[('active', 'pressed', 'yellow'),('!active','#FCFDFD'), ('active','!pressed', '#D3D8E2')])
s.map('zc.TButton',relief=[('pressed','sunken'),('!pressed','groove')])
calc_button=ttk.Button(root, text="classic", style='zc.TButton')
calc_button.grid(column=0,row=0,sticky='nsew')
root.mainloop()