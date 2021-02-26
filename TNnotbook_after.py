#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 05, 2020 11:28:05 PM CST  platform: Windows NT

from ttkthemes import ThemedTk
from PIL import ImageTk,Image
import ttk
import Tkinter as tk

class Toplevel1(object):
	def __init__(self):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		self.root = ThemedTk(theme="arc")
		self.style = ttk.Style()
		# self.root = tk.Tk()
		self.root.geometry("1200x661+284+114")
		# self.root.minsize(120, 1)
		# self.root.maxsize(1924, 1061)
		self.root.resizable(1, 1)
		self.root.title("New Toplevel")
		
		self.img = Image.open(r"G:\MoveOn\Gispot\GUIs\Icons\folder1.png")
		self.image_1 = ImageTk.PhotoImage(self.img)
		
		# top.configure(background="#d9d9d9")
		#
		# self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		# top.configure(menu = self.menubar)
		
		# self.style.configure('TNotebook.Tab', background=_bgcolor)
		# self.style.configure('TNotebook.Tab', foreground=_fgcolor)
		# self.style.map('TNotebook.Tab', background=
		#     [('selected', _compcolor), ('active',_ana2color)])
		self.TNotebook1 = ttk.Notebook(self.root)
		self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0,
							  relwidth=1.0)
		self.TNotebook1.configure(takefocus="")
		self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
		
		
		self.TNotebook1.add(self.TNotebook1_t1, padding=3)
		self.TNotebook1.tab(0, text="Page 1", compound="left",
							image = self.image_1)
		self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
		self.TNotebook1.add(self.TNotebook1_t2, padding=3)
		self.TNotebook1.tab(1, text="Page 2", compound="left",
							underline="-1", )
		self.f = tk.Frame(self.TNotebook1_t1, width=20, height=100
						 )
		self.f.place(x=0, y=0)
		self.set_button()
		
		# self.f2 = tk.Frame(self.TNotebook1_t1, width=20, height=100, bg="blue")
		# self.f2.place(x=0, y=600,anchor="nw")
		# self.set_label()
	
	def set_button(self):
		button = ttk.Button(self.TNotebook1_t1,text = "bt",command = self.set_button_command)
		# lambda 形式也可以
		# button = ttk.Button(self.TNotebook1_t1,text = "bt",command = lambda:(self.root.after(2000, self.add_label)))
		button.pack()
	
	def add_label(self):
		lb = ttk.Button(self.f, text=1)
		lb.pack()
		# 加入该行可以循环添加
		self.set_button_command()
			
	def set_button_command(self):
			self.root.after(100, self.add_label)
			
	


w = None

def destroy_Toplevel1():
	global w
	w.destroy()
	w = None



if __name__ == '__main__':
	app = Toplevel1()
	app.root.mainloop()





