# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              OpacityContour
# Author:            Hygnic
# Created on:        2021/5/31 12:46
# Version:           
# Reference:         
"""
Description:         9级缓冲，同一种颜色，不过透明度
                     依次降低
                     已经导入工具箱 <<发光轮廓>>
Usage:               
"""
# -------------------------------------------
import arcpy
import os
import sys
from random import randint


#------------------------------
#------------path--------------
#       在导入的情况下
arcpy.AddMessage("CURRENT: {}".format(os.getcwd()))
# CURRENT: C:\Windows\system32

# 返回工具箱的完整名称
toolbox = os.path.abspath(sys.argv[0])
arcpy.AddMessage(toolbox)

tool_dir = os.path.abspath(os.path.dirname(toolbox))
# lyr
dir_lyr = os.path.join(tool_dir, "lyr") # StyleTool/lyr
# 制图表达相关
representation = os.path.join(tool_dir, "Representation")
rp_gdb = os.path.join(representation, "rep_base.gdb")
#------------path--------------
#------------------------------

#------------------------------
#----------workspace-----------
os.chdir(tool_dir)
gdb = "workspace.gdb"
if not arcpy.Exists(gdb):
    arcpy.CreateFileGDB_management(os.getcwd(), gdb)
arcpy.env.workspace = os.path.abspath(gdb)
work = arcpy.env.workspace
#----------workspace-----------
#------------------------------



class OpacityContour(object):
    
    def __init__(self, in_f, times, lyr):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.df = arcpy.mapping.ListDataFrames(self.mxd)[0]
        
        self.in_f = in_f
        self.times = times
        self.lyr = arcpy.mapping.Layer(lyr)
        
        self.distance = [i*10 for i in xrange(1, 10)]
        
        self.make_buffer_ring()
        self.set_opacity()

    def make_buffer_ring(self):
        num = int(self.times)
        inputfile = self.in_f
        distance = [_*num for _ in self.distance]
        name = arcpy.CreateScratchName("opacitybuffer", data_type="FeatureClass", workspace = work)
        arcpy.MultipleRingBuffer_analysis(inputfile, name, distance, "Meters", Outside_Polygons_Only=True)
        
        # set symbol and add layer to ArcMap
        self.res_lyr = arcpy.mapping.Layer(name)
        # self.res_lyr = arcpy.mapping.Layer(inputfile)
        
        
    def set_opacity(self):
        f_name = "opacity"
        arcpy.AddMessage("12")
        self.add_field(self.res_lyr, [f_name], "SHORT")

        with arcpy.da.UpdateCursor(self.res_lyr, f_name) as cursor:
            arcpy.AddMessage("122")
            in_count = 0
            for row in cursor:
                row[0] = self.distance[in_count]
                in_count += 1
                cursor.updateRow(row)
        arcpy.AddMessage("13")
        arcpy.mapping.UpdateLayer(self.df,  self.res_lyr, self.lyr)
        arcpy.AddMessage("14")
        arcpy.mapping.AddLayer(self.df, self.res_lyr)
        arcpy.AddMessage("15")
        arcpy.AddMessage(self.res_lyr.dataSource)
        
    """--------------------------------"""
    """--------------------------------"""
    """字段添加"""
    def check_field_exit(self, field_obj, check_field):
        """
        检查图层是否存在该字段
        :param field_obj: field_obj = arcpy.ListFields(layer)
        :param check_field: field
        :return: {Bolean}
        """
        field_names = [i.name for i in field_obj] # field.aliasName
        return check_field in field_names
    
    
    def add_field(self, layer, names, f_type, f_length=None, delete=True):
        """添加相同类型和长度的多个或者单个字段，只支持要素图层(如果存在相同名字的字段则不会添加字段)
          <特别注意因为字段类型和长度造成的后续错误>
          such as: add_field(layer_p,["ZWMC1","ZWMC2"],"TEXT",50)
        layer{String}: shp文件对象
          # TODO 按理应该可以使用图层对象，arcpy.mapping.Layer(path)，但是报错（arcgis10.3）
              # 已经解决： 因为arcpy.AddField_management 只支持要素图层，如果是shp文件地址的话
              # 需要使用arcpy.MakeFeatureLayer_management函数将要素类转为要素图层
        names: {List} 新增字段名称
        f_type: {String} 字段类型
        f_length: {Long} 字段长度
        delete: {Boolean} True 如果存在该字段，先删除再创建
        return: 返回当前的图层对象
        """
        the_fields = arcpy.ListFields(layer)
        for name in names:
            if not self.check_field_exit(the_fields, name):
                arcpy.AddField_management(layer, name, f_type, field_length=f_length)
                msg = "Created {0} field success".format(name)
                print msg
            # 存在该字段
            else:
                if delete:
                    arcpy.DeleteField_management (layer, name)
                    arcpy.AddField_management(layer, name, f_type, field_length=f_length)
                else:
                    print "Field exist"
        
        return layer
    """字段添加"""
    """--------------------------------"""
    """--------------------------------"""
    

if __name__ == '__main__':
    # arcpy.env.addOutputsToMap = True
    lyr_file = os.path.join(dir_lyr, "opacity.lyr")
    OpacityContour(arcpy.GetParameterAsText(0),
                     arcpy.GetParameterAsText(1), lyr_file)