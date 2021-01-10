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
import ttk
import Tkinter as tk










# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
#
# """____________________________________________________________________________"""
# """____________________________________________________________________________"""
# on_enter(frame)
# on_leave(frame)
#
# """____________________________________________________________________________"""
# """____________________________________________________________________________"""
#
# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill="y")
# txt = tk.Text(frame, yscrollcommand= scrollbar.set)
# txt.insert("end", "this is tkinter\n"*50)
# mouse_move(txt)
# txt.pack()
# scrollbar.configure(command=txt.yview)

# root.mainloop()


if __name__ == '__main__':
    
    class ScrollWidge(object):
        
        
        def __init__(self):
            self.master = tk.Tk()
            self.frame = ttk.Frame(self.master)
            self.frame.pack()
            self.flag_focus_on_srollarea = 0
            # 创建滚动条
            scrollbar = tk.Scrollbar(self.frame)
            scrollbar.pack(side=tk.RIGHT, fill="y")

            self.canvas = tk.Canvas(self.frame, highlightthickness=0, bg="blue")
            self.canvas.pack(expand=True, fill="both")

            scrollbar.configure(command=self.canvas.yview)
            # mouse_move(self.canvas, scrollbar)

            self.on_enter(self.canvas, scrollbar)
            self.on_leave(self.canvas)
            # self.mouse_move(self.canvas, scrollbar)
            
            self.innerframe = ttk.Frame(self.canvas,)
            self.innerframe.pack(expand=True, fill="both")
            print self.innerframe.info()

            self.canvas.create_window(20, 20, window=self.innerframe, tags="inner_frame", height=600, width=600)
            
            self.canvas.configure(
                scrollregion="0 0 %s %s" % (400, 600))
            self.canvas.itemconfigure("inner_frame", width=600, height=600)


            for i in xrange(40):
                self.entry = tk.Button(self.innerframe, text=i)
                self.entry.pack(expand=False, fill="both")

        def on_enter(self, widget, bar):
            def inner(event):
                print "enter"
                print event.y

            self.flag_focus_on_srollarea=1
            widget.bind("<Enter>", lambda e:self.mouse_move(self.canvas, bar))

        def on_leave(self,widget):
            def inner(event):
                print "leave"
                print event.delta

            self.flag_focus_on_srollarea = 0
            widget.bind("<Leave>", lambda e:self.unbind_mouse(self.canvas))
            # widget.unbind_all("<MouseWheel>", lambda e:self.unbind_mouse(self.canvas))

        def mouse_move(self, widget, bar):
            # def inner(event):
            #     print "move"
            #     print event.delta # 向上滑是120，向下是-120
            # if self.flag_focus_on_srollarea:
            widget.bind_all("<MouseWheel>", lambda e: self.y_move(widget, e))
            widget.configure(yscrollcommand=bar.set)
            
        def unbind_mouse(self, widget):
            widget.unbind_all("<MouseWheel>")

        def y_move(self, widget, event):
            widget.yview_scroll(-1 * int(event.delta / 120), 'units')
                    
    
    
    
    ScrollWidge().master.mainloop()
