#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: 廖晨辰
# Created on: 2019 1104
# Reference:
# python2.7
"""
Description:
	运用多进程技术导出图片
	集成Tkinter
	使用了多进程技术
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
import arcpy
import os
import time
from multiprocessing import Process
from gpconfig import multication
# from hybag import time
import tooltk
from hybag import hybasic


# slices_set = [] # 包含多个 地址列表的切片包 的列表（列表的列表）

def address_clip(mxds, process_core):
    """
    从文件夹中选出mxd文档，将全部mxd地址划分为几个切片然后装进列表中备用
    :param process_core: 运行进程数量
    :param mxds:需要出图的mxd文档的路径
    :return: slices_set 包含多个 地址列表的切片包 的列表（列表的列表）
    其他: mxdpath_list = [] # 所有地址的列表
    """
    # global slices_set
    # slices_set = [] # 初始化列表，避免程序二次运行时重复出图
    mxdpaths = []
    for a_mxd in os.listdir(mxds):
        if a_mxd[-3:].lower() == 'mxd':
            mxd_path = os.path.join(mxds, a_mxd)
            mxdpaths.append(mxd_path) # 将筛选的mxd路径加入列表
    
    slices_set = hybasic.make_chunk(mxdpaths, process_core)
    return slices_set # 包含多个 地址列表的切片包 的列表（列表的列表）
# slice_size = len(mxdpaths) // process_core
# print "path_list_num: ", slice_size
# def chunks(l, n):
# 	# successive n-sized chunks from l.
# 	for i in xrange(0, len(l), n):
# 		path_slice = l[i:i + n]
# 		slices_set.append(path_slice)
# 	# return slices_set
#
# chunks(mxdpaths, slice_size)
# print "mxd_num: ", len(mxdpaths)
# print "slice_num: ", len(slices_set)
# return slices_set


def export_jpeg(me_queue, path_slice_set, res):
    """
    主要的出图功能函数
    获取地址列表切片进行出图处理
    :param me_queue: 进程之间沟通用
    :param path_slice_set: 地址列表 的 一个切片包（列表）
    :param res: 分辨率 int
    :return:
    """
    arcpy.env.overwriteOutput = True
    for one_path in path_slice_set:
        mxd1 = arcpy.mapping.MapDocument(one_path)
        arcpy.mapping.ExportToJPEG(mxd1, one_path[:-3] + 'jpg',
                                   resolution=res)
        del mxd1
        info = u"{} Done! \n".format(os.path.basename(one_path))
        me_queue.put(info)

# our_master = tool_entrance.AppEntrance.rootwindow
class MultipExp(tooltk.Tooltk):
    
    def __init__(self,master1):
        """
        :param master1: mian_f , a widget from tool_entrance.py
        """
        super(MultipExp, self).__init__(master1,
                                        "multiplexport.gc",
                                        self.confirm_mu)
        self.name=u"多进程批量导图"
        frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
        # block1
        self.block1 = tooltk.blockDIR_in(frame, u"mxd文档文件夹")
        # block2 取消按钮
        self.block2 = tooltk.blockValue(frame, u"进程数")
        # block3 取消按钮
        self.block3 = tooltk.blockValue(frame, u"出图分辨率")
        # self.addfile_button.config(state = "disable")
        # self.addfile_button.pack_forget()  # 隐藏模块
        # self.addfile_button.destroy()	# 隐藏模块
        
        # stdout = multication.StdoutQueue()
        # sys.stdout = stdout.new_stdout
        self.commu = multication.MuCation()
    
    
    def confirm_mu(self):
        # 获取Entry的值
        v =[self.block1.get(),self.block2.get(),self.block3.get()]
        # 进程数
        core = int(v[1])
        res = int(v[2])
        # 获取列表
        sets_lists, msg = address_clip(v[0], core)
        for a_msg in msg: # 读取大致分组信息
            self.commu.que.append(a_msg+";\n")
        for set_li in sets_lists:
            time.sleep(0.5)
            p = Process(
                target=self.commu.decor, args=(export_jpeg,set_li, res))
            # p.deamon = True
            p.start()
            # print "\t" + u"进程通道已打开 " + str(p.pid)
            # print "process start"
            # print "start process communication"
            self.commu.process_communication(self.major_msgframe)
        # t = Thread(target=self.process_communication, args=(p,))
        # t.start()
        # p.terminate()
        # 初始化列表，以免二次输入时报错
        self.block_list = []