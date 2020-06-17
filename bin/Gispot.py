# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/10
# python2.7

# explode.py: import arcpy

import os
import sys
from site import addsitedir # py2exe
import multiprocessing
from xml.etree.ElementTree import ElementTree
# ------------ py2exe
interpreter = sys.executable
sitepkg = os.path.dirname(interpreter) + "\\site-packages"
# sitepkg1 = os.path.dirname(interpreter) + "\\Lib\\site-packages"
print(sitepkg)
addsitedir(sitepkg)
# addsitedir(sitepkg1)
# ------------ py2exe

"""
程序的入口，未以__file__为基准地址的文件的地址都以此入口为锚点
,现在使用sys.argv[0]
"""

bin_p = os.path.abspath(os.path.dirname(sys.argv[0]))
print "bin_p",bin_p
# real:  E:\move on move on\gispot\bin
root_p = os.path.abspath(os.path.dirname(bin_p))  # E:/move on move on/gispot
# print "root_P:",root_p
sys.path.append(os.path.join(root_p, "GUIs"))


import entrance

if __name__ == '__main__':
	# 支持多进程打包为可执行文件
	multiprocessing.freeze_support()
	# print sys.path
	print "ProcessID:{}\n".format(os.getpid())
	entrance = entrance.AppEntrance()
	entrance.menu()
	# 操控所有循环
	entrance.rootwindow.mainloop()
	
	
	
	
	
	
	
	
	
# sys.path.append(r"D:\Python27\ArcGIS10.7\tcl\tcl8.5")
# apppath = r"bin\entrance.py"
# sys.path.append("../docs")

# path = "../docs/gstrename.gc"

# with open(path,"r") as f:
# 	s = f.readlines()
# 	for i in s:
# 		print i
