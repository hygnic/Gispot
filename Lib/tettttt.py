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
	u"转换工具": (1,
		(func1, u"坐标系转换"),
		(func2, u"Excel转shp")
	),
	u"高标准农田": (2,
		(func3, u"坐标系转换2"),
		(func4, u"Excel转shp2")
	)
}

func_name2 = OrderedDict()
func_name2[u"转换工具"] = (
	(func1, u"坐标系转换"),
	(func2, u"Excel转shp")
)
func_name2[u"高标准农田"] = (
	(func3, u"坐标系转换2"),
	(func4, u"Excel转shp2")
)
# func_name2 = (u"转换工具",((func1,u"坐标系转换"),(func2,u"Excel转shp")),u"高标准农田",((func3,u"坐标系转换2"),(func4,u"Excel转shp2")))

dictsort = sorted(func_name,key=func_name.__getitem__,reverse=True)
print dictsort