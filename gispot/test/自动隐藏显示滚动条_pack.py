# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/13
# python2

from Tkinter import *

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the pack geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.pack_forget()
        else:
            if self.cget("orient") == HORIZONTAL:
                self.pack(fill=X)
            else:
                self.pack(fill=Y)
        Scrollbar.set(self, lo, hi)
    def grid(self, **kw):
        raise TclError, "cannot use grid with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"

# create scrolled canvas

root = Tk()

hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
canvas = Canvas(root,
                xscrollcommand=hscrollbar.set)
canvas.pack(side=TOP, fill=BOTH, expand=True)
hscrollbar.pack()

hscrollbar.config(command=canvas.xview)

# make the canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# create canvas contents

frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

rows = 5
for i in range(1,rows):
    for j in range(1,10):
        button = Button(frame, padx=7, pady=7, text="[%d,%d]" % (i,j))
        button.grid(row=i, column=j, sticky='news')

canvas.create_window(0, 0, anchor=NW, window=frame)

frame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()