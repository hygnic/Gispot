# -*- coding:cp936 -*-
# User: liaochenchen
# Date: 2020/3/4
# python2 arcgis10.6
"""
�����̵���JPEGͼƬ �������ļ��к͵���mxd�ĵ�
cmd Ĭ��ʶ��cp936���������

���Լ��� u"�����ļ���" ʧ��
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
# 				# ExportToJEPG�ĵڶ��������ǵ���ͼƬ�����ƺ�Ŀ¼����
# 				arcpy.mapping.ExportToJPEG(
# 					mxd1, os.path.join(path, afile[:-3] + 'jpg'), resolution=resolution
# 				)
# 				print afile + ' finished'
# 				print "\n----------------"
# 				del mxd1
# 			else:
# 				pass
				
# ʹ�ô˺������ù��ܺ���������ֱ�ӽ��û���������д��
def func():
	# dir_path = raw_input(u'�ļ��л�mxd�ĵ���')
	dir_path = ur"G:\���������ȼ�\����19��"
	# res = int(raw_input(u'�ֱ��ʣ�'))
	res = 100
	hybasic.export(dir_path, res)
	
	
if __name__ == '__main__':
	func()

