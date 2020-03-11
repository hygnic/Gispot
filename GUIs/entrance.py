# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19
"""该工具的主体界面"""
import os
import Tkinter as tk
import sys
import ttk
import tkMessageBox
from webbrowser import open as weberopen

# from PIL import Image, ImageTk


# 获取当前的文件位置
# E:\move on move on\gispot\GUIs\entrance.py
realp = os.path.abspath(__file__)
# 该文件所处的文件夹绝对路径
realp_dir = os.path.abspath(os.path.dirname(__file__))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# E:\move on move on\gispot\gispot
rb_GisCat = os.path.join(root_base, "gispot")
# E:\move on move on\gispot\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\gispot\GUIs\Icons
rbg_Icons = os.path.join(rb_GUIs, "Icons")
rbdoc = os.path.join(root_base, "docs")
rb_bin = os.path.join(root_base, "bin")
rb_libs = os.path.join(root_base, "libs")

giscat_paths = [root_base,
                rb_GisCat,
                rb_GUIs,
                rbg_Icons,
                rbdoc,
                rb_bin,
                rb_libs]
for giscat_path in giscat_paths:
    sys.path.append(giscat_path)

# import ccname # 识别不了gstrename

# from gispot.ccname import gstrename
# from gispot.crcpy import multip_ejpg
# from gispot.crcpy import explode_mulitp
# from gispot.crcpy import task_dispatch
# 界面模块导入
import mainlayout
# 功能模块导入
import ccname.gstrename
import crcpy.multiplexport
import crcpy.explode
import crcpy.task_dispatch
import commandorder.export
# 配置包导入
from TkGUIconfig import newidgets
from TkGUIconfig import paths


import Tix
# from Tkconstants import *
class AppEntrance(object):
    """进行打包的可视化外壳"""
    prograss_int = 0
    def __init__(self):
        self.rootwindow = tk.Tk()
        self.rootwindow.title(u"主界面")
        newidgets.screen_cetre(self.rootwindow, width=1192, height=650)
        self.rootwindow.iconbitmap(default=
                                   os.path.join(rbg_Icons,"icon.ico"))
        # self.rootwindow.resizable(False, False)
        self.menu()
        # bt.config()
        # bt.pack(side='left')
        # self.rootwindow.attributes('-topmost', 0)
        self.gradient_bar()
        self.upgrade_from_github()
        # -------------------------------------
        # cmb = ttk.Menubutton(self.rootwindow, text="io")
        # cmb.pack()
        #
        # image_octacat = Tix.ComboBox(self.rootwindow)
        # aa1 = Tix.ComboBox(image_octacat)
        # image_octacat.pack()
        # aa1.pack()
      
        # -------------------------------------
        self.main_f = tk.Frame(self.rootwindow,relief = "groove")
        self.main_f.pack(expand = True,fill ="both")
       
        self.rootwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        # 安排界面格局
        self.run_menu()
        self.run_panel()
    
    def prograssbar(self):
        self.prograss_int +=10
        bb = Tix.Meter(self.main_f, value=self.prograss_int,
                       fillcolor="#ffc851")
        bb.pack()
        # impure_data = 0
        # for i in xrange(10):
        #     time.sleep(2)
        #     bb["value"] = i * 10 + impure_data
        #
       
    def gradient_bar(self):
        self.gradient_canv = newidgets.GradientCanvas(self.rootwindow,
                                                  "#ffc851", "#808000", relief= "flat")
        self.gradient_canv.pack(side="bottom", anchor=tk.SE, fill="x")
        self.gradient_canv.create_text(32,18,text = "gispot 1")
    
    def upgrade_from_github(self):
        def open_u():
            update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
            weberopen(update_url, new=0, autoraise=True)
        self.image_octacat = tk.PhotoImage(file = paths.GifPath.gif_github)
        ap_button = newidgets.HoverButton(master=self.gradient_canv,
                                          command=open_u, bd = 2,
                                          image = self.image_octacat,
                                          width = 30, height = 30)
        ap_button.pack(side='top', expand='yes', anchor="se")
        # exxp = tk.Text(self.gradient_canv,height = 1)
        # exxp.pack()
        # exxp.insert("end","im ok")
    
    
    def menu(self):
        """设置置顶菜单栏"""
        self.menubar = tk.Menu(self.rootwindow,background = "#808000")
        #创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，# Exit功能项）
        self.menubar_file = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='File', menu=self.menubar_file)
        # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，
            # 每一个小菜单对应命令操作。
        self.menubar_file.add_command(label='New', command=None)
        self.menubar_file.add_command(label='Open', command=None)
        self.menubar_file.add_command(label='Save', command=None)
        self.menubar_file.add_command(label='Prograss Bar',
                                      command=self.prograssbar)
        self.menubar_file.add_separator()  # 添加一条分隔线
        self.menubar_file.add_command(label='Exit',
                                 command=self.rootwindow.quit)  # 用tkinter里面自带的quit()函数
        submenu = tk.Menu(self.menubar_file)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
        # 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
        submenu.add_command(label='Submenu_1',
                            command=None)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
        # 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
        # 创建第二级菜单，即菜单项里面的菜单
        self.menubar_file.add_cascade(label='Import', menu=submenu,
                                 underline=0)  # 给放入的菜单submenu命名为Import
        # edit菜单栏
        self.menubar_edit = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='Edit', menu=self.menubar_edit)
        self.menubar_edit.add_command(label='Cut', command=None)
        self.menubar_edit.add_command(label='Copy', command=None)
        self.menubar_edit.add_command(label='Paste', command=None)
        
        # 两区公示图 菜单栏
        self.menubar_gst = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = u"两区公示图", menu=self.menubar_gst)
        self.menubar_gst.add_command(label=u'公示图命名规范化',
                                command=self.open_GSTrename)
        
        # 制图mapping菜单栏
        self.menubar_map = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=u"制图", menu=self.menubar_map)
        self.menubar_map.add_command(label=u'多进程批量出图(JPEG)',
                                command=self.open_Multip_exp)
        self.menubar_map.add_command(label=u'批量出图(JPEG;ONGOING)',
                                     command=None)
        self.menubar_map.add_command(label=u'拆分多部件',
                                     command=self.explode_mulitp)
        self.menubar_map.add_command(label=u'任务分配',
                                     command=self.start_dispatch_task)
        # 关于 栏
        self.menubar_about = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=u"关于", menu=self.menubar_about)
        self.menubar_about.add_command(label=u'获取更新',
                                     command=self.upgrade_from_github)
        
    # 配置安放菜单栏，写成方法便于调控纯程序
    def run_menu(self):
        self.rootwindow.config(menu=self.menubar)
    
    # def trans_name(self):
    #     """
    #     之前要将四川标准的图片名称改为国家标准的名称，
    #     没用上，以后也没有用了
    #     """
    #     def open_gst_trans():
    #         from ccname import gst_trans
    #         open_gst_trans = gst_trans.App()
    #         open_gst_trans.window.mainloop()
    #
    #     def open_fbt_trans():
    #         from ccname import fbt_trans
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
    def open_GSTrename(self):
        newidgets.destroy_chird(self.main_f)
        # gstrename.App(self.main_f)
        ccname.gstrename.App(self.main_f)
    
    def open_Multip_exp(self):
        newidgets.destroy_chird(self.main_f)
        # multip_ejpg.MultipExp(self.main_f)
        crcpy.multiplexport.MultipExp(self.main_f)

    def explode_mulitp(self):
        newidgets.destroy_chird(self.main_f)
        # explode_mulitp.App(self.main_f)
        crcpy.explode.App(self.main_f)
    
    def start_dispatch_task(self):
        newidgets.destroy_chird(self.main_f)
        # task_dispatch.StartApp(self.main_f)
        crcpy.task_dispatch.StartApp(self.main_f)
    # ----------------------------------------
    
    def run_panel(self):
        # 使程序主要面板运行起来
        button1 = mainlayout.Panel(self.main_f)
        button1.config()
        
        
        
    def button_config(self):
        def open_u():
            import webbrowser
            update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
            webbrowser.open(update_url, new=0, autoraise=True)
        ap_button = ttk.Button(text = u"获取更新",command = open_u)
        ap_button.pack(side='top', expand='yes',anchor = "se")

    def on_closing(self):
        # 退出确认功能，防止误触发
        if tkMessageBox.askokcancel("Quit", "   Do you want to quit?"):
            self.rootwindow.destroy()

    
    










# if __name__ == '__main__':
#     app = AppEntrance()
#     app.rootwindow.mainloop()