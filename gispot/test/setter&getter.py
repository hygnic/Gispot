#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/13 22:06
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
import ttk

class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.

        methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        # print methods
        """
        ['bubbletip', 'forget', '__module__', 'configure', 'pack_configure',
        'pack_slaves', 'pack_forget', 'pack_propagate', 'propagate', 'slaves',
        'pack_info', 'config', '__doc__', 'pack', '__module__', 'forget',
        'grid_propagate', 'grid_columnconfigure', 'grid_slaves', 'grid_bbox',
        'size', 'location', 'config', '__doc__', 'configure', 'grid_info',
        'columnconfigure', 'grid_remove', 'grid_configure', 'grid', 'bbox',
        'grid_rowconfigure', 'bubbletip', 'grid_size', 'grid_forget', 'slaves',
        'grid_location', 'propagate', 'rowconfigure', 'bubbletip', '__module__',
        'configure', 'place_forget', 'place_configure', 'place_info', 'place',
        'slaves', 'place_slaves', 'config', '__doc__', 'forget']
             """
        for meth in methods:
            # print meth
            if meth[0] != '_' and meth not in ('config', 'configure'):
                print meth
                setattr(self, meth, getattr(master, meth))
                
if __name__ == '__main__':
    root = tk.Tk()
    txt = tk.Text(root)
    txt.pack()
    txt.insert("end","3")
    print txt.info()
    sd = AutoScroll(txt)
    print sd.info()
    
    root.mainloop()