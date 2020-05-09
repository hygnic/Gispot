#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/28 15:57
# Reference:
"""
Description: py2exe 脚本设置文件
Usage:
"""
# ---------------------------------------------------------------------------
from distutils.core import setup
import py2exe
options = {"py2exe": {"excludes": ["arcpy"]}}
setup(console=["Gispot.py"], options=options)