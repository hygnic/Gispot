# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/21
# python2.7
"""
GUI  所用工具和脚本用GUI"""
from __future__ import  print_function
from __future__ import  absolute_import
# from __future__ import  unicode_literals
import Tkinter as tk
import ttk
import tkFileDialog
from PIL import Image, ImageTk
import os
import codecs

# 导入配置包、地址包
from gpconfig import newGUI
from gpconfig import gppath
from gpconfig import hyini
from gpconfig.hyini import *
from gpconfig.gppath import PngIcon


#----------------------para-------------------------------
# 将 input_log.log 文件中保存的输入地址等输入信息框
input_log = os.path.join(gppath.Docs_p, "input_log.log")


class GIF(object):
    
    def __init__(self):
        self.text = tk.PhotoImage(file=gppath.GifPath.textfile)
        self.addfile = tk.PhotoImage(file=gppath.GifPath.add_file)
        
        self.folder = tk.PhotoImage(file=gppath.GifPath.folder)
        self.close = tk.PhotoImage(file=gppath.GifPath.close)
        self.quit = tk.PhotoImage(file=gppath.GifPath.close)
        self.help = tk.PhotoImage(file=gppath.GifPath.info)
        self.confirm = tk.PhotoImage(file=gppath.GifPath.confirm)
        self.empty_1 = tk.PhotoImage(file=gppath.GifPath.empty1)


# @staticmethod
# def dd():
# 	empty_1 = tk.PhotoImage(file=paths.GifPath.gif_empty1)


class Tooltk(object):
    """工具的GUI界面"""
    # 如果是图片，表示 24 像素单位，否则不是
    _button_size = 24
    
    # 调用类变量也要加self
    def __init__(self, master, help_path, confirm_method):
        """
        :param master:
        :param help_path: path of help information file（can be None）
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
        self.initial_color()  # 颜色
        self.initial_icon()  # 配置图片
        self.initial_frames()  # 配置框架
        self.initial_buttons()  # 配置按钮
        # color  "SystemHighlight","SystemMenuText"
        self.read_help()
    
    @property
    def Frame(self):
        return self.block_frame
    
    # static information box(Upper right corner)
    @property
    def FrameStatic(self):
        return self.msgframe
    
    # dynamic information box(lower right corner)
    @property
    def FrameDynamic(self):
        return self.major_msgframe
    
    def initial_color(self):
        self.color1 = "#F1F1F1"  # help bar
        self.color5 = "#808000"  # Olive,显示text
        self.color3 = "#F1F1F1"  # 主框的上半部分颜色 侧栏颜色
        # self.color4 = "Cornsilk" # 侧栏颜色
        self.color2 = "#E1E1E1"  # 茶色 较深
    
    def initial_icon(self):
        # 必须加file参数，不然不显示图片（arcgis10.6）
        self.gif_addfile = tk.PhotoImage(file=gppath.GifPath.add_file)
        
        self.gif_folder = tk.PhotoImage(file=gppath.GifPath.folder)
        self.gif_close = tk.PhotoImage(file=gppath.GifPath.close)
        self.gif_quit = tk.PhotoImage(file=gppath.GifPath.close)
        self.gif_help = tk.PhotoImage(file=gppath.GifPath.info)
        self.gif_confirm = tk.PhotoImage(file=gppath.GifPath.confirm) # gif
        
        self.png_quit = ImageTk.PhotoImage(Image.open(PngIcon.cancel))  # png
        self.png_help = ImageTk.PhotoImage(Image.open(PngIcon.help_info))  # png
        self.png_confirm = ImageTk.PhotoImage(Image.open(PngIcon.OK))  # png
        
        self.gif_empty_1 = tk.PhotoImage(file=gppath.GifPath.empty1)
        # self.gif_empty_2 = tk.PhotoImage(file=gispotpath.GifPath.gif_empty2)
        
        # ph = tk.PhotoImage(file=gispotpath.GifPath.gif_confirm)
        # self.gif_check_green16 =  ph.zoom(x= 2,y = 2)
        # self.gif_check_green16 =  ph.subsample(x= 40,y=40)
        
        """
        使用pillow设置按键图标
        from PIL import Image, ImageTk
        self.gif_comfirm = ph
        # test
        im = Image.open(r"E:/move on move on/Gispot/GUIs/66.png")
        self.ph_im = ImageTk.PhotoImage(im)
        """
    # set display frames
    def initial_frames(self):
        # 1192/2 = 596
        #______________________________right-frame_______________________________
        self.frame_right_side = ttk.Frame(self.window, width=496, border=0, relief="flat")
        self.frame_right_side.pack(side="right", expand=True, fill="both")
        #______________________________left-frame_______________________________
        self.frame_left_side = ttk.Frame(self.window, width=696, border=0)
        self.frame_left_side.pack(side="left", expand=True, fill="both")
        #______________________upper part of left-frame_________________________
        self.block_frame = ttk.Frame(self.frame_left_side)
        self.block_frame.pack(expand=True, fill="both")
        #______________________bottom part of left-frame________________________
        # use for contain botton: comfirmed button; cancel button; bubbletip button
        self.frame_bottom_bar = ttk.Frame(self.frame_left_side, height="60")
        self.frame_bottom_bar.pack(expand=False, fill="both")
        #_______________________________________________________________________
        # expand=False, fill ="x" 表示不会随着界面变大而变大，但是在
        # x轴（左右）方向上会拉伸
        # 左边主框中的帮助信息
        #_____________________info-frame within left-frame______________________
        help_f = ttk.Frame(self.block_frame, relief=tk.GROOVE) # bd=2, padx=3
        help_f.pack(side=tk.BOTTOM, anchor="s", expand=True, fill="both")
        # help_f.pack_propagate(0)
        # 设置带滚动条的text
        # s_bar = tk.Scrollbar(help_f, relief="flat", elementborderwidth=-15)
        s_bar = ttk.Scrollbar(help_f)
        s_bar.pack(side="right", fill="y")
        self.help_text = newGUI.NeewwText(
            help_f, relief=tk.FLAT, height=20,
            fg=self.color5, yscrollcommand=s_bar.set)
        
        self.help_text.pack(expand=True, fill="both")
        s_bar.config(command=self.help_text.yview)
        
        """----------------------------------------------------------------"""
        """----------------------------------------------------------------"""
            # 右边主框插入文本框，文本框分成上下两部分，上部分显示固定的信息，
            # 下半部分显示动态信息
        """----------------------------------------------------------------"""
        """----------------------------------------------------------------"""
        #_____________________________upper block_______________________________
        # wrap="word" 如果大段的文字超过容纳限制，就会强制换一行输出
        self.msgframe = tk.Text(self.frame_right_side, relief="flat", bd=0)  # width="50"
        
        # 将所用txt都标记了
        # self.text.tag_add("tag1","1.end","2.end")
        self.msgframe.insert(
            tk.END,
            "-----------------Python 2.7 Author: Liaochenchen 2019#00#00--------------------\n"
        )  # ,"tag1"
        # self.text.tag_config("tag1", underline=True, foreground="Ivory")
        self.msgframe.pack(
            side="top", anchor="n", expand=True, fill="both")
        upper_bar = ttk.Scrollbar(self.msgframe)
        upper_bar.pack(side="right", fill="y")
        
        with open(input_log, "r") as read_msgs:
            text_cont = 0 #
            for read_line in read_msgs.readlines():
                # 显示20条参数数据
                if text_cont == 20:
                    break
                text_cont += 1
                line_msg = read_line.strip()
                # self.msgframe.insert(tk.END, "  "+line_msg)
                # 创建历史输入记录的按钮
                msgb = newGUI.clipboardButton(
                    self.msgframe, text=line_msg, msg=u"复制到剪贴板"
                    )
                self.msgframe.window_create("end", window=msgb)
                # self.msgframe.window_create("2.0", window=msgb) # 第二行，第一列
                
                # msgb = newGUI.HoverButton(
                # 	self.msgframe, msg=u"点击复制",text=line_msg,
                #  cursor ="arrow",hover=("raised","flat",
                # 						hyini.light_system_grey, hyini.more_light_blue))
                # msgb.config(command = msgb.send_to_clibboard)
                # self.msgframe.window_create("end", window=msgb )
        
        # _____________________________bottom block_____________________________
        # show infomation of running program
        # s_bar = tk.Scrollbar(self.frame_right_side, relief="flat", elementborderwidth=-15)
        s_bar = ttk.Scrollbar(self.frame_right_side)
        s_bar.pack(side="right", fill="y")
        self.major_msgframe = newGUI.NeewwText(
            self.frame_right_side, yscrollcommand=s_bar.set, height=28, relief = "groove")
        # choose font color
        self.major_msgframe.tag_config(
            "tag_warn", backgroun="yellow", foreground="red")
        self.major_msgframe.tag_config(
            "tag_info", backgroun=hyini.light_blue2, foreground=hyini.white)
        # support go back, use 'Ctrl+Z'; wrap = "char"
        # self.text_major_msg.insert(tk.END, ">>>" * 80)
        self.major_msgframe.pack(
            side="top", anchor="n", expand=True, fill="both", padx=2)
        s_bar.config(command=self.major_msgframe.yview)
    
    # __________Read help information and insert in help frame__________________
    # Read help information and insert in help frame
    def read_help(self):
        if self.helppath is not None:
            filename = os.path.join(gppath.Docs_p, self.helppath)
            with open(filename, "r") as read_msgs:
                for read_line in read_msgs.readlines():
                    self.help_text.insert(tk.END, read_line)
                self.help_text["state"] = "disabled"
    
    
    def initial_buttons(self):
        """
        create three button:
         1.button_confirm: the main function start up button
         2.button_quit: back button
         3.button_help: jump to a website which shows help information (most unused)
        """
        self.button_confirm = newGUI.HoverButton(
            self.frame_bottom_bar, msg="OK",
            image=self.png_confirm,
            command=self.confirm_method,
            width=self._button_size,
            height=self._button_size)
        
        # print "tooltk.py>>Border:", self.button_confirm["borderwidth"] # 2
        # height = 18, width = 18,
        # help button
        self.button_help = newGUI.HoverButton(
            self.frame_bottom_bar, msg="Info",
            image=self.png_help,
            width=self._button_size,
            height=self._button_size)
        
        def __quit_inner():
            """
            使用该方法来删除main_f下的子部件，如果直接使用
            command=self.windows.destory ,会删除掉main_f,
            导致打开其他功能时找不到main_f而报错
            """
            newGUI.destroy_child(self.window)
        
        # Back button
        self.button_quit = newGUI.HoverButton(
            self.frame_bottom_bar, msg="Cancel",
            image=self.png_quit,
            command=__quit_inner,
            width=self._button_size,
            height=self._button_size)
        # pack
        self.button_confirm.pack(side=tk.LEFT, anchor=tk.E, padx=5)
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
    
    @staticmethod
    def divider_bar_block(master, color11, color22):
        """
        最下面的那个分隔栏
        :return:
        """
        s = newGUI.GradientCanvas(
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
            infoo = "msg: {0}, type: {1}".format(msg, type(msg))
            print(infoo)
            if type(msg) == type("str"):  # unicode
                msg = msg.decode("cp936")
                # print "msg: {0}, type: {1}".format(msg, type(msg))
                self.block_list.append(msg)
            else:
                # unicode格式的直接加进去
                self.block_list.append(msg)
            # 将信息显示到右上角
            self.msgframe.insert("end", "\n  " + msg)
        # print len(self.block_list)
        # print self.block_list[3]
        return self.block_list

class SingleFileBlock(object):
    """单个文件选择功能块
    ss = tooltk.SingleFileBlock(frame, "添加文件",
                                    tkFileDialog.askopenfilename，[(u'文本文档', '*.txt'), ('All Files', '*')],
                                    "add_file")"""
    def __init__(self, frames, name, tkFileDialogFunc, filetype, image, tip):
        """
        :param frames: {Tuple} GUI界面中几个主要框架
            *self.block_frame,self.msgframe,self.major_msgframe
             self.block_frame 父组件，左上界面
             self.msgframe 右上 静态信息界面
             self.major_msgframe 右下 动态信息界面
            
        :param name: {String} 块（Block）名字
        
        :param tkFileDialogFunc: tkFileDialog 模块名称
            *tkFileDialog.askopenfilename: 获取单个文件的位置和名称
                file_path = tkFileDialog.askopenfilename([(u'文本文档', '*.txt'), ('All Files', '*')])
            *tkFileDialog.askdirectory:
                file_path = tkFileDialog.askdirectory()
        
        :param filetype: tkFileDialog {List} 文件选择类型
            *__sfb_filetype = [(u'文本文档', '*.txt'), ('All Files', '*')]
        
        :param image: {String} 按键图片名字，使用了反射
            * "add_file"
            
        :param tip:
        """
        # 传入参数 三个frame
        self._master, self._static, self._dymnic= frames
        self._sfb_filetype = filetype
        self.dialoge_type = tkFileDialogFunc
        self._tip = tip
        # self.tkFileDialog.askopenfilename = tkFileDialog.askopenfilename
        self.var = tk.StringVar()
        self.image(image)
        self.single_file_block(name)
    
    # 设置图片,使用了反射
    # 方案一：使用gif图片
    # def image(self,image):
    # 	# print "getattr(GifPath,image):",getattr(GifPath,image)
    # 	raw_p = getattr(GifPath,image)
    # 	# tk.PhotoImage需要设置成全局变量才生效，一个bug
    # 	global a_gif
    # 	a_gif = tk.PhotoImage(file=raw_p)
    # 	self.but_image = a_gif
    def image(self, image):
        # print "getattr(GifPath,image):",getattr(GifPath,image)
        raw_p = getattr(PngIcon, image)
        img = Image.open(raw_p)
        photo = ImageTk.PhotoImage(img)
        # tk.PhotoImage需要设置成全局变量才生效，一个bug
        # global a_gif
        # a_gif = tk.PhotoImage(file=raw_p)
        self.but_image = photo
    
    # 打开 文件/文件夹 选取窗口
    def dialog(self):
        file_path = self.dialoge_type(filetypes=self._sfb_filetype)
        
        # file_path = tkFileDialog.askopenfilename(
        # 		[(u'文本文档', '*.txt'), ('All Files', '*')])
        # 刷新normal_single_block() 中的Entry
        self.var.set(file_path)
    
    def single_file_block(self, sfb_name):
        """主Frame中的功能块之一，将通过Filedialog获取的 文件 传递更新给Entry,
        同时可以获取 用户直接在Entry中输入的文件路径
        _sfb_filetype: {List} tkFileDialog
        
        sfb_name: {String} label name; ues to describe function
        """
        label_1 = ttk.Label(self._master, text=sfb_name)
        label_1.pack(side=tk.TOP, expand=tk.NO, anchor=tk.NW, padx=10)

        # 整齐排列Entry和按钮
        frame_one = ttk.Frame(self._master)  # , border =1 ,relief = "raised"
        frame_one.pack(side="top", anchor="center", expand=False, fill="x")
        
        # Entry
        self._newEntry = newGUI.NeewwEntry(frame_one)
        self._newEntry.pack(side=tk.LEFT, anchor=tk.W, expand=True, fill=tk.X, padx=10)
        self._newEntry.configure(textvariable=self.var)
        
        
        # self._newEntry.configure(border=0)
        
        self._button = newGUI.HoverButton(
            frame_one, msg=self._tip,
            command=self.dialog,
            image=self.but_image,
            width=hyini.BUTTON_PIXEL_SIZE,
            height=hyini.BUTTON_PIXEL_SIZE)
        self._button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10)
        
        # if focus_flag ==1:
        # 	self._newEntry.focus()
        
    # 点击确认键的时候获取Entry中的值
    def get(self):
        block_list = []
        # 由于Entry输出纯英文数字时是str格式，为方便后续进行比较等操作
        # 将str转换为unicode
        msg = self._newEntry.get()
        frame = self._static
        # print("msg", msg)
        # print("msg's type", type(msg))
        
        with codecs.open(input_log, "r+",  "utf8") as log_file:
            if type(msg) == type("str"):  # unicode
                msg = msg.decode("utf8")
                frame.insert("end", "  parameter: " + msg)
                # 将参数写入记录文本中
                content = log_file.read()
                log_file.seek(0, 0)
                info2 = msg+"\n"+content
                log_file.write(info2) # UnicodeDecodeError/
                # log_file.write(msg.encode("cp936")+"\n")
                return msg
            else:
                # unicode格式的直接加进去
                frame.insert("end", "  parameter: " + msg)
                # 将参数写入记录文本中
                # try:
                # 	content = log_file.read()
                # 	log_file.seek(0, 0)
                # 	log_file.write(msg.encode("utf8")+"\n"+content)
                # except UnicodeEncodeError:
                # 	print("tooltk.py error1")
                return msg

    
    @property
    def button(self):
        return self._button
    
    @property
    def entry(self):
        return self._newEntry


# 文件夹模块
def blockDIR_in(frames, name):
    return SingleFileBlock(frames, name, tkFileDialog.askdirectory, None, "folder1", u"文件夹")


def blockSheet(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.askopenfilename,
        [(u'工作簿', '*.xlsx'), (u'工作簿', '*.xls'), ('All Files', '*')],
        "sheet", u"工作簿")


def blockDIR_out(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.askdirectory, None, "folder2", u"文件夹")


# 数字输入模块（没有button）
def blockValue(frames, name):
    inner = SingleFileBlock(
        frames, name, None, None, "empty2", u"输入值")
    # inner.block_button["state"] ="disabled"  #不行
    # inner.block_button.config(state ="disabled") # 不行
    # 解除绑定
    inner.button.close()  # state = "disabled",  normal,active
    return inner

"""______________________________shp_file___________________________________"""
"""_________________________________________________________________________"""
def blockShp_in(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.askopenfilename,
        [('shapefile', '*.shp')],
        "shapefile","shapefile"
    )
def blockShp_out(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.asksaveasfilename,
        [('shapefile', '*.shp'), ('All Files', '*')],
        "shapefile","shapefile"
    )
"""______________________________mxd_file___________________________________"""
"""_________________________________________________________________________"""
def blockMXD_in(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.askopenfilename,
        [('地图文档', '*.mxd'), ('All Files', '*')],
        "mxd","mxd"
    )

def blockMXD_out(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.asksaveasfilename,
        [('地图文档', '*.mxd'), ('All Files', '*')],
        "mxd","mxd"
    )
"""_____________________________text_file___________________________________"""
"""_________________________________________________________________________"""
def blockTEXT_in(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.askopenfilename,
        [('txt', '*.txt'), ('All Files', '*')],
        "text","txt"
    )

def blockTEXT_out(frames, name):
    return SingleFileBlock(
        frames, name, tkFileDialog.asksaveasfilename,
        [('txt', '*.txt'), ('All Files', '*')],
        "text","txt"
    )


if __name__ == '__main__':
    class TstApp(Tooltk):
        def __init__(self):
            # master = tk.Tk()
            from ttkthemes import ThemedTk
            master = ThemedTk(theme="arc")
            super(TstApp, self).__init__(master,
                                             "area_cal.gc",
                                             None)
            self.name = u"计算地类面积"
            frame = (self.Frame, self.FrameStatic, self.FrameDynamic)
            # block1
            self.block1 = blockDIR_in(frame, u"数据文件地址")
            self.block2 = blockShp_in(frame, u"DLTB图层")
            self.block3 = blockSheet(frame, u"复核表")
            self.block4 = blockValue(frame, u"进程数")
        
        # self.addfile_button["state"] = "disabled"
        # self.addfile_button.pack_forget() # 隐藏模块
        # self.addfile_button.destroy()	# 隐藏模块
        # 触发命令获取Entry的值
        
        def confirm_method(self):
            self.get_blockvalue(self.input_sfb, self.input_sdb)
            print("self.block_list: ", self.block_list)
            for i in self.block_list:
                print(i, " type: ", type(i))
            # 重置
            self.block_list = []
            """
            文件
            filedialog: C:/Users/hygnic/Desktop/打开host.txt  type:  <type 'unicode'>
            filedialog: C:/Users/hygnic/Desktop/204863.txt  type:  <type 'str'>
            文件夹
            filedialog+手动: E:/move on move on/是多少  type:  <type 'unicode'>
            手动: G:\软件包  type:  <type 'unicode'>
            手动: G:\music  type:  <type 'str'>
            filedialog: E:/move on move on/gispot/bin  type:  <type 'str'>
            filedialog: E:/move on move on/公示图  type:  <type 'unicode'>
            结论:
            """
    
    
    app = TstApp()
    app.window.mainloop()
