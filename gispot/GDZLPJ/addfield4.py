# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              addfield1
# Author:            Hygnic
# Created on:        2021/6/9 10:41
# Version:           
# Reference:         土壤类型代码表
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
    # add_field(layer1,
    #           [ u"实体长度",],
    #           "DOUBLE", delete=False)

    # add_field(layer1,
    #           [u"内部标识码"],"LONG", delete=False)
    
    add_field(layer1,[u"县土类",u"县亚类",u"县土属",u"县土种",
                      u"县土类名称",u"县亚类名称",u"县土壤代码",u"县土属名称",
                      u"县土种名称",u"省土壤代码",u"省土壤名称",u"县土壤名称",],
              "TEXT", delete=False)

    with arcpy.da.UpdateCursor(layer1,
                               [u"县土类",u"县亚类",u"县土属",u"县土种",
                                u"县土类名称",u"县亚类名称",u"县土壤代码",u"县土属名称",
                                u"县土种名称",u"省土壤代码",u"省土壤名称",u"县土壤名称",
                                u"土类",u"亚类",u"土属",u"土种"]) as cursor:
        for row in cursor:
            tulei = row[-4] # 土类
            yalei = row[-3] # 亚类
            tushu = row[-2] # 土属
            tuzhong = row[-1] # 土种
            row[0] = tulei
            row[1] = yalei
            row[2] = tushu
            row[3] = tuzhong
            
            row[4] = tulei
            row[5] = yalei
            # row[6] = tushu # 县土壤代码
            row[7] = tushu
            row[8] = tuzhong
            # row[9] = tulei # 省土壤代码
            row[10] = tuzhong
            row[11] = tuzhong
            
            
            cursor.updateRow(row)


if __name__ == '__main__':
    mxd = arcpy.mapping.MapDocument("CURRENT")
    # lyr = arcpy.mapping.ListLayers(mxd, wildcard=u"耕层土壤有机质等值线图")[0]
    lyr = arcpy.mapping.ListLayers(mxd)[0]
    arcpy.AddMessage("ok-0")
    # para = arcpy.GetParameterAsText(0)
    arcpy.AddMessage("ok0")
    add_func(lyr)