#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/12 20:54
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from Tkinter import *
import ttk


class Notebook:
	def __init__(self):
		self.root = Tk()
		self.root.title('Note Book')
		self.build_Menu()
		self.build_NoteBook()
		self.build_page_1()
		self.root.mainloop()
	
	def build_Menu(self):
		# MENU WIDGET CONFIGURATION
		self.menu = Menu(self.root)
		self.root.configure(menu=self.menu)
		self.filemenu = [None] * 3
		for f in xrange(1, 3):
			self.filemenu[f] = Menu(self.menu, tearoff=False)
		# FILE MENU
		self.menu.add_cascade(label='File', menu=self.filemenu[1])
		for i in ['New', 'Open', 'Save', 'Print', 'Exit']:
			if i == 'New':
				self.filemenu[1].add_command(label=i, command=self.Add_New_Tab)
			elif i == 'Print':
				self.filemenu[1].add_command(label=i)
				self.filemenu[1].add_separator('')
			elif i == 'Exit':
				self.filemenu[1].add_command(label=i, command=quit)
			else:
				self.filemenu[1].add_command(label=i)
		# EDIT MENU
		self.menu.add_cascade(label='Edit', menu=self.filemenu[2])
		for i, k, l in [('Copy', 'Ctrl+C', ''), ('Cut', 'Ctrl+X', 's'),
						('Paste', 'Ctrl+P', ''), ('Select All', 'Ctrl+A', 's'),
						('Delete', 'Delete', '')]:
			if i == 'Delete':
				self.filemenu[2].add_command(label=('{} {}:>20'.format(i,k)),
											 command=lambda: self.canvas.delete(
												 ALL))
			elif l == 's':
				self.filemenu[2].add_command(label=('{} {}:>20'.format(i,k)))
				self.filemenu[2].add_separator('')
			else:
				self.filemenu[2].add_command(label=('{} {}:>20'.format(i,k)))
	
	# ADD NEW TAG CODE
	def Add_New_Tab(self):
		for k in range(2, 3):
			self.notebook.add(self.tab[k], text='Page {}'.format(k))
	
	def build_NoteBook(self):
		# NOTEBOOK WIDGET CONFIGURATION
		self.notebook = ttk.Notebook(self.root, height=400, width=800)
		self.tab = [None] * 10
		global t
		for t in range(1, 10):
			self.tab[t] = ttk.Frame(self.notebook)
		
		self.notebook.add(self.tab[1], text='Page 1', underline=0)
		# self.notebook.add(self.tab[2], text='Page 2')
		# self.notebook.add(self.tab[3], text='Page 3')
		# self.notebook.add(self.tab[4], text='Page 4')
		self.notebook.pack(fill=BOTH, expand=YES, padx=5, pady=5)
	
	# PAGE ONE CONTENTS
	def build_page_1(self):
		self.canvas = Canvas(self.tab[1], width=100, height=50, bg='#ffffff',
							 cursor='heart')
		self.canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)
		self.canvas.bind('<B1-Motion>', self.bind_paint)
		ttk.Button(self.tab[1], text='clean',
				   command=lambda: self.canvas.delete(ALL)).pack(side=LEFT,
																 anchor=CENTER,
																 padx=90,
																 pady=5, fill=X,
																 expand=1)
		ttk.Button(self.tab[1], text='close', command=quit).pack(side=LEFT,
																 padx=90,
																 fill=X,
																 anchor=CENTER,
																 expand=1)
	
	# BINDING MOTION THAT SKETCHED THE CIRCLES RED COLORS
	def bind_paint(self, event):
		x1, y1 = (event.x - 5), (event.y - 5)
		x2, y2 = (event.x + 5), (event.y + 5)
		i = self.canvas.create_oval(x1, y1, x2, y2, fill='#ff0000',
									outline='#000000')
		return i


if __name__ == '__main__':
	Notebook()