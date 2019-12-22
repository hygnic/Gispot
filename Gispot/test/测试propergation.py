# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/20

import Tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=400)
# Does not work at the moment, textBox is missing
# frame.pack_propagate(0)
frame.pack()

textBox = tk.Label(frame, text="(x,y): ")
textBox.pack()

root.mainloop()

