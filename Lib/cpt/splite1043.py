# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/24

import arcpy
import os

template = 'CURRENT'
mxd1 = arcpy.mapping.MapDocument(template)
dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
layer = arcpy.mapping.ListLayers(mxd1, "XJQY", dataframe1)[0]
layer2 = arcpy.mapping.ListLayers(mxd1, "DZDW", dataframe1)[0]
# layer.definitionQuery = ''
outpath = ur"G:\正安县\正安县公示图\we"
fields = ["XJQYDM", "XJQYMC"]
# outFeatureName = "temp"

def makeringbuffer(layers, field):

    cursor = arcpy.da.SearchCursor(layers, field)
    counter = 0
    for row in cursor:
        getvalue_field = row[0]
        getvalue_name = row[1]

    # 创建feature class，这一步可要可不要
        outFeatureName = 'feature_class'
        print counter
        arcpy.MakeFeatureLayer_management(layer2, outFeatureName)

    # 选中各个乡镇级图斑
        arcpy.SelectLayerByAttribute_management(outFeatureName, 'NEW_SELECTION',
									"\"XJQYDM\" = \'" + getvalue_field+"'")

  
    # 输出图层
        arcpy.CopyFeatures_management(outFeatureName,
									  os.path.join(outpath,getvalue_name))
        counter += 1
    del cursor

if __name__ == '__main__':
	makeringbuffer(layer, fields)