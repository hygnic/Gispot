# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              ChangeField
# Author:            Hygnic
# Created on:        2021/4/23 14:27
# Version:           
# Reference:         
"""
Description:         调用 ArcPy 修改矢量文件的字段;
                    1.获取旧字段的属性：长度、精度、字段类型
                    2.创建新字段，使用就字段的属性
                    3.将旧字段的属性赋予新字段
Usage:               
"""
# -------------------------------------------
from __future__ import absolute_import
from __future__ import unicode_literals
import arcpy


class ChangeField(object):
    
    def __init__(self, lyr, field, new_field):
        self.lyr = lyr
        self.f = field
        self.new_f = new_field
        
        
        self.get_old_attr()
        self.change()
        
    def get_old_attr(self):
        # desc = arcpy.Describe()
        fields = arcpy.ListFields(self.lyr)
        for field in fields:
            print field.name
            if field.name == self.f:
                f_type = field.type
                f_precision = field.precision
                f_length = field.length
                f_scale = field.scale
                break
                
            # else:
            #     raise RuntimeError("Old field is not exist")
        self.para=(f_type, f_precision, f_scale, f_length)
        
        
    def change(self):
        para = self.para
        arcpy.AddField_management(self.lyr, self.new_f, *para)
        expression = "!{}!".format(self.f)
        arcpy.CalculateField_management(
            self.lyr, self.new_f, expression, "PYTHON_9.3"
        )
        
        
if __name__ == '__main__':
    # toolbox
    argv = tuple(arcpy.GetParameterAsText(i)
             for i in range(arcpy.GetArgumentCount()))
    ChangeField(*argv)
    
    # script
    # arcpy.env.workspace = ur"D:\共享文件夹"
    # layer = u"表1耕地质量变更调查表_XY数据点图.shp"
    # old_f = u"固定编号"
    # new_f = "texte111"
    # ChangeField(layer, old_f, new_f)
    
    
    