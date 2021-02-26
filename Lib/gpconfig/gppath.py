#!/usr/bin/env python
# -*- coding:utf-8 -
# python2 arcgis10.6
"""
# Author: LiaoChenchen,hygnic
# Created on: 2019/11/30
# Reference:
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description:……………………………………………………………………………………
1.图片地址的配置
2.GUI 界面的颜色配置
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description………………………………………………………………………………………
Usage:
# ---------------------------------------------------------------------------
"""

# 锚点文件,从__file__改用sys.args[0]
import os
import sys

# from PIL import  ImageTk,Image
# import Tkinter as tk


# 不使用该方法
_paths_gispot = os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# print "_paths_gispot:",_paths_gispot
_paths_bin = os.path.dirname(_paths_gispot)  # G:\MoveOn\Gispot_copy\bin
_Groot = os.path.dirname(_paths_bin)  # E:\move on move on\gispot
_GUIs_p = os.path.join(_Groot, "GUIs")
Docs_p = os.path.join(_Groot, "docs")
base_icons_path = os.path.abspath(os.path.join(_GUIs_p, "Icons")) # E:\move on move on\gispot\GUIs\Icons
# Docs_p = _Docs_p # 测试用2020 0914

# G:\MoveOn\GUIs\Icons\GitHub_32.gif
# docs

# root = os.path.abspath(os.path.dirname(sys.argv[0]))
# _docs_p = os.path.join(root,"docs")
# _explode_mulitp = os.path.join(_docs_p, r"explode.gc")
# _gstrename = os.path.join(_docs_p, r"multiplexport.gc")
# _multip_ejpg = os.path.join(_docs_p, r"multiplexport.gc")
# _path_bin = os.path.dirname(sys.argv[0])  # G:\MoveOn\Gispot\bin
# _path_root = os.path.dirname(_path_bin)  # G:\MoveOn\Gispot
# _GUIs_p = os.path.join(_path_root, "GUIs")
# base_icons_path = os.path.abspath(os.path.join(_GUIs_p, "Icons"))

def code2exe():
    """配置doc文件和图片，用于py2exe封装"""
    global base_icons_path
    global Docs_p
    # py2exe_path = "images"
    base_icons_path = "images"
    Docs_p = "gisdocs"
# 不封装时关闭该函数
# code2exe()


class GifPath(object):
    """
    gif图片的路径
    """
    # base_icons_path
    forbid = os.path.join(base_icons_path, "forbit.gif")
    close = os.path.join(base_icons_path, "close30_4.gif")
    folder = os.path.join(base_icons_path, "folder1.gif")
    
    textfile = os.path.join(base_icons_path, "Text_File16.gif")
    add_file = os.path.join(base_icons_path, "file3.gif")
    
    info = os.path.join(base_icons_path, "help_info_3.gif")
    confirm = os.path.join(base_icons_path, "confirm32_9.gif")
    
    github = os.path.join(base_icons_path, "GitHub_32.gif")
    # gif_github= os.path.join(ur"G:\MoveOn\Gispot_copy\bin\dist\images", "GitHub_32.gif")
    # gif_github= os.path.join(ur"images", "GitHub_32.gif")
    
    empty1 = os.path.join(base_icons_path, "empty.gif")
    # gif_test= os.path.join(base_icons_path, "folder_1.gif")
    
    # 应用于toolbar中的按钮图标
    dos = os.path.join(base_icons_path, "dos.gif")
    editor = os.path.join(base_icons_path, "editor.gif")
    tool = os.path.join(base_icons_path, "toolbox.gif")

# def __init__(self):
# 	self.addfile = tk.PhotoImage(file=self.gif_add_file)


# G:\MoveOn\Gispot\docs
# class DocPath(object):
# 	# doc_me = os.path.join(Docs_p, "multiplexport.gc")
# 	# doc_em = os.path.join(Docs_p, "explode.gc")
# 	doc_trans_fbt = os.path.join(Docs_p, "trans_fbt.gc")
# 	doc_trans_gst = os.path.join(Docs_p, "trans_gst.gc")
# 	doc_gstrename = os.path.join(Docs_p, "gstrename.gc")
# 	doc_task_dispatch = os.path.join(Docs_p, "task_dispatch.gc")
# 	doc_ZLDJ = os.path.join(Docs_p, "ZLDJ.gc")


class PngIcon(object):
    folder1 = os.path.join(base_icons_path, "folder3.png") # 最新使用的
    folder2 = os.path.join(base_icons_path, "folder2.png")
    empty = os.path.join(base_icons_path, "empty.gif")
    empty2 = os.path.join(base_icons_path, "empty2.jpg")
    sheet = os.path.join(base_icons_path, "sheet_28.png")
    icon = os.path.join(base_icons_path, "icon.ico")
    shapefile = os.path.join(base_icons_path, "shp_28.png")
    mxd = os.path.join(base_icons_path, "mxd_28.png")
    text = os.path.join(base_icons_path, "text_28.png")
    github = os.path.join(base_icons_path, "GitHub_15.png")
    
    # 主界面左边工具栏及其相应子界面的图标
    toolbox_45 = os.path.join(base_icons_path, "toolbox-45.png")
    home=os.path.join(base_icons_path, "home45.png")
    
    # 功能函数界面下方三个图标
    OK =os.path.join(base_icons_path, "ok_28.png")
    help_info =os.path.join(base_icons_path, "info_28.png")
    cancel =os.path.join(base_icons_path, "quit_cancel_28.png")


if __name__ == '__main__':
    aa = GifPath.github
    print os.path.exists(aa)
