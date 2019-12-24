# -*- coding:cp936 -*-
# 2019 1104
# 廖晨辰
# python2.7
"""
运用多进程技术导出图片
集成Tkinter
使用了多进程技术 牛逼！！！！！！！！！！
"""
import Tkinter as tk
import arcpy,os
from multiprocessing import Process,Queue
# from threading import Thread

from TkGUIconfig import multication
# sys.path.append("../GUIs")
import tooltk


# mxdpath = "" 地图文档的地址
slices_set = [] # 包含多个 地址列表的切片包 的列表（列表的列表）

def address_clip(mxds, process_core):
    """
    从文件夹中选出mxd文档，将全部mxd地址划分为几个切片然后装进列表中备用
    :param process_core: 运行进程数量
    :param mxds:需要出图的mxd文档的路径
    :return: slices_set 包含多个 地址列表的切片包 的列表（列表的列表）
    其他: mxdpath_list = [] # 所有地址的列表
    """
    global slices_set
    mxdpaths = []
    # paths_list = os.listdir(mxdpath)
    for all_path in os.listdir(mxds):
        if all_path[-3:].lower() == 'mxd':
            mxd_path = os.path.join(mxds, all_path)
            # 将筛选的mxd路径加入列表
            mxdpaths.append(mxd_path)
    # process_core = int(process_core)
    slice_size = len(mxdpaths) // process_core
    print "path_list_num: ", slice_size
    def chunks(l, n):
        # successive n-sized chunks from l.
        for i in xrange(0, len(l), n):
            path_slice = l[i:i + n]
            slices_set.append(path_slice)
        # return slices_set

    chunks(mxdpaths, slice_size)
    print "mxd_num: ", len(mxdpaths)
    print "slice_num: ", len(slices_set)
    return slices_set


def export_jpeg(me_queue, path_slice_set, res):
    """
    主要的出图功能函数
    获取地址列表切片进行出图处理
    :param me_queue:
    :param path_slice_set: 地址列表 的 一个切片包（列表）
    :param res: 分辨率 int
    :return:
    """
    arcpy.env.overwriteOutput = True
    for one_path in path_slice_set:
        mxd1 = arcpy.mapping.MapDocument(one_path)
        # print u"正在出图..."
        arcpy.mapping.ExportToJPEG(mxd1, one_path[:-3] + 'jpg',
                                   resolution=res)
        del mxd1
        info = os.path.basename(one_path) + " Done! \n"
        print info
        me_queue.put(info)
    
# our_master = tool_entrance.AppEntrance.rootwindow
class MultipExp(tooltk.Tooltk):
    
    commu = multication.MuCation()
    ququ = Queue()
    def __init__(self,master1):
        """
        :param master1: mian_f , a widget from tool_entrance.py
        """
        super(MultipExp, self).__init__(master1,
                                        "../docs/multip_ejpg.gc",
                                        self.confirm_mu)
        # block1
        self.single_dir_block(u"mxd文档文件夹")
        # block2 取消按钮
        input_msgg = tk.StringVar()
        self.single_vari_block(u"进程数", input_msgg)
        
        # self.addfile_button.config(state = "disable")
        # block3 取消按钮
        self.single_int_block2(u"出图分辨率")
        # self.addfile_button.config(state = "disable")
        # self.addfile_button.pack_forget()  # 隐藏模块

        # self.addfile_button.destroy()	# 隐藏模块
    
    def confirm_mu(self):
        # 获取Entry的值
        # 第一个是文件夹，第二个是进程数，第三个是分辨率
        v = self.get_blockvalue(self.input_sdb, self.input_svb,
                                self.input_sib2)
        # 进程数
        core = int(v[1])
        print core, "type: ", type(core)
        res = int(v[2])
        print res, "type: ", type(res)
        # 获取列表
        sets_lists = address_clip(v[0], core)
        # res = 10
        for set_li in sets_lists:
            # print path_slice_set
            p = Process(target=self.commu.decor,
                        args=(self.commu.que,
                              export_jpeg,set_li, res)
                        )
            p.deamon = True
            p.start()
            print "\t" + "进程通道已打开 " + str(p.pid)
            print "process start"
            print "process_communication: begin"
            self.commu.process_communication(self.text_major_msg)
            # t = Thread(target=self.process_communication, args=(p,))
            # t.start()
        # 初始化列表，以免二次输入时报错
        self.block_list = []


# if __name__ == '__main__':
#     # 这里实际不会运行的，
#     app_Multip = MultipExp()
#     # app_Multip.confirm_method()
#     app_Multip.window.mainloop()


# address_clip(r"G:\test\gst", 5)
# address_clip(self.block_list[0],core)
# export_jpeg(slices_set, 20)
# print "准备开启多进程通道："
# for path_slice_set in slices_set:
#     p = Process(target=export_jpeg, args=(path_slice_set, 20))
#     p.start()
#     print "\t" + "进程通道已打开 " + str(p.pid)
#     print "start process"