# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/5
# python2 arcgis10.6
"""填充程序的主要界面，就是菜单栏下的大片区域，该模块会被entrance.py文件导入并生效"""
import os
import tkinter as tk
from TkGUIconfig import newidgets
from TkGUIconfig import paths
from commandorder import export

class FangFa(object):
    """方法。      方法函数的集合，哈哈哈哈"""
    def dos(self):
        export.export()


class Panel(object):
    """
    程序初始界面的主要部分的布局
    dos按键的布局
    """
    def __init__(self,master):
        self.icon()
        self.window = master
        self.button = newidgets.HoverButton(self.window,
                                            image = self.icon_dos,
                                            width = 45,
                                            height = 45,command =FangFa.dos)
        self.button.pack(side ="right",anchor = "ne")
        self.window.mainloop()
		
    def icon(self):
        """图标设置，在__init__中引入；必须加入file（arcgis10.6）"""
        self.icon_dos = tk.PhotoImage(file = paths.GifPath.gif_dos)





if __name__ == '__main__':
    a = Panel(tk.Tk())
    a.window.mainloop()