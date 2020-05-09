#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/27 15:08
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
def points_genarator(txt_file):
	"""
	points_genarator(txt_file)   return list

	txt_file 文本文件地址
	将txt转换为可以使用的点集列表
	"""
	fffs = open(txt_file, "r")
	input_data = fffs.readlines()
	# input_data.remove("\n")
	# 去除换行符
	# input_data = [x.strip() for x in input_data]
	# input_data = input_data[2:]  # 去除前13行
	input_data = [x.strip() for x in input_data if "@" not in x]  # 去除带@的行
	while True:
		if input_data[0][:2] != "J1":
			del input_data[0]
		else:
			break
	return input_data

path  = ur"G:\高标准分布图\乐山市市中区\自然资源局拐点坐标\自然资源局捌点坐标\坐标\九龙乡新建村.txt"
sss = points_genarator(path)
print sss