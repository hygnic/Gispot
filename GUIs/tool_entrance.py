# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19

import os
import Tkinter as tk
import sys
import ttk
# from PIL import Image, ImageTk


# 获取程序当前的文件夹位置
# E:\move on move on\Gispot\GUIs\tool_entrance.py
realp = os.path.abspath(__file__)
# 上级 绝对路径
# E:\move on move on\Gispot
root_base = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# E:\move on move on\Gispot\Gispot
rb_GisCat = os.path.join(root_base, "Gispot")
# E:\move on move on\Gispot\GUIs
rb_GUIs = os.path.join(root_base, "GUIs")
# E:\move on move on\Gispot\GUIs\Icons
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
from ccname import gstrename
from ccarcpy import multip_ejpg
from ccarcpy import explode_mulitp

# 配置包导入
from hyconf import GUIutils

class AppEntrance(object):
    """进行打包的可视化外壳"""
    def __init__(self):
        self.rootwindow = tk.Tk()
        self.rootwindow.title(u"主界面")
        GUIutils.screen_cetre(self.rootwindow, width=700, height=500)
        self.rootwindow.iconbitmap(default=os.path.join(rbg_Icons,"cpt2.ico"))
        self.menu()
        # bt.config()
        # bt.pack(side='left')
        # self.rootwindow.attributes('-topmost', 0)
        self.button_config()
        
        # 放最后
        self.menu_run()
    # @property
    # def pp(self):
    #     return self.rootwindow
        
    
    def menu(self):
        """设置置顶菜单栏"""
        # window = tk.Tk()
        # window.title('My Window')
        # window.geometry('500x300')
        label_uesless = tk.Label(self.rootwindow, bg='olive')
        label_uesless.pack(side = "bottom",anchor = tk.SE, fill = "x")
        self.counter = 0
        def do_job():
            # counter = 0
            label_uesless.config(text=str(self.counter) + '  time!')
            self.counter += 1
        # 创建菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
        self.menubar = tk.Menu(self.rootwindow)
        # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，
            # Exit功能项）
        self.menubar_file = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='File', menu=self.menubar_file)
        # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，
            # 每一个小菜单对应命令操作。
        self.menubar_file.add_command(label='New', command=do_job)
        self.menubar_file.add_command(label='Open', command=do_job)
        self.menubar_file.add_command(label='Save', command=do_job)
        self.menubar_file.add_separator()  # 添加一条分隔线
        self.menubar_file.add_command(label='Exit',
                                 command=self.rootwindow.quit)  # 用tkinter里面自带的quit()函数
        submenu = tk.Menu(self.menubar_file)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
        # 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
        submenu.add_command(label='Submenu_1',
                            command=do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
        # 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
        # 创建第二级菜单，即菜单项里面的菜单
        self.menubar_file.add_cascade(label='Import', menu=submenu,
                                 underline=0)  # 给放入的菜单submenu命名为Import
        # edit菜单栏
        self.menubar_edit = tk.Menu(self.menubar, tearoff=0)
        # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='Edit', menu=self.menubar_edit)
        # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元,
            # 就会触发do_job的功能
        self.menubar_edit.add_command(label='Cut', command=do_job)
        self.menubar_edit.add_command(label='Copy', command=do_job)
        self.menubar_edit.add_command(label='Paste', command=do_job)
        
        # 制图mapping菜单栏
        self.menubar_gst = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = u"两区公示图", menu=self.menubar_gst)
        self.menubar_gst.add_command(label=u'公示图命名规范化',
                                command=self.open_GSTrename)
        
        
        # 创建菜单栏完成后，配置让菜单栏self.menubar显示出来
        self.menubar_map = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=u"制图", menu=self.menubar_map)
        self.menubar_map.add_command(label=u'多进程导图JPEG',
                                command=self.open_Multip_exp)
        self.menubar_map.add_command(label=u'拆分多部件',
                                     command=self.explode_mulitp)
    # 配置安放菜单栏，写成方法便于调控纯程序
    def menu_run(self):
        self.rootwindow.config(menu=self.menubar)
        
    def trans_name(self):
        """
        之前要将四川标准的图片名称改为国家标准的名称，
        没用上，以后也没有用了
        """
        def open_gst_trans():
            from ccname import gst_trans
            open_gst_trans = gst_trans.App()
            open_gst_trans.window.mainloop()

        def open_fbt_trans():
            from ccname import fbt_trans
            open_fbt_trans = fbt_trans.App()
            open_fbt_trans.window.mainloop()
        
        # 图件命名转换 菜单栏
        self.menubar_trans = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=u"两区图件名称装换", menu=self.menubar_trans)
        self.menubar_trans.add_command(label=u'公示图名称',
                                  command=open_gst_trans)
        self.menubar_trans.add_command(label=u'分布图名称',
                                  command=open_fbt_trans)
        # self.menubar_trans.add_command(label=u'标志牌名称'）
        
        # 创建菜单栏完成后，配置让菜单栏self.menubar显示出来
        self.rootwindow.config(menu=self.menubar)


        
    
    @staticmethod
    def open_GSTrename():
        GST_app = gstrename.App()
        GST_app.window.mainloop()
    
    @staticmethod
    def open_Multip_exp():
        mul_app = multip_ejpg.MultipExp()
        mul_app.window.mainloop()

    @staticmethod
    def explode_mulitp():
        explode_app = explode_mulitp.App()
        # explode_app.window.mainloop()
        

    
    def button_config(self):
        def open_u():
            import webbrowser
            update_url = r"https://github.com/hygnic/GisCat/archive/master.zip"
            webbrowser.open(update_url, new=0, autoraise=True)
        ap_button = ttk.Button(text = u"获取更新",command = open_u)
        ap_button.pack(side='top', expand='yes',anchor = "se")

        
        
    


# if __name__ == '__main__':
#     app = AppEntrance()
#     app.rootwindow.mainloop()