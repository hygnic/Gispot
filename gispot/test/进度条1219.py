# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/19

from Tkinter import *

from ttk import Progressbar

import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=0)

window.mainloop()