# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/11

import arcpy, os
# from multiprocessing import Process

arcpy.env.overwriteOutput = True
# mxdpath = "" 地图文档的地址
slices_set = [] # 包含多个 地址列表的切片包 的列表（列表的列表）


def address_clip(mxds, process_core):
    """
    从文件夹中选出mxd文档，将全部mxd地址划分为几个切片然后装进列表中备用
    :param process_core: 运行进程数量
    :param mxds:需要出图的mxd文档的路径
    :return: None 但是从内部定义了
    但是从内部声明了两个全局变量列表
        clip_lists = [] # 包含多个 地址列表的切片包 的列表（列表的列表）
        mxdpath_list = [] # 所有地址的列表
    """
    global slices_set
    mxdpaths = []
    # paths_list = os.listdir(mxdpath)
    for all_path in os.listdir(mxds):
        if all_path[-3:].lower() == 'mxd':
            mxd_path = os.path.join(mxds, all_path)
            # 将筛选的mxd路径加入列表
            mxdpaths.append(mxd_path)
    slice_size = len(mxdpaths) // process_core
    print "path_list_num: ", slice_size
    def chunks(l, n):
        # successive n-sized chunks from l.
        for i in xrange(0, len(l), n):
            path_slice = l[i:i + n]
            slices_set.append(path_slice)
        # return slices_set

    chunks(mxdpaths, slice_size)
    print "mxd_num", len(mxdpaths)
# 列表的列表，用来装地址列表切片
# address_clip(ur"G:\test\gst")
# print slices_set

def export_jpeg(path_slice_set, res):
    """
    获取地址列表切片进行出图处理
    :param path_slice_set: 地址列表 的 一个切片包（列表）
    :param res: 分辨率 int
    :return:
    """
    count = 1
    for one_path in path_slice_set:
        mxd1 = arcpy.mapping.MapDocument(one_path)
        # print u"正在出图..."
        arcpy.mapping.ExportToJPEG(mxd1, one_path[:-3] + 'jpg', resolution=res)
        del mxd1
        count += 1
        print one_path + " Done!"
        
address_clip(r"G:\test\gst", 5)
