# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/20
# python2 arcgis10.3

import arcpy
from multiprocessing import Process
from hyconf import multication
import tooltk




class StartApp(tooltk.Tooltk):
	""""""
	def __init__(self, master_f):
		"""
		:param master_f: mian_f , a widget from tool_entrance.py
		"""
		super(StartApp, self).__init__(master_f,
										"../docs/task_dispatch.gc",
									   self.confirm)
		# block1
		self.single_file_block(
			[(u'地图文档', '*.mxd'), ('All Files', '*')],"mxd"
		)
		# block2
		self.single_dir_block(u"输出文件夹")
		# block3
		self.single_text_block(u"分组")
		self.window.mainloop()
		
		
	def confirm(self):
		pass
