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
from GUIconfig import GUIpath
import tooltk
# import tkFileDialog
# import tkinter as tk


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
	path_list = hybasic.getfiles(path, suff, False)
	for i in path_list:
		i_base = os.path.basename(i)
		name = os.path.splitext(i_base)[0]
		new_path = new_dir
		# mxd_p =os.path.join(path,i)
		# print mxd_p
		mxd1 = arcpy.mapping.MapDocument(i)
		mxd1.saveACopy(new_path+"\\"+name+".mxd",version=version)
		
doc_path = GUIpath.DocPath.doc_saveacopy
class SaveACopy(tooltk.Tooltk):

	def __init__(self, master):
		super(SaveACopy, self).__init__(master,
										doc_path,
										self.confirm)
		frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
		# block1
		# self.single_dir_block(u"文件夹路径")
		# block1 = tooltk.SingleFileBlock(frame, u"文件夹路径1",
		# 							tkFileDialog.askdirectory, 	None,
		# 							"folder")
		block1 = tooltk.blockDIR_in(frame, u"文件夹地址")
		block1.entry.focus_force()
		# block2
		# self.single_dir_block2(u"保存文件夹路径")
		# block2 = tooltk.SingleFileBlock(frame, u"保存文件夹路径2",
		# 								tkFileDialog.askdirectory, None,
		# 								"folder")
		# block2 = tooltk.blockInt(frame, u"保存文件夹路径")
		block2 = tooltk.blockDIR_out(frame, u"文件夹保存地址")
		

		self.value1 = block1.get
		self.value2 = block2.get
		
	def confirm(self):
		# para = self.get_blockvalue(self.input_sdb,self.input_sdb2)
		# p1= para[0]
		# p2 = para[1]
		p1 =self.value1()
		p2 =self.value2()
		#
		# p1 =self.block1.gett_entry()
		# p2 =self.block2.gett_entry()
		print "p1",p1
		
		print "p2",p2
		# with open(p3,"r") as e:
		# 	print e.readlines()
		main(p1,p2,10.1)
		
		# msg: G:\内江市\市中区分布图\MXD\10.3
		# 版本
		# msg's type: <type 'unicode'>
		# msg: G:\内江市\市中区分布图\MXD\10.3
		# 版本\新建文件夹
		# msg's type: <type 'unicode'>

		
if __name__ == '__main__':
	main(ur"G:\正安县\正安县分布图\成果",
		 ur"G:\正安县\正安县分布图\test",10.3)