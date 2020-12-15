# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/13
# python2

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk


class AutoScrollbar(ttk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the pack geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.pack_forget()
        # else:
        #     if self.cget("orient") == tk.HORIZONTAL: # 将字符串转变为关键字
        #         self.pack(fill=tk.X)
        #     else:
        #         self.pack(fill=tk.X)
        ttk.Scrollbar.set(self, lo, hi)
    def grid(self, **kw):
        raise tk.TclError("cannot use grid with this widget")
    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")

# create scrolled canvas

root = tk.Tk()

hscrollbar = ttk.Scrollbar(root)
vscrollbar = ttk.Scrollbar(root, orient='horizontal')
hscrollbar.pack(side=tk.RIGHT, fill="y")
vscrollbar.pack(side=tk.BOTTOM, fill="x")


test_text = tk.Text(root, wrap=tk.NONE, yscrollcommand=hscrollbar.set,
                    xscrollcommand=vscrollbar.set)
test_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

hscrollbar.config(command=test_text.xview)
vscrollbar.config(command=test_text.yview)


# canvas.create_window(0, 0, anchor=tk.NW, window=frame)

# test_text.update_idletasks()

# test_text.config(scrollregion=test_text.bbox("all"))

poem_name = "Do Not Go Gentle into That Good Night.txt"
with open(poem_name, "r") as f:
    msg = f.readlines()
    for i in msg:
        test_text.insert(tk.END, i)
    
root.mainloop()