# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19

"""
*************************************该工具的主体界面****************************
********************************************************************************
*************************************CLASS: AppEntrance*************************
*************************************MAIN FEATURES:*****************************
                                menu: menu
                                run_toolbar_viewer: Toolbar
                                
********************************************************************************
********************************************************************************
"""
import os
import Tkinter as tk
import sys
import ttk
import tkMessageBox
from webbrowser import open as weberopen
from PIL import Image, ImageTk

exist_ttkthemes = 0
try:
    from ttkthemes import ThemedTk
    exist_ttkthemes = 1
except ImportError:
    print "NO ttkthemes"
    exist_ttkthemes = 0

# 获取当前的文件位置
# E:\move on move on\gispot\GUIs\entrance.py
realp = os.path.abspath(sys.argv[0])
print "os.path.abspath(sys.argv[0]):",os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# 该文件所处的文件夹绝对路径
realp_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = os.path.abspath(os.path.dirname(realp_dir))
print "os.path.dirname(sys.argv[0]):", os.path.dirname(sys.argv[0])
print "root_base:",root_base
# E:\move on move on\gispot\gispot
rb_GisCat = os.path.join(root_base, "gispot")
# E:\move on move on\gispot\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\gispot\GUIs\Icons
rbg_Icons = os.path.join(rb_GUIs, "Icons")
rbdoc = os.path.join(root_base, "docs")
rb_bin = os.path.join(root_base, "bin")
rb_libs = os.path.join(root_base, "Lib")
rb_GUIconfig = os.path.join(rb_libs, "gpconfig")

giscat_paths = (root_base,
                rb_GisCat,
                rb_GUIs,
                rbg_Icons,
                rbdoc,
                rb_bin,
                rb_libs,
                rb_GUIconfig)
for giscat_path in giscat_paths:
    sys.path.append(giscat_path)

# print "sys.path:",sys.path

# import LQHD # 识别不了gstrename
# from gispot.LQHD import gstrename
# from gispot.crcpy import multip_ejpg
# from gispot.crcpy import explode_mulitp
# from gispot.crcpy import task_dispatch


# 界面模块导入
import interface
# 配置包导入
from gpconfig import newGUI,hyini
from gpconfig import gppath

# Gispot图标
icon = gppath.PngIcon.icon


def kill_pid(pid):
    # 本函数用于中止传入pid所对应的进程
    if os.name == 'nt':
        # Windows系统
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        try:
            os.system(cmd)
            print(pid, 'killed')
        except Exception as e:
            print(e)
    elif os.name == 'posix':
        # Linux系统
        cmd = 'kill ' + str(pid)
        try:
            os.system(cmd)
            print(pid, 'killed')
        except Exception as e:
            print(e)
    else:
        print('Undefined os.name')


class AppEntrance(object):
    """进行打包的可视化外壳"""
    prograss_int = 0
    
    def __init__(self):
        """
         if exist_ttkthemes:
            # self.rootwindow = tk.Tk()
            self.rootwindow = ThemedTk(theme="arc")
        else:
            self.rootwindow = tk.Tk()
        self.rootwindow.title("")
        
        """

        if exist_ttkthemes:
            # self.rootwindow = tk.Tk()
            self.rootwindow = ThemedTk(theme="arc")
        else:
            self.rootwindow = tk.Tk()
            self.rootwindow.title("")
        
        # self.rootwindow = tk.Tk()
        # self.rootwindow.title("")
        # self.rootwindow.title("GISPOT")
        # self.rootwindow.update_idletasks()
        # self.rootwindow.overrideredirect(True)
        # self.rootwindow.tk_setPalette(background="#f5f6f7") # 一次性修改所有背景颜色
        newGUI.screen_cetre(self.rootwindow, width=hyini.width, height=hyini.height)
        self.rootwindow.iconbitmap(default=icon)
        self.rootwindow.resizable(1, 1)
        # self.rootwindow.attributes('-topmost', 0)
        self.gradient_bar()
        self.upgrade_from_github()
        # -------------------------------------
        # 主界面左侧图标工具栏
        # Frame的实际大小不仅仅受width控制，如果其中有其它部件，
        # 以其它部件大小为准
        self.main_face = tk.Frame(self.rootwindow, relief="sunken" ,width= 55, height = 600,bd =1)
        self.main_face.pack(side="left", fill="both", expand=True)
        # self.toolbar.place(x=0,y=0)
        # 初始界面右侧的交互界面的框架 interface_frame
        # self.interface_frame = tk.Frame(self.rootwindow, relief="groove",width= 900, height = 600)
        # self.interface_frame.pack(side="right", expand=True, fill="both")
        # self.interface_frame.place(x=55,y=0)
        
        # 绑定退出弹窗与退出功能，实现退出功能
        self.rootwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        # 界面
        # self.run_menu()
        # self.run_toolbar_viewer()
        tnb = interface.ttknotebook(self.main_face)
        interface.ToolSet(tnb.notebook2)

        self.rootwindow.mainloop()
    
    def gradient_bar(self):
        self.gradient_canv = newGUI.GradientCanvas(
            self.rootwindow, "#ffc851", "#808000", relief="flat")
        self.gradient_canv.pack(side="bottom", anchor=tk.SE, fill="x")
        self.gradient_canv.create_text(32, 10, text="gispot 1")
    
    def upgrade_from_github(self):
        def open_u():
            update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
            weberopen(update_url, new=0, autoraise=True)
        # self.image_octacat = tk.PhotoImage(file=gispotpath.PngIcon.github)
        self.image_octacat = ImageTk.PhotoImage(
            Image.open(gppath.PngIcon.github))
        ap_button = newGUI.HoverButton(master=self.gradient_canv,
                                       command=open_u, bd=2,
                                       image=self.image_octacat,
                                       width=15, height=15)
        # ap_button = ttk.Button(master=self.gradient_canv,
        # 							   command=open_u,
        # 							   image=self.image_octacat)
        ap_button.pack(side='top', expand='yes', anchor="se")
    
    # ----------------------------------------
    
    def button_config(self):
        def open_u():
            import webbrowser
            update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
            webbrowser.open(update_url, new=0, autoraise=True)
        ap_button = ttk.Button(text=u"获取更新",command=open_u)
        ap_button.pack(side='top', expand='yes', anchor="se")
    
    def on_closing(self):
        # 退出确认功能，防止误触发
        if tkMessageBox.askokcancel("Quit", "   Do you want to quit?"):
            self.rootwindow.destroy()
