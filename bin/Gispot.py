# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/10
# python2.7
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

"""WHICH PACKAGE I USE"""
"""PIL"""
"""pywin32"""
"""xlwings"""

"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# explode.py: import arcpy
import os
import sys
from site import addsitedir  # py2exe
import multiprocessing
from xml.etree.ElementTree import ElementTree

# ------------ py2exe
interpreter = sys.executable
sitepkg = os.path.dirname(interpreter) + "\site-packages"
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
print "bin_p", bin_p
root_p = os.path.abspath(os.path.dirname(bin_p))  # E:/move on move on/gispot
sys.path.append(os.path.join(root_p, "GUIs"))

import entrance



if __name__ == '__main__':
    
    
    multiprocessing.freeze_support() # 支持多进程打包为可执行文件
    print "ProcessID:{}\n".format(os.getpid())
    entrance = entrance.AppEntrance()
# entrance.rootwindow.mainloop()