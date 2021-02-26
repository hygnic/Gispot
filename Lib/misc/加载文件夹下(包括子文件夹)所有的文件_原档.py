#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# User: liaochenchen
# Date: 2020/3/11
# Python2 arcgis10.6 arcgis10.3
# Reference:
"""
Description: ����hybag_base �еķ������ͷ�����
*�Ѿ����빤����
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy,os

def hybag_addshp(shp_path,fresh=True):
	"""
	import arcpy,os
	����shp�ļ�����ǰmxd
	:param shp_path: file path.
	:param df_name: dataframe name; default first df.
	:param fresh:bollean; refresh; default ture.
	:return: None
	"""
	mxd = arcpy.mapping.MapDocument("CURRENT")
	dataframe = arcpy.mapping.ListDataFrames(mxd)[0]
	layer = arcpy.mapping.Layer(shp_path)
	arcpy.mapping.AddLayer(dataframe, layer)
	if fresh:
		arcpy.RefreshActiveView()  # ˢ�µ�ͼ�Ͳ��ִ���
		arcpy.RefreshTOC()  # ˢ�������б�

_getall_items = []
_not_get = []
def recur_search(dirs_p, suffix,size_limit, matchword=None):
	"""
	import os
	�������һ���ļ��У��������ļ��У������еķ��Ϻ�׺��item
	recur ʹ�õݹ飬�ر�ע�⣬������Ҫ̫��
	:param size_limit: �ļ���С���� �ֽ�
	:param dirs_p: dir address
	:param suffix: ��׺
	:param matchword: ƥ���ֶΣ���ɸѡ������ƥ���ֶε���Ŀ
	:return: list
	"""
	global _getall_items
	global _not_get
	matchword=str(matchword)
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			# �ݹ�
			recur_search(file_path, suffix,size_limit, matchword)
		else:
			# arcpy.AddMessage(4)
			if matchword: # ��֤��ʹ��matchwordƥ���ֶ�ʱҲ����������
				# arcpy.AddMessage(6)
				# if file_p[-3:].lower() == suffix and matchword in file_p and os.path.getsize(file_path)!=100:
				if file_p[-3:].lower() == suffix and matchword in file_p:
					# ʹ�����ļ���С�����Ҳ����ϴ�СҪ��
					if size_limit and os.path.getsize(file_path)!=size_limit:
						print type(matchword)
						print matchword
						_getall_items.append(file_path)
					# û��ʹ�ô�С����
					elif not size_limit:
						_getall_items.append(file_path)
					# ʹ���˴�С���ƣ����ϴ�СҪ��
					else:
						# ���ڿ�ͷ��� cp936���У�����arctoolbox����EOL error
						_not_get.append(file_path)
						arcpy.AddMessage("����Ŀ/δ����")
						arcpy.AddMessage(os.path.splitext(os.path.basename(file_path))[0])
			else:
				# arcpy.AddMessage(9)
				if file_p[-3:].lower() == suffix:
					# ʹ�����ļ���С�����Ҳ����ϴ�СҪ��
					if size_limit and os.path.getsize(file_path) != size_limit:
						print type(matchword)
						print matchword
						_getall_items.append(file_path)
					# û��ʹ�ô�С����
					elif not size_limit:
						_getall_items.append(file_path)
					# ʹ���˴�С���ƣ����ϴ�СҪ��
					else:
						# ���ڿ�ͷ��� cp936���У�����arctoolbox����EOL error
						_not_get.append(file_path)
						arcpy.AddMessage("����Ŀ/δ����")
						arcpy.AddMessage(
							os.path.splitext(os.path.basename(file_path))[0])
					# print type(matchword)
					# print matchword
					# __getall_items.append(file_path)
	return _getall_items


dir_path = arcpy.GetParameterAsText(0)
# dir_path = ur"F:\19-20����Զ��\��Զ11-18��\510000�߱�׼ũ�ｨ����ͼ�������20200702"
match_w = arcpy.GetParameterAsText(1)
# match_w = "GBZ"
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

match_w = str(match_w)
print match_w
print type(match_w)
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

filelist = recur_search(dir_path, "shp",100, matchword=match_w)
count = len(filelist)
count1 = len(_not_get)
arcpy.AddMessage("\n"+"loading...")
for afile in filelist:
	hybag_addshp(afile)
msg1 = str(count)+ " files loaded"
msg2 = str(count1)+ " files not loaded"
arcpy.AddMessage("\n"+msg1)
arcpy.AddMessage(msg2)

# if __name__ == '__main__':
# 	files = hybag_getall_item(
# 		ur"G:\�߱�׼�ֲ�ͼ\�ന��\510000�߱�׼ũ�ｨ����ͼ�������20200113","shp","GBZ")
# 	print len(files)
# 	for afile in files:
# 		hybag_addshp(afile)
# 	msg1 = u"{0}���ļ��������".format(len(files))
# 	print msg1


# filess = hybag_getall_item(ur"G:\�߱�׼�ֲ�ͼ\yi��\shp",
# 				  "shp")
# print len(filess)
# print type(filess)
# for afile in filess:
# 	print type(afile)
# 	hybag_addshp(afile)
#
# path1=ur"G:\�߱�׼�ֲ�ͼ\yi��\shp"
# print os.path.isfile(path1)
# hybag_addshp(path1)
# hybag_addshp(ur"G:\�߱�׼�ֲ�ͼ\����\510502������\���ɹ�����\510000�߱�׼ũ�ｨ����ͼ�������20200115\510000CZ20165105022016�����ũҵ������չˮ����ĿYS\GBZ2016510502CZ2016�����ũҵ������չˮ����ĿYS.shp")


