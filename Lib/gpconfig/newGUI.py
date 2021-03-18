# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/28
"""
功能：
一：
	完善主窗口（tool_entrance）的功能：
		窗口居中
		清除父部件中的子部件
二:
	定义新类 HoverButton,NeewwEntry,NeewwText
"""
from __future__ import absolute_import
from __future__ import print_function
import Tkinter as tk
from time import time
try:
    import win32clipboard
except ImportError as e:
    print(e.message)

import gpconfig.hyini as ini
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def screen_cetre(master, width=None, height=None):
    # 窗口居中
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    if width is None:
        width, height = 800, 660
    geometry_size = "{}x{}+{}+{}".format(
        width, height, (screenwidth - width) / 2, #         width, height, (screenwidth - width) / 2-200,
                       (screenheight - height) / 2)
    master.geometry(geometry_size)
# geometry = '%dx%d+%d+%d' % (
# width, height, (screenwidth - width) / 2, (screenheight - height) / 2)


def destroy_child(master):
    """
    监测一个部件内部是否有子部件，如果有，
    那么删除子部件
    :param master: 父部件
    :return:
    """
    widget_set = master.winfo_children()
    
    if widget_set:
        for i in widget_set:
            i.destroy()
        # i.pack_forget()
        # pass


class HoverButton(tk.Button):
    """
    features detail:
        1.继承Button.实现鼠标悬停时，按键变化的效果
        2.bind bubbletip bubbles to button
        3.点击可以将信息复制到 win10 粘贴板
        4.实现 Button click counter in Python https://stackoverflow.com/questions/56904280/button-click-counter-in-python
    注意事项：
        图片按键和文字按键的width和height的度量单位不一样
    """
    
    def __init__(self, master, msg=None, follow = True,**kw):
        """
        follow(Boolean): 提示气泡是否跟随鼠标
        msg(Unicode): 提示消息
        """
        tk.Button.__init__(self, master=master, **kw)
        self.msg = msg
        self.follow = follow
        self.state = 0
        # there is no tip bubble
        # self.state = 1 # exist tip bubble but no enought time to show tip bubble
        # mouse pointer leaves	button while tip bubble hide.
        self.defaultBackground = self["background"]
        self.config(relief="flat", activebackground=ini.light_yellow2)
        # print self["state"] # disabled normal
        if not self["state"] == "disabled":
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
            if msg:
                self.bind("<Motion>", self.on_move)
    
    # unbind
    def close(self):
        self.unbind("<Enter>")
        self.unbind("<Leave>")
        self.unbind("<Motion>")
    
    def on_enter(self, event):
        self['background'] = self['activebackground']
        # self['relief'] = "groove"
        # self['bd'] = 3
        # ToolTip, set message bubble
        # self.after(int(self.delay * 1000),
        # 		   self.show)
        if self.msg:
            self.state = 0
            self.spawn_tip(event)
            self.after(600,self.show_tip)
    
    def on_leave(self, event):
        self['background'] = self.defaultBackground
        self['relief'] = "flat"
        if self.msg:
            self.state = 1 # 防止鼠标在
            self.hide_tip(event)
    
    def on_move(self, event):
        self.tip.geometry('+%i+%i' % (event.x_root + 10,event.y_root + 10))
    # self.after(1000, self.show_tip)
    
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # bind bubbletip bubble to a button
    # let tooltip follow you mouse pointer's motion
    def spawn_tip(self, event):
        self.tip = tk.Toplevel(self, bg='black', padx=1, pady=1)
        self.tip.overrideredirect(True)  # remove
        self.tip.withdraw()
        output = tk.StringVar()
        output.set(self.msg)
        # "#ffc851" '#FFFFDD'
        tk.Message(
            self.tip, textvariable=output, bg="#FFFFDD",
            aspect=1000).grid()  # aspect: use to modify size
    
    def show_tip(self):
        if self.state != 1:
            self.tip.deiconify()
    
    def hide_tip(self, event):
        self.tip.withdraw()
    # self.tip.destroy()


class clipboardButton(HoverButton):
    """点击按键，将信息复制到windows粘贴板上"""
    def __init__(self, master,msg, **kw):
        HoverButton.__init__(self, master, msg=msg, follow = True,**kw)
        self.master = master
        # self.text = text
        self.default_color = self['background']
        self["command"] = self.send_to_clibboard
        self.default_relief = "raised"
        self.config(
            relief=self.default_relief, activebackground=ini.light_blue,
            cursor ="arrow"
        )
        # 绑定
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    
    def send_to_clibboard(self):
        """将数据传入win10剪贴板"""
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        # win32clipboard.CF_UNICODETEXT, self.text.decode("utf8") 不然会乱码
        try:
            win32clipboard.SetClipboardData(
                win32clipboard.CF_UNICODETEXT, self["text"].decode("utf8"))
        except UnicodeEncodeError:
            win32clipboard.SetClipboardData(
                win32clipboard.CF_UNICODETEXT, self["text"].decode("utf8"))
        win32clipboard.CloseClipboard()
    
    def on_leave(self, event):
        self['background'] = self.default_color
        self["relief"] = self.default_relief
        if self.msg:
            self.state = 1  # 防止鼠标在
            self.hide_tip(event)
    
    def on_enter(self, event):
        self['background'] = ini.more_light_blue
        self["relief"] = "flat"
        if self.msg:
            self.state = 0
            self.spawn_tip(event)
            self.after(600,self.show_tip)


class NeewwEntry(ttk.Entry):
    """
    from https://stackoverflow.com/questions/41477428/
        ctrl-a-select-all-in-entry-widget-tkinter-python
    继承Entry，实现以下功能
        1.Ctrl A 实现全选的功能
    """
    def __init__(self, master, **kw):
        ttk.Entry.__init__(self, master=master, **kw)
        self.bind("<Control-a>", self.select_all)
    # new_textvariable = self["textvariable"]
    # self["textvariable"] = new_textvariable.decode("utf8")
    
    @staticmethod
    def select_all(event):
        # select text
        event.widget.select_range(0, 'end')
        # move cursor to the end
        event.widget.icursor('end')
        # stop propagation
        return 'break'




class NeewwText(tk.Text):
    """
    from (https://stackoverflow.com/questions/5870561/
        re-binding-select-all-in-text-widget)
    继承Text，实现以下功能
        1.Ctrl A 实现全选的功能
    """
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master=master, **kw)
        self.config(maxundo=15, undo=True)
        self.bind_class("Text", "<Control-a>", self.selectall)
    
    def selectall(self, event):
        event.widget.tag_add("sel","1.0","end")
    
    # 重新复写tk.Text().get()方法，默认其获得全部信息
    def get(self, index1="0.0", index2="end"):
        """Return the text from INDEX1 to INDEX2 (not included)."""
        return self.tk.call(self._w, 'get', index1, index2)


class NeewwFrame(tk.LabelFrame):
    def __init__(self, master, **kw):
        tk.LabelFrame.__init__(self, master=master, **kw)
        # self.deaf = self["relief"]
        self.pre_colour = self["background"]
        self.bind("<Enter>", self.f_enter)
        self.bind("<Leave>", self.f_leave)
    
    def f_enter(self, event):
        # self["relief"] = "groove"
        # SystemWindow
        self["background"] = "SystemWindow"
    # self.config(relief = "groove" )
    
    def f_leave(self, event):
        # self["relief"] = "groove"
        # self["borderwidth"] = 4
        self["background"] = self.pre_colour


class GradientCanvas(tk.Canvas):
    """
    from Bryan Oakley on (https://stackoverflow.com/questions/26178869/
                            is-it-possible-to-apply-gradient-colours-
                            to-bg-of-tkinter-python-widgets)
    A gradient frame which uses a canvas to draw the background
    parent:
    color11: 渐变颜色1
    color22: 渐变颜色2
    """
    def __init__(self, parent, color1= "#ffc851", color2="#808000", **kwargs):
        # "#808000" olive
        """default gradient color: red to black"""
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)
        self.config(relief="flat", highlightthickness=0)
    
    def _draw_gradient(self, event=None):
        """Draw the gradient"""
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit
        
        for i in xrange(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")


class ButtonFrame(tk.Frame):
    """图标按钮与名称的组合frame"""
    def __init__(self, master, image, name, command, **kw):
        """
        :param master:
        :param image: 图标地址
        :param name: 名字
        :param command: button响应事件
        :param kw:
        """
        tk.Frame.__init__(self, master=master, **kw)
        # 设置图标路径
        self.image = image
        self.name = name
        self.command = command
        wrap_frame = tk.Frame(self.master, relief="groove", bd=10)
        wrap_frame.pack(side="left", anchor="nw", fill=None, expand=False)
        # wrap_frame.grid(column=0,row=0)
        self.button = HoverButton(
            wrap_frame, image=self.image, command=self.command)
        self.button.pack(side="top", fill=None, expand=False)
        label = tk.Label(wrap_frame, text=self.name)
        label.pack(side="top", fill=None, expand=False)
        print("ok")
    
    @property
    def framebutton(self):
        return self.button


class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    Example: ToolTip(self.button_help, "CANCEL", None, 0.5)
    """
    
    def __init__(self, wdgt, msg=None, msgFunc=None, delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        self.parent = self.wdgt.master  # The parent of the ToolTip is the parent of the ToolTips widget
        tk.Toplevel.__init__(
            self, self.parent, bg='black', padx=1, pady=1)  # Initalise the Toplevel
        self.withdraw()  # Hide initially
        self.overrideredirect(
            True)  # The ToolTip Toplevel should have no frame or title bar
        
        self.msgVar = tk.StringVar()  # The msgVar will contain the text displayed by the ToolTip
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(
            self, textvariable=self.msgVar, bg='#FFFFDD', aspect=1000).grid()  # The test of the ToolTip is displayed in a Message widget
        # <Enter>: The mouse pointer entered the widget
        self.wdgt.bind(
            '<Enter>', self.spawn
        )  # Add bindings to the widget.  This will NOT override bindings that the widget already has
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    
    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        self.after(int(self.delay * 1000),
                   self.show)  # The after function takes a time argument in miliseconds
    
    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()  # show Toplevel widget
    
    def move(self, event):
        """
        Processes motion within the widget.

        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        if not self.follow:  # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root + 10,
                                  event.y_root + 10))  # Offset the ToolTip 10x10 pixes southwest of the pointer
        try:
            self.msgVar.set(
                self.msgFunc())  # Try to call the message function.  Will not change the message if the message function is None or the message function fails
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    
    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget

        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

"""__________________________________________________________________________"""
"""______________________________scoll_widget________________________________"""
# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))
    
    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped
    
    def __str__(self):
        return str(self.master)

def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    """A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed."""
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

"""______________________________scoll_widget________________________________"""
"""__________________________________________________________________________"""

if __name__ == '__main__':
    def send_to_clibboard():
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, "hello")
        win32clipboard.CloseClipboard()
    send_to_clibboard()