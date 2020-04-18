# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/5
# python2 arcgis10.6
"""
程序打开的初始界面，左边为部分一，右面为部分二
部分一：toolbar 可视化的工具栏
部分二：toolbar_viewer 点击工具栏弹出的工具浏览窗口
"""

import Tkinter as tk
from GUIconfig import newidgets
from GUIconfig import paths
import vitems

class InitialInterface(object):
    """
    entrance界面左侧的toolbar区域以及entrance界面右侧的viewer中的工具，脚本等
    """
    def __init__(self, master1,master2):
        
        # 引入toolbar中的图标
        self.toolbar()
        self.window1 = master1
        self.window2 = master2
        # 第yi个button,仅仅是一个查看器，方便复制到arcpy的Python脚本栏等
        self.button_two = newidgets.HoverButton(self.window1,
                                                width=45,
                                                image = self.icon_editor,
                                                height = 45, command =self.first_viewer)
        self.button_two.pack(side ="top", anchor ="nw")
        # 第er个button，作用是调出dos命令等（暂时）
        self.button_one = newidgets.HoverButton(self.window1,
                                                width=45,
                                                image = self.icon_dos,
                                                height = 45, command =self.second_viewer)
        self.button_one.pack(side ="top", anchor ="nw")
        # self.window1.mainloop()
		
    def toolbar(self):
        """界面左侧的toolbar；必须加入file（arcgis10.6）"""
        # toolbar中直接使用dos命令行的工具（暂定）#TODO 应该不止这些
        self.icon_dos = tk.PhotoImage(file = paths.GifPath.gif_dos)
        # 对应second_viewer
        self.icon_editor = tk.PhotoImage(file=paths.GifPath.gif_editor)

        
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
        
        
    # -------------------------
    # 将带有参数的类变成方法和button绑定
    # def show_first_viewer(self):
    