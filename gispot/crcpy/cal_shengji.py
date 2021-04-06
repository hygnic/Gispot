#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/3/25 12:08
# Reference:
"""
Description: 统计每个项目（图层）的非耕地面积有多少，并将非耕地分类显示各自面积
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
import arcpy
from hybag import hybasic
from hybag import ezarcpy
from hybag import glwings





def check_name(inputpath, excel_path):
    # 根据输入的文件夹获取初始数据 inputpath:矢量数据文件夹; excel_path:sheet
    # 返回合并图层和完全合并图层以及项目名称集合
    raw_shp = hybasic.filter_file(hybasic.getfiles(inputpath, "shp"), "GBZ")
    merge_layer = "merge"
    arcpy.Merge_management(raw_shp, output=merge_layer)
    with arcpy.da.SearchCursor(merge_layer, "XMMC") as cursor:
        name_set = set([row[0] for row in cursor])
        cursor.reset()

    # 获取excel表中的项目名称
    with glwings.open_xlwings(excel_path) as f:
        rows_count = f.api.UsedRange.Rows.count
        name_sheet = f.range("C4:C"+str(rows_count-1)).value
        
    if set(name_set)==set(name_sheet):
        # 当矢量文件名字和excel中名字对的上时才继续。
        return merge_layer, name_sheet
    else:
        raise RuntimeError(u"项目名称不匹配".encode("cp936"))


def data_init(inputpath):
    # 根据输入的文件夹获取初始数据 inputpath:矢量数据文件夹; excel_path:sheet
    # 返回合并图层和完全合并图层以及项目名称集合
    raw_shp = hybasic.filter_file(hybasic.getfiles(inputpath, "shp"), "GBZ")
    return raw_shp


def fill_excel(excel_path):
    with glwings.open_xlwings(excel_path) as f:
        rows_count = f.api.UsedRange.Rows.count
        name_sheet = f.range("C4:C"+str(rows_count-1)).value
    return name_sheet


def cal_other(lyr):
    """
    计算lyr中非耕地的其他几种地物的面积
    :param lyr:
    :return:
    """
    get_value=[]
    names = [_.name for _ in arcpy.ListFields(lyr)]
    if u"地类编码" in names:
        name = u"地类编码"
    else:
        name = "DLBM_1" # 大小写是否有影响？
    print "DLTB_NAME:", name
    print u"标识完成"
    
    gd_area = 0 # 耕地面积
    zzyd_area = 0 # 种植用地面积
    ld_area = 0 # 林地面积
    cd_area = 0 # 草地面积
    qt_area = 0 # 其它面积
    jsyd_area =  0 # 建设面积
    
    with arcpy.da.SearchCursor(lyr, [name, "SHAPE@AREA"]) as cursor:
        cursor.reset()
        for row in cursor:
            dlbm = row[0]
            area = row[-1]
            if dlbm in ("011", "012", "013"):
                gd_area += area
            elif dlbm.startswith("02"): # 种植用地面积
                zzyd_area += area
            elif dlbm.startswith("03"): # 林地面积
                ld_area += area
            elif dlbm.startswith("04"): # 草地面积
                cd_area += area
            elif dlbm in ("121", "122", "123", "124", "125", "126", "127"): # 其它面积
                qt_area += area
            else:
                jsyd_area += area
        cursor.reset()
        
    get_value.append(round((zzyd_area+ld_area+cd_area+qt_area+jsyd_area)*0.0015, 4)) # 获取非耕地面积
    get_value.append(round(ld_area*0.0015,4)) # 林地
    get_value.append(round(cd_area*0.0015, 4)) # 草地
    get_value.append(round(zzyd_area*0.0015, 4)) # 种植用地面积
    get_value.append(round(jsyd_area*0.0015,4)) # 建设用地
    get_value.append(round(qt_area*0.0015, 4)) # 其它用地

    for i in get_value:
        print i

    return get_value
    


    
    
if __name__ == '__main__':
    arcpy.env.overwriteOutput =True
    scratch_path, scratch_gdb = ezarcpy.InitPath()
    arcpy.env.workspace = scratch_gdb
    
    # dltb = "path"
    # shps = data_init(ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\入库成果数据\510000高标准农田建设上图入库数据20201227")
    # identity_dltb = "identity_dltb"
    # for a_shp in shps:
    #     arcpy.Identity_analysis(
    #         in_features=a_shp, identity_features=dltb, out_feature_class=identity_dltb)
    #     cal_other(identity_dltb)
    #
    # for a_shp in fill_excel(ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\高标评估项目清单详细分解表.xlsx"):
    
    
    # 东坡区
    # path_shapefile = ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\入库成果数据\510000高标准农田建设上图入库数据20201227"
    # path_sheet =  ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\高标评估项目清单详细分解表.xlsx"
    # dltb = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511402东坡区\底图数据\DLTB5114022018.shp"

    # 彭山区
    path_shapefile = ur"D:\文档\高标准农田\第三次最终\眉山市\511403彭山区\入库成果数据\510000高标准农田建设上图入库数据20201222"
    path_sheet =  ur"D:\文档\高标准农田\第三次最终\眉山市\511403彭山区\高标评估项目清单详细分解表彭山.xlsx"
    dltb = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511403彭山县\底图数据\DLTB5114002018.shp"
    
    # 测试用地址
    # path_shapefile = ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\入库成果数据\510000高标准农田建设上图入库数据20201227"
    # path_sheet =  ur"D:\文档\高标准农田\第三次最终\眉山市\511402东坡区\test.xlsx" # 测试用
    
    
    merge, nams = check_name(path_shapefile, path_sheet)
    sba = arcpy.SelectLayerByAttribute_management
    identity_dltb = "identity_dltb"
    
    count_flag=3
    with glwings.open_xlwings(path_sheet) as f:
        for a_shp in nams:
            print a_shp
            count_flag +=1
            print "XMMC = '{}'".format(a_shp.encode("utf8"))
            arcpy.MakeFeatureLayer_management(merge, "merge_layer")
            # sba("merge_layer", "NEW_SELECTION", "XMMC = '{}'".format(a_shp.encode("utf8")))
            sba("merge_layer", "NEW_SELECTION", "XMMC = '{}'".format(a_shp.encode("utf8")))
            arcpy.CopyFeatures_management("merge_layer", "merge_layer12312")
            arcpy.Identity_analysis("merge_layer12312", dltb, identity_dltb)
            # arcpy.Identity_analysis("merge_layer", dltb, identity_dltb)
            print 'OK'
            area_value = cal_other(identity_dltb)
            f.range("G{0}:L{0}".format(str(count_flag))).value = area_value
    print "Done"