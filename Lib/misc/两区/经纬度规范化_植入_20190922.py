# -*- coding:cp936 -*-
# User: 廖晨辰
# Date: 2019/9/19
import arcpy
import datetime

time1=datetime.datetime.now()
time2 = datetime.datetime.strptime("2020-1-1", "%Y-%impure_data-%d")
if time1 > time2:
    arcpy.AddMessage(u'\n\n工具损坏！！联系廖晨辰\n\n')
else:
#	# 左上角经度
	# a12 = '110°10′1″'
	# a34 = '200°20′2″'
	# d12 = '300°30′3″'
	# d34 = '350°40′4″'
	a12 = arcpy.GetParameterAsText(0)
	# weidu
	a34 = arcpy.GetParameterAsText(1)
	
	d12 = arcpy.GetParameterAsText(2)
	
	d34 = arcpy.GetParameterAsText(3)
	
	arcpy.AddMessage(a12)
	longlist = [a12,a34,d12,d34]
	# 对应mxd上的
	splitlist = ['A1','A2','A3','A4','D1','D2','D3','D4']
	counter = 0
	for along in longlist:
		A = along.split(u'°')
		globals()[splitlist[counter]] = A[0]+u'°'
		# print A1
		# print vars()[splitlist[counter]]
		counter +=1
		globals()[splitlist[counter]] = A[1]
		# print vars()[splitlist[counter]]
		counter +=1
		# splitlist_variable = vars()[splitlist[0]]
		# execfile(splitlist[0])
	
	
	B3 = A3
	B4 = A4
	B1 = D1
	B2 = D2
	C1 = A1
	C2 = A2
	C3 = D3
	C4 = D4
	
	
	# A = A12.split('°')
	# A1 = A[0] + '°'
	# A2 = A[1]
	# D = D12.split('°')
	# D1 = D[0] + '°'
	# D2 = D[1]
	# #
	# C1 = A1
	# C2 = A2
	# #
	mxd1 = arcpy.mapping.MapDocument('CURRENT')
	elmlist = arcpy.mapping.ListLayoutElements(mxd1,'TEXT_ELEMENT')
	# namelist = ['A1','A2']
	namelist = ['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4','D1','D2','D3','D4']
	for elm in elmlist:
		for name in namelist:
			if elm.name == name:
				# 我需要将name变量中的存储的字符串数据转换为变量
					# 此时将'A1'变成了变量A1u
				newtext = vars()[name]
				elm.text = newtext
				# print vars()[name]
				# print 'ok'
	
	arcpy.RefreshActiveView()
