# -*- coding:utf-8 -*-
# User: hygnic liaochenchen
# Date: 2019/10/2

import arcpy, os

# 可以进行覆盖
arcpy.env.overwriteOutput = True
arcpy.env.addOutputsToMap = False
# 选取图层
layername = arcpy.GetParameterAsText(0)
# 检索字段
text = arcpy.GetParameterAsText(1)
# 缓冲区目录
bufferoutput = arcpy.GetParameterAsText(2)
# 获取缓冲距离；多选
nums = arcpy.GetParameterAsText(3)
nums = nums.split(';')
# # 将split获取的str列表转换为int列表，用于计算缓冲区
distance = map(int, nums)

arcpy.AddMessage(layername)
arcpy.AddMessage(text)
arcpy.AddMessage(bufferoutput)
arcpy.AddMessage(layername)


template = 'CURRENT'
mxd1 = arcpy.mapping.MapDocument(template)
dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
layer = arcpy.mapping.ListLayers(mxd1, layername, dataframe1)[0]
layer.definitionQuery = ''
# 检索字段 读取属性表
# field = arcpy.GetParameterAsText(0)


def makeRingBuffer(layer, field, bufferoutput, distance):
    """图层，图层检索字段，缓冲区目录,多环缓冲距离"""

    cursor = arcpy.da.SearchCursor(layer, field)
    counter = 0
    for row in cursor:
        getvalue_field = row[0]

    # 创建feature class，这一步可要可不要
        outFeatureName = 'feature_class'+str(counter)
        print counter
        arcpy.MakeFeatureLayer_management(layer,outFeatureName)

    # 选中各个乡镇级图斑
        arcpy.SelectLayerByAttribute_management(outFeatureName, 'NEW_SELECTION', "\"XJQYMC\" = \'" + getvalue_field+"'")

    # make buffer
        inFeatures = outFeatureName
        outBufferName = 'buffer' + str(counter)
        bufferunit = 'meters'
        arcpy.MultipleRingBuffer_analysis(inFeatures, outBufferName, distance,bufferunit, '', '', 'OUTSIDE_ONLY')




        indata = outBufferName
        outdata = os.path.join(bufferoutput, getvalue_field + 'buffer')
        arcpy.CopyFeatures_management(indata, outdata)
        counter += 1
    del cursor
#
makeRingBuffer(layer, text, bufferoutput, distance)