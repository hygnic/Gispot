#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/13 12:51
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
import ttk


class ToolSet(object):
	"""
	用于显示工具箱button中的内容
	点击工具箱启动该类
	"""
	
	def __init__(self):
		self.master = tk.Tk()
		self.padding2 = 3  # 水平 tab 栏
		self.notebook_type2() # 自定义notebook tab
	
	
	def notebook_type2(self):
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9'  # X11 color: 'gray85'
		_ana1color = '#d9d9d9'  # X11 color: 'gray85'
		_ana2color = '#ececec'  # Closest X11 color: 'gray92'
		global _images
		_images = (
			
			tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
						 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
						 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
						 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
						 KkoNUtRHpYYAADs= '''),
			
			tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
						 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
						 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
						 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
						 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),
			
			tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
						 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
						 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
						 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
						 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
		)
		
		self.style = ttk.Style()
		self.style.element_create("close", "image", "img_close",
								  ("active", "pressed", "!disabled",
								   "img_closepressed"),
								  ("active", "alternate", "!disabled",
								   "img_closeactive"), border=8, sticky='')
		
		self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
												{"sticky": "nswe"})])
		self.style.layout("ClosetabNotebook.Tab", [
			("ClosetabNotebook.tab",
			 {"sticky": "nswe",
			  "children": [
				  ("ClosetabNotebook.padding", {
					  "side": "top",
					  "sticky": "nswe",
					  "children": [
						  ("ClosetabNotebook.focus", {
							  "side": "top",
							  "sticky": "nswe",
							  "children": [
								  ("ClosetabNotebook.label", {"side":
																  "left",
															  "sticky": ''}),
								  ("ClosetabNotebook.close", {"side":
																  "left",
															  "sticky": ''}), ]})]})]})])
		
		PNOTEBOOK = "ClosetabNotebook"
		
		self.style.configure('TNotebook.Tab', background=_bgcolor)
		self.style.configure('TNotebook.Tab', foreground=_fgcolor)
		self.style.map('TNotebook.Tab', background=
		[('selected', _compcolor), ('active', _ana2color)])
		
		self.PNotebook1 = ttk.Notebook(self.master)
		# 设置竖直的tab
		# self.PNotebook1 = ttk.Notebook(self.master, style='lefttab.TNotebook')
		# self.style.configure('lefttab.TNotebook', tabposition='wn')
		
		self.PNotebook1.place(relx=0, rely=0, relheight=1
							  , relwidth=1)
		# self.PNotebook1.configure(takefocus="")
		self.PNotebook1.configure(style=PNOTEBOOK)
		self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
		self.PNotebook1.add(self.PNotebook1_t1, padding=2)
		self.PNotebook1.tab(0, text="Page 1", compound="left")
		# self.PNotebook1_t1.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t2 = tk.Frame(self.PNotebook1)
		self.PNotebook1.add(self.PNotebook1_t2, padding=2)
		self.PNotebook1.tab(1, text="Page 2", compound="left")
		# self.PNotebook1_t2.configure(highlightbackground="#d9d9d9")
		self.PNotebook1.bind('<Button-1>', _button_press)
		self.PNotebook1.bind('<ButtonRelease-1>', _button_release)
		self.PNotebook1.bind('<Motion>', _mouse_over)
	

	


# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
	widget = event.widget
	element = widget.identify(event.x, event.y)
	if "close" in element:
		index = widget.index("@%d,%d" % (event.x, event.y))
		widget.state(['pressed'])
		widget._active = index


def _button_release(event):
	widget = event.widget
	if not widget.instate(['pressed']):
		return
	element = widget.identify(event.x, event.y)
	try:
		index = widget.index("@%d,%d" % (event.x, event.y))
	except TclError:
		pass
	if "close" in element and widget._active == index:
		widget.forget(index)
		widget.event_generate("<<NotebookTabClosed>>")
	
	widget.state(['!pressed'])
	widget._active = None


def _mouse_over(event):
	widget = event.widget
	element = widget.identify(event.x, event.y)
	if "close" in element:
		widget.state(['alternate'])
	else:
		widget.state(['!alternate'])
		
if __name__ == '__main__':
	ToolSet().master.mainloop()