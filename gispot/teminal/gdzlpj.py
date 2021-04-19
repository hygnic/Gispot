# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              gdzlpj
# Author:            Hygnic
# Created on:        2021/4/19 14:27
# Version:           ArcGIS 10.3 python2.7
# Reference:         
"""
Description:         迭代处理 以表格显示分区统计 会遗漏部分区域的问题
Usage:               
"""
# -------------------------------------------
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import arcpy
from arcpy.sa import KrigingModelOrdinary as KModel
from arcpy.sa import Kriging
from arcpy.sa import ZonalStatisticsAsTable as ZonalTable

from hybag import ezarcpy

arcpy.env.workspace = ezarcpy.InitPath()[1]
arcpy.env.overwriteOutput = True

class GDZLPJ(object):
    
    def __init__(self, point, unit, aoi, field):
        self.pt = point # 点
        self.unit = unit # 管理单元
        self.aoi = aoi # 范围
        self.field = field # 字段 参数 有机质 有效磷
        
        # 设置栅格范围和掩膜
        arcpy.env.extent = self.aoi
        arcpy.env.mask = self.aoi
        
        # function
        self.krigingraster()
        
    
    def krigingraster(self):
        """
        创建克里金栅格
        :return:
        """
        #______output kriging raster_____
        para = self.field
        k_model = KModel("SPHERICAL")
        kriging = Kriging(self.pt, para, k_model, 30)
        kriging_name = "kriging_" + para
        kriging.save(kriging_name)
        print "Output FeatureClass:", kriging_name
        '''
        SPHERICAL
        c0    = 552.153
        c     = 51.800
        a     = 260179.453
        sill  = 603.953
        '''
        self.kriging = kriging_name
        

    def zonalStatisticsAsTable(self, nullunit=None):
        """
        1.使用 以表格显示分区统计（ZonalStatisticsAsTable）工具将
        栅格属性赋予矢量；
        2.然后连接表与矢量；
        3.导出有值的矢量和空值矢量。
        :return:
        """
        
        if nullunit is None:
            nullunit = self.unit
            
        #___zonalStatisticsAsTable___
        # 内部用于连接的唯一标识码
        bsm = "ORIG_FID"
        out_table = "table_" + self.field # table_有效土层厚
        ZonalTable(nullunit, bsm, self.kriging, out_table, "DATA", "MEAN")
        print "Output Table:", out_table
        
        #___connect table with lyr___
        f_lyr = "AOIFeatureLayer"
        arcpy.MakeFeatureLayer_management(nullunit, f_lyr)

        # connect
        # 可能会因为表中没有该字段而报错
        arcpy.JoinField_management() # TODO 重新梳理
        # arcpy.AddJoin_management(f_lyr, bsm, out_table, bsm)
        aoi_lyr = "aoi"
        
        arcpy.CopyFeatures_management(f_lyr, aoi_lyr)
        # 添加字段
        expression0 = "!{}_{}!".format(out_table,"MEAN") # !table_有效土层厚_MEAN!
        print expression0
        # 将连接过来的字段值赋予我们新建字段
        arcpy.CalculateField_management(aoi_lyr, self.field, expression0, "PYTHON_9.3")
        # 筛选出空值的要素
        expression = "{}.{} is NULL".format(out_table,"MEAN") # TODO 这里可能报错
        arcpy.SelectLayerByAttribute_management(f_lyr, "NEW_SELECTION", expression)
        
        # 创建空 AOI 和有值的 AOI 的唯一名称
        aoi_false = arcpy.CreateScratchName(
            "aoi_false", "", "featureclass", arcpy.env.workspace)
        aoi_true = arcpy.CreateScratchName(
            "aoi_true", "", "featureclass", arcpy.env.workspace)
        
        # 输出为空值的 AOI
        arcpy.CopyFeatures_management(f_lyr, aoi_false)
        print "Output FeatureClass:", aoi_false
        # 反选，输出有值的 AOI
        arcpy.SelectLayerByAttribute_management(f_lyr, "SWITCH_SELECTION")
        arcpy.CopyFeatures_management(f_lyr, aoi_true)
        print "Output FeatureClass:", aoi_true

        #___handle filed with two featureclass___


        arcpy.Delete_management("not_exits")
        # arcpy.Delete_management(kriging)
        # ezarcpy.add_field(f_lyr, [self.field], "DOUBLE")
        
        
        return aoi_true, aoi_false
    
    
    def loop_f(self, times):
        """
        loop function
        :param times: {Int} 循环次数
        :return:
        """
        result = []
        # flag = True
        # while flag:
        #     times -= 1
        res, nullaoi = self.zonalStatisticsAsTable()
        result.append(res)
        # arcpy.DeleteField_management(nullaoi, [])
        # nullaoi.
            
            
            # if times == 0:
            #     flag = False
    

if __name__ == '__main__':
    # 公司
    # gdzlpj = GDZLPJ(ur"D:\共享文件夹\表1耕地质量变更调查表_XY数据点图.shp",
    #                 ur"D:\共享文件夹\管理单元_二次合并.shp")
    # gdzlpj.zonalStatisticsAsTable(u"有效土层厚")
    
    # home
    gdb_p = "E:\MyD\耕地质量评价\kriging_test.gdb"
    test_aoi = os.path.join(gdb_p, "AOI")
    test_unit = os.path.join(gdb_p, "test_unit")
    test_point = os.path.join(gdb_p, "test_point")
    
    gdzlpj = GDZLPJ(test_point, test_unit, test_aoi, "有效土层厚")
    gdzlpj.loop_f(3)