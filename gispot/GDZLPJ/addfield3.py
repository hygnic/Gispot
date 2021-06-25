# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              addfield1
# Author:            Hygnic
# Created on:        2021/6/9 10:41
# Version:           
# Reference:         仅仅添加字段，不做计算
"""
Description:         
Usage:               
"""
# -------------------------------------------
import arcpy


def add_field(layer, names, f_type, f_length=None, delete=True):

    the_fields = arcpy.ListFields(layer)
    for name in names:
        if not check_field_exit(the_fields, name):
            arcpy.AddField_management(layer, name, f_type, field_length=f_length)
            msg = "Created {0} field success".format(name.encode("utf8"))
            print msg
        else:
            if delete:
                arcpy.DeleteField_management (layer, name)
                arcpy.AddField_management(layer, name, f_type, field_length=f_length)
            else:
                print "Field exist"
    
    return layer

def check_field_exit(field_obj, check_field):
    """
    检查图层是否存在该字段
    :param field_obj: field_obj = arcpy.ListFields(layer)
    :param check_field: field
    :return: {Bolean}
    """
    field_names = [i.name for i in field_obj] # field.aliasName
    return check_field in field_names


def add_func(layer1):
    add_field(layer1,
              [ u"实体长度",],
              "DOUBLE", delete=False)

    add_field(layer1,
              [u"内部标识码"],"LONG", delete=False)
    
    add_field(layer1,[u"实体类型",],
              "TEXT", delete=False)

    with arcpy.da.UpdateCursor(layer1,
                               [ u"实体长度", u"内部标识码",
                                "OID@", "SHAPE@LENGTH"]) as cursor:
        for row in cursor:
            row[0] = row[-1]
            row[1] = row[-2]
            cursor.updateRow(row)


if __name__ == '__main__':
    mxd = arcpy.mapping.MapDocument("CURRENT")
    # lyr = arcpy.mapping.ListLayers(mxd, wildcard=u"耕层土壤有机质等值线图")[0]
    lyr = arcpy.mapping.ListLayers(mxd)[4]
    arcpy.AddMessage("ok-0")
    # para = arcpy.GetParameterAsText(0)
    arcpy.AddMessage("ok0")
    add_func(lyr)