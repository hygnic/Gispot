#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/21 14:51
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import division
from hybag import hybasic
import time
import datetime

# start = time.clock()
# time.sleep(3)
# end = time.clock()

# time1=datetime.datetime.now()
# start_time = datetime.datetime.strftime(time1,"%Y-%m-%d-%H:%M:%S")
# time2 = datetime.datetime.strptime("2019-9-1", "%Y-%m-%d")
# delt = (time2-time1) # -408 days, 13:40:14.996000 <type 'datetime.timedelta'>
# print type(delt)
# print delt
# print delt.total_seconds() # -408
#
# delt = (time2-time1).days # -408 , <type 'int'>
# print type(delt)
# print delt
#
# print start_time
#
# print round(60/3600, 4)
hyt = hybasic.HyTime()
t1 = hyt.time_now
time.sleep(2)
t2=hyt.time_now
print t1
print t2[0]-t1[0]
sss=hyt.elapsed_time(t1[0], t2[0])
print sss