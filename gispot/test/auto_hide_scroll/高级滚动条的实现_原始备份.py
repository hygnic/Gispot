#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/12/19 21:43
# Reference: https://stackoverflow.com/questions/47996265/how-to-scroll-a-gui-with-tkinter-in-python-using-the-mouse-wheel-on-the-center-o
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import Tkinter as tk
from random import randint

# --- classes ---
try:
    from Tkinter import Canvas, Frame
    from ttk import Scrollbar

    from Tkconstants import *
except ImportError:
    from tkinter import Canvas, Frame
    from tkinter.ttk import Scrollbar

    from tkinter.constants import *

import platform

OS = platform.system()


class Mousewheel_Support(object):

    # implemetation of singleton pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, root, horizontal_factor=2, vertical_factor=2):

        self._active_area = None

        if isinstance(horizontal_factor, int):
            self.horizontal_factor = horizontal_factor
        else:
            raise Exception("Vertical factor must be an integer.")

        if isinstance(vertical_factor, int):
            self.vertical_factor = vertical_factor
        else:
            raise Exception("Horizontal factor must be an integer.")

        if OS == "Linux":
            root.bind_all('<4>', self._on_mousewheel, add='+')
            root.bind_all('<5>', self._on_mousewheel, add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self._on_mousewheel, add='+')

    def _on_mousewheel(self, event):
        if self._active_area:
            self._active_area.onMouseWheel(event)

    def _mousewheel_bind(self, widget):
        self._active_area = widget

    def _mousewheel_unbind(self):
        self._active_area = None

    def add_support_to(self, widget=None, xscrollbar=None, yscrollbar=None, horizontal_factor=None, vertical_factor=None):
        if xscrollbar is None and yscrollbar is None:
            return

        if xscrollbar is not None:
            horizontal_factor = horizontal_factor or self.horizontal_factor

            xscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'x')
            xscrollbar.bind('<Enter>', lambda event, scrollbar=xscrollbar: self._mousewheel_bind(scrollbar))
            xscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        if yscrollbar is not None:
            vertical_factor = vertical_factor or self.vertical_factor

            yscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'y')
            yscrollbar.bind('<Enter>', lambda event, scrollbar=yscrollbar: self._mousewheel_bind(scrollbar))
            yscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        main_scrollbar = yscrollbar if yscrollbar is not None else xscrollbar

        if widget is not None:
            if isinstance(widget, list) or isinstance(widget, tuple):
                list_of_widgets = widget
                for widget in list_of_widgets:
                    widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                    widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                    widget.onMouseWheel = main_scrollbar.onMouseWheel
            else:
                widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                widget.onMouseWheel = main_scrollbar.onMouseWheel

    @staticmethod
    def _make_mouse_wheel_handler(widget, orient):
        view_command = getattr(widget, orient + 'view')

        if OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll", (-1), "units")
                elif event.num == 5:
                    view_command("scroll", 1, "units")

        elif OS == 'Windows':
            def onMouseWheel(event):
                # view_command("scroll", (-1) * int((event.delta / 120) * factor), what)
                view_command("scroll", -1*int(event.delta/120), "units")

        elif OS == 'Darwin':
            def onMouseWheel(event):
                view_command("scroll", event.delta, "units")

        return onMouseWheel


class Scrolling_Area(Frame, object):

    def __init__(self, master, width=None, anchor=N, height=None, mousewheel_speed=2, scroll_horizontally=True, xscrollbar=None, scroll_vertically=True, yscrollbar=None, background=None, inner_frame=Frame, **kw):
        Frame.__init__(self, master, class_="Scrolling_Area", background=background)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._width = width
        self._height = height

        self.canvas = Canvas(self, background=background, highlightthickness=0, width=width, height=height)
        self.canvas.grid(row=0, column=0, sticky=N + E + W + S)

        if scroll_vertically:
            if yscrollbar is not None:
                self.yscrollbar = yscrollbar
            else:
                self.yscrollbar = Scrollbar(self, orient=VERTICAL)
                self.yscrollbar.grid(row=0, column=1, sticky=N + S)

            self.canvas.configure(yscrollcommand=self.yscrollbar.set)
            self.yscrollbar['command'] = self.canvas.yview
        else:
            self.yscrollbar = None

        if scroll_horizontally:
            if xscrollbar is not None:
                self.xscrollbar = xscrollbar
            else:
                self.xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                self.xscrollbar.grid(row=1, column=0, sticky=E + W)

            self.canvas.configure(xscrollcommand=self.xscrollbar.set)
            self.xscrollbar['command'] = self.canvas.xview
        else:
            self.xscrollbar = None

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.innerframe = inner_frame(self.canvas, **kw)
        self.innerframe.pack(anchor=anchor)

        self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")

        self.canvas.bind('<Configure>', self._on_canvas_configure)

        Mousewheel_Support(self).add_support_to(self.canvas, xscrollbar=self.xscrollbar, yscrollbar=self.yscrollbar)

    @property
    def width(self):
        return self.canvas.winfo_width()

    @width.setter
    def width(self, width):
        self.canvas.configure(width=width)

    @property
    def height(self):
        return self.canvas.winfo_height()

    @height.setter
    def height(self, height):
        self.canvas.configure(height=height)

    def set_size(self, width, height):
        self.canvas.configure(width=width, height=height)

    def _on_canvas_configure(self, event):
        width = max(self.innerframe.winfo_reqwidth(), event.width)
        height = max(self.innerframe.winfo_reqheight(), event.height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
        self.canvas.itemconfigure("inner_frame", width=width, height=height)

    def update_viewport(self):
        self.update()

        window_width = self.innerframe.winfo_reqwidth()
        window_height = self.innerframe.winfo_reqheight()

        if self._width is None:
            canvas_width = window_width
        else:
            canvas_width = min(self._width, window_width)

        if self._height is None:
            canvas_height = window_height
        else:
            canvas_height = min(self._height, window_height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (window_width, window_height), width=canvas_width, height=canvas_height)
        self.canvas.itemconfigure("inner_frame", width=window_width, height=window_height)


class Question:

    def __init__(self, parent, question, answer):
        self.parent = parent
        self.question = question
        self.answer = answer
        self.create_widgets()

    def get_input(self):
        value = self.entry.get()
        print('value:', value)
        if value == self.answer:
            print("Right it's " + self.answer)
            self.label['text'] = self.question + "Right it's " + self.answer
        else:
            self.label['text'] = "Sorry, it was " + self.answer

    def create_widgets(self):
        self.labelframe = tk.LabelFrame(self.parent, text="Domanda:")
        self.labelframe.pack(fill="both", expand=True)

        self.label = tk.Label(self.labelframe, text=self.question)
        self.label.pack(expand=True, fill='both')

        self.entry = tk.Entry(self.labelframe)
        self.entry.pack()
        self.entry.bind("<Return>", lambda x: self.get_input())

        # self.button = tk.Button(self.labelframe, text="Click", command=self.get_input)
        # self.button.pack()

# --- main ---


root = tk.Tk()
root.title("Quiz")
root.geometry("400x300")


window = Scrolling_Area(root)
window.pack(expand=True, fill='both')


text = tk.Text(window.innerframe, width=10, height=20)
text.pack(expand=1, fill="both")

with open("Do Not Go Gentle into That Good Night.txt", "r") as f:
    for i in f.readlines():
        text.insert("end",i)
        text.see("end")

# for i in range(10):
#     one = randint(1, 10)
#     two = randint(1, 10)
#     Question(window.innerframe, "How is the result of {} + {} ?".format(one, two), str(one + two))
#
# domande = [("Qual è la prima leva del marketing mix? (prodotto o prezzo?", "prodotto")]
#
#
# for d, r in domande:
#     Question(window.innerframe, d, r)


root.mainloop()