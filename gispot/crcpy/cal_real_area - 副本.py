#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/2/18 16:28
# Reference:
"""
Description: 第三次高标复核后，以县级为单位，计算实际建设了多少耕地。（剔除重叠和非耕地）
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
import arcpy
import numpy as np
import os

import tooltk
from hybag import hybasic
from hybag import ezarcpy
from hybag import glwings
from multiprocessing import Process
from gpconfig import multication
from gpconfig import gppath



wp, wps = ezarcpy.InitPath()
arcpy.env.overwriteOutput = True
arcpy.env.workspace = wps

temp_dir = os.path.join(gppath.Docs_p, "template")
temp = os.path.join(temp_dir , u"模板.xlsx")
"""______________________________________________________________________"""
"""_________________________________para_________________________________"""
# 新建的两个字段名称
XZQ = "XZQ"
MJM = "MJM"
"""_________________________________para_________________________________"""
"""______________________________________________________________________"""


class RealArea(object):
    
    
    def __init__(self, input_dltb, input_xzq, gbz_f, name, gbz_f1920=0):
        """
        :param input_dltb: dltb
        :param input_xzq: xzq
        :param gbz_f: 高标准农田文件夹
        :param gbz_f1920: 19年20年高标准农田文件夹
        :param name: 县名称，用于输出的表头名
        """
        self.input_dltb = input_dltb
        self.input_xzq = input_xzq
        self.gbz_f = gbz_f
        self.gbz_f1920 = gbz_f1920
        self.name = name
        self.field_confirmed = None  # 存放确定存在于图层中的字段名称的列表
        
        if 0:
            buildarea  = self.gross2net(self.arcpy_query(), self.merge_target_lyr())
            result_lyr = self.geo_process(buildarea)
            self.export(result_lyr)
        else:
            result_lyr = self.geo_process_gross(self.merge_target_lyr())
            self.export(result_lyr)

    
    def arcpy_query(self):
        # 处理DLTB图层，区分出字段是地类编码还是字母的DLBM，然后设置定义查询语句：DLBM like "01%"
        fields_o = arcpy.ListFields(self.input_dltb)
        self.dlbm_name = ezarcpy.field_chooser(u"地类编码", "DLBM", fields_o)
        
        _dltb_lyr = "dltb"
        arcpy.MakeFeatureLayer_management(self.input_dltb, _dltb_lyr)
        arcpy.SelectLayerByAttribute_management(_dltb_lyr, "NEW_SELECTION",
                                                self.dlbm_name + " LIKE '01%' ")
        print "Query success"
        return _dltb_lyr


    def merge_target_lyr(self):
        # 合并所有高标准农田图层，如果输入了1920年的，一并合并
        gbz1 = hybasic.getfiles(self.gbz_f, "shp")
        gbzs = hybasic.HBfilter(gbz1, "GBZ")
        merge_gbzs = "meger_gbzs"
        # 处理19-20年的数据
        if self.gbz_f1920:
            hybasic._getall_items = []  # 清空递归列表
            gbz2 = hybasic.getfiles(gbz_19_20, "shp")
            new_gbz = gbz2 + gbzs
            print len(new_gbz)
            for i in new_gbz:
                print i
            arcpy.Merge_management(new_gbz, merge_gbzs)
        else:
            arcpy.Merge_management(gbzs, merge_gbzs)
        total_merge = ezarcpy.merger_all2(merge_gbzs)  # GBZ完全合并图层
        print "Merge all suceess"
        return merge_gbzs
    
    
    def gross2net(self, gbz_merge_lyr, dltb_query_lyr):
        """
        # 处理完全合并的图层。旨在将毛面积处理成净面积
        :param dltb_query_lyr: 定义查询后的地类图斑数据
        :param gbz_merge_lyr: 所有高标注农田的合并图层
        :return:
        """
        out_feature_class = "erase_left"
        arcpy.Erase_analysis(dltb_query_lyr, gbz_merge_lyr, out_feature_class)
        print "Erase success"
        builded_area = "builded_area"
        arcpy.Erase_analysis(dltb_query_lyr, out_feature_class, builded_area)
        print "Erase success"
        return builded_area
    

    def geo_process(self, builded_areas):
        """
        地理逻辑处理 将建成区域面积标识，挂上行政区信息，然后建立字段等
        :param builded_areas: 建成区域面积
        :return:
        """
        builded_area_id = "builded_area_id"
        arcpy.Identity_analysis(builded_areas, self.input_xzq, builded_area_id)
        print "Identity success"
        fields_o = arcpy.ListFields(builded_area_id)
        f_exist = all([ezarcpy.check_field_exit(fields_o, i) for i in
                       ["XZQDM", "XZQMC", "Shape_Area"]])
        if not f_exist:
            raise RuntimeError("field does not exist")
    
        # 添加字段XZQ，用于存放XZQDM&XZQMC
        ezarcpy.add_field(builded_area_id, [XZQ], "TEXT", 60)
        expression = "[XZQDM] & [XZQMC]"
        arcpy.CalculateField_management(builded_area_id, XZQ, expression, "VB")
        cal_rel_area = "cal_rel_area"
        if self.name:
            cal_rel_area = self.name
        arcpy.Dissolve_management(builded_area_id, cal_rel_area, "XZQ")
        print "Dissolve suceess"
        # 添加字段MJM，用于存放面积亩
        ezarcpy.add_field(cal_rel_area, [MJM], "DOUBLE")
        expression2 = "[Shape_Area] * 0.0015"
        arcpy.CalculateField_management(cal_rel_area, MJM, expression2, "VB")
        print u"output {}.shp".format(self.name)
        return cal_rel_area
    
    
    def geo_process_gross(self, gbz_merge_lyr):
        # 计算每个村的建设的毛面积，不扣除重叠和非耕地
        return self.geo_process(gbz_merge_lyr)
        
        
    
    
    """__________________________export function_____________________________"""
    """______________________________________________________________________"""
    
    # def export_sheet(layer):
    #     # 将 shp文件转换为 sheet 表格
    #     shp_array = arcpy.da.FeatureClassToNumPyArray(layer, [XZQ, MJM])
    #
    #     new_array2 = np.vstack((shp_array[XZQ], shp_array[MJM]))  # 合并
    #     # ref:https://stackoverflow.com/questions/36705724/write-numpy-unicode-array-to-a-text-file
    #     newnw = np.char.encode(new_array2, 'cp936')
    #     np.savetxt("out.csv", newnw.T, fmt="%s", )

    def export(self, layer):
        # 使用xlwings将numpy文件数据导入sheet表中
        shp_array = arcpy.da.FeatureClassToNumPyArray(layer, [XZQ, MJM])
        # r_array = np.arange(0.0,5.0)
        # print list(r_array)
        # list(r_array)
        XZQ_array = shp_array[XZQ]
        MJM_array = shp_array[MJM]
        total_sun = np.sum(MJM_array)
        output_name = u"{}.xlsx".format(self.name)
        output_path = os.path.join(temp_dir, output_name)
        with glwings.open_xlwings(temp,output_path) as f:
            _ = list(XZQ_array)
            len_count = len(_)
            f.range('A1').options(transpose=True).value = self.name
            f.range('A3').options(transpose=True).value = _
            f.range('B3').options(transpose=True).value = list(MJM_array)
            f.range('A' + str(3 + len_count)).options(
                transpose=True).value = u"合计"
            f.range('B' + str(3 + len_count)).options(
                transpose=True).value = total_sun
        print "Export success"

def warper(me_queue, input1, input2, input3, input4, input5):
    RealArea(input1, input2, input3, input4, input5)


class MainGUI(tooltk.Tooltk):
    commu = multication.MuCation()
    
    def __init__(self, master):
        super(MainGUI, self).__init__(master,
                                      "cal_real_area.gc",
                                      self.confirm)
        self.name=u"计算真实面积"
        frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
        # block
        self.block1 = tooltk.blockShp_in(frame, u"DLTB图层")
        self.block2 = tooltk.blockShp_in(frame, u"XZQ图层")
        self.block3 = tooltk.blockDIR_in(frame, u"GBZ文件夹")
        self.block4 = tooltk.blockValue(frame, u"区县名称")
        self.block5 = tooltk.blockDIR_in(frame, u"GBZ文件夹（19-20年）")
 
    def confirm(self):
        p1, p2, p3, p4, p5 = self.block1.get(), self.block2.get(),self.block3.get(),self.block4.get(),self.block5.get()
        if p5 == u"0": # 等于零时表示不添加19-20年的高标准文件
            p = Process(target=self.commu.decor,
                        args=(warper, p1, p2, p3, p4 ,int(p5))
                        )
        else:
            p = Process(target=self.commu.decor,
                        args=(warper, p1, p2, p3, p4 ,p5)
                        )
        p.start()
        # 将信息输出到右下方的动态信息栏
        self.commu.process_communication(self.major_msgframe)
    

if __name__ == '__main__':
   
    # gbz_folder = ur"D:\文档\高标准农田\CPT第三次收件\吴英\510921蓬溪县\入库数据成果\510000高标准农田建设上图入库数据20201219"
    # xzq = ur"D:\文档\高标准农田\CPT第三次收件\吴英\510921蓬溪县\底图数据\XZQ5109212018.shp"
    # dltb_path = ur"D:\文档\高标准农田\CPT第三次收件\吴英\510921蓬溪县\底图数据\DLTB5109212018.shp"

    # 顺庆区
    xzq_name = u"顺庆区"
    gbz_folder = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511302顺庆区\入库成果数据\510000高标准农田建设上图入库数据20201225"
    gbz_19_20 = None
    xzq = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511302顺庆区\底图数据\511302XZQ.shp"
    dltb_path = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511302顺庆区\底图数据\DLTB5113022018.shp"

    # laptop 顺庆区
    # result_name = u"顺庆区"
    # gbz_folder = ur"G:\MoveOn\Gispot\Local\511302顺庆区\入库成果数据\510000高标准农田建设上图入库数据20201225"
    # gbz_19_20 = None
    # xzq = ur"G:\MoveOn\Gispot\Local\511302顺庆区\底图数据\XZQ5113022018.shp"
    # dltb_path = ur"G:\MoveOn\Gispot\Local\511302顺庆区\底图数据\DLTB5113022018.shp"

    # 五通桥
    # result_name = u"五通桥"
    # gbz_folder = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511112五通桥区\入库成果数据\510000高标准农田建设上图入库数据20201224"
    # gbz_19_20 = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511112五通桥区\19-20"
    # xzq = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511112五通桥区\底图数据\XZQ.shp"
    # dltb_path = ur"D:\文档\高标准农田\CPT第三次收件\吴英\511112五通桥区\底图数据\DLTB.shp"

    """_________________________________para_________________________________"""
    """______________________________________________________________________"""
    ra = RealArea(dltb_path, xzq, gbz_folder, xzq_name, gbz_19_20)
    
  

    
    


