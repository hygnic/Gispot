#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/13 21:38
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk


class ScrollCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
    
    def create_window(self, child):
        tk.Canvas.create_window(self,(0, 0), window=child, anchor='nw')
        child.bind("<Configure>", self.on_configure)
    
    def on_configure(self, event):
        w = event.widget
        bbox = x, y, width, height = 0, 0, w.winfo_width(), w.winfo_height()
        self.configure(scrollregion=bbox, width=width)
  
if __name__ == '__main__':
    root = tk.Tk()
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")
    sc = ScrollCanvas(root, yscrollcommand=scrollbar.set)
    sc.pack(expand=1, fill="both")
    txt = tk.Text(sc)
    txt.pack()
    sc.create_window(txt)
    
    scrollbar['command'] =sc.yview
    
    root.mainloop()