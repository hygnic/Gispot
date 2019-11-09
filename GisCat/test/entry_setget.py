# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/7
import Tkinter as tk
import tkFileDialog
class EntryTest(object):
    def __init__(self):
        master = tk.Tk()
        input_msg1 = tk.StringVar()
        input_msg1.set(u"初始值")
        e = tk.Entry(master,textvariable=input_msg1)
        e.pack()
        e.focus_set()
        
        def open_file():
            dirname = tkFileDialog.askdirectory()
            input_msg1.set(dirname)
            
        b = tk.Button(master, text="get dir", width=10, command=open_file)
        b.pack()
        new_txt = "er"
        def comf():
            
            global new_txt
            new_txt = input_msg1.get()
            print new_txt
            print type(new_txt)
            
        b = tk.Button(master, text="confirm", width=10, command=comf)
        b.pack()
        print "input_msg1: ",input_msg1,"  type: ",type(input_msg1)
        
        master.mainloop()

if __name__ == '__main__':
    EntryTest()