# -*- coding:cp936 -*-
# User: liaochenchen
# Date: 2020/3/4
# python2 arcgis10.6
"""
单进程导出JPEG图片 适用于文件夹和单个mxd文档
cmd 默认识别cp936编码的中文

尝试加入 u"输入文件夹" 失败
"""
from __future__ import absolute_import
from hybag import hybasic


# import arcpy, os
#
# def export(path,resolution):
# 	arcpy.env.overwriteOutput = True
# 	if not os.path.isdir(path) and path[-3:].lower() == 'mxd':
# 		print "file"
# 		mxd1 = arcpy.mapping.MapDocument(path)
# 		print 'exporting...'
# 		arcpy.mapping.ExportToJPEG(
# 			mxd1, os.path.abspath(path[:-3] + 'jpg'), resolution=resolution)
# 		a = os.path.split(path)
# 		print a[1]+"finished"
# 	else:
# 		print "folder"
# 		for afile in os.listdir(path):
# 			if afile[-3:].lower() == 'mxd':
# 				mxd1 = arcpy.mapping.MapDocument(os.path.join(path, afile))
# 				print 'exporting...'
# 				# ExportToJEPG的第二个参数是导出图片的名称和目录设置
# 				arcpy.mapping.ExportToJPEG(
# 					mxd1, os.path.join(path, afile[:-3] + 'jpg'), resolution=resolution
# 				)
# 				print afile + ' finished'
# 				print "\n----------------"
# 				del mxd1
# 			else:
# 				pass
				
# 使用此函数调用功能函数，不想直接将用户交互界面写入
def func():
	# dir_path = raw_input(u'文件夹或mxd文档：')
	dir_path = ur"G:\耕地质量等级\阿坝19年"
	# res = int(raw_input(u'分辨率：'))
	res = 100
	hybasic.export(dir_path, res)
	
	
if __name__ == '__main__':
	func()

