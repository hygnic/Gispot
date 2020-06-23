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

class A(object):
	name = 'python'
	@staticmethod
	def func():
		return 'A()类的方法func()'



print hasattr(A, 'func')
aa = A()
ss = getattr(A, 'func')
print ss()