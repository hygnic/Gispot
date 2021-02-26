#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/29 9:58
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import os
import sys

p1 = os.path.abspath(os.path.dirname(sys.argv[0]))
print p1
p2 = os.path.abspath(os.path.dirname(__file__))
print p2
p3 = os.path.abspath(os.path.dirname(__file__))
print p3
p4 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
p5 = sys.argv[0]
p6 = __file__
print p5
print p6