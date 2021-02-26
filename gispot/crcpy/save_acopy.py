#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/7 9:34
# Reference:
"""
Description: 将高版本的arcgis另存为低版本 安装arcgis 10.3版本可以使用，10.1不能
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import print_function
from __future__ import absolute_import
import arcpy
import os
from multiprocessing import Process

from hybag import hybasic
import tooltk
from gpconfig import multication

def main(dir_p, new_dir, version=None):
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
		print("here1")
		# mxd1.saveACopy(new_path + "\\" + name + ".mxd", version=version)
		mxd1.saveACopy(ur"D:\test\df.mxd", version=version)

def new_mian(qq,input_file, out_file, version):
	mxd = arcpy.mapping.MapDocument(input_file)
	info1 = "begin..."
	# print(info1)
	qq.append(info1)
	mxd.saveACopy(out_file, version=version)
	qq.append("COMPLETE\n")
	
class SaveACopyFunction(tooltk.Tooltk):
	"""
	:param master1: self.master, a widget from interface.py
	"""
	
	def __init__(self, master1):
		super(SaveACopyFunction, self).__init__(
			master1, "save_acopy.gc", self.confirm)
		frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
		# block1
		self.block1 = tooltk.blockMXD_in(frame, u"MXD文件")
		# block2
		self.block2 = tooltk.blockMXD_out(frame, u"保存路径")
		self.commu = multication.MuCation()
		self.name="版本降低"
		
	def confirm(self):
		v = [self.block1.get(), self.block2.get()]
		# main(v[0], v[1])
		p = Process(
			target=self.commu.decor, args=(new_mian, v[0], v[1], "10.1")
		)
		p.deamon = True
		p.start()
		self.commu.process_communication(self.major_msgframe)

if __name__ == '__main__':
	okok = []
	new_mian(okok,
		ur"G:\耕地质量等级\阿坝19年\1.mxd",
		ur"G:\耕地质量等级\阿坝19年\2.mxd",
		version="10.1")