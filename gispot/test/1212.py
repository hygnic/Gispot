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


class AutoScrollbar(tk.Scrollbar):
    """Create a scrollbar that hides iteself if it's not needed. Only
    works if you use the pack geometry manager from tkinter.
    """
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


#Creating the root, canvas, and autoscrollbar
root = tk.Tk()
vscrollbar = AutoScrollbar(root)
canvas = tk.Canvas(root, yscrollcommand=vscrollbar.set)
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