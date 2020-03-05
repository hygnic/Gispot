# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/5
# python2 arcgis10.6
"""
单进程导出JPEG图片
"""
import arcpy, os

def export(path, resolution):
	if not os.path.isdir(path):
		print u"文件夹名字或格式出错"
	resolution = int(resolution)
	arcpy.env.overwriteOutput = True
	for afile in os.listdir(path):
		if afile[-3:].lower() == 'mxd':
			mxd1 = arcpy.mapping.MapDocument(os.path.join(path, afile))
			print u'出图中...'
			# ExportToJEPG的第二个参数是导出图片的名称和目录设置
			arcpy.mapping.ExportToJPEG(
				mxd1, os.path.join(path, afile[:-3] + 'jpg'), resolution=resolution
			)
			print afile + u' 出图完成'
			print "\n----------------"
			del mxd1
		else:
			None
