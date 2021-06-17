# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              addfield1
# Author:            Hygnic
# Created on:        2021/6/9 10:41
# Version:           
# Reference:         农用地地块图添加字段
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
              [u"实体面积", u"实体长度",
               u"地类面积", u"计算面积", u"平差面积",],
              "DOUBLE", delete=False)
    
    add_field(layer1,
              [u"内部标识码"],"LONG", delete=False)

    add_field(layer1,[u"实体类型", u"地类号", u"地类名称"],
              "TEXT", delete=False)

    add_field(layer1,
              [u"报告日期"], "DATE", delete=False)
    
    with arcpy.da.UpdateCursor(layer1,
                               [u"实体面积", u"实体长度",
                                u"地类面积", u"计算面积", u"平差面积",
                                "SHAPE@AREA", "SHAPE@LENGTH"]) as cursor:
        for row in cursor:
            row[0] = row[-2]
            row[2] = row[-2]
            row[3] = row[-2]
            row[4] = row[-2]
            row[1] = row[-1]
            cursor.updateRow(row)


if __name__ == '__main__':
    mxd = arcpy.mapping.MapDocument("CURRENT")
    lyr = arcpy.mapping.ListLayers(mxd, wildcard=u"农用地地块图")[0]
    arcpy.AddMessage("ok-0")
    # para = arcpy.GetParameterAsText(0)
    arcpy.AddMessage("ok0")
    add_func(lyr)