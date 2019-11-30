# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/10
import os,sys

"""
程序的入口，未以__file__为地址的文件的地址都以此入口为锚点
"""

bin_p = os.path.dirname(__file__)
# real:  E:\move on move on\Gispot\bin
root_p = os.path.dirname(bin_p)
# print "root_P:  ",root_p  #  E:/move on move on/Gispot
sys.path.append(os.path.join(root_p, "GUIs"))

import tool_entrance

if __name__ == '__main__':
	# print sys.path
	entrance = tool_entrance.AppEntrance()
	entrance.menu()
	entrance.rootwindow.mainloop()
	
	
	
	
	
	
	
	
	
	
# sys.path.append(r"D:\Python27\ArcGIS10.7\tcl\tcl8.5")
# apppath = r"bin\tool_entrance.py"
# sys.path.append("../docs")

# path = "../docs/gstrename.gc"

# with open(path,"r") as f:
# 	s = f.readlines()
# 	for i in s:
# 		print i
