#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/13 13:05
# Reference:
"""
Description: menubar
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
import gstrename
import crcpy.multiplexport
import crcpy.explode
import crcpy.task_dispatch
import crcpy.ZLDJ
from gpconfig import newGUI,hyini

class MenuBar(object):
    def __init__(self, master):
        self.master = master
        self.menu()
    
    def menu(self):
        """设置置顶菜单栏"""
        self.menubar = tk.Menu(self.master)
        # 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，# Exit功能项）
        self.menubar_file = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='File', menu=self.menubar_file)
        # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，
        # 每一个小菜单对应命令操作。
        self.menubar_file.add_command(label='New', command=None)
        self.menubar_file.add_command(label='Open', command=None)
        self.menubar_file.add_command(label='Save', command=None)
        self.menubar_file.add_command(label='Prograss Bar',
                                      command=None)
        self.menubar_file.add_separator()  # 分隔线
        self.menubar_file.add_command(
            label='Exit', command=self.master.quit)  # 用tkinter里面自带的quit()函数
        submenu = tk.Menu(self.menubar_file)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
        # 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
        submenu.add_command(
            label='Submenu_1',
            command=None)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
        # 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
        # 创建第二级菜单，即菜单项里面的菜单
        self.menubar_file.add_cascade(
            label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import
        # edit菜单栏
        self.menubar_edit = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='Edit', menu=self.menubar_edit)
        self.menubar_edit.add_command(label='Cut', command=None)
        self.menubar_edit.add_command(label='Copy', command=None)
        self.menubar_edit.add_command(label='Paste', command=None)
        
        # 两区公示图 菜单栏
        self.menubar_gst = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="两区公示图", menu=self.menubar_gst)
        self.menubar_gst.add_command(
            label='公示图命名规范化', command=self.open_GSTrename)
        
        # 制图mapping菜单栏
        self.menubar_map = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=u"制图", menu=self.menubar_map)
        self.menubar_map.add_command(
            label=u'多进程批量出图(JPEG)', command=self.open_Multip_exp)
        self.menubar_map.add_command(label='拆分多部件',
                                     command=self.explode_mulitp)
        self.menubar_map.add_command(label='任务分配',
                                     command=self.start_dispatch_task)
        
        # 高标准农田
        self.menubar_GBZ = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="高标准农田", menu=self.menubar_GBZ)
        self.menubar_GBZ.add_command(label='修改质量等级',
                                     command=self.start_ZLDJ)
        
        # 关于 栏
        self.menubar_about = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="关于", menu=self.menubar_about)
        self.menubar_about.add_command(
            label='获取更新', command=self.upgrade_from_github)
    
    # 配置安放菜单栏，写成方法便于调控纯程序
    def run_menu(self):
        self.master.config(menu=self.menubar)
    
    # def trans_name(self):
    #     """
    #     之前要将四川标准的图片名称改为国家标准的名称，
    #     没用上，以后也没有用了
    #     """
    #     def open_gst_trans():
    #         from LQHD import gst_trans
    #         open_gst_trans = gst_trans.App()
    #         open_gst_trans.window.mainloop()
    #
    #     def open_fbt_trans():
    #         from LQHD import fbt_trans
    #         open_fbt_trans = fbt_trans.App()
    #         open_fbt_trans.window.mainloop()
    #
    #     # 图件命名转换 菜单栏
    #     self.menubar_trans = tk.Menu(self.menubar, tearoff=0)
    #     self.menubar.add_cascade(label=u"两区图件名称装换", menu=self.menubar_trans)
    #     self.menubar_trans.add_command(label=u'公示图名称',
    #                               command=open_gst_trans)
    #     self.menubar_trans.add_command(label=u'分布图名称',
    #                               command=open_fbt_trans)
    #     # self.menubar_trans.add_command(label=u'标志牌名称'）
    #
    #     # 创建菜单栏完成后，配置让菜单栏self.menubar显示出来
    #     self.rootwindow.config(menu=self.menubar)
    
    # ----------------------------------------
    """
    全是一些按键的command指令，放在这里方便添加修改一些自定义功能
    使用的各种函数方法说明：
        newidgets.destroy_child(self.main_f): 在打开一个功能的GUI界面时，销毁覆盖
            之前存在的GUI界面
    """
    
    def open_GSTrename(self):
        newGUI.destroy_child(self.interface_frame)
        # gstrename.App(self.main_f)
        gstrename.App(self.interface_frame)
    
    def open_Multip_exp(self):
        newGUI.destroy_child(self.interface_frame)
        # multip_ejpg.MultipExp(self.main_f)
        crcpy.multiplexport.MultipExp(self.interface_frame)
    
    # 多进程导出JPEG图片
    def explode_mulitp(self):
        newGUI.destroy_child(self.interface_frame)
        # explode_mulitp.App(self.main_f)
        crcpy.explode.App(self.interface_frame)
    
    def start_dispatch_task(self):
        newGUI.destroy_child(self.interface_frame)
        # task_dispatch.StartApp(self.main_f)
        crcpy.task_dispatch.StartApp(self.interface_frame)
    
    def start_ZLDJ(self):
        # pool_list = MuCation.submultiprocess
        # while pool_list:
        #     print dead_p
        #     dead_p =pool_list.pop()
        #     kill_pid(dead_p)
        newGUI.destroy_child(self.interface_frame)
        # task_dispatch.StartApp(self.main_f)
        crcpy.ZLDJ.ZLDJGui(self.interface_frame)
