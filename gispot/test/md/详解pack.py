#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/10 16:36
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk

# py2.7 tk8.5
if __name__ == '__main__':
    
    class ScrollWidge(object):
        def __init__(self):
            self.master = tk.Tk()
            self.frame = tk.Frame(self.master)
            # self.frame.pack(expand=True, fill="both") # 示例1.2
            self.frame.pack() # 示例1.1
            
            self.canvas = tk.Canvas(self.frame,bg="blue")
            self.canvas.pack(expand=True, fill="both")
            
    
    ScrollWidge().master.mainloop()
