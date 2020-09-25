#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/25 17:36
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import re

sample = "mean,9078780990,df23,meanmeans"
result = re.findall("mean",sample)
print(result)
