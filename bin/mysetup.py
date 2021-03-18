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
from os.path import isfile, join, abspath, dirname
from os import listdir
from distutils.core import setup
import py2exe

# E:\move on move on\gispot\GUIs\entrance.py
realp = abspath(sys.argv[0])
print "abspath(sys.argv[0]):",abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# 该文件所处的文件夹绝对路径
realp_dir = abspath(dirname(sys.argv[0]))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = abspath(dirname(realp_dir))
print "dirname(sys.argv[0]):",dirname(sys.argv[0])
print "root_base:",root_base
# E:\move on move on\gispot\gispot
rb_GisCat = join(root_base, "gispot")
# E:\move on move on\gispot\GUIs
rb_GUIs = join(root_base, "GUIs")
# E:\move on move on\gispot\GUIs\Icons
rbg_Icons = join(rb_GUIs, "Icons")
rbdoc = join(root_base, "docs")
rb_tempalte = join(root_base, "docs/template")
rb_bin = join(root_base, "bin")
rb_site_packages = join(rb_bin, "package_py2exe/site-packages")
rb_ttkthemes_patch = join(rb_bin, "package_py2exe/ttkthemes_patch/ttkthemes_patch.zip")
rb_libs = join(root_base, "Lib")
rb_GUIconfig = join(rb_libs, "gpconfig")

giscat_paths = [root_base,
				rb_GisCat,
				rb_GUIs,
				rbg_Icons,
				rbdoc,
				rb_tempalte,
				rb_bin,
				rb_libs,
				rb_GUIconfig]
for giscat_path in giscat_paths:
	sys.path.append(giscat_path)
"""_____________________________________________________________________________
info:
can't compress when skipping archive
"""
options = {
	"py2exe":{
		"includes": ["matplotlib","Tkinter", "ttk"],
		# "includes": ["matplotlib","Tkinter", "ttk", "ttkthemes"],
		"excludes": ["arcpy"],
		"dll_excludes": ["MSVCP90.dll"],
		# "skip_archive": False,# 跳过压缩的话，不会将大部分的py包放进libray.zip压缩文件（使用ttktheme时请取消注释）
		# "bundle_files":1, # 无法成功
		# "compressed": True, # 压缩
		# "optimize": 2,
		
	}
}
# py2exe打包过程中遇到该问题 Could not find the matplotlib data files
import matplotlib
setup(data_files=matplotlib.get_py2exe_datafiles(),)

# 添加图片
images = [join(rbg_Icons, _) for _ in listdir(rbg_Icons) if isfile(join(rbg_Icons, _))]
# 添加文档
gisdocs = [join(rbdoc, _) for _ in listdir(rbdoc) if isfile(join(rbdoc, _))]
# 添加 .path 文件
site_packages = [join(rb_site_packages, _) for _ in listdir(rb_site_packages)]
# 添加 ttkthemes_patch.zip 文件, 解压后是ttkthemes模块的配置文件等
ttkthemes_patch = [rb_ttkthemes_patch] # just one file
# C:\Users\Administrator\Desktop\Gispot-master\docs\template
# 添加模板
template = [join(rb_tempalte, _) for _ in listdir(rb_tempalte) if isfile(join(rb_tempalte, _))]


# windows 独立窗口
# console 带dos界面
setup(
	windows=[{'script':'Gispot.py', 'icon_resources': [(1, u'icon_black.ico')]}],
	options=options,
	name = 'LCC',
	data_files=[('images',images), ("gisdocs",gisdocs),("template",template),
				("site-packages",site_packages), ("ttkthemes", ttkthemes_patch)],
	zipfile = None, # If zipfile is set to None, the files will be bundle within the executable instead of library.zip.
	  )

# data_files=[('images', ['..\GUIs\Icons\close30_4.gif','..\GUIs\Icons\GitHub_32.gif'])]
# setup(console=["Gispot.py"], options=options)