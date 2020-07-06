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
from collections import OrderedDict


def func1():
	# name: 坐标系转换
	print "func1"


def func2():
	# name: Excel转shp
	print "func2"


def func3():
	# name: 坐标系转换
	print "func1"


def func4():
	# name: Excel转shp
	print "func2"


func_name = {
	u"顺序":(
		u"转换工具",u"高标准农田"
	),
	u"转换工具": (
		(func1, u"坐标系转换"),
		(func2, u"Excel转shp")
	),
	u"高标准农田": (
		(func3, u"坐标系转换2"),
		(func4, u"Excel转shp2")
	)
}

real_list = (u"转换工具",u"高标准农田")
for i in real_list:
	print func_name[i]
print "--------------"

dictorder = func_name[u"顺序"]
for i in dictorder:
	print func_name[i]
print "---------------"

print func_name.pop(u"顺序")
print func_name
