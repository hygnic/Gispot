# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/6

import arcpy
import os
import sys
print sys.path[0]
print sys.executable

scriptPath = sys.path[0]
arcpy.AddMessage("1--------------------")
arcpy.AddMessage(__file__)
# ooo = open(sys.argv[0],'r')
# arcpy.AddMessage(ooo.read())
arcpy.AddMessage("Script folder: " + scriptPath)

arcpy.AddMessage("2--------------------")
toolSharePath = os.path.dirname(scriptPath)
arcpy.AddMessage("ToolShare folder: " + toolSharePath)

arcpy.AddMessage("3--------------------")
# 可以获得工具箱的真实路径
pathname = os.path.realpath(sys.argv[0])
tool_path = pathname.split(".tbx",1)[0]+".tbx"
arcpy.AddMessage("Toolbox: " + tool_path)

# 遍历工具箱

for dirpath, dirnames, filenames in arcpy.da.Walk(tool_path,topdown=True,datatype = "Toolbox"):
	"""返回值，植入工具箱
	G:\MoveOn\doctools1\2019分布图.tbx
	[]
	[u'e', u'r', u'yy', u'gggg', u'w', u'q', u'tt', u'ImporttoolboxLcc1',
	u'Arcsettings', u'kk', u'dsfdfd', u'KKfa',
	u'installhygnicsettings', u'getpath']"""
	
	arcpy.AddMessage(dirpath)
	arcpy.AddMessage(dirnames)
	arcpy.AddMessage(filenames)
	outpath = os.path.join(dirpath,"getpath_CatofLcc.py")
	arcpy.AddMessage(outpath)
	for filename in filenames:
		if filename == "q":
			f = open(outpath,"r")
			print f.read()
			arcpy.AddMessage(f.read())
		else:
			arcpy.AddMessage("no")
	
# arcpy.ImportToolbox(pathname)
# print arcpy.cpttool.Arcsettings.make_authentication_setting("2020-3-1")

# 工具箱中输出结果
# Script folder: G:\MoveOn\doctools
# ToolShare folder: G:\MoveOn
# G:\MoveOn\doctools\2019分布图.tbx  #ImporttoolboxLcc1_cpttool.py

# G:\MoveOn\doctools\2019分布图.tbx