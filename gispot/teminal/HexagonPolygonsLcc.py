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
import sys, os, arcpy, traceback
import math
from hybag import ezarcpy


# overwrite setting
arcpy.env.overwriteOutput = True

def hexagon_polygon(inputfeature, output_theissen, width='5', clip=True, *args):

    """A function to check for correct field types between the from and to fields."""

    descinput = arcpy.Describe(inputfeature)
    if descinput.dataType == 'FeatureLayer':
        inputAreaOfInterest = descinput.CatalogPath # TODO CatalogPath的含义是什么
    else:
        inputAreaOfInterest = inputfeature


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
    originX = str(x_min + width * factor1)
    originY = str(y_min + height * factor1)
    origin = originX + " " + originY

    factor2 = 2.0
    oppositeCornerX = str(x_max + width * factor2)
    oppositeCornerY = str(y_max + height * factor2)
    oppositeCorner = oppositeCornerX + " " + oppositeCornerY

    factor3 = 0.5
    newOriginX = str(float(originX) + float(width) * factor3)
    newOriginY = str(float(originY) + float(height) * factor3)
    newOrigin = newOriginX + " " + newOriginY

    newOppositeCornerX = str(float(oppositeCornerX) + float(width) * factor3)
    newOppositeCornerY = str(float(oppositeCornerY) + float(height) * factor3)
    newOppositeCorner = newOppositeCornerX + " " + newOppositeCornerY

    yAxisCoordinates1 = str(float(originX)) + " " + str(float(oppositeCornerY))
    yAxisCoordinates2 = str(float(newOriginX)) + " " + str(float(newOppositeCornerY))

    # Calculate Length, hexagonal area and number of columns
    hexg_len =  float(height) / math.sqrt(3)
    # 等边六边形面积计算公式：根号3 * 3 / 2 * 边长 * 边长
    hexg_area = math.sqrt(3)*3/2*pow(hexg_len, 2)

    # Add Messages
    arcpy.AddMessage("Width: " + str(height))
    arcpy.AddMessage("Height: " + str(width))
    arcpy.AddMessage("Hexagon Area: " + str(hexg_area))

    try:
        cfm = arcpy.CreateFishnet_management
        ctpa = arcpy.CreateThiessenPolygons_analysis
        cfcm = arcpy.CreateFeatureclass_management
        
        workspace = os.path.dirname(output_theissen)
        arcpy.env.scratchWorkspace = os.path.dirname(output_theissen)

        
        #------ first fishnet ------
        # fishnet1_point -> fishnet1_p point
        # fishnet1_result -> fishnet1_res
        # fishnet1_label -> fishnet1_lb
        
        fishnet1_p = (os.path.join(workspace, "Fishnet_1"))
        fishnet1_res = cfm(fishnet1_p, origin, yAxisCoordinates1,
                       width, height, "0", "0", oppositeCorner,
                       "LABELS")
        fishnet1_lb = fishnet1_res.getOutput(1)
        
        #------ second fishnet ------
        fishnet2_p = (os.path.join(workspace, "Fishnet_2"))
        fishnet2_res = cfm(
            fishnet2_p, newOrigin, yAxisCoordinates2,
            width, height, "0", "0", newOppositeCorner, "LABELS")
        fishnet2_lb = fishnet2_res.getOutput(1)
        
        
        # Process: Create Feature Class...
        ref = arcpy.Describe(inputAreaOfInterest).spatialReference
        hexPoints = cfcm(
            workspace, "hex_points", "POINT", "", "", "", ref)

        # Get fishnet labels from the results of the fishnet tool...
        # fishnetLabel1 = fishnet1_res.getOutput(1)
        # fishnetLabel2 = fishnet2_res.getOutput(1)

        # Define projection for the fishnet labels
        arcpy.DefineProjection_management(fishnet1_lb, ref)
        arcpy.DefineProjection_management(fishnet2_lb, ref)

        # Process: Append...
        inputForAppend = "{0};{1}".format(fishnet1_lb, fishnet2_lb)
        arcpy.Append_management(inputForAppend, hexPoints, "NO_TEST", "", "")

        # Process: Create Thiessen Polygons...
        fullTheissen = ctpa(
            hexPoints,
            (os.path.join(workspace, "FullTheissen")),
            "ONLY_FID")
        
        arcpy.AddMessage("Creating hexagonal polygons.")
        arcpy.CopyFeatures_management(fullTheissen, output_theissen)

        
        # Delete all intermediate data
        # arcpy.Delete_management(fishnet1)
        # arcpy.Delete_management(fishnet2)
        # arcpy.Delete_management(fishnetLabel1)
        # arcpy.Delete_management(fishnetLabel2)
        # arcpy.Delete_management(hexPoints)
        # arcpy.Delete_management(fullTheissen)

        # arcpy.AddMessage("Congratulations! You have created the most beautiful polygons ever :)")

    except:
        # get the traceback object
        tb = sys.exc_info()[2]
        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]
        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + \
                str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        # generate a message string for any geoprocessing tool errors
        msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"

        # return gp messages for use with a script tool
        arcpy.AddError(msgs)
        arcpy.AddError(pymsg)

        # print messages for use in Python/PythonWin
        print msgs
        print pymsg

if __name__ == '__main__':
    # toolbox
    # argv = tuple(arcpy.GetParameterAsText(i)
    #          for i in range(arcpy.GetArgumentCount()))
    # hexagon_polygon(*argv)

    from hybag import ezarcpy
    # arcpy.env.workspace = ezarcpy.InitPath()[-1]
    arcpy.env.overwriteOutput = True
    hexagon_polygon("Hexagon_test.shp",ur"G:\MoveOn\Gispot\gispot\teminal\test1122","300", clip=True)
    # hexagon_polygon(r"C:\Users\Administrator\Documents\ArcGIS\Default.gdb\CJQY519090", ur"G:\MoveOn\Gispot\gispot\teminal\test1122", "300", clip=True)
