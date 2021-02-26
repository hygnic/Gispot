# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/21
# python2 arcgis10.6
"""
数据烹饪师
	将GUI界面的数据经过二次处理，返回给我们的主要功能模块，如crcpy中的功能
"""



def str2dict(raw_str):
	"""
	将我们从前端图形界面的获得的 杂糅了大量信息的
	列表 转换为一一对应的字典
	:param raw_str: 获得的杂糅数据 字符串
	# :param raw_list:
	:return: 返回字典
	"""
	import sys, time, re
	raw_data = raw_str
	impure_data = raw_data.split("\n")
	# remove blank values ""
	pure_data = [i for i in impure_data if i != '']
	group_len = len(pure_data)
	if group_len%2 != 0:
		print pure_data
		print u"分组异常"
		time.sleep(5)
		sys.exit()
		
	group_keys = []
	pre_group_values = []
	group_values = []
	conter = 0
	# flag = True
	while pure_data:
		_v = pure_data.pop(0)
		# 偶数，key
		if conter % 2 == 0:
			group_keys.append(_v)
		else:
			pre_group_values.append(_v)
		conter +=1
		# print conter
		# if conter == group_len:
		# 	flag = False
	for pre_group_value in pre_group_values:
		g_value = re.findall("\d+", pre_group_value)
		# print g_value
		group_values.append(g_value)
		
	# print "impure_data: ",impure_data
	# print "pure_data: ",pure_data
	# print "group_keys: ",group_keys
	# print "pre_group_values: ",pre_group_values
	# print "group_values: ",group_values
	# 将 group_keys 和 group_values组合成字典
	group_dict = dict(zip(group_keys,group_values))
	# for v in cooked_dict:
	# 	print v
	return group_dict

if __name__ == '__main__':
	got_list = [
		u'1',
		u'2',
		u'\u5c0f\u660e\n*510,242,333*\n'
		u'\u5c0f\u7ea2\n*43,67,09*\n'
		u'\u5c0f\u5f20\n*987,178,990*\n\n'
	]
	got_str = u'\u5c0f\u660e\n*510,242,333*\n\u5c0f\u7ea2\n*43,67,09*\n\u5c0f\u5f20\n*987,178,990*\n'
	a = str2dict(got_str)
	print a
