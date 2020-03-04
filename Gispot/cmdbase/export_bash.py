# -*- coding:cp936 -*-
# User: liaochenchen
# Date: 2020/3/4
# python2 arcgis10.6

"""
单进程导出JPEG图片
cmd 默认识别cp936编码的中文

尝试加入 u"输入文件夹" 失败
"""

import arcpy, os

dir_path = raw_input('输入文件夹：')
if not os.path.isdir(dir_path):
	print "文件夹名字或格式出错"
res = raw_input('设置分辨率：')
res = int(res)
arcpy.env.overwriteOutput = True
for afile in os.listdir(dir_path):
	if afile[-3:].lower() == 'mxd':
		mxd1 = arcpy.mapping.MapDocument(os.path.join(dir_path, afile))
		print '出图中...'
		# ExportToJEPG的第二个参数是导出图片的名称和目录设置
		arcpy.mapping.ExportToJPEG(
			mxd1, os.path.join(dir_path, afile[:-3] + 'jpg'), resolution=res
		)
		print afile + ' 出图完成'
		print "\n----------------"
		del mxd1
	else:
		None
