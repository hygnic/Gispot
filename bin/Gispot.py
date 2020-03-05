# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/10
# python2.7
import os
import sys
"""
程序的入口，未以__file__为基准地址的文件的地址都以此入口为锚点
"""

bin_p = os.path.abspath(os.path.dirname(__file__))
# real:  E:\move on move on\GiSpot\bin
root_p = os.path.abspath(os.path.dirname(bin_p))
# print "root_P:  ",root_p  #  E:/move on move on/GiSpot
sys.path.append(os.path.join(root_p, "GUIs"))


import entrance

if __name__ == '__main__':
	# print sys.path
	print os.getpid()
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
