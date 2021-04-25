# -*- coding:utf-8 -*-
'''--------------------------------------------------------------------------------------
Name:              HexagonalPolygons
Purpose:           The tool creates a hexagonal polygon feature class and gives the
                   hexagon polygons an ID based on a polygon's spatial location starting
                   from left to right and bottom to top.
Author:            Esri
Created:           07/01/2012
ArcGIS Version:    10.1
Python Version:    2.6.1
Usage:             HexagonPolygons: <AOI> <Output_Hexagonal_Polygons> <Height_of_Hexagon>
---------------------------------------------------------------------------------------'''
# Import system modules
# import sys, traceback
import os
import arcpy
import math


# overwrite setting


def hexagon_polygon(inputfeature, output_theissen, width='5', *args):
    """
    
    :param inputfeature: 输入要素 范围
    :param output_theissen: 输出的结果
    :param width:
    :param args:
    :return:
    """

    # 创建镶嵌六边形
    descinput = arcpy.Describe(inputfeature)
    if descinput.dataType == "FeatureLayer":
        print "FeatureLayer"
        inputAreaOfInterest = descinput.CatalogPath # 数据路径
    else:
        print "Not FeatureLayer"
        inputAreaOfInterest = inputfeature


    ref = arcpy.Describe(inputAreaOfInterest).spatialReference
    
    # Describe the Input and get its extent properties
    desc = arcpy.Describe(inputAreaOfInterest)
    ext = desc.extent
    
    x_min = ext.XMin
    x_max = ext.XMax
    
    y_min = ext.YMin
    y_max = ext.YMax
    
    height = float(width) * math.sqrt(3)

    # Invert the height and width so that the flat side of the hexagon is on the bottom and top
    width, height = float(height), float(width)

    # Calculate new offset origin, opposite corner and Y axis point coordinates
    factor1 = -2.0
    origin_x = x_min + width * factor1
    origin_y = y_min + height * factor1
    origin = str(origin_x) + " " + str(origin_y)
    
    # The opposite corner of the fishnet set
    factor2 = 2.0
    corner_coordx = x_max + width * factor2
    corner_coordy = y_max + height * factor2
    corner_coord=str(corner_coordx) + " " +str(corner_coordy)
    # 新原点
    factor3 = 0.5
    new_origin_x = str(origin_x + width * factor3)
    new_origin_y = str(origin_y + height * factor3)
    new_origin = new_origin_x + " " + new_origin_y
    # new opposite corner
    corner_coordx2 = str(corner_coordx + width * factor3)
    corner_coordy2 = str(corner_coordy + height * factor3)
    corner_coord2 = corner_coordx2 + " " + corner_coordy2
    # note: 使用的是 str
    y_coord1 = str(origin_x) + " " + str(corner_coordy)
    y_coord2 = new_origin_x + " " + corner_coordy2

    # Calculate Length, hexagonal area and number of columns
    hexg_len =  float(height) / math.sqrt(3)
    # 等边六边形面积计算公式：根号3 * 3 / 2 * 边长 * 边长
    hexg_area = math.sqrt(3)*3/2*pow(hexg_len, 2)

    # Add Messages
    arcpy.AddMessage("Width: " + str(height))
    arcpy.AddMessage("Height: " + str(width))
    arcpy.AddMessage("Hexagon Area: " + str(hexg_area))

        
    workspace = os.path.dirname(output_theissen)
    arcpy.env.scratchWorkspace = workspace

    
    #------ first fishnet ------
    # fishnet1_point -> fishnet1_p point
    # fishnet1_result -> fishnet1_res
    # fishnet1_label -> fishnet1_lb
    CF = arcpy.CreateFishnet_management
    fishnet1_path = (os.path.join(workspace, "Fishnet1"))
    fishnet1 = CF(fishnet1_path, origin, y_coord1,
                   width, height, "0", "0", corner_coord,"LABELS")
    
    #------ second fishnet ------
    fishnet2_path = (os.path.join(workspace, "Fishnet2"))
    fishnet2 = CF(fishnet2_path, new_origin, y_coord2,
                width, height, "0", "0", corner_coord2, "LABELS")
    
    # label point
    fishnet1_lb = fishnet1.getOutput(1)
    fishnet2_lb = fishnet2.getOutput(1)
    arcpy.DefineProjection_management(fishnet1_lb, ref)
    arcpy.DefineProjection_management(fishnet2_lb, ref)

    # 将新旧标注点（label）合并
    hex_points = fishnet1_lb
    in_lyr = fishnet2_lb
    full_pt = arcpy.Append_management(in_lyr, hex_points)

    # Create Thiessen Polygons
    full_theissen = arcpy.CreateThiessenPolygons_analysis(
        full_pt,(os.path.join(workspace, "FullTheissen")))
    # 1.将完整的泰森多边形创建为要素图层
    # 2.按位置选择出和输入目标图层相交的部分
    # 3.导出要素图层
    f_lyr = "_lyr"
    arcpy.MakeFeatureLayer_management(full_theissen,f_lyr)
    arcpy.SelectLayerByLocation_management(
        f_lyr,"INTERSECT",inputfeature)
    arcpy.CopyFeatures_management(f_lyr, output_theissen)

    
    # Delete intermediate data
    # arcpy.Delete_management(fishnet1)
    # arcpy.Delete_management(fishnet2)
    # arcpy.Delete_management(fishnet1_lb)
    # arcpy.Delete_management(fishnet2_lb)
    # arcpy.Delete_management(full_theissen)
    # arcpy.Delete_management(f_lyr)


    arcpy.AddMessage("Completed hexagonal polygons.")



if __name__ == '__main__':
    # toolbox
    # argv = tuple(arcpy.GetParameterAsText(i)
    #          for i in range(arcpy.GetArgumentCount()))
    # hexagon_polygon(*argv)


    arcpy.env.overwriteOutput = True
    output = r"G:\MoveOn\Gispot\gispot\teminal\test501"
    hexagon_polygon("Hexagon_test.shp", output, "300")
    # hexagon_polygon(r"C:\Users\Administrator\Documents\ArcGIS\Default.gdb\CJQY519090", ur"G:\MoveOn\Gispot\gispot\teminal\test1122", "300", clip=True)
