#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/5/21 17:55
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------

from win32com.client import Dispatch
xlApp = Dispatch('Excel.Application')
xlApp.DisplayAlerts=False