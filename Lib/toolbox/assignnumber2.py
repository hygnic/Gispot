# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              assinnumber
# Author:            Hygnic
# Created on:        2021/10/20 15:18
# Version:           
# Reference:         
"""
Description:         用于要素编号
相同的字段使用同一个号码，不同的升序排列，跳过空行；号码从1开始
Usage:
"""
# -------------------------------------------
import arcpy
import random

def assign_number(input_feature, field, start_number, new_field):
    # field_name = u"标号{}".format(random.randint())

    # start_number = "（1）"
    
    # 新建字段
    arcpy.AddField_management(input_feature, new_field, "TEXT")
    cursor = arcpy.da.SearchCursor(input_feature, [field])
    list11 = set(list(cursor))
    for i in list11:
        
        arcpy.AddMessage(i[0])
    # with arcpy.da.UpdateCursor(input_feature, [field]) as cursor:
    #     for row in cursor:
    #     list11 = set(cursor)
    #     arcpy.AddMessage(list11)


if __name__ == '__main__':
    arcpy.env.overwriteOutput = True
    argv = tuple(arcpy.GetParameterAsText(i)
             for i in range(arcpy.GetArgumentCount()))

    assign_number(*argv)
