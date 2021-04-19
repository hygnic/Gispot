# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              gdzldj
# Author:            Hygnic
# Created on:        2021/4/19 14:27
# Version:           ArcGIS 10.3 python2.7
# Reference:         
"""
Description:         迭代处理 以表格显示分区统计 会遗漏部分区域的问题
Usage:               
"""
# -------------------------------------------
import arcpy
from hybag import ezarcpy
from arcpy.sa import KrigingModelOrdinary as KModel
from arcpy.sa import Kriging
from arcpy.sa import ZonalStatisticsAsTable as ZonalTable

arcpy.env.workspace = ezarcpy.InitPath()[1]
arcpy.env.overwriteOutput = True

class GDZLDC(object):
    def __init__(self, point, unit, aoi):
        self.pt = point # 点
        self.unit = unit # 管理单元
        self.aoi = aoi # 范围
        
        # 设置栅格范围和掩膜
        arcpy.env.extent = self.aoi
        arcpy.env.mask = self.aoi
        

    def zonalStatisticsAsTable(self, index):
        """
        
        :param index: {Str} 参数 有机质 有效磷
        :return:
        """
        #______output kriging raster_____
        k_model = KModel("SPHERICAL")
        kriging = Kriging(self.pt, index, k_model, 30)
        kriging_name = "kriging_" + index
        kriging.save(kriging_name)
        print "Output FeatureClass:", kriging_name
        '''
        SPHERICAL
        c0    = 552.153
        c     = 51.800
        a     = 260179.453
        sill  = 603.953
        '''
        

        #___zonalStatisticsAsTable___
        # 内部用于连接的唯一标识码
        bsm = "ORIG_FID"
        out_table = ("table_" + index).encode("cp936")
        ZonalTable(self.unit, bsm, kriging, out_table, "DATA", "MEAN")
        print "Output Table:", out_table
        
        #___connect table with lyr___
        f_lyr = "AOIFeatureLayer"
        arcpy.MakeFeatureLayer_management(self.unit, f_lyr)
        # connect
        # 可能会因为表中没有该字段而报错
        arcpy.AddJoin_management(f_lyr, bsm, out_table, bsm)
        # 筛选出空值的要素
        expression = "{}.{} is NULL".format(out_table,"MEAN") # TODO 这里可能报错
        arcpy.SelectLayerByAttribute_management(f_lyr, "NEW_SELECTION", expression)
        # 输出为空值的 AOI
        aoi_null = "aoi_null"
        arcpy.CopyFeatures_management(f_lyr, aoi_null)
        print "Output FeatureClass:", aoi_null
        # 反选，输出有值的 AOI
        arcpy.SelectLayerByAttribute_management(f_lyr, "SWITCH_SELECTION")
        aoi_result = "aoi_result"
        arcpy.CopyFeatures_management(f_lyr, aoi_result)
        print "Output FeatureClass:", aoi_result
        
        # arcpy.Delete_management(out_table)
        # arcpy.Delete_management(kriging)
    

if __name__ == '__main__':
    gdzldj = GDZLDC(ur"D:\共享文件夹\表1耕地质量变更调查表_XY数据点图.shp",
                    ur"D:\共享文件夹\管理单元_二次合并.shp")
    gdzldj.zonalStatisticsAsTable(u"有效土层厚")