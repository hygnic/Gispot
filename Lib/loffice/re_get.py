#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/12 15:44
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os


def recur_search(dirs_p,suffix, recur=True,counter =0):		# 002
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	ss = recur_search(ur"G:\高标准","",True)
	ss = recur_search(ur"G:\高标准","xlsx",True)
	ss = recur_search(ur"G:\高标准",["xlsx","xls"],True)
	
	recur 使用递归，特别注意，层数不要太多
	:param recur: bool 是否启用递归
	:param dirs_p: dir address
	:param suffix: 后缀 str或者列表
	:param counter: 计数 用于缩进\t
	:return: list
	
	"""
	__getall_items = []
	# global __getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			print "\t"*counter+"dir:",file_p
			# 递归
			if recur:
				recur_search(file_path,suffix,recur,counter+1)
		else:
			# print "\t"*counter+file_p
			if suffix:
				# 单个后缀
				if not isinstance(suffix,list):
					# stage 1 筛选后缀
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name =name_and_suffix[0]
					if f_suffix == suffix:
						print "\t" * counter, base_name
						__getall_items.append(file_path)
				# 多个后缀组成列表
				else:
					base_name = os.path.basename(file_path)
					name_and_suffix = os.path.splitext(base_name)
					f_suffix = name_and_suffix[1][1:]
					f_name = name_and_suffix[0]
					if f_suffix in suffix:
						print "\t" * counter, base_name
						__getall_items.append(file_path)
			# 无后缀要求，获取所有文件
			else:
				__getall_items.append(file_path)
				
	return __getall_items

def filter_list(raw_list,matchword, size_limit =None):
	"""
	使用字符匹配和文件大小（如果列表元素是地址的话）对列表中进行筛选
	import os
	oo = filter_list(ss,u"评估")
	oo = filter_list(ss,u"评估",100)
	:param raw_list:
	:param size_limit: int 排除等于该大小的文件 计量单位 字节
	:param matchword: 匹配字段，筛选符合该条件的元素
	:return: list
	"""
	_bridge_list=[]
	if matchword:
		for a_raw in raw_list:
			if matchword in os.path.basename(a_raw):
				_bridge_list.append(a_raw)
		raw_list = _bridge_list
	if size_limit:
		_bridge_list=[]
		_bridge_list = [x for x in raw_list if os.path.getsize(x)!=size_limit]
	return _bridge_list

	
# match_word=12
# match_word="12"
match_word=u"附件"
# match_word= str(match_word)
ss = recur_search(ur"G:\高标准农田\复核\乐山市","",True)
# print filter_list.__name__
for s in ss:
	print "ii",s # G:\高标准农田\复核\乐山市\附件：“十二五”以来高标准农田建设评估复核统计表（夹江）(1).xlsx

oo = filter_list(ss,match_word)
for o in oo:
	print "oo:",o