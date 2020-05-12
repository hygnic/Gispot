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

__getall_items = []
def recur_search(dirs_p, suffix=None, size_limit=None, matchword=None):		# 002
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	recur 使用递归，特别注意，层数不要太多
	:param size_limit: 文件大小限制 字节
	:param dirs_p: dir address
	:param suffix: 后缀
	:param matchword: 匹配字段，简单筛选出符合匹配字段的项目
	:return: list
	"""
	print "begin"
	global __getall_items
	matchword=str(matchword)
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			print "this is dir"
			# 递归
			recur_search(file_path, suffix,size_limit, matchword)
		else:
			# stage 1
			# arcpy.AddMessage(4)
			if matchword: # 保证不使用matchword匹配字段时也能正常运行
				# arcpy.AddMessage(6)
				# if file_p[-3:].lower() == suffix and matchword in file_p and os.path.getsize(file_path)!=100:
				if file_p[-3:].lower() == suffix and matchword in file_p:
					# 使用了文件大小限制且不符合大小要求
					if size_limit and os.path.getsize(file_path)!=size_limit:
						print type(matchword)
						print matchword
						__getall_items.append(file_path)
					# 没有使用大小限制
					elif not size_limit:
						__getall_items.append(file_path)
					# 使用了大小限制，符合大小要求
					else:
						print "2"
						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
						# arcpy.AddMessage("空项目/未添加项：")
						# arcpy.AddMessage(os.path.splitext(os.path.basename(file_path))[0])
			else:
				# arcpy.AddMessage(9)
				if file_p[-3:].lower() == suffix:
					# 使用了文件大小限制且不符合大小要求
					if size_limit and os.path.getsize(file_path) != size_limit:
						print type(matchword)
						print matchword
						__getall_items.append(file_path)
					# 没有使用大小限制
					elif not size_limit:
						__getall_items.append(file_path)
					# 使用了大小限制，符合大小要求
					else:
						print "3"
						# 得在开头添加 cp936才行，不让arctoolbox报错EOL error
						# arcpy.AddMessage("空项目/未添加项：")
						# arcpy.AddMessage(
						# 	os.path.splitext(os.path.basename(file_path))[0])
					# print type(matchword)
					# print matchword
					# __getall_items.append(file_path)
	return __getall_items

ss = recur_search(ur"G:\高标准农田\复核\乐山市","xlsx")
print ss