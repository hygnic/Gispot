#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/5 23:34
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# from __future__ import print_function
from __future__ import absolute_import
import sys

savedStdout = sys.stdout  # 保存标准输出流
file=open('out.txt', 'w+')
sys.stdout = file  # 标准输出重定向至文件
print 'This message is for file!'


# sys.stdout = savedStdout  # 恢复标准输出流
print 'This message is for screen!'

file.close()