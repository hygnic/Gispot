#!/usr/bin/env python
# -*- coding:cp936 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/3/26 14:48
"""
Description:
1.Ϊʲôд�����ںϣ��������У���Ϊ�Դ��Ĺ����������ںϵ����ļ�ʱ��
�޷�ͳһָ�����ƺʹ洢λ��
2.�����ںϣ�����ļ����Ʋ���
	ע������
	1.	�����ںϵ�ͼ�㲻������ͼ������
Usage:
�Ѿ�����
"""
# ---------------------------------------------------------------------------
import arcpy

# ��ѡ;����;Ҫ��ͼ��
in_f  =arcpy.GetParameterAsText(0)
# ����ļ���
output_dir = arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True
arcpy.env.workspace = output_dir
arcpy.AddMessage("\n")
# ��ɢ����б�
in_f = in_f.split(";")
count = 1 # ����
for feature in in_f:
	arcpy.AddMessage(str(count)+". "+feature)
	arcpy.Dissolve_management(feature,
							  feature,
							  ["XMMC"], "", "MULTI_PART",
							  "DISSOLVE_LINES")
	count+=1
arcpy.AddMessage("\n")


