#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/21 14:51
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy,time
import Tkinter as tk


def click(key):
	# print the key that was pressed
	print key.char


def main():
	a = time.time()
	mxd_path = ur"G:\高标准分布图\510604罗江县_没有出图\罗江.mxd"
	mxd1 = arcpy.mapping.MapDocument(mxd_path)
	
	lys = arcpy.mapping.ListLayers(mxd1)
	b = time.time()
	print b - a

mainwin = tk.Tk()
entryy = tk.Entry(mainwin,invalidcommand = "all")
entryy.pack()
entryy.bind("<Key>", click)

mainwin.mainloop()
