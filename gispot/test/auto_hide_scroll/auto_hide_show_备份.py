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
import Tkinter as tk
import platform

class AutoScrollbar(tk.Scrollbar):
    """Create a scrollbar that hides iteself if it's not needed. Only
    works if you use the pack geometry manager from tkinter.
    """
    def __init__(self, master):
        tk.Scrollbar.__init__(self, master)
    
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.pack_forget()
        else:
            if self.cget("orient") == tk.HORIZONTAL:
                self.pack(fill=tk.X, side=tk.BOTTOM)
            else:
                self.pack(fill=tk.Y, side=tk.RIGHT)
        tk.Scrollbar.set(self, lo, hi)
    def grid(self, **kw):
        raise tk.TclError("cannot use grid with this widget")
    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")

#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________________________________________________________________

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

class ActiveFrame(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master)
    
        self.bind("<Enter>", self.on_enter2)
        # self.bind("<Enter>", lambda e: self.on_enter(e, ))
        # self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event, widget):
        child = widget.winfo_children()[1]
        print "child", widget.winfo_children()
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
            # child.bind_all('<Shift-MouseWheel>',
            #                lambda e: _on_shiftmouse(e, child))

    def on_enter2(self, event):
        self.bind("<MouseWheel>", self.yview_scroll(-1*int(event.delta/120),'units'))

    # def on_leave(self, event, widget):/
    #     print "leaveing"
    
#Creating the root, canvas, and autoscrollbar
root = tk.Tk()
fff = ActiveFrame(root)
fff.pack(expand=True, side="right", fill="y")
vscrollbar = AutoScrollbar(fff)
canvas = tk.Canvas(fff, yscrollcommand=vscrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
vscrollbar.config(command=canvas.yview)

#Creating the frame its contents
frame = tk.Frame(canvas)
label = tk.Label(frame, text="text", font=("Arial", "512"))
label.pack()

#Stuff that I don't quite understand
canvas.create_window(0, 0, anchor=tk.NW, window=frame)
frame.update_idletasks()

# A tuple (w, n, e, s) that defines over how large an area the canvas can be scrolled,
# where w is the left side, n the top, e the right side, and s the bottom.
canvas.config(scrollregion=canvas.bbox("all"))
# canvas.config(scrollregion=(10, 10, 10, 10))

root.mainloop()