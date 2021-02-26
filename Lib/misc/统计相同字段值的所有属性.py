#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# User: liaochenchen
# Date: 2020/3/19
# python2 arcgis10.6
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import arcpy
import codecs
"""
����ͼ��
	��λ��ѡ��
	���Ա��ȡģ��
	д��
"""


def getvalue_from_attribute(layer, txt_output, strrr, class_field, value_field):
	# ��ȡlayerͼ�����Ա���������ֵͬ�ĺͣ������ȡһ��ͬһ�������£�����TBDLMJ�ĺ�
	"""
	:param layer:  ͼ��
	:param txt_output:  ���TXT·��
	:param strrr:
	:param class_field: ���ڷ�����ֶ� �� CJQYMC
	:param value_field: ������Ҫ�����ݵ��ֶΣ���������ֶ� "SHAPE@AREA" ��
	:return:
	"""
	field_list = [class_field, value_field]
	with arcpy.da.UpdateCursor(layer, field_list) as cursor:
		name = None
		class_field_list = []
		# get the names with list format
		for row in cursor:
			if row[0] not in class_field_list:
				class_field_list.append(row[0])
		cursor.reset()
		for name in class_field_list:
			mjm = 0
			mj = 0
			# cursor ֻ�ܱ���һ��
			for roww in cursor:
				if name == roww[0]:
					tbdlmj = float(roww[1])
					mj += tbdlmj
					mjm += round(tbdlmj * 0.0015, 4)
					# mj+=roww[0]
			cursor.reset()
			# mian ji dan wei   mu
			msgg = "," + name + "," + str(mjm) + "\n"
			print msgg
			f11 = codecs.open(txt_output, "a", "utf8")
			# f=open(txt_output,"a")
			f11.write(strrr)
			f11.write(msgg)
		f11.write("\n")
		f11.close()


"""__________________________________________________________________________"""
if __name__ == '__main__':
	# ע�⣺GBZũ�ﲻ���ǿձ� �ձ����´��Ժ��ٽ��
	"""
	Runtime error
	Traceback (most recent call last):
	File "<string>", line 84, in <module>
	File "<string>", line 64, in getvalue_from_attribute
		UnboundLocalError: local variable 'f11' referenced before assignment
	"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	txt_path = ur"G:\121.txt" # �� G:\121.txt �滻������Ҫ�����txt��ַ�����Զ�����TXT�ļ���
	mxd = arcpy.mapping.MapDocument("CURRENT")
	layer_dltb = arcpy.mapping.ListLayers(mxd, "DLTB")[0]
	layer_GBZ = arcpy.mapping.ListLayers(mxd, "GBZ*")  # [...,"GBZ2018510604GT�������޽���۳������������������ĿSS",...]
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	"""______________________________attention_______________________________"""
	
	print "GBZ_count:", len(layer_GBZ)
	for i in layer_GBZ:
		print "GBZ_name:", i.name
		real_name = i.name[15:-2]
		try:
			arcpy.SelectLayerByLocation_management(
				layer_dltb, "WITHIN", i, "", "NEW_SELECTION")  # 10.1ֻ�����Ҫ��
		except arcpy.ExecuteError as e:
			print e.message
			continue
		# ��Ҫ��DLTB���ռ����� ������������������
		getvalue_from_attribute(layer_dltb, txt_path, real_name, "XZQMC", "TBDLMJ")
		# getvalue_from_attribute(layer_dltb, txt_path,real_name,"MC_new", "TBDLMJ")
