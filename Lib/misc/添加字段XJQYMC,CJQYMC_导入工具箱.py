#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/7 10:00
# Reference:
"""
Description:�������shp�ļ��ֶ�CJQYDM��MC;XJQYDM��MC
Usage: �Ѿ������Զ��幤���� @�塢���ֶ����
"""
# ---------------------------------------------------------------------------
import arcpy
# from ezarcpy import ezlayer
# ezlayer.add_field()
def add_field(layer, names, f_type, f_length):
	"""����ֶ�
	:param layer:{String} shp�ļ�·��
	:param names:{List} �����ֶ�����
	:param f_type: {String} �ֶ�����
	:param f_length: {Long} �ֶγ���
	:return: ���ص�ǰ��ͼ�����
	"""
	the_fields = arcpy.ListFields(layer)
	# ��ǰͼ����ֶ������б�
	fields_array = []
	for field in the_fields:
		# fields_array.append(field.aliasName)
		fields_array.append(field.name)
	arcpy.AddMessage("\n")
	for name in names:
		if name not in fields_array:
			arcpy.AddField_management(layer, name, f_type, field_length = f_length)
			# arcpy.AddMessage("\n")
			arcpy.AddMessage(name)
	return layer
	
	

if __name__ == '__main__':
	
	in_layer = arcpy.GetParameterAsText(0)
	# �½��ֶ����� Ĭ�� XJQYMC XJQYDM CJQYDM CJQYMC
	new_names = arcpy.GetParameterAsText(1)
	# new_names = "XJQYMC;XJQYDM;CJQYDM;CJQYMC"
	# �ֶγ��� Ĭ��100
	length = arcpy.GetParameterAsText(2)
	# length = 100
	new_names = new_names.split(";")
	# mxd0 = arcpy.mapping.MapDocument("CURRENT")
	add_field(in_layer,new_names,"TEXT",length)
	
	arcpy.AddMessage("Done")
	arcpy.AddMessage("\n")