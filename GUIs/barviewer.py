# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/5
# python2 arcgis10.6
"""选择entrance主界面的左侧图形化按钮toolbar，打开toolbar_viewer界面
部分一：toolbar
部分二：toolbar_viewer"""

import tkinter as tk
from TkGUIconfig import newidgets
from TkGUIconfig import paths
import vitems

class ToolbarViewer(object):
    """
    entrance界面左侧的toolbar区域以及entrance界面右侧的viewer中的工具，脚本等
    """
    def __init__(self, master1,master2):
        
        # 引入toolbar中的图标
        self.toolbar()
        self.window1 = master1
        self.window2 = master2
        # 第一个button，作用是调出dos命令等（暂时）
        self.button_one = newidgets.HoverButton(self.window1,
                                                width=45,
                                                image = self.icon_dos,
                                                height = 45, command =self.viewer)
        self.button_one.pack(side ="left", anchor ="nw")

        # self.window1.mainloop()
		
    def toolbar(self):
        """界面左侧的toolbar；必须加入file（arcgis10.6）"""
        # toolbar中直接使用dos命令行的工具（暂定）#TODO 应该不止这些
        self.icon_dos = tk.PhotoImage(file = paths.GifPath.gif_dos)
    
    def viewer(self):
        # 界面右侧的viewer
        # master2 就是 input_interface这个frame
        # master2
        # newidgets.destroy_child(master1)
        newidgets.destroy_child(self.window2)
        vitems.export_s(self.window2)
        
