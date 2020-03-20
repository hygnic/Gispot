# -*- coding:utf8 -*-
# User: liaochenchen
# Date: 2019/9/19
import arcpy
import os


arcpy.env.overwriteOutput = True
arcpy.env.addOutputsToMap = False

layername = arcpy.GetParameterAsText(0)
text = arcpy.GetParameterAsText(1)
bufferoutput = arcpy.GetParameterAsText(2)
nums = arcpy.GetParameterAsText(3)
nums = nums.split(';')
distance = map(int, nums)

arcpy.AddMessage(layername)
arcpy.AddMessage(text)
arcpy.AddMessage(bufferoutput)
arcpy.AddMessage(distance)


template = 'CURRENT'
mxd1 = arcpy.mapping.MapDocument(template)
dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
layer = arcpy.mapping.ListLayers(mxd1, layername, dataframe1)[0]
layer.definitionQuery = ''


def makeringbuffer(layers, field, bufferoutputs, distances):
    """图层，图层检索字段，缓冲区目录,多环缓冲距离"""

    cursor = arcpy.da.SearchCursor(layers, field)
    counter = 0
    for row in cursor:
        getvalue_field = row[0]

    # 创建feature class，这一步可要可不要
        outFeatureName = 'feature_class'
        print counter
        arcpy.MakeFeatureLayer_management(layers, outFeatureName)

    # 选中各个乡镇级图斑
        arcpy.SelectLayerByAttribute_management(outFeatureName, 'NEW_SELECTION',
									"\"XJQYMC\" = \'" + getvalue_field+"'")

    # make buffer
        inFeatures = outFeatureName
        outBufferName = 'buffer'
        bufferunit = 'meters'
        arcpy.MultipleRingBuffer_analysis(inFeatures, outBufferName, distances, bufferunit, '', '', 'OUTSIDE_ONLY')

    # 输出缓冲区
    #     outdata1 = os.path.join(bufferoutputs, getvalue_field + 'buffer')
        arcpy.CopyFeatures_management(outBufferName,
			  os.path.join(bufferoutputs, getvalue_field + 'buffer'))
        counter += 1
    del cursor

if __name__ == '__main__':

    makeringbuffer(layer, text, bufferoutput, distance)
    






