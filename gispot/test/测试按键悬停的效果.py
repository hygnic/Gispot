# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/12
# python2

import Tkinter as tk

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

root = tk.Tk()

classButton = HoverButton(root,text="Classy Button", activebackground='green')
classButton.grid()

root.mainloop()
