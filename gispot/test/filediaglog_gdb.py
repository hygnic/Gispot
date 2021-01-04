#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/4 16:22
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
# import pythonaddins
from arcpy import env

import Tkinter,tkFileDialog
from Tkinter import *
import tkMessageBox
import ttk
from tkFileDialog import askopenfilename
from tkFileDialog import askopenfile


env.workspace = "C:\\temp\\miniPilot\\miniPilot.gdb"

def browseFor_inFC():
    import os
    ws_name = tkFileDialog.askdirectory()
    #print ws_name
    env.workspace = ws_name
    #print env.workspace
    # wsName.set(ws_name)
    feature_classes = []
    #fc = ()
    for dirpath, dirnames, filenames in arcpy.da.Walk(ws_name, datatype="FeatureClass",type="Polyline"):
        for filename in filenames:
            feature_classes.append(os.path.join(dirpath, filename))
            print filename

    print feature_classes
    #print fc
    #fcCombo['values']=fc

def cancel():
    root.destroy()

def remove():
    fields = arcpy.ListFields(inFC)

    for field in fields:
        print field.name
        if field.name <> "OBJECTID" and field.name <> "SHAPE" and field.name <> "SHAPE_Length":

            arcpy.DeleteField_management(inFC, field.name)



root=Tk()
root.title("XXXXXX")

# The first frame named 'mainframe'
mainframe = Frame(root, relief='flat', borderwidth=6)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# set up Tkinter variables, which are global variables, for the first gui -- the root window
inFC = StringVar()

# widgets on the mainframe
Label(mainframe, text="Specify the feature class: ").grid(column=1, row=1, sticky=E)
inFC_entry = Entry(mainframe, width=36, textvariable=inFC)
inFC_entry.grid(column=2, row=1, sticky=(W, E))
inFC_browser_Button=Button(mainframe, text="...", height=1, width=3, command=browseFor_inFC).grid(column=3, row=1, sticky=W)

# two button widgets
refract_Button=Button(mainframe, text="OK", command=remove).grid(column=0, row=2, sticky=E)
cancel_Button=Button(mainframe, text="CANCEL", command=cancel).grid(column=4, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()   # create an event loop