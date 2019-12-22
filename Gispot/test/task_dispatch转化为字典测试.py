# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/21
import sys, time, re
raw_list = [
	u'1',
	u'2',
	u'\u5c0f\u660e\n*510,242,333*\n'
	u'\u5c0f\u7ea2\n*43,67,09*\n'
	u'\u5c0f\u5f20\n*987,178,990*\n\n'
]
raw_data = raw_list[2]
impure_data = raw_data.split("\n")
# remove blank values ""
pure_data = [i for i in impure_data if i != '']
group_len = len(pure_data)
if group_len%2 != 0:
	print u"分组异常"
	time.sleep(5)
	sys.exit()
	
group_keys = []
group_valus = []
conter = 0
# flag = True
while pure_data:
	_v = pure_data.pop(0)
	# 偶数，key
	if conter % 2 == 0:
		group_keys.append(_v)
	else:
		group_valus.append(_v)
	conter +=1
	print conter
	# if conter == group_len:
	# 	flag = False
for ii in group_valus:
	
	valus = re.findall("\d+",ii)
	print valus
	
s = dict
print "impure_data: ",impure_data
print "pure_data: ",pure_data
print "group_keys: ",group_keys
print "group_valus: ",group_valus