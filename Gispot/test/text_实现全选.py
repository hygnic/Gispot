# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/19

from Tkinter import *

# Select all the text in textbox (not working)
def select_all(event):
    textbox.tag_add(SEL, "1.0", END)
    textbox.mark_set(INSERT, "1.0")
    textbox.see(INSERT)

# Open a window
mainwin = Tk()

# Create a text widget
textbox = Text(mainwin, width=40, height=10)
textbox.pack()

# Add some text
textbox.insert(INSERT, "Select some text then right click in this window")

# Add the binding
textbox.bind("<Control-Key-a>", select_all)

# Start the program
mainwin.mainloop()