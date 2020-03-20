# -*- coding: utf-8 -*-
# User: liaochenchen
# Date: 2019/9/16

import arcpy
import datetime

time1=datetime.datetime.now()
time2 = datetime.datetime.strptime("2020-1-1", "%Y-%impure_data-%d")
if time1 > time2:
    arcpy.AddMessage(u'工具损坏，联系廖晨辰')
else:
    # cp1
    value1 = arcpy.GetParameterAsText(0)
    # c1
    value1_2 = arcpy.GetParameterAsText(1)
    # rp1
    value2 = arcpy.GetParameterAsText(2)
    # r1
    value2_2 = arcpy.GetParameterAsText(3)
    
    mxd1 = arcpy.mapping.MapDocument('CURRENT')
    df1 = arcpy.mapping.ListDataFrames(mxd1)[0]
    elm = arcpy.mapping.ListLayoutElements(mxd1, 'TEXT_ELEMENT')
    for elm1 in elm:
        namelist = ['c1', 'cp1']
        for name in namelist:
            if elm1.name == name:
                # 'c1' or elm1.name == 'cp1' or elm1 == 'r1' or elm1 == 'rp1':
                # print elm1.elementPositionY
                # print 'ok'
                # value1 = 422
                for i in range(1, 20):
                    # print type(i)
                    elm2 = elm1.clone()
                    # 修改r1符号数字
                    if elm2.name == 'c1_' + str(i):
                        elm2.text = int(value1_2) + i
                    if elm2.name == 'cp1_' + str(i):
                        elm2.name = value1
                    elm2.elementPositionY = elm1.elementPositionY + i * 10
                    
        # 设置第一个标注
        
        if elm1.name == 'c1':
            elm1.text = value1_2
        if elm1.name == 'cp1':
            elm1.text = value1
    
    
    for elm3 in elm:
        namelist = ['r1', 'rp1']
        for name in namelist:
            if elm3.name == name:
                for i in range(1, 20):
                    elm4 = elm3.clone()
                    if elm4.name == 'r1_' + str(i):
                        elm4.text = int(value2_2) + i
                    if elm4.name == 'rp1_' + str(i):
                        elm4.text = value2
                    elm4.elementPositionX = elm3.elementPositionX + i * 10
        
        if elm3.name == 'r1':
            elm3.text = value2_2
        if elm3.name == 'rp1':
            elm3.text = value2
    
    # 匹配规则未知
    # allelm = arcpy.mapping.ListLayoutElements(mxd1, 'TEXT_ELEMENT')
    # for aelm in allelm:
    #     if aelm.name == 'cp*':
    #         aelm.text = value1
    #
    #     if aelm.name == 'rp*':
    #         aelm.text = value2
        
        
        
        
        # 设置列- 3
        # if elm1.name == 'cp1':
        #     count = 0
        #     while count <= 5:
        #         count += 1
        #         elm2 = elm1.clone()
        #         elm2.elementPositionY = elm1.elementPositionY + count*283.3699
        
    
    #查看距离
    # for elm1 in elm:
    #     if elm1.name == '23':
    #         a = elm1.elementPositionY
    #     if elm1.name == '24':
    #         b = elm1.elementPositionY
    #     c= b-a
    #     print a, b, c
    
    
    # 1=1
    # 1+1
    # b= 1+1