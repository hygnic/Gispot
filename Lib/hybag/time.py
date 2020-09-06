#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/3 23:57
# Reference:
"""
Description: 时间模块
目前含有以下功能
	1.时间计算装饰函数
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import print_function
# 由于存在Python自带的标准time模块，所以需要使用绝对导入
from __future__ import absolute_import
import time

# 装饰函数 计算程序运行时间
def timewrap(func):
	def inner():
		start = time.time()
		func()
		end = time.time()
		print('Time consuming: ',end - start)
	return inner

# 装饰函数 计算CPU执行时间
def timewrap_cpu(func):
	def inner():
		start = time.clock()
		func()
		end = time.clock()
		print('CPU time consuming: ',end - start)
	return inner
