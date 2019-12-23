# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/28
"""
功能：
一：
	完善主窗口（tool_entrance）的功能：
		窗口居中
		清除父部件中的子部件
二:
	定义新类 HoverButton,NeewwEntry,NeewwText
"""

import Tkinter as tk

def screen_cetre(master, width=None, height=None):
	# 窗口居中
	screenwidth = master.winfo_screenwidth()
	screenheight = master.winfo_screenheight()
	if width is None:
		width, height = 800,660
	geometry_size = "{}x{}+{}+{}".format(width, height,
										 (screenwidth - width) / 2,
										 (screenheight - height) / 2)
	master.geometry(geometry_size)
	# geometry = '%dx%d+%d+%d' % (
	# width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	
def destroy_chird(master):
	"""
	监测一个部件内部是否有子部件，如果有，
	那么删除子部件
	:param master: 父部件
	:return:
	"""
	widget_set = master.winfo_children()
	if widget_set:
		for i in widget_set:
			i.destroy()


class HoverButton(tk.Button):
	"""
	继承Button.实现鼠标悬停时，按键变化的效果
	注意事项：
		图片按键和文字按键的width和height的度量单位不一样
	"""
	
	def __init__(self, master, **kw):
		tk.Button.__init__(self, master=master, **kw)
		self.defaultBackground = self["background"]
		self.config(relief="flat",
					activebackground="#ffc851")
		# print self["state"] # disabled normal
		if not self["state"] == "disabled":
			self.bind("<Enter>", self.on_enter)
			self.bind("<Leave>", self.on_leave)
	
	def on_enter(self, event=None):
		self['background'] = self['activebackground']
	
	def on_leave(self, event=None):
		self['background'] = self.defaultBackground


class NeewwEntry(tk.Entry):
	"""
	from https://stackoverflow.com/questions/41477428/
		ctrl-a-select-all-in-entry-widget-tkinter-python
	继承Entry，实现以下功能
		1.Ctrl A 实现全选的功能
	"""
	def __init__(self, master, **kw):
		tk.Entry.__init__(self, master=master, **kw)
		self.bind("<Control-a>", self.select_all)
	
	@staticmethod
	def select_all(event):
		# select text
		event.widget.select_range(0, 'end')
		# move cursor to the end
		event.widget.icursor('end')
		# stop propagation
		return 'break'


class NeewwText(tk.Text):
	"""
	from (https://stackoverflow.com/questions/5870561/
		re-binding-select-all-in-text-widget)
	继承Text，实现以下功能
		1.Ctrl A 实现全选的功能
	"""
	def __init__(self, master, **kw):
		tk.Text.__init__(self, master=master, **kw)
		self.config( maxundo=15, undo=True)
		self.bind_class("Text","<Control-a>", self.selectall)
	
	def selectall(self, event):
		event.widget.tag_add("sel","1.0","end")
	# 重新复写tk.Text().get()方法，默认其获得全部信息
	def get(self, index1="0.0", index2="end"):
		"""Return the text from INDEX1 to INDEX2 (not included)."""
		return self.tk.call(self._w, 'get', index1, index2)

	
class GradientCanvas(tk.Canvas):
	"""
	from Bryan Oakley on (https://stackoverflow.com/questions/26178869/
							is-it-possible-to-apply-gradient-colours-
							to-bg-of-tkinter-python-widgets)
	A gradient frame which uses a canvas to draw the background
	parent:
	color11: 渐变颜色1
	color22: 渐变颜色2
	"""
	def __init__(self, parent, color1= "#ffc851", color2="#808000", **kwargs):
		# "#808000" olive
		"""default gradient color: red to black"""
		tk.Canvas.__init__(self, parent, **kwargs)
		self._color1 = color1
		self._color2 = color2
		self.bind("<Configure>", self._draw_gradient)
		self.config(relief = "flat",highlightthickness = 0)

	def _draw_gradient(self, event=None):
		"""Draw the gradient"""
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = width
		(r1,g1,b1) = self.winfo_rgb(self._color1)
		(r2,g2,b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2-r1) / limit
		g_ratio = float(g2-g1) / limit
		b_ratio = float(b2-b1) / limit

		for i in xrange(limit):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
			self.create_line(i,0,i,height, tags=("gradient",), fill=color)
		self.lower("gradient")