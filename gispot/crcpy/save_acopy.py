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
import arcpy
import os
from hybag import hybasic


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
		print "here1"
		# mxd1.saveACopy(new_path + "\\" + name + ".mxd", version=version)
		mxd1.saveACopy(ur"D:\test\df.mxd", version=version)

def new_mian(input_file, out_file, version):
	mxd = arcpy.mapping.MapDocument(input_file)
	mxd.saveACopy(out_file, version=version)
	
	
if __name__ == '__main__':
	new_mian(
		ur"G:\高标准分布图\金堂县\金堂县.mxd",
		ur"G:\高标准分布图\金堂县\金堂县2.mxd",
		version="10.1")