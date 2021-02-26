#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/15 0:02
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk


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
	
	def __init__(self, parent, color1="#ffc851", color2="#808000", **kwargs):
		# "#808000" olive
		"""default gradient color: red to black"""
		tk.Canvas.__init__(self, parent, **kwargs)
		self._color1 = color1
		self._color2 = color2
		self.bind("<Configure>", self._draw_gradient)
		self.config(relief="flat", highlightthickness=0)
	
	def _draw_gradient(self, event=None):
		"""Draw the gradient"""
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = width
		(r1, g1, b1) = self.winfo_rgb(self._color1)
		(r2, g2, b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2 - r1) / limit
		g_ratio = float(g2 - g1) / limit
		b_ratio = float(b2 - b1) / limit
		
		for i in xrange(limit):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
			self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
		self.lower("gradient")


if __name__ == '__main__':
	root = tk.Tk()
	colors = ["#ffc851", "#808000","#f5f6f7" ,"#5294e2" ]
	gc=GradientCanvas(root,width=700,height = 100)
	gc.pack(fill = "both")
	root.mainloop()