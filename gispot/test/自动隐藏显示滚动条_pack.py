# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/13
# python2

import Tkinter as tk
import ttk

class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the pack geometry manager.
    def __init__(self, parent, **kwargs):
        tk.Scrollbar.__init__(self, parent, **kwargs)
    
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.pack_forget()
        else:
            if self.cget("orient") == tk.HORIZONTAL: # 将字符串转变为关键字
                self.pack(fill=tk.X)
            else:
                self.pack(fill=tk.Y)
        tk.Scrollbar.set(self, lo, hi)
    def grid(self, **kw):
        raise tk.TclError, "cannot use grid with this widget"
    def place(self, **kw):
        raise tk.TclError, "cannot use place with this widget"

# create scrolled canvas

root = tk.Tk()

hscrollbar = AutoScrollbar(root, orient=tk.HORIZONTAL)
# vscrollbar = AutoScrollbar(root, orient=tk.VERTICAL)

canvas = tk.Canvas(root,
                xscrollcommand=hscrollbar.set)
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
hscrollbar.pack()

hscrollbar.config(command=canvas.xview)

# make the canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# create canvas contents

frame = tk.Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

rows = 5
for i in range(1,rows):
    for j in range(1,10):
        button = tk.Button(frame, padx=7, pady=7, text="[%d,%d]" % (i,j))
        button.grid(row=i, column=j, sticky='news')

canvas.create_window(0, 0, anchor=tk.NW, window=frame)

frame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()