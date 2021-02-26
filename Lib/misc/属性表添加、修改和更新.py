# -*- coding: cp936 -*-
# GB2312
# 2019 0814 廖晨辰
# 该方法，目前，是在同一个mxd文件中，将不同的图层的属性更新到其它的图层


import arcpy

def update_layer():
    mxd1 = arcpy.mapping.MapDocument("CURRENT")
    #G:\自流井区\区域确认图\土地流转.mxd

    layer1 = arcpy.mapping.ListLayers(mxd1,'自流井区')[0]
    layer2 = arcpy.mapping.ListLayers(mxd1,'LQDKHB')[0]
    print layer1.name + ' is ok'
    print layer2.name + ' is ok\n'

            
    cursor = arcpy.da.UpdateCursor(layer1,('SRF','SRFFZR','LXFS','LZYT1','LZYT2'))
    cursorList= cursor.next()
    SRF = cursorList[0]
    SRFFZR = cursorList[1]
    LXFS = cursorList[2]
    LZYT1 = cursorList[3]
    LZYT2 = cursorList[4]

    print SRF +'\n'+SRFFZR
        
    del cursor

    print '属性表获取成功\n'

    with arcpy.da.UpdateCursor(layer2,("JYZT","JYZTDB",'LXDH','ZZZW1','ZZZW2')) as cursor:
        for row in cursor:
            row[0] = SRF
            row[1] = SRFFZR
            row[2] = LXFS
            row[3] = LZYT1
            row[4] = LZYT2
            
            cursor.updateRow(row)
            print '更新完成'

            
    # 使用计算器转移字段 ,       
    # arcpy.CalculateField_management(layer2, 'JYZT', 'a')
    
    
update_layer()
