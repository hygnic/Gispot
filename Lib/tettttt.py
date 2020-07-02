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
def decorator(cls):
	print "6666666"
	return cls


@decorator
class Model(object):
	def __init__(self):
		print "model created"


if __name__ == '__main__':
	model = Model()
