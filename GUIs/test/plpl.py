# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/7

import tkinter
import tkinter.messagebox
import random
from PIL import Image, ImageTk # <---

root = tkinter.Tk()
color = 'white'

item = tkinter.Button(root,
                text=color,
                width=20,
                height=10,
                relief='raised',
                borderwidth=5,
                bg=color
            )

original = Image.open(r"66.png")
ph_im = ImageTk.PhotoImage(original) # <----------
item.config(image=ph_im)
item.pack(side='left')
root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
#
#
# root = tk.Tk()
# image = Image.open("66.png")
# photo = ImageTk.PhotoImage(image)
# label = tk.Label(root, image=photo)
# label.image = photo
# label.grid(row=2, column=0)
# #Start the program
# root.mainloop()