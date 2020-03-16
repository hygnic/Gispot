# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/5
# python2 arcgis10.6
"""选择entrance主界面的左侧图形化按钮toolbar，打开toolbar_viewer界面
部分一：toolbar
部分二：toolbar_viewer"""

import os
import tkinter as tk
from TkGUIconfig import newidgets
from TkGUIconfig import paths
from commandorder import export

class FangFa(object):
    """方法。      方法函数的集合，哈哈哈哈"""
    def dos(self):
        export.export()


class ToolbarViewer(object):
    """entrance界面右侧的view界面中的工具，脚本等"""
    def __init__(self, master):
        # master 就是 input_interface这个frame
        self.window = master
        # newidgets.destroy_child(master)
        newidgets.destroy_child(self.window)
        
        
        

class ToolPan(object):
    """
    entrance界面左侧的toolbar区域
    """
    def __init__(self, master):
        self.icon()
        self.window = master
        # 第一个button，作用是调出dos命令等（暂时）
        self.button_one = newidgets.HoverButton(self.window,
                                                width=45,
                                                image = self.icon_dos,
                                                height = 45, command =FangFa.dos)
        self.button_one.pack(side ="left", anchor ="nw")
        self.window.mainloop()
		
    def icon(self):
        """图标设置，在__init__中引入；必须加入file（arcgis10.6）"""
        self.icon_dos = tk.PhotoImage(file = paths.GifPath.gif_dos)





if __name__ == '__main__':
    a = ToolPan(tk.Tk())
    a.window.mainloop()