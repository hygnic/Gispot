#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/19 22:04
# Reference:
"""
Description: 希望实现非点击状态下的移动滚动条和内容
目前只实现了移动滚动条
Usage:
"""
# ---------------------------------------------------------------------------
try:
    import Tkinter as tk
    import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

import platform
OS = platform.system()




class ScrollWidget(ttk.Frame):

    def __init__(self, master, **kw):
        # frame{
        #   canvas{
        #       frame{create_window{}
        #           }
        #       }
        #   }
        
        ttk.Frame.__init__(self, master, **kw)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # 放置滚动条 垂直方向
        self.yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yscrollbar.pack(side="right", fill="y")
        # 放置滚动条 水平方向
        self.xscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side="bottom", fill="x")
        
        self.canvas = tk.Canvas(self, highlightthickness=0, bg="red")
        # self.canvas.grid(row=0, column=0, sticky=N + E + W + S)   # self.canvas.pack()
        self.canvas.pack(fill="x")
       
        self.canvas.configure(xscrollcommand=self.xscrollbar.set)
        self.xscrollbar['command'] = self.canvas.xview
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar['command'] = self.canvas.yview
        
        self.innerframe = ttk.Frame(self.canvas)
        self.innerframe.pack(anchor="n", fill="x", expand=True)
        # self.innerframe.pack(anchor=N)
        
        self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")
        self.canvas.bind('<Configure>', self.updata_scrollarea) #  '<Configure>' 改变组件大小
        # self.canvas.configure(scrollregion="0 0 %s %s" % (100, 600))
        
        self.on_enter()
        self.on_leave()
    
    @property
    def box(self):
        return self.innerframe
    
    
    def updata_scrollarea(self, event):
        # 更新scrollarea, 如果scrollarea大小不对会导致滚动条显示不出来
        # self.canvas.configure(scrollregion="0 0 %s %s" % (100, 600)) 比如这样
        # 会导致横向的滚动条显示不出来
        width = max(self.innerframe.winfo_reqwidth(), event.width)
        height = max(self.innerframe.winfo_reqheight(), event.height)
        self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
        # self.canvas.itemconfigure("inner_frame", width=width, height=height)
    
    def on_enter(self):
        # 鼠标进入canvas区域时，激活方法self.mouse_move
        # def inner(event):
        #     print "enter"
        #     print event.y
        self.canvas.bind("<Enter>", self.mouse_move)

    def on_leave(self):
        # def inner(event):
        #     print "leave"
        #     print event.delta
        # 鼠标离开canvas区域时，激活方法sself.unbind_mouse
        self.canvas.bind("<Leave>", self.unbind_mouse)

    def mouse_move(self, event):
        # def inner(event):
        #     print "move"
        #     print event.delta # 向上滑是120，向下是-120
        # 滚动鼠标滑轮时，激活方法self.y_move（该方法用于移动界面）
        self.canvas.bind_all("<MouseWheel>", self.y_move)
        # 同时将滚动条和滚动区域界面互相绑定（避免出现滚动区域成功移动但是滚动条不动的状况）
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)

    def unbind_mouse(self, event):
        # 离开滚动区域时，取消绑定，不然鼠标在外面也能滚动界面
        self.canvas.unbind_all("<MouseWheel>")

    def y_move(self, event):
        # 使可滚动界面根据鼠标滑轮滚动
        self.canvas.yview_scroll(-1 * int(event.delta / 120), 'units')

# --- main ---


root = tk.Tk()
root.title("Quiz")
# root.geometry()
upper = tk.Frame(root, height=400)
upper.pack()
bottom = tk.Frame(root, bg="blue")
bottom.pack(side="bottom", fill="x")
tk.Button(bottom, text="test").pack()

window = ScrollWidget(bottom)
window.pack(expand=True, fill='both')
for i in xrange(20):
    tk.Entry(window.box, width=100).pack(fill="x")


root.mainloop()

