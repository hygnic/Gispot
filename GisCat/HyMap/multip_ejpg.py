# -*- coding:cp936 -*-
# 2019 1104
# 廖晨辰

import arcpy,os,sys
from multiprocessing import Process
# sys.path.append("../GUIs")
import tooltk


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

def export_jpeg(path_slice_set, res):
    """
    获取地址列表切片进行出图处理
    :param path_slice_set: 地址列表 的 一个切片包（列表）
    :param res: 分辨率 int
    :return:
    """
    for one_path in path_slice_set:
        mxd1 = arcpy.mapping.MapDocument(one_path)
        # print u"正在出图..."
        arcpy.mapping.ExportToJPEG(mxd1, one_path[:-3] + 'jpg', resolution=res)
        del mxd1
        print one_path + " Done!"

class MultipExp(tooltk.Tooltk):
    def __init__(self):
        super(MultipExp, self).__init__(u"多进程导出jpeg")
        # block1
        self.single_dir_block(u"mxd文档文件夹")
        # block2 取消按钮
        self.single_int_block(u"进程数")
        self.addfile_button.config(text=u"—", state="disabled")
        # block3 取消按钮
        self.single_int_block2(u"出图分辨率")
        self.addfile_button.config(text=u"—", state="disabled")

        # self.button_confirm["command"] = self.confirm_method
        # 读取帮助信息
        self.read_help("docs/multip_ejpg")
        self.button_confirm["command"] = self.confirm_method

    def confirm_method(self):
        # 获取Entry的值
        # 第一个是文件夹，第二个是进程数，第三个是分辨率
        self.get_Entry_fromblock(self.input_sdb, self.input_sib,
                                 self.input_sib2)
        print self.block_list
        for i in self.block_list:
            self.text.insert("end","\n  "+i)
            # print i, "type: ", type(i)  # G:/test/gst 20 20 被dpi覆盖

        core = int(self.block_list[1])
        print core, "type: ", type(core)
        res = int(self.block_list[2])
        print res, "type: ", type(res)
        address_clip(self.block_list[0], core)
        # address_clip(self.block_list[0],core)
        # export_jpeg(slices_set,20)
        print "准备开启多进程通道："
        # res = 10
        print slices_set
        for path_slice_set in slices_set:
            # print path_slice_set
            p = Process(target=export_jpeg, args=(path_slice_set, res))
            p.start()
            print "\t" + "进程通道已打开 " + str(p.pid)
            print "start process"
        # 初始化列表，以免二次输入时报错
        self.block_list = []


if __name__ == '__main__':
    # 这里实际不会运行的，
    app_Multip = MultipExp()
    # app_Multip.confirm_method()
    app_Multip.window.mainloop()


# address_clip(r"G:\test\gst", 5)
# address_clip(self.block_list[0],core)
# export_jpeg(slices_set, 20)
# print "准备开启多进程通道："
# for path_slice_set in slices_set:
#     p = Process(target=export_jpeg, args=(path_slice_set, 20))
#     p.start()
#     print "\t" + "进程通道已打开 " + str(p.pid)
#     print "start process"