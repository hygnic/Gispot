#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/15 12:33
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
from threading import Thread
import time

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
		# self.bind("<Configure>", self._draw_gradient)
		self.config(relief = "flat",highlightthickness = 0)
		t = Thread(target=self.test1)
		t.setDaemon(True)
		t.start()
	
	def test1(self):
		# draw gradient color;
		# For showing gradient color bar we have to set explicit height&width values(without bind "<Configure>").
		flag = True
		colors=["#ffc851","#808000","#f5f6f7","#5294e2"]
		colors2 = [
			"#fffcf9","#fffcf9","#fff7ef","#fff4ea","#fff2e5","#ffefe0","#ffeddb",
			"#ffead6", "#ffe8d1", "#ffe5cc", "#ffe2c6","#ffe0c1", "#ffddbc",
			"#ffdbb7"
		]
		colors= colors2
		while colors:
			c1 = colors.pop(0)
			c2 = colors.pop(0)
			time.sleep(2)
			self.config(bg=c1)
			self.delete("all")
			width =700
			height = 100
			limit = width
			
			(r1, g1, b1) = self.winfo_rgb(c1)
			(r2, g2, b2) = self.winfo_rgb(c2)
			colors.append(c1)
			colors.append(c2)
			r_ratio = float(r2 - r1) / limit
			g_ratio = float(g2 - g1) / limit
			b_ratio = float(b2 - b1) / limit
			for i in xrange(limit):
				nr = int(r1 + (r_ratio * i))
				ng = int(g1 + (g_ratio * i))
				nb = int(b1 + (b_ratio * i))
				color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
				self.create_line(i, 0, i, height, tags=("gradient",), fill=color)


	
	def _draw_gradient(self, event=None):
		"""Draw the gradient"""
		def inner():
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
		return inner()
	
if __name__ == '__main__':
	root = tk.Tk()
	root.geometry("700x100+200+200")
	
	# def fun1(gcc):
	# 	time.sleep(2)
	# 	gcc.destroy()
	# 	gc1 = GradientCanvas(root, color1="#f5f6f7", height=100, width=700)
	# 	gc1.pack(fill="both")
	#
	gc = GradientCanvas(root,height = 5, width =700,bg="blue")
	gc.pack(fill="both")
	# t =Thread(target=fun1, args=(gc,))
	# t.start()
	
	# root.after(10000, fun1(gc))

	root.mainloop()
	