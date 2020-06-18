#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/7 9:34
# Reference:
"""
Description: 将高版本的arcgis另存为低版本
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
import os
from hybag import hybasic

try:
	import tooltk
	import tkinter as tk
	from GUIconfig import paths
except ImportError as e:
	print e

def main(dir_p,new_dir,version=None):
	"""
	main(dir_p,new_dir,{version})
	Provides an option to save a map document ( .mxd ) to a new file, and optionally, to a previous version.
	 dir_p(String):
	 new_dir(String):
	 version(Float):
	*10.3: Version
		10.3
		
		*10.1:   Version
		10.1 / 10.2
		
		*10.0: Version
		10.0
		
		*9.3:   Version
		9.3
		
		*9.2:   Version
		9.2
		
		*9.0:   Version
		9.0 / 9.1

		*8.3:   Version
		8.3
	"""
	path = dir_p
	suff = "mxd"
	version = str(version)
	# 获取文件夹下所有文件
	path_list = hybasic.HBgetfile(path, suff, False)
	for i in path_list:
		i_base = os.path.basename(i)
		name = os.path.splitext(i_base)[0]
		new_path = new_dir
		# mxd_p =os.path.join(path,i)
		# print mxd_p
		mxd1 = arcpy.mapping.MapDocument(i)
		mxd1.saveACopy(new_path+"\\"+name+".mxd",version=version)
		
doc_path = paths.DocPath.doc_saveacopy
class SaveACopy(tooltk.Tooltk):

	def __init__(self, master):
		super(SaveACopy, self).__init__(master,
										doc_path,
										self.confirm)
		# block1
		self.single_dir_block(u"文件夹路径")
		# block2 取消按钮
		self.single_dir_block2(u"保存文件夹路径")
		frame = (self.block_frame,self.msgframe,self.major_msgframe)
		ss = tooltk.SingleFileBlock(frame, [(u'文本文档', '*.txt'), ('All Files', '*')], "io")
		
	def confirm(self):
		para = self.get_blockvalue(self.input_sdb,self.input_sdb2)
		p1 = para[0]
		p2 = para[1]
		main(p1,p2,10.1)
	
if __name__ == '__main__':
	main(ur"G:\正安县\正安县分布图\成果",
		 ur"G:\正安县\正安县分布图\test",10.3)