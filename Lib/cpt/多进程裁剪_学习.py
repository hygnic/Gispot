# -*- coding:utf-8 -*-
# User: lcc
# Date: 2019/9/27

# -*- coding:utf-8 -*-
__author__ = 'kikita'

import arcpy
import timeit
import time
import multiprocessing
import os

arcpy.env.workspace =  r'D:\LearnAboutPython\MyPythonProject\UsingCurser\DemoDataS.gdb'
arcpy.env.overwriteOutput = True

# 批量裁剪函数
def MyBatchClip(Parameter):
    # 参数
    inputFC = Parameter[0]
    ClipArea = Parameter[1]
    OutputWS = Parameter[2]
    Prefix = Parameter[3]
    # 字段列表，其中 SHAPE@用于访问数据几何
    Fields = ['OBJECTID','SHAPE@']
    with arcpy.da.SearchCursor(ClipArea,Fields) as cursor:
        for row in cursor:
            outputFC = os.path.join(OutputWS, Prefix+str(row[0])+'.shp')
            arcpy.Clip_analysis(inputFC, row[1], outputFC)
            print Prefix+str(row[0])+'.shp'


if __name__ == '__main__':
    # 参数
    OutputWS = r'D:\LearnAboutPython\MyPythonProject\UsingCurser\OutputWS'
    # SDE库输出
    #OutputWS = r'C:\Connection131.sde'
    Parameter1 = ['CountyPoints','Area_A',OutputWS, 'AAA_']
    Parameter2 = ['hyd_line','Area_B',OutputWS, 'BBB_']
    Parameter3 = ['River_line.shp','Area_C.shp',OutputWS,'CCC_']
    Parameters = [Parameter1,Parameter2,Parameter3]
    # 当前CPU核数
    print 'CPU Count:' + str(multiprocessing.cpu_count())
    # 进程池
    MyGPpool = multiprocessing.Pool()
    # 多进程并行处理
    StartTime = time.time()
    results = MyGPpool.map(MyBatchClip,Parameters)
    EndTime = time.time()
    print 'Elapsed: ' + str(EndTime - StartTime) + ' Seconds...'