#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/21 15:18
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import cmath
import math
import sys


def get_float(msg, allow_zero):
	x = None
	while x is None:
		try:
			x = float(raw_input(msg))
			if not allow_zero and abs(x) < sys.float_info.epsilon:
			# 在python中float是双精度，精度不够，在比较时容易出错，所以需要用函数sys.float_info.epsilon
			# sys.float_info.epsilon代表无限接近 0，是机器可以区分出的两个浮点数的最小区别
				print(u'不允许为0')
				x = None
		except ValueError as err:
			print(err)
	return x

def main():
	a = get_float('enter a: ',False)
	b = get_float('enter b: ',True)
	c = get_float('enter c: ',True)
	
	x1 = None
	x2 = None
	discriminant = (b**2)-(4*a*c)
	if discriminant == 0:
		x1 = -(b/(2*a))
	else:
		if discriminant >0:
			root = math.sqrt(discriminant)
		else:
			root = cmath.sqrt(discriminant)
		x1 = (-b+root)/(2*a)
		x2 = (-b-root)/(2*a)
	equation = ("{0}x+{1}x+{2}=0"
				"  x={3}").format(a,b,c,x1)
	# \N{RIGHTWARDS ARROW} 代表显示一个箭头标识(→)
	# \N{SUPERSCRIPT TWO}
	
	if x2 is not None:
		equation +=' or x={0}'.format(x2)
	print(equation)
	
main()
# print "{:.2f}".format(3.1415926)