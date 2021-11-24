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
from __future__ import absolute_import
import arcpy
import sys
import os

#------------添加环境变量
Script_dir = os.path.dirname(__file__)
Base_dir = os.path.dirname(Script_dir)
Libs_dir = os.path.join(Base_dir, "libs")
sys.path.append(Libs_dir)
#------------

import ezarcpy2
import hybasic2
#<<<<<<<<<<<<<<<IMPORT SETTING>>>>>>>>>>>>>>

arcpy.env.overwriteOutput= True



def export_by_filed(layer, field, output_featurecalss, folder):
    """
    :param layer: {Strings} 图层对象
    :param field: {Strings} 字段
    :param folder:{Boolean} 是否给每个导出的shp创建文件夹
    :param output_featurecalss: {Strings} 输出文件夹
    :return:
    """
    field_values = ezarcpy2.field_value_shower(layer, field)
    
    featurea_lyr = "featurea_lyr"
    arcpy.MakeFeatureLayer_management(layer, featurea_lyr)
    
    for value in field_values:
        
        # name+" LIKE '01%' "
        where_clause =  field + "=" + "'" + value + "'"
        arcpy.SelectLayerByAttribute_management(featurea_lyr, "NEW_SELECTION", where_clause)
        
        if folder:
            new_folder = os.path.join(output_featurecalss,value)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            out_feature_lyr = os.path.join(new_folder,value+".shp")
            arcpy.CopyFeatures_management(featurea_lyr, out_feature_lyr)
    
        else:
            out_feature_lyr = os.path.join(output_featurecalss,value+".shp")
            arcpy.CopyFeatures_management(featurea_lyr, out_feature_lyr)





if __name__ == '__main__':
    pass
    # lyr_path = ur"E:\中江LQDK\成果数据\柏树乡\Export_Output.shp"
    # in_lyr = arcpy.mapping.Layer(lyr_path)
    # ouput_path = ur"E:\中江LQDK\成果数据\柏树乡"
    #
    #
    # export_by_filed(in_lyr, "CJQYMC", True, ouput_path)