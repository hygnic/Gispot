#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/15 10:38
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
test_list = [1,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,34,3,67,8,98,39,98,]
a_group = []


def sub_list(father,son,son_len):
	"""选择
	:param father: {List} 父列表，我们的主要列表
	:param son: {List} 一个子列表，父列表的一个切片
	:param son_len: {Int} 切片长度，使用pop方法
	:return: {List} son 返回一个子列表
	"""
	# g_father = father
	# global g_father
	son=[]
	for ii7 in xrange(son_len):
		son.append(father.pop(0))
	# print "son:",son
	return son
for i in xrange(3):
	ss = sub_list(test_list,a_group,6)
	print ss