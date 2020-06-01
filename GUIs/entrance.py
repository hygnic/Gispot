# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/19
"""该工具的主体界面"""
import os
import Tkinter as tk
import sys
import ttk
import tkMessageBox
import tkFileDialog
import ScrolledText as stt
from webbrowser import open as weberopen

# from PIL import Image, ImageTk


# 获取当前的文件位置
# E:\move on move on\gispot\GUIs\entrance.py
realp = os.path.abspath(sys.argv[0])
print "os.path.abspath(sys.argv[0]):",os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# 该文件所处的文件夹绝对路径
realp_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
# 上级 绝对路径
# E:\move on move on\gispot
root_base = os.path.abspath(os.path.dirname(realp_dir))
print "os.path.dirname(sys.argv[0]):",os.path.dirname(sys.argv[0])
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
rb_GUIconfig = os.path.join(rb_libs, "GUIconfig")

giscat_paths = [root_base,
                rb_GisCat,
                rb_GUIs,
                rbg_Icons,
                rbdoc,
                rb_bin,
                rb_libs,
                rb_GUIconfig]
for giscat_path in giscat_paths:
    sys.path.append(giscat_path)
print "sys.path:",sys.path

# import LQHD # 识别不了gstrename

# from gispot.LQHD import gstrename
# from gispot.crcpy import multip_ejpg
# from gispot.crcpy import explode_mulitp
# from gispot.crcpy import task_dispatch
# 界面模块导入
import initial_interface
# 功能模块导入
import LQHD.gstrename
import crcpy.multiplexport
import crcpy.explode
import crcpy.task_dispatch
import ccmd.export
# 配置包导入
from GUIconfig import newidgets
from GUIconfig import paths


import Tix
# from Tkconstants import *
class AppEntrance(object):
    """进行打包的可视化外壳"""
    prograss_int = 0
    def __init__(self):
        self.rootwindow = tk.Tk()
        self.rootwindow.title("GISPOT")
        newidgets.screen_cetre(self.rootwindow, width=1192, height=650)
        # self.rootwindow.iconbitmap(default=
        #                            os.path.join(rbg_Icons,"icon.ico")) #TODO 暂时关闭图标
        self.rootwindow.resizable(False, False)
        self.menu()
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
        # 主界面左侧图标工具栏
                        # Frame的实际大小不仅仅受width控制，如果其中有其它部件，
                            # 以其它部件大小为准
        self.toolbar = tk.Frame(self.rootwindow, relief="sunken" ,width= 80, bd =1)
        self.toolbar.pack(side="left",fill = "both", expand =False)
        # 初始界面右侧的交互界面的框架 interface_frame
        self.interface_frame = tk.Frame(self.rootwindow, relief ="groove")
        self.interface_frame.pack(side="right", expand =True, fill ="both")
        
        # 绑定退出弹窗与退出功能，实现退出功能
        self.rootwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        # 界面
        self.run_menu()
        self.run_toolbar_viewer()
    
    def prograssbar(self):
        self.prograss_int +=10
        bb = Tix.Meter(self.interface_frame, value=self.prograss_int,
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
        print paths.GifPath.gif_github
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
        self.menubar_file.add_separator()  # 分隔线
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
    #         from LQHD import gst_trans
    #         open_gst_trans = gst_trans.App()
    #         open_gst_trans.window.mainloop()
    #
    #     def open_fbt_trans():
    #         from LQHD import fbt_trans
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
    """
    全是一些按键的command指令，放在这里方便添加修改一些自定义功能
    使用的各种函数方法说明：
        newidgets.destroy_child(self.main_f): 在打开一个功能的GUI界面时，销毁覆盖
            之前存在的GUI界面
    """
    def open_GSTrename(self):
        newidgets.destroy_child(self.interface_frame)
        # gstrename.App(self.main_f)
        LQHD.gstrename.App(self.interface_frame)
    
    def open_Multip_exp(self):
        newidgets.destroy_child(self.interface_frame)
        # multip_ejpg.MultipExp(self.main_f)
        crcpy.multiplexport.MultipExp(self.interface_frame)
    
    # 多进程导出JPEG图片
    def explode_mulitp(self):
        newidgets.destroy_child(self.interface_frame)
        # explode_mulitp.App(self.main_f)
        crcpy.explode.App(self.interface_frame)
    
    def start_dispatch_task(self):
        newidgets.destroy_child(self.interface_frame)
        # task_dispatch.StartApp(self.main_f)
        crcpy.task_dispatch.StartApp(self.interface_frame)
    # ----------------------------------------
    
    def run_toolbar_viewer(self):
        # 使程序主要面板运行起来
        # return 1
        # toolbar_viewer就是建立在input_interface上的
        button1 = initial_interface.InitialInterface(self.toolbar, self.interface_frame)
        # button1.config()
        
        
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


class Tooltk(object):
    """工具的GUI界面"""
    _button_size = 24
    
    # 调用类变量也要加self
    def __init__(self, master, help_path, confirm_method):
        """
		:param master:
		:param help_path: 帮助文档的路径
		:param confirm_method: 按下确认键后的响应事件
		"""
        self.block_list = []
        self.window = master
        # self.window.remove_sth(window_name)
        self.helppath = help_path
        self.confirm_method = confirm_method
        # self.window.overrideredirect(True)
        # 给Toplevel窗口设置透明度
        # self.window.attributes('-alpha',0.5)
        # 设置窗口置顶优先度
        # self.window.attributes('-topmost', 1)
        # self.window = tk.Tk()
        # GUIutils.screen_cetre(self.window, width=800, height=660)
        # self.window.iconbitmap(default=os.path.dirname(sys.argv[0])+
        # 							   "/Icons/toolbox.ico")
        # 重新抓取设置，使Toplevel显示在最上面
        # self.window.grab_set()
        # self.window.grab_release()
        # self.window.resizable(False, False)
        # self.input_str_1 = tk.StringVar()
        # self.input_str_2 = tk.StringVar()
        # self.input_int = tk.IntVar()
        self.color_mylife()  # 颜色
        self.icon_set()  # 配置图片
        self.create_frames()  # 配置框架
        self.create_button()  # 配置按钮
        # color   "SystemHighlight","SystemMenuText"
        self.read_help()
    
    def color_mylife(self):
        self.color1 = "#F1F1F1"  # 帮助栏颜色
        self.color5 = "#808000"  # 橄榄色，显示text
        self.color3 = "#F1F1F1"  # 主框的上半部分颜色 侧栏颜色
        # self.color4 = "Cornsilk" # 侧栏颜色
        self.color2 = "#E1E1E1"  # 茶色 较深
        self.color6 = '#EBEEEE'  # 底栏颜色
    
    def icon_set(self):
        # 必须加file参数，不然不显示图片（arcgis10.6）
        self.gif_text = tk.PhotoImage(file=paths.GifPath.gif_textfile)
        self.gif_addfile = tk.PhotoImage(file=paths.GifPath.gif_add_file)
        
        self.gif_folder = tk.PhotoImage(file=paths.GifPath.gif_folder)
        self.gif_close = tk.PhotoImage(file=paths.GifPath.gif_close)
        self.gif_quit = tk.PhotoImage(file=paths.GifPath.gif_close)
        self.gif_help = tk.PhotoImage(file=paths.GifPath.gif_info)
        self.gif_confirm = tk.PhotoImage(file=paths.GifPath.gif_confirm)
        
        self.gif_empty_1 = tk.PhotoImage(file=paths.GifPath.gif_empty1)
        # self.gif_empty_2 = tk.PhotoImage(file=gispotpath.GifPath.gif_empty2)
        
        # ph = tk.PhotoImage(file=gispotpath.GifPath.gif_confirm)
        # self.gif_check_green16 =  ph.zoom(x= 2,y = 2)
        # self.gif_check_green16 =  ph.subsample(x= 40,y=40)
        
        """
		使用pillow设置按键图标
		from PIL import Image, ImageTk
		self.gif_comfirm = ph
		# test
		im = Image.open(r"E:\move on move on\Gispot\GUIs\66.png")
		self.ph_im = ImageTk.PhotoImage(im)
		"""
    
    def create_frames(self):
        # 1192/2 = 596
        # 右边的主框
        self.frame_right_side = tk.Frame(self.window, width=496,
                                         border=0, relief="flat")
        self.frame_right_side.pack(side="right",
                                   expand=True, fill="both")
        # self.frame_right_side.propagate(False)
        # 左边的主框
        self.frame_left_side = tk.Frame(self.window, width=696,
                                        border=0, relief="flat")
        self.frame_left_side.pack(side="left",
                                  expand=True, fill="both")
        # 里面 的 上部分
        self.frame_major = tk.Frame(self.frame_left_side, width=696,
                                    relief="flat")
        self.frame_major.pack(expand=True, fill="both")
        # 主框下的底部栏
        self.frame_bottom_bar = tk.Frame(self.frame_left_side, height="60",
                                         bg=self.color6)  # ffc851
        # self.frame_bottom_bar.pack_propagate(0)
        self.frame_bottom_bar.pack(expand=False, fill="both")
        # expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
        # x轴（左右）方向上会拉伸
        # 左边主框中的帮助信息
        help_f = tk.Frame(self.frame_major,
                          relief=tk.GROOVE, bd=2, padx=3)
        # help_f.pack_propagate(0)
        help_f.pack(side=tk.BOTTOM, anchor="s",
                    expand=True, fill="both")
        # 设置带滚动条的text
        s_bar = tk.Scrollbar(help_f, relief="flat",
                             elementborderwidth=-15)
        s_bar.pack(side="right", fill="y")
        self.help_text = newidgets.NeewwText(help_f, relief=tk.FLAT, height=20,
                                             fg=self.color5,
                                             yscrollcommand=s_bar.set)
        
        self.help_text.pack(expand=True, fill="both")
        s_bar.config(command=self.help_text.yview)
        
        """"
			右边主框插入文本框，文本框分成上下两部分，上部分显示固定的信息，
		下半部分显示动态信息"""
        # 上栏
        self.text = stt.ScrolledText(self.frame_right_side, height="10",
                                     width="90")
        # 不起作用，将所用txt都标记了
        # self.text.tag_add("tag1","1.end","2.end")
        self.text.insert(tk.END,
                         "Python 2.7.12 (v2.7.12:d33e0cf91556,Jun 27 2016, "
                         "15:19:22) author: Liaochenchen 2019#00#00")  # ,"tag1"
        # self.text.tag_config("tag1",underline = True,foreground = "Ivory")
        self.text.pack(side="top", anchor="n", expand=True, fill="both",
                       padx=2)
        # 下栏 主要的动态信息显示栏
        s_bar = tk.Scrollbar(self.frame_right_side, relief="flat",
                             elementborderwidth=-15)
        s_bar.pack(side="right", fill="y")
        self.text_major_msg = newidgets.NeewwText(self.frame_right_side,
                                                  height="60",
                                                  yscrollcommand=s_bar.set)
        # 配置字体颜色
        self.text_major_msg.tag_config("tag_1", backgroun="yellow",
                                       foreground="red", )
        # 支持撤销操作，支持换行 wrap = "char"
        # self.text_major_msg.insert(tk.END, ">>>" * 80)
        self.text_major_msg.pack(side="top", anchor="n", expand=True,
                                 fill="both", padx=2)
        s_bar.config(command=self.text_major_msg.yview)
        return 1
    
    # 读取帮助信息并插入帮助框中
    def read_help(self):
        """
		读取帮助信息并插入帮助框中
		:return:
		"""
        filename = self.helppath
        with open(filename, "r") as read_msgs:
            for read_line in read_msgs.readlines():
                self.help_text.insert(tk.END, read_line)
            self.help_text["state"] = "disabled"
    
    # print read_line
    
    def create_button(self):
        """
		create second window button
		"""
        
        # self.confirm_method 确认按键所触发的方法
        self.button_confirm = newidgets.HoverButton(self.frame_bottom_bar,
                                                    image=self.gif_confirm,
                                                    command=self.confirm_method,
                                                    width=self._button_size,
                                                    height=self._button_size)
        # print "tooltk.py>>Border:", self.button_confirm["borderwidth"] # 2
        # height = 18, width = 18,
        self.button_help = newidgets.HoverButton(self.frame_bottom_bar,
                                                 image=self.gif_help,
                                                 width=self._button_size,
                                                 height=self._button_size)
        
        def inner_quit():
            """
			使用该方法来删除main_f下的子部件，如果直接使用
			command=self.windows.destory ,会删除掉main_f，
			导致打开其他功能时找不到main_f而报错
			:return:
			"""
            newidgets.destroy_child(self.window)
        
        self.button_quit = newidgets.HoverButton(self.frame_bottom_bar,
                                                 image=self.gif_quit,
                                                 command=inner_quit,
                                                 width=self._button_size,
                                                 height=self._button_size)
        # pack
        self.button_confirm.pack(side=tk.LEFT, anchor=tk.E,
                                 padx=5)
        self.button_help.pack(side=tk.LEFT, anchor=tk.E, padx=5)
        self.button_quit.pack(side=tk.RIGHT, anchor=tk.E, padx=5)
        # buttonttk["command"] = self.kk
        # --------------- 获取部件的query_class
        # print self.button_confirm.winfo_class()
        # print self.button_help.winfo_class()
        # print self.button_quit.winfo_class()
        """
		# 测试ttk.Style.layout()
		ttk.Style().layout("TButton",
				[('Button.button', {'children':
					[('Button.focus', {'children':
						[('Button.border', {'border':1,'children':
							[('Button.label', {'sticky': 'nswe'})],
						'sticky': 'nswe'})],
					'sticky': 'nswe'})],
				'sticky': 'nswe'})])
		ttk.Style().configure("TButton", foreground="#ffc851", background="blue")
		# padding = 10
		"""
        # print ttk.Style().layout('TButton')
        # 原版
        # [('Button.button',
        #   {'children': [(
        # 	  'Button.focus', {'children': [('Button.padding',{'children': [('Button.label',{'sticky': 'nswe'})],'sticky': 'nswe'})],'sticky': 'nswe'})],'sticky': 'nswe'})]
        """
		"""
        # ---------------
        
        return 1
    
    def single_file_block(self, sfb_filetype, sfb_name):
        # sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
        """
		sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
        
        # 文件选取菜单
        def select_file():
            file_path = tkFileDialog.askopenfilename(filetypes=sfb_filetype)
            # 刷新normal_single_block() 中的Entry
            input_msg1.set(file_path)
        
        label_1 = tk.Label(self.frame_major, text=sfb_name)
        label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
        # 块一
        # 将Entry和按钮整齐的放到一起
        frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        
        # Entry
        input_msg1 = tk.StringVar()
        self.input_sfb = newidgets.NeewwEntry(frame_one,
                                              textvariable=input_msg1, border=0)
        self.input_sfb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
                            fill=tk.X, padx=10)
        self.addfile_button = newidgets.HoverButton(frame_one, text=u"选择",
                                                    command=select_file,
                                                    image=self.gif_addfile,
                                                    width=self._button_size,
                                                    height=self._button_size)
        self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        return 1
    
    def save_path_block(self, sfb_filetype, sfb_name):
        # sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
        """
		major-Frame中的功能块之一，该模块让用户选择文件的保存位置和名字
		sfb_filetype: tkFileDialog type
		sfb_name: label name;ues to describe function
		"""
        
        # 文件选取菜单
        def select_file():
            file_path = tkFileDialog.asksaveasfilename(filetypes=sfb_filetype)
            # 刷新normal_single_block() 中的Entry
            # lis = self.file_paths_.append(file_path)
            # print lis
            input_msg1.set(file_path)
        
        name_label = tk.Label(self.frame_major, text=sfb_name)
        name_label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=16)
        # 块一
        # 将Entry和按钮整齐的放到一起
        frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        # 按钮
        # photo = tk.PhotoImage(file=r"Icons/GenericBlackAdd32.png")
        self.addfile_button = newidgets.HoverButton(frame_one,
                                                    image=self.gif_addfile,
                                                    command=select_file,
                                                    width=self._button_size,
                                                    height=self._button_size)
        self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        # Entry
        input_msg1 = tk.StringVar()
        self.input_sb = newidgets.NeewwEntry(frame_one, textvariable=input_msg1,
                                             border=2, relief=tk.FLAT)
        self.input_sb.pack(side=tk.LEFT, anchor=tk.W, expand=True,
                           fill=tk.X, padx=15)
        return 1
    
    def single_dir_block(self, sdb_name):
        """
		sdb_name: label name;ues to describe function
		主Frame中的功能块之一，将通过Filedialog获取的 文件夹  传递更新给Entry,
		同时可以获取 用户直接在Entry中输入的文件路径
		"""
        
        def select_file():
            # global file_path
            file_path = tkFileDialog.askdirectory()
            # 刷新normal_single_block() 中的Entry
            input_msg1.set(file_path)
        
        label_2 = tk.Label(self.frame_major, text=sdb_name)
        label_2.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
        # 将Entry和按钮整齐的放到一起
        frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        # Entry
        input_msg1 = tk.StringVar()
        self.input_sdb = newidgets.NeewwEntry(frame_one,
                                              textvariable=input_msg1, bd=0)
        self.input_sdb.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X,
                            padx=10)
        # input_msg.set(one_file_path)
        self.addfile_button = newidgets.HoverButton(frame_one,
                                                    command=select_file,
                                                    image=self.gif_folder,
                                                    width=self._button_size,
                                                    height=self._button_size)
        self.addfile_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        return 1
    
    def single_vari_block(self, gib_name, input_msg1):
        """
		主Frame中的功能块之一，直接通过Entry获取变量值，
		其变量类型，可以根据需要灵活指定。
		:param input_msg1: # input_msg1 = tk.StringVar()
		:param gib_name: label name;ues to describe function
		:return:
		"""
        label_3 = tk.Label(self.frame_major, text=gib_name)
        label_3.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
        # 块一
        # 将Entry和按钮整齐的放到一起
        frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        # Entry
        # input_msg1 = tk.StringVar()
        self.input_svb = newidgets.NeewwEntry(
            frame_one, textvariable=input_msg1, border=0
        )
        self.input_svb.pack(side=tk.LEFT, anchor=tk.W,
                            expand=True, fill=tk.X, padx=10)
        # input_msg.set(one_file_path)
        # 按钮
        int_button_1 = newidgets.HoverButton(frame_one, image=self.gif_empty_1,
                                             state="disabled",
                                             width=self._button_size,
                                             height=self._button_size)
        int_button_1.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        return 1
    
    def single_int_block2(self, gib_name):
        """
		主Frame中的功能块之一，直接通过Entry获取Int值
		:param gib_name: label name;ues to describe function
		:return:
		"""
        _label = tk.Label(self.frame_major, text=gib_name)
        _label.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)
        # 块一
        # 将Entry和按钮整齐的放到一起
        frame_one = tk.Frame(self.frame_major)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        # 按钮
        int_button_2 = newidgets.HoverButton(
            frame_one, state="disabled",
            image=self.gif_empty_1,
            width=self._button_size,
            height=self._button_size
        )
        int_button_2.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        # Entry
        input_msg1 = tk.StringVar()
        self.input_sib2 = newidgets.NeewwEntry(
            frame_one,
            textvariable=input_msg1, border=0
        )
        # , state = "readonly"
        self.input_sib2.pack(
            side=tk.LEFT, anchor=tk.W,
            padx=10, expand=True, fill=tk.X
        )
        # input_msg.set(one_file_path)
        return 1
    
    def single_text_block(self, stb_name):
        """
		text组件
		:param stb_name:
		:return:
		"""
        # 块名称
        tk.Label(self.frame_major, text=stb_name). \
            pack(side=tk.TOP, anchor=tk.NW, padx=40)
        frame_one = tk.Frame(self.frame_major)
        frame_one.pack(side="top", anchor="center",
                       expand=True, fill="both")
        # 右边障碍要素
        newidgets.HoverButton(
            frame_one, state="disabled",
            image=self.gif_empty_1,
            width=60,
            height=self._button_size
        ).pack(side=tk.RIGHT, padx=10)
        # 左边障碍要素
        newidgets.HoverButton(
            frame_one, state="disabled",
            image=self.gif_empty_1,
            width=13,
            height=self._button_size
        ).pack(side=tk.LEFT, padx=10)
        
        # frame_one.columnconfigure(0, weight=1)
        # frame_one.columnconfigure(1, weight=1)
        self.input_tb = newidgets.NeewwText(frame_one, wrap="none",
                                            relief="flat", height=10)
        self.input_tb.pack(expand=True, fill="both")
    
    # text.grid(column = 0,sticky = "nesw")
    
    def divider_bar_block(self, master, color11, color22):
        """
		最下面的那个分隔栏
		:return:
		"""
        s = newidgets.GradientCanvas(
            master, color11, color22,
            height=10, bd=0
        ).pack(fill="x")
    
    def get_blockvalue(self, *arg):
        """
		列表初始化
		获取Entry值，组成列表
		:param arg: 各个block的Entry模块组成的元组
		:return: self.block_list 返回 含有用户输入的各种因子的 列表
		"""
        self.block_list = []
        for i in arg:
            # 由于Entry输出纯英文数字时是str格式，为方便后续进行比较等操作
            # 将str转换为unicode
            msg = i.get()
            # print msg
            # print type(msg)
            if type(msg) == type("str"):  # unicode
                msg = msg.decode("cp936")
                self.block_list.append(msg)
            else:
                # unicode格式的直接加进去
                self.block_list.append(msg)
            # 将信息显示到右上角
            self.text.insert("end", "\n  " + msg)
        # print len(self.block_list)
        # print self.block_list[3]
        return self.block_list

# got_msg1 = arg[0].get()
# # .decode("cp936")
# got_msg2 = arg[1].get()
# self.block_list.append(got_msg1)
# self.block_list.append(got_msg2)
