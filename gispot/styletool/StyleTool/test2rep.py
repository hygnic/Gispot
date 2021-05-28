# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              test2rep
# Author:            Hygnic
# Created on:        2021/5/28 15:06
# Version:           
# Reference:         
"""
Description:         制图表达相关的
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
arcpy.env.workspace = gdb
work = arcpy.env.workspace
#----------workspace-----------
#------------------------------


rep_lyr = os.path.join(representation, "BlueGradient.lyr")
if arcpy.Exists(rep_lyr):
    arcpy.AddMessage("okok")

def main(inputfile):
    randnum = randint(1000000, 9999999)
    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    
    # create a new layer
    in_lyr = arcpy.mapping.Layer(inputfile)
    new_n = "{}_{}".format(in_lyr.name.encode("utf8"), randnum)
    arcpy.CopyFeatures_management(inputfile, new_n)
    # arcpy.AddMessage(type(new_n)) # <'str'>
    new_lyr = arcpy.mapping.Layer(new_n)
    
    # make representation symbol to new layer
    representation_lyr = arcpy.mapping.Layer(rep_lyr)
    r_func = arcpy.AddRepresentation_cartography
    rp_name = "Rep_{}".format(randnum)
    r_func(new_lyr, rp_name, import_rule_layer=representation_lyr)
    
    # add new layer to arcmap
    arcpy.mapping.AddLayer(df, new_lyr)
    
    
if __name__ == '__main__':
    main(arcpy.GetParameterAsText(0))