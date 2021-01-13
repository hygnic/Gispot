#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/19 22:04
# Reference:
"""
Description: 实现在非点击状态下的移动滚动条和内容；实现自动隐藏滚动条

Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import print_function
from ttkthemes import ThemedTk

import platform
try:
    import Tkinter as tk
    import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk



OS = platform.system()

def print_widt(widget22):
    print("{} {} {} {}".format(
        widget22.winfo_reqwidth(), widget22.winfo_reqheight(), widget22.winfo_width(), widget22.winfo_height()))



class ResizingCanvas(tk.Canvas):
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
    
    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)




class AutoScrollbar(ttk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        # print("lo:",lo)
        # print("hi:",hi)
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
        
    def pack(self, **kw):
        raise tk.TclError, "cannot use pack with this widget"

    def place(self, **kw):
        raise tk.TclError, "cannot use place with this widget"



class ScrollWidget(tk.Frame):

    def __init__(self, master, **kw):
        # frame{
        #   canvas{
        #       frame{create_window{}
        #           }
        #       }
        #   }
        
        tk.Frame.__init__(self, master, **kw)
        # # 放置滚动条 垂直方向
        self.yscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.yscrollbar.pack(side="right", fill="y")
        # # 放置滚动条 水平方向
        self.xscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side="bottom", fill="x")
        
        self.canvas = tk.Canvas(self, highlightthickness=0,) #  bg="red"
        # self.canvas.grid(row=0, column=0, sticky=tk.N + tk.E + tk.W + tk.S)   # self.canvas.pack()
        self.canvas.pack(fill="x")

        # self.make_scroll(tk.Scrollbar)
       
        self.canvas.configure(xscrollcommand=self.xscrollbar.set)
        self.xscrollbar['command'] = self.canvas.xview
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar['command'] = self.canvas.yview
        
        self.innerframe = tk.Frame(self.canvas) #  bg="red", relief="sunken", bd=10
        self.innerframe.pack(anchor="n", fill="x", expand=True)
        # self.innerframe.pack(anchor=N)
        
        self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")
        # self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")
        
        self.canvas.bind('<Configure>', self.updata_scrollarea) #  '<Configure>' 改变组件大小
        # self.canvas.configure(scrollregion="0 0 %s %s" % (378, 265))
        # self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.on_enter()
        self.on_leave()
        

    def make_scroll(self, scrollclass):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.yscrollbar = scrollclass(self, orient=tk.VERTICAL)
        self.yscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
    
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar['command'] = self.canvas.yview
    
        self.xscrollbar = scrollclass(self, orient=tk.HORIZONTAL)
        self.xscrollbar.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.canvas.configure(xscrollcommand=self.xscrollbar.set)
        self.xscrollbar['command'] = self.canvas.xview
    
    
    @property
    def box(self):
        return self.innerframe
    
    def updata_scrollarea(self, event):
        # 更新scrollarea, 如果scrollarea大小不对会导致滚动条显示不出来
        # self.canvas.configure(scrollregion="0 0 %s %s" % (100, 600)) 比如这样
        # 会导致横向的滚动条显示不出来
        width = max(self.innerframe.winfo_reqwidth(), event.width)
        height = max(self.innerframe.winfo_reqheight(), event.height)
        # self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # canvas.create_window会创建一个"inner_frame"的窗口
        self.canvas.itemconfigure("inner_frame", width=width, height=height)
    
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
        # 适配多种操作系统
        if platform.system() == 'Windows':
            self.canvas.yview_scroll(-1 * int(event.delta / 120), 'units')
        elif platform.system() == 'Darwin':
            self.canvas.yview_scroll(-1 * int(event.delta), 'units')
        else:
            if event.num == 4:
                self.canvas.yview_scroll(-1, 'units')
            elif event.num == 5:
                self.canvas.yview_scroll(1, 'units')



if __name__ == '__main__':
    root = ThemedTk(theme="arc")
    # root = tk.Tk()
    root.title("adv scrollbar")
    # root.geometry()
    # upper = tk.Frame(root, height=400)
    # upper.pack()
    # bottom = tk.Frame(root, bg="blue")
    # bottom.pack(side="bottom", fill="x")
    # tk.Button(bottom, text="test").pack()
    
    window = ScrollWidget(root)
    window.pack(expand=True, fill='both')
    window.update_idletasks()
    text = tk.Text(window.box) # width=600, height=800
    text.pack(expand=1, fill="both") # expand=1, fill="both"
    with open("Do Not Go Gentle into That Good Night.txt", "r") as f:
        for i in f.readlines():
            text.insert("end",i)
    
    
    root.mainloop()
