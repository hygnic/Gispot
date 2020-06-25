#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# python2 arcgis10.6
"""
# Author: LiaoChenchen
# Created on: 2020/3/5
# Reference:
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description:……………………………………………………………………………………
程序打开的初始界面
    包含：
    1.toolbar 左侧工具栏
Usage:
# ---------------------------------------------------------------------------
"""

import Tkinter as tk
from GUIconfig import newidgets
from GUIconfig import paths
import vitems
from crcpy import save_acopy


class InitialInterface(object):
    """
    entrance界面左侧的toolbar区域以及entrance界面右侧的viewer中的工具，脚本等
    """
    def __init__(self, master1,master2):
        
        # 引入toolbar中的图标
        self.toolbar_icon()
        self.window1 = master1 # 左边
        self.window2 = master2 # 右边
        # 第yi个button,仅仅是一个查看器，方便复制到arcpy的Python脚本栏等
        self.button_viewer = newidgets.HoverButton(self.window1,
                                                   width=45,
                                                   image = self.icon_editor,
                                                   height = 45, command =self.first_viewer)
        self.button_viewer.pack(side ="top", anchor ="nw")
        # 第er个button，作用是调出dos命令等（暂时）
        self.button_dos = newidgets.HoverButton(self.window1,
                                                width=45,
                                                image = self.icon_dos,
                                                height = 45, command =self.second_viewer)
        self.button_dos.pack(side ="top", anchor ="nw")
        # 第san个button，工具箱button
        self.button_tool = newidgets.HoverButton(self.window1,
                                                width=45,
                                                image=self.icon_tool,
                                                height=45,
                                                command=self.open_viewer3)
        self.button_tool.pack(side="top", anchor="nw")
        # self.window1.mainloop()
		
    def toolbar_icon(self):
        """初始界面左侧的 toolbar 图标；tk.PhotoImage必须加入file（arcgis10.6）"""
        
        # toolbar中直接使用dos命令行的工具（暂定）#TODO 应该不止这些
        self.icon_dos = tk.PhotoImage(file = paths.GifPath.dos)
        # 对应second_viewer
        self.icon_editor = tk.PhotoImage(file=paths.GifPath.editor)
        self.icon_tool = tk.PhotoImage(file=paths.GifPath.tool)
        self.toolbar_viewer_icon1= tk.PhotoImage(file=paths.GifPath.python32)

        
    # toolbar第yi个图标(一个查看器)打开的物品集 browser
    # 查看器，不可运行
    def first_viewer(self):
        newidgets.destroy_child(self.window2)
        pass
        # vitems.Filter(self.window2)

    def second_viewer(self):
        """放置可运行的
        界面右侧的viewer,放置一个一个的图标
        master2  interface_frame
        master2
        newidgets.destroy_child(master1)"""
        newidgets.destroy_child(self.window2)
        vitems.export_s(self.window2)

    def open_viewer3(self):
        """调用Third_Viewer类"""
        newidgets.destroy_child(self.window2)
        Third_Viewer(self.window2,  self.toolbar_viewer_icon1)
        
    # -------------------------
    # 将带有参数的类变成方法和button绑定
    # def show_first_viewer(self):

class Third_Viewer(object):
    """
    用于显示工具箱button中的内容
    点击工具箱button启动该类
    """
    def __init__(self, master, icon):
        """
        :param master: tkinter 父部件
        :param icon: 图标地址
        """
        self.master = master
        self.icon = icon # paths.GifPath.gif_python32
        # print "icon:",icon
        button1_1 = newidgets.HoverButton(self.master,
                                          width=32,
                                          image=self.icon,
                                          height=32,
                                          command=self.button1)
        button1_1.pack(side="top", anchor="nw")
        
    def button1(self):
        newidgets.destroy_child(self.master)
        save_acopy.SaveACopy(self.master)