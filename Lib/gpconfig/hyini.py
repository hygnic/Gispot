#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/14 23:25
# Reference:
"""
Description: 字符串数据的配置， 颜色配置
Usage:
"""
# ---------------------------------------------------------------------------

"""--------------------------------用于设置常量的类--------------------------"""
# 设置常量 1.常量一旦确定就不可变 2.常量使用大写和 '_'
# class Const(object):
#     class ConstError(TypeError):pass
#     class ConstCaseError(ConstError):pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             if not hasattr(cls, "_instance"):
#                 cls._instance = object.__new__(cls)
#         return cls._instance
#
#     def __setattr__(self, name, value):
#         if self.__dict__.has_key(name):
#             raise self.ConstError, "Can't change const {}".format(name)
#         self.__dict__[name] = value
#         if not name.isupper():
#             raise self.ConstCaseError, 'const name {} is not all uppercase'.format(
#                 name)
# ct = Const()
# ct.CONT = 60
"""--------------------------------用于设置常量的类--------------------------"""

"""--------------------------------GUI--------------------------"""
"""--------------------------------GUI--------------------------"""
width = 1192
height = 650
# GUI中各项功能的主操作块的大小
BUTTON_PIXEL_SIZE = 24
# width = 1600
# height = 800

"""--------------------------------------color-------------------------------"""
"""--------------------------------------color-------------------------------"""
"""--------------------------------------color-------------------------------"""

light_blue = "#5294e2" # 浅蓝色
light_blue2 = "#5599E9" # 浅蓝色 更浅
light_blue3 = "#7DD6FF" # 浅蓝色 更浅
more_light_blue = "#76A8E2" # # 去饱和的蓝色
light_white = "#f5f6f7"  # 浅灰白
white = "#ffffff" # 白色

# SystemWindow
light_system_grey="#f0f0f0"

# 按钮 聚焦状态的颜色
yellow = "#ffc851"
light_yellow = "#FFD67D"
light_yellow2 = "#FFE09E"


"""--------------------------------------GDB-------------------------------"""
"""--------------------------------------GDB-------------------------------"""
"""--------------------------------------GDB-------------------------------"""
WORKSPACE_GDB = "D:\doc\Scratch"
WORKSPACE_GDB2 = "E:\doc\Scratch"

