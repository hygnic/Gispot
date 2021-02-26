#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/13 1:14
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from Tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
    
    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    
    # add some widgets to the canvas
    mycanvas.create_line(0, 0, 200, 100)
    mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")
    
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

def main2():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    innerframe = Frame(mycanvas)
    innerframe.pack(fill=BOTH, expand=YES)
    
    # add some widgets to the canvas
    mycanvas.create_window(0, 0, window=innerframe, anchor='nw', tags="inner_frame")
    # mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    # mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")
    text = Text(innerframe) # width=600, height=800
    text.pack(expand=1, fill="both") # expand=1, fill="both"
    with open("Do Not Go Gentle into That Good Night.txt", "r") as f:
        for i in f.readlines():
            text.insert("end",i)
    
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()