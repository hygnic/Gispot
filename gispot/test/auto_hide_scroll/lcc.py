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
            self.frame = ttk.Frame(self.master, width=300, height = 500)
            self.frame.pack()
            
            # 创建滚动条
            self.scrollbar = tk.Scrollbar(self.frame)
            self.scrollbar.pack(side=tk.RIGHT, fill="y")

            self.canvas = tk.Canvas(self.frame, highlightthickness=0, bg="blue", width=300, height = 500)
            self.canvas.pack(expand=False, fill="both")

            self.scrollbar.configure(command=self.canvas.yview)

            self.innerframe = ttk.Frame(self.canvas,)
            self.innerframe.pack(expand=True, fill="both")
            self.canvas.create_window(5, 5, window=self.innerframe, tags="inner_frame")
            
            self.canvas.configure(
                scrollregion="0 0 %s %s" % (0, 800))
            # self.canvas.itemconfigure("inner_frame", width=600, height=600)
            
            print self.canvas.winfo_width()
            print self.canvas.winfo_height()
            print self.canvas.winfo_reqwidth()
            print self.canvas.winfo_reqheight()
            self.canvas.update_idletasks()
            """________________________mouse binding_________________________"""
            self.on_enter()
            self.on_leave()
            """________________________mouse binding_________________________"""
            for i in xrange(40):
                self.entry = tk.Button(self.innerframe, text=i)
                self.entry.pack(expand=False, fill="both")

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
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            
        def unbind_mouse(self, event):
            # 离开滚动区域时，取消绑定，不然鼠标在外面也能滚动界面
            self.canvas.unbind_all("<MouseWheel>")

        def y_move(self, event):
            # 使可滚动界面根据鼠标滑轮滚动
            self.canvas.yview_scroll(-1 * int(event.delta / 120), 'units')
                    
    
    
    
    ScrollWidge().master.mainloop()
