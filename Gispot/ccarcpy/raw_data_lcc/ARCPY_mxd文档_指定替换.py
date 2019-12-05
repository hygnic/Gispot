# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/27
"""
批量替换 mxd 中的图层，which 图层数据格式为文件夹保存形式，
用于正安县的两区 DK、PK 图层的替换，但我突然发现，直接将文
件夹中对应文件换掉就行了。
"""



import arcpy
import os

m_path = u"地图文档文件夹"
mxd_names = os.listdir(m_path)
for mxd_name in mxd_names:
	# filter mxd
	if mxd_name[-3:].lower() == "mxd":
		mxd1 = arcpy.mapping.MapDocument(os.path.join(
			m_path,mxd_name)
		)



