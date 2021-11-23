# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              export_by_field
# Author:            Hygnic
# Created on:        2021/11/23 16:53
# Version:           
# Reference:         
"""
Description:         从要素类中根据字段名称导出多个要素类
Usage:               
"""
# -------------------------------------------

#<<<<<<<<<<<<<<<IMPORT SETTING>>>>>>>>>>>>>>
import arcpy
import sys
import os

#------------添加环境变量
Script_dir = os.path.dirname(__file__)
Base_dir = os.path.dirname(Script_dir)
Libs_dir = os.path.join(Base_dir, "libs")
sys.path.append(Libs_dir)
#------------

import ezarcpy
#<<<<<<<<<<<<<<<IMPORT SETTING>>>>>>>>>>>>>>


def export_by_filed(layer, field):
    """
    :param layer: 图层对象
    :param field: 字段
    :return:
    """
    field_values = ezarcpy.field_value_shower(layer, field)
    
    
    
    
    
    
    