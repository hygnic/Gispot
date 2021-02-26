#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/6 22:06
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk



import ttk
import Tkinter

root = Tkinter.Tk()
# root = ThemedTk(theme="breeze")

style = ttk.Style()
# style.theme_settings("default", {
#    "TCombobox": {
#        "configure": {"padding": 5},
#        "map": {
#            "background": [("active", "green2"),
#                           ("!disabled", "green4")],
#            "fieldbackground": [("!disabled", "green3")],
#            "foreground": [("focus", "OliveDrab1"),
#                           ("!disabled", "OliveDrab2")]
#        }
#    }
# })
ttk.Radiobutton().pack()
ttk.Checkbutton().pack()
combo = ttk.Combobox()
combo.pack()

root.mainloop()
#***************************
# import Tkinter
# import ttk
#
# root = Tkinter.Tk()
#
# style = ttk.Style()
# style.map("C.TButton",
#     foreground=[('pressed', 'red'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )
#
# colored_btn = ttk.Button(text="Test", style="C.TButton").pack()
#
# root.mainloop()
# *************************

# import ttk
# import Tkinter
#
# root = Tkinter.Tk()
#
# style = ttk.Style()
# style.layout("TMenubutton", [
#    ("Menubutton.background", None),
#    ("Menubutton.button", {"children":
#        [("Menubutton.focus", {"children":
#            [("Menubutton.padding", {"children":
#                [("Menubutton.label", {"side": "left", "expand": 1})]
#            })]
#        })]
#    }),
# ])
#
# mbtn = ttk.Menubutton(text='Text')
# mbtn.pack()
# root.mainloop()