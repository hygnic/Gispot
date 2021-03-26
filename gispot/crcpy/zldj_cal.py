#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/21 14:31
# Reference:
"""
Description: 第三次高标复核修改计算质量等级 2020 1222
计算耕地各质量等级之间的比例
重叠部分质量等级等于双方中较的那个
Usage:
"""
# ---------------------------------------------------------------------------
import arcpy
from shutil import copyfile
import os
from multiprocessing import Process
from hybag import ezarcpy
from hybag import hybasic
import tooltk
from gpconfig import multication


scratch_path, scratch_gdb = ezarcpy.InitPath()
arcpy.env.workspace = scratch_gdb
arcpy.env.overwriteOutput = True

def cal_shp_area(input_file):
    if arcpy.Exists(input_file):
        _area = 0
        with arcpy.da.SearchCursor(input_file, ["SHAPE@AREA"]) as cursor:
            for roww in cursor:
                _area += roww[0]
        return _area
    else:
        u"待计算的{}图层不存在".format(input_file)

def show_shp_area(input_file):
    if arcpy.Exists(input_file):
        _area = 0
        with arcpy.da.SearchCursor(input_file, ["Shape_Area"]) as cursor:
            for roww in cursor:
                _area += roww[0]
        return _area
    else:
        u"待计算的{}图层不存在".format(input_file)


def zldj_cal(input_path, dltb_path):
    all_shp = hybasic.getfiles(input_path, "shp")
    gbz_shp = hybasic.filter_file(all_shp,"GBZ")
    merge_layer = scratch_gdb + "/merge23"
    arcpy.Merge_management(gbz_shp, output=merge_layer)
    
    # out_feature_class = scratch_gdb + "/dissolve_layer"
    
    with arcpy.da.UpdateCursor(merge_layer, ["ZLDJ"]) as cursor:
        for row in cursor:
            if row[0] == u"需要提质改" or row[0]==u"需要提质":
                row[0]=u"需要提质改造"
                cursor.updateRow(row)
    
    out_feature_class = "dissolve_layer"
    arcpy.Dissolve_management(merge_layer, out_feature_class, "ZLDJ")
    
    
    
    # 按属性选择
    # if arcpy.Exists(scratch_gdb+)
    
    fuhe = "fuhe"
    jibenfuhe = "jibenfuhe"
    xytzgz = "xytzgz"
    
    for _ in [fuhe, jibenfuhe, xytzgz]:
        try:
            arcpy.Delete_management(_)
            print "delete:", _
        except:
            print 1
    
    arcpy.MakeFeatureLayer_management(out_feature_class, "lyr")
    print arcpy.Exists("lyr")
    # 可能部分质量等级没有
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " \"ZLDJ\" = '符合' ")
    # 加了 U 报错
    # arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " 'ZLDJ' = u'符合' ")
    arcpy.CopyFeatures_management("lyr", "fuhe")
    arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " \"ZLDJ\" LIKE '基本符%' ")
    arcpy.CopyFeatures_management("lyr", "jibenfuhe")
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " \"ZLDJ\" LIKE '需要%' ")
    arcpy.CopyFeatures_management("lyr", "xytzgz")
    print u"分离质量等级成功"
    
    
    zldj_layers=[]
    if arcpy.Exists(fuhe):
        zldj_layers.append(fuhe)
    if arcpy.Exists(jibenfuhe):
        zldj_layers.append(jibenfuhe)
    if arcpy.Exists(xytzgz):
        zldj_layers.append(xytzgz)
    
    
    dltb_fields = arcpy.ListFields(dltb_path)
    dltb_field_names = [i.name for i in dltb_fields]
    print dltb_field_names
    if u"地类编码" in dltb_field_names:
        name = u"地类编码"
    
    else:
        name = "DLBM"  # 大小写是否有影响？
    print "DLTB_NAME:", name
    
    dltb = "dltb"
    arcpy.MakeFeatureLayer_management(dltb_path, dltb)
    arcpy.SelectLayerByAttribute_management(dltb, "NEW_SELECTION", name+" LIKE '01%' ")
    for a_shp in zldj_layers:
        new_name = a_shp+"_DLTB"
        arcpy.Identity_analysis(
            in_features=a_shp, identity_features=dltb, out_feature_class=new_name)
        print "a_shp：", a_shp
        arcpy.MakeFeatureLayer_management(new_name, "a_shp_2")
        arcpy.SelectLayerByAttribute_management("a_shp_2", "NEW_SELECTION",
                                                name+" LIKE '01%' ")
        
        arcpy.CopyFeatures_management("a_shp_2", a_shp)
    
    
    layername_area = [] # 将图层名和面积组成的列表放进列表 [["fuhe",3455], ["jibenfuhe", 899.976]]
    for i in zldj_layers:
        area = cal_shp_area(i)
        layername_area.append([i, area])
    
    print layername_area # [['fuhe', 43179889.3465107], ['jibenfuhe', 28166402.1104696], ['xytzgz', 97004089.0362233]]
    
    zldj_area = []
    if arcpy.Exists(xytzgz): # 存在需要提质改造的项目
        area3 = layername_area[-1][1]
        if len(layername_area) > 2: # 存在前两种情况
            erase_jibenfuhe = "layer0"
            erase_fuhe1 = "layer1"
            erase_fuhe2 = "layer1_2"
            area1 = layername_area[0][1]
            area2 = layername_area[1][1]
            # 需要提质改造和基本符合擦除
            arcpy.Erase_analysis(
                in_features=jibenfuhe, erase_features=xytzgz, out_feature_class=erase_jibenfuhe)
            area_jibenfuhe = show_shp_area(erase_jibenfuhe) # 基本符合的面积
            # 与基本符合擦除，保留符合
            arcpy.Erase_analysis(
                in_features=fuhe, erase_features=erase_jibenfuhe, out_feature_class=erase_fuhe1)
            # area_jibenfu_part1 = area1-area_fuhe1
            # 与xytzgz擦除，保留符合
            arcpy.Erase_analysis(
                in_features=erase_fuhe1, erase_features=xytzgz, out_feature_class=erase_fuhe2)
            area_fuhe = show_shp_area(erase_fuhe2)  # 符合的面积
            
            
            # zldj_area = [] # 三种质量等级的列表
            zldj_area.append([u"符合",area_fuhe])
            zldj_area.append([u"基本符合",area_jibenfuhe])
            zldj_area.append([u"需要提质改造",area3])
        elif len(layername_area) == 2:
            # 只有基本符合和提质改造或者符合图层和提质改造
            erase_ = "layer1_4"
            arcpy.Erase_analysis(
                in_features=layername_area[0][0], erase_features=xytzgz, out_feature_class=erase_)
            erase_area = show_shp_area(erase_) # 擦除后的面积就是非 提质改造 图层的真实面积
            xytzgz_area = area3
            zldj_area.append([layername_area[0][0], erase_area])
            zldj_area.append([u"需要提质改造", xytzgz_area])
        elif len(layername_area) == 1:
            # 只存在提质改造
            xytzgz_area = layername_area[0][1]
            zldj_area.append([u"需要提质改造", xytzgz_area])
    else: # 不存在需要提质改造的图层
        if len(layername_area) == 2:
            # 存在符合和基本符合
            erase_fuhe = "layer1_41"
            arcpy.Erase_analysis(
                in_features=fuhe, erase_features=jibenfuhe, out_feature_class=erase_fuhe)
            erase_area_fuhe = show_shp_area(erase_fuhe)  # 擦除后的面积就是非 提质改造 图层的真实面积
            
            zldj_area.append([u"符合", erase_area_fuhe])
            zldj_area.append([u"基本符合", layername_area[1][1]])
        
        else:
            # 只存在 符合 或者 基本符合 一种图层
            zldj_area.append([layername_area[0][0], layername_area[0][1]])
    a=0
    for i in zldj_area:
        name, area = i
        print name, area*0.0015
        a+=area*0.0015
    print a
    
    zldj_area = [round(_[1]*0.0015, 4) for _ in zldj_area]
    
    print "____________________________________________________________________"
    print "____________________________________________________________________"
    print "____________________________________________________________________"
    for i in zldj_area:
        print i
    
    return zldj_area

def write_excel(inputs, fill_value, range_cell):
    import xlwings as xw
    try:
        print "\n"
        app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
        app1.display_alerts = False  # 关闭Excel的提示和警告信息
        app1.screen_updating = False  # 不更新屏幕显示
        # app1.screen_updating = True
        
        
        # 打开清理统计表
        wb1 = app1.books.open(inputs)
        ws1 = wb1.sheets[0]
        # v1 = sheet1.range("a1:a7").value
        # v1 = sheet1.range("d1:d300").expand().value #TODO 不清楚expand的作用
        wbs1_rowcount = ws1.api.UsedRange.Rows.count
        
        value = ws1.range("K7:M7").value
        gross_area, dup_area, non_gd = value
        gd_area = gross_area - dup_area - non_gd
        # print gd_area
        """_______________________________________"""
        # ws1.range("T7:T7").value = gd_area
        # v1, v2, v3 = fill_value
        # v3 = gd_area- v1-v2
        # fill_value = [v1, v2, v3]
        """_______________________________________"""
        
        targe_cells = ws1.range(range_cell)
        targe_cells.value = fill_value
        
        
        wb1.save()
    finally:
        app1.quit()
        print "\n close application"




def run_function(qq, para1, para2, para3):
    """
    :param qq:
    :param para1:
    :param para2:
    :param para3:
    :return:
    """
    result = zldj_cal(para1, dltb_path=para2)
    write_excel(para3, result, "U7:Z7")

class ZLDJCalGui(tooltk.Tooltk):
    commu = multication.MuCation()
    
    def __init__(self, master1):
        super(ZLDJCalGui, self).__init__(master1,
                                         "zldj_cal.gc",
                                         self.confirm)
        self.name = u"计算耕地质量等级"
        frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
        # block1
        self.block1 = tooltk.blockDIR_in(frame, u"数据文件地址")
        self.block2 = tooltk.blockShp_in(frame, u"DLTB图层")
        self.block3 = tooltk.blockSheet(frame, u"复核表")
    
    def confirm(self):
        folder, shp, sheet = [self.block1.get(), self.block2.get(),
                              self.block3.get()]
        p = Process(target=self.commu.decor,
                    args=(run_function, folder, shp, sheet)
                    )
        # p.deamon = True
        p.start()
        # 将信息输出到右下方的动态信息栏
        self.commu.process_communication(self.major_msgframe)


if __name__ == '__main__':
    """———————————————————————————————para———————————————————————————————————————"""
    """———————————————————————————————para———————————————————————————————————————"""
    # folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
    # 测试路径
    # folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\test"
    # folder_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
    folder_path = ur"F:\511403彭山区\成果1\入库成果数据\510000高标准农田建设上图入库数据20201220"
    # dltb
    path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\底图数据\DLTB5114002018.shp"
    excel_path = ur"G:\第三次高标复核\眉山市\511403彭山区\成果1\附表：“十二五”以来高标准农田建设评估复核修正统计表.xlsx"
    """———————————————————————————————para———————————————————————————————————————"""
    """———————————————————————————————para———————————————————————————————————————"""
    # 可单独使用
    result = zldj_cal(folder_path, dltb_path=path)
    write_excel(excel_path, result, "U7:W7")