#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/5 13:38
# Reference:
"""
Description: 快速添加标志牌shp,设置定义查询
Usage:
"""
# ---------------------------------------------------------------------------



def label(layer,expression):
	"""显示且更改图层的标注
	 layer{Layer}:
	图层对象
	 expression{String}:
	标注表达式:
	红色18号字体 "\"<CLR red=\'255\'><FNT size = \'18\'>\" + [BZPBH] + \"</FNT></CLR>\""
	return longName
		"""
	if layer.supports("LABELCLASSES"):
		layer.showLabels = True
		for lblClass in layer.labelClasses:
			lblClass.expression = expression
			# print "Class Name:  " + lblClass.className
			# print "Expression:  " + lblClass.expression
			# print "SQL Query:   " + lblClass.SQLQuery
	else:
		print "Layer not support LabelClasses"
	return layer.longName

