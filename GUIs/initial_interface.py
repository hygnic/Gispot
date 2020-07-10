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
………………………………………………………………………………………………Description………………………………………………………………………………………
………………………………………………………………………………………………Description………………………………………………………………………………………
Usage:
# ---------------------------------------------------------------------------
"""

import Tkinter as tk
import ttk
from PIL import ImageTk,Image

from GUIconfig import newidgets
from GUIconfig.guisetting import PngIcon,GifPath,Colour
import vitems
from crcpy import save_acopy


class InitialInterface(object):
    """
    entrance界面左侧的toolbar区域以及entrance界面右侧的viewer中的工具，脚本等
    """
    def __init__(self, master1,master2):
        
        # 引入toolbar中的图标
        self.interface_image()
        self.window1 = master1 # 左边
        self.window2 = master2 # 右边
        # 第yi个button,仅仅是一个查看器，方便复制到arcpy的Python脚本栏等
        self.button_viewer = newidgets.HoverButton(self.window1,
                                                   width=45, height=45,
                                                   image = self.icon_editor,
                                                   command =self.first_viewer)
        self.button_viewer.pack(side ="top", anchor ="nw")
        # 第er个button，作用是调出dos命令等（暂时）
        self.button_dos = newidgets.HoverButton(self.window1,
                                                width=45, height = 45,
                                                image = self.icon_dos,
                                                command =self.second_viewer)
        self.button_dos.pack(side ="top", anchor ="nw")
        # Tool button,the Third button which shows some features button
        self.button_tool = newidgets.HoverButton(self.window1,msg= "Tools",
                                                width=45, height=45,
                                                image=self.icon_tool,
                                                command=self.open_viewer3)
        self.button_tool.pack(side="top", anchor="nw")
        
		
    def interface_image(self):
        """初始界面左侧的 toolbar 图标；tk.PhotoImage必须加入file（arcgis10.6）"""
        # <PIL>
        self.icon_dos = tk.PhotoImage(file = GifPath.dos)
        # 对应second_viewer
        self.icon_editor = tk.PhotoImage(file=GifPath.editor)
        # self.icon_tool = tk.PhotoImage(file=paths.GifPath.tool)
        self.icon_tool = ImageTk.PhotoImage(Image.open(PngIcon.toolbox_45))
        self.toolset = ImageTk.PhotoImage(Image.open(PngIcon.toolset_image))
        # dd = paths.PngIcon()
        # self.circle= dd.circle_icon_fun()

        
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
        ToolSet(self.window2)
        # Third_Viewer(self.window2, self.circle)
        
    # -------------------------
    # 将带有参数的类变成方法和button绑定
    # def show_first_viewer(self):

# def func1():
#     # name: 坐标系转换
#     print "func1"
#
# def func2():
#     # name: Excel转shp
#     print "func2"
#
#
# def func3():
#     # name: 坐标系转换
#     print "func1"
#
#
# def func4():
#     # name: Excel转shp
#     print "func2"
#
# func_name = {
# 	u"顺序":(
# 		u"转换工具",u"高标准农田"
# 	),
#     u"转换工具":(
#         (func1,u"坐标系转换"),
#         (func2,u"Excel转shp")
#     ),
#     u"高标准农田":(
#         (func3,u"坐标系转换2"),
#         (func4,u"Excel转shp2")
#     )
# }

# func_name2 = OrderedDict()
# func_name2[u"转换工具"] = (
#         (func1,u"坐标系转换"),
#         (func2,u"Excel转shp")
#     )
# func_name2[u"高标准农田"] =  (
#         (func3,u"坐标系转换2"),
#         (func4,u"Excel转shp2")
#     )
# # func_name2 = (u"转换工具",((func1,u"坐标系转换"),(func2,u"Excel转shp")),u"高标准农田",((func3,u"坐标系转换2"),(func4,u"Excel转shp2")))
#
# for k,v in func_name2.items():
#     print k,v

        
class ToolSet(object):
    """
    用于显示工具箱button中的内容
    点击工具箱button启动该类
    """
    
    def __init__(self, master):
        """
        :param master: tkinter 父部件
        """
        self.master = master
        self.white_light = Colour.white_light
        self.icon = ImageTk.PhotoImage(Image.open(PngIcon.toolset_image))
        frames = self.main_widget(self.make_test_dict())
        # for a_f in frames:
        #     a_f.bind("<Enter>", self.on_enter)

    # def on_enter(event):
    #     labelframe["relief"] = "groove"
    #
    # def on_leave(event):
    #     labelframe["relief"] = "flat"
    #
    # labelframe.bind("<Enter>", on_enter)
    # labelframe.bind("<Leave>", on_leave)
    
    
    def main_widget(self,funcs):
        """
         funcs(Dict): a function which return a dictionary containing feature widget(function)
         such as :
            def make_test_dict(self):
                func_name = {
                    u"顺序": (
                        u"转换工具", u"高标准农田"
                    ),
                    u"转换工具": (
                        (self.test_func1, u"坐标系转换"),
                        (self.test_func2, u"Excel转shp")
                    ),
                    u"高标准农田": (
                        (self.test_func3, u"坐标系转换2"),
                        (self.test_func4, u"Excel转shp2")
                    )
                }
                return func_name
        :return:
        """
        _widgets_l = []
        # The order of tool frame type:List
        frame_order = funcs[u"顺序"]
        for i in frame_order:
            feature_set = funcs[i] # ((func3, u"坐标系转换2"),(func4, u"Excel转shp2"))
        
            # font=('Times',10,'bold','italic') # ,bg="#5294e2"
            # foreground="#5294e2", background= "#ffffff" #f5f6f7 SystemWindow
            # tk.LabelFrame; newidgets.NeewwLabelFrame
            labelframe = newidgets.NeewwLabelFrame(
                self.master, text=i, labelanchor="nw",width=10,
                relief="flat",borderwidth =3,background= self.white_light)
            labelframe.pack(anchor="nw",fill="x")
            # print labelframe.winfo_class() # Labelframe
            
            _widgets_l.append(labelframe)
            # A SET OF BUTTONS**************************************************
            for a_feature in feature_set:
                tool_func = a_feature[0]
                # print "tool_func:",tool_func
                tool_name = a_feature[1]
            
                frame = tk.Frame(labelframe, relief="flat",background= self.white_light)
                frame.pack(anchor = "w",side="left") # 保证横向排列
                # frame.grid()
                # print "frame.grab_set():",frame.grab_set() # None
                # tk.LabelFrame
                button1_1 = newidgets.HoverButton(frame,background= self.white_light,
                                                  width=38,
                                                  image=self.icon,
                                                  height=38,
                                                  command=tool_func)
                button1_1.pack(side="top", anchor="center")
                label = tk.Label(frame, text=tool_name,width=10,background= self.white_light)
                label.pack()
            #*******************************************************************
    
        return _widgets_l

        
        
        
        
    def button1(self):
        newidgets.destroy_child(self.master)
        save_acopy.SaveACopy(self.master)
        
    def test_func1(self):
        # name: 坐标系转换
        print "func1"

    def test_func2(self):
        # name: Excel转shp
        print "func2"

    def test_func3(self):
        # name: 坐标系转换
        print "func1"

    def test_func4(self):
        # name: Excel转shp
        print "func2"
    
    def make_test_dict(self):
        func_name = {
            u"顺序": (
                u"转换工具", u"高标准农田"
            ),
            u"转换工具": (
                (self.test_func1, u"坐标系转换"),
                (self.test_func2, u"Excel转shp")
            ),
            u"高标准农田": (
                (self.test_func3, u"坐标系转换2"),
                (self.test_func4, u"Excel转shp2")
            )
        }
        return func_name