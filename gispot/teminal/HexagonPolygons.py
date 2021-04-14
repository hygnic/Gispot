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
import collections
import sys, os, arcpy, traceback
from arcpy import env
import math


# overwrite setting
env.overwriteOutput = 1

def hexagon_polygon(inputAOI, outputTheissen, width='5', clipToAOI=True, *args):

    """A function to check for correct field types between the from and to fields."""

    descInput = arcpy.Describe(inputAOI)
    if descInput.dataType == 'FeatureLayer':
        inputAreaOfInterest = descInput.CatalogPath
    else:
        inputAreaOfInterest = inputAOI


    # Describe the Input and get its extent properties
    desc = arcpy.Describe(inputAreaOfInterest)
    ext = desc.extent
    xcoord = ext.XMin
    ycoord = ext.YMin
    urxcoord = ext.XMax
    urycoord = ext.YMax
    height = float(width) * math.sqrt(3)

    # Invert the height and width so that the flat side of the hexagon is on the bottom and top
    tempWidth = width
    width = height
    height = tempWidth

    # Calculate new offset origin, opposite corner and Y axis point coordinates
    factor1 = -2.0
    origin = str(xcoord + float(width) * factor1) + " " + str(ycoord + float(height) * factor1)
    originX = str(xcoord + float(width) * factor1)
    originY = str(ycoord + float(height) * factor1)

    factor2 = 2.0
    oppositeCorner = str(urxcoord + float(width) * factor2) + " " + str(urycoord + float(height) * factor2)
    oppositeCornerX = str(urxcoord + float(width) * factor2)
    oppositeCornerY = str(urycoord + float(height) * factor2)

    factor3 = 0.5
    newOrigin = str(float(originX) + float(width) * factor3) + " " + str(float(originY) + float(height) * factor3)
    newOriginX = str(float(originX) + float(width) * factor3)
    newOriginY = str(float(originY) + float(height) * factor3)

    newOppositeCorner = str(float(oppositeCornerX) + float(width) * factor3) + " " + str(float(oppositeCornerY) + float(height) * factor3)
    newOppositeCornerX = str(float(oppositeCornerX) + float(width) * factor3)
    newOppositeCornerY = str(float(oppositeCornerY) + float(height) * factor3)

    yAxisCoordinates1 = str(float(originX)) + " " + str(float(oppositeCornerY))
    yAxisCoordinates2 = str(float(newOriginX)) + " " + str(float(newOppositeCornerY))

    # Calculate Length, hexagonal area and number of columns
    sideLength =  float(height) / math.sqrt(3)
    hexagonArea = 2.598076211 * pow(sideLength, 2)
    numberOfColumns = int((urxcoord - xcoord)  / int(width))

    # Add Messages
    arcpy.AddMessage("------------------------")
    arcpy.AddMessage("Width: " + str(height))
    arcpy.AddMessage("Height: " + str(width))
    arcpy.AddMessage("Hexagon Area: " + str(hexagonArea))
    arcpy.AddMessage("Number of Columns: " + str(numberOfColumns))
    arcpy.AddMessage("------------------------")

    try:
        outputWorkspace = os.path.dirname(outputTheissen)
        arcpy.env.scratchWorkspace = os.path.dirname(outputTheissen)

        # Process: Create Fishnet...
        fishnetPath1 = (os.path.join(outputWorkspace, "Fishnet_1"))
        fishnet1 = arcpy.CreateFishnet_management(fishnetPath1, origin, yAxisCoordinates1, width, height, "0", "0", oppositeCorner, "LABELS", "")

        # Process: Create Fishnet (2)...
        fishnetPath2 = (os.path.join(outputWorkspace, "Fishnet_2"))
        fishnet2 = arcpy.CreateFishnet_management(fishnetPath2, newOrigin, yAxisCoordinates2, width, height, "0", "0", newOppositeCorner, "LABELS")

        # Process: Create Feature Class...
        spatialRef = arcpy.Describe(inputAreaOfInterest).spatialReference
        hexPoints = arcpy.CreateFeatureclass_management(outputWorkspace, "hex_points", "POINT", "", "", "", spatialRef)

        # Get fishnet labels from the results of the fishnet tool...
        fishnetLabel1 = fishnet1.getOutput(1)
        fishnetLabel2 = fishnet2.getOutput(1)

        # Define projection for the fishnet labels
        arcpy.DefineProjection_management(fishnetLabel1, spatialRef)
        arcpy.DefineProjection_management(fishnetLabel2, spatialRef)

        # Process: Append...
        inputForAppend = "{0};{1}".format(fishnetLabel1, fishnetLabel2)
        arcpy.Append_management(inputForAppend, hexPoints, "NO_TEST", "", "")

        # Process: Create Thiessen Polygons...
        fullTheissen = arcpy.CreateThiessenPolygons_analysis(hexPoints, (os.path.join(outputWorkspace, "FullTheissen")), "ONLY_FID")
        arcpy.AddMessage("Creating hexagonal polygons.")

        # Process: Minimum Bounding Geometry...
        AOIEnvelope = arcpy.MinimumBoundingGeometry_management(inputAreaOfInterest, (os.path.join(outputWorkspace, "AOIEnvelope")), "ENVELOPE", "ALL" )

        # Process: Make Feature Layer...
        hexLayer = arcpy.MakeFeatureLayer_management(fullTheissen, "Hex_Layer", "", "", "")

        # Process: Select Layer By Location...
        arcpy.SelectLayerByLocation_management(hexLayer, "INTERSECT", AOIEnvelope)

        # Process: Add Field (1)...
        arcpy.AddField_management(hexLayer, "X_Coord", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Add Field (2)...
        arcpy.AddField_management(hexLayer, "Y_Coord", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate X Value...
        arcpy.CalculateField_management(hexLayer, "X_Coord", "GetXValue(!shape.centroid!)", "PYTHON", "def GetXValue(centroid):\\n    coords = centroid.split(\" \")\\n    return round(float(coords[0]),2)")

        # Process: Calculate Y Value...
        arcpy.CalculateField_management(hexLayer, "Y_Coord", "GetYValue(!shape.centroid!)", "PYTHON", "def GetYValue(centroid):\\n    coords = centroid.split(\" \")\\n    return round(float(coords[1]),2)")

        # Process: Add Field (3)...
        arcpy.AddField_management(hexLayer, "hexagonID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        if clipToAOI == "true":
            arcpy.Clip_analysis(hexLayer, inputAOI,  outputTheissen)

            #Calculate Hexagon Polygon ID(hexLayer)
            cur = arcpy.UpdateCursor(outputTheissen, "", "", "", "y_coord A; x_coord A")


            for ID, row in enumerate(cur, 1):
                row.hexagonID = ID
                cur.updateRow(row)

            # Process: Add Spatial Index...
            arcpy.AddSpatialIndex_management(outputTheissen)
            arcpy.AddMessage("Adding Hexagon Id to clip polygons.")



        else:
            #Calculate Hexagon Polygon ID(hexLayer)
            cur = arcpy.UpdateCursor(hexLayer, "", "", "", "y_coord A; x_coord A")


            for ID, row in enumerate(cur, 1):
                row.hexagonID = ID
                cur.updateRow(row)


            # Process: Add Spatial Index...
            arcpy.AddSpatialIndex_management(hexLayer)
            arcpy.AddMessage("Adding Hexagon Id to polygons.")
            arcpy.CopyFeatures_management(hexLayer, outputTheissen)

        # Delete all intermediate data
        arcpy.Delete_management(fishnet1)
        arcpy.Delete_management(fishnet2)
        arcpy.Delete_management(fishnetLabel1)
        arcpy.Delete_management(fishnetLabel2)
        arcpy.Delete_management(hexPoints)
        arcpy.Delete_management(fullTheissen)
        arcpy.Delete_management(AOIEnvelope)

        arcpy.AddMessage("Congratulations! You have created the most beautiful polygons ever :)")

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
    argv = tuple(arcpy.GetParameterAsText(i)
             for i in range(arcpy.GetArgumentCount()))
    hexagon_polygon(*argv)

# End of hexagon_polygon function.