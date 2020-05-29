#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/28 15:57
# Reference:
"""
Description: py2exe 脚本设置文件
Usage:
"""
# ---------------------------------------------------------------------------
import sys
import os
from distutils.core import setup
import py2exe

# E:\move on move on\gispot\GUIs\entrance.py
realp = os.path.abspath(sys.argv[0])
print "os.path.abspath(sys.argv[0]):",os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# 该文件所处的文件夹绝对路径
realp_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = os.path.abspath(os.path.dirname(realp_dir))
print "os.path.dirname(sys.argv[0]):",os.path.dirname(sys.argv[0])
print "root_base:",root_base
# E:\move on move on\gispot\gispot
rb_GisCat = os.path.join(root_base, "gispot")
# E:\move on move on\gispot\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\gispot\GUIs\Icons
rbg_Icons = os.path.join(rb_GUIs, "Icons")
rbdoc = os.path.join(root_base, "docs")
rb_bin = os.path.join(root_base, "bin")
rb_libs = os.path.join(root_base, "Lib")
rb_GUIconfig = os.path.join(rb_libs, "GUIconfig")

giscat_paths = [root_base,
				rb_GisCat,
				rb_GUIs,
				rbg_Icons,
				rbdoc,
				rb_bin,
				rb_libs,
				rb_GUIconfig]
for giscat_path in giscat_paths:
	sys.path.append(giscat_path)

options = {
	"py2exe":{
		"excludes": ["arcpy"]
	}
}
# 添加图片
images = []
imgs = os.listdir(rbg_Icons)
for img in imgs:
	image_p = os.path.join(rbg_Icons, img)
	if os.path.isfile(image_p):
		images.append(image_p)
# 添加文档
gisdocs = []
docs = os.listdir(rbdoc)
for doc in docs:
	doc_p = os.path.join(rbdoc,doc)
	if os.path.isfile(doc_p):
		gisdocs.append(doc_p)

setup(windows=["Gispot.py"], options=options,
	  data_files=[('images',images),("gisdocs",gisdocs)]
	  )

data_files=[('images', ['..\GUIs\Icons\close30_4.gif','..\GUIs\Icons\GitHub_32.gif'])]
# setup(console=["Gispot.py"], options=options)