# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/10
# python2.7

import Tkinter as tk
import ttk

wuya = tk.Tk()
wuya.title("wuya")
wuya.geometry("300x200+10+20")

# 创建下拉菜单
cmb = ttk.Combobox(wuya)
cmb['value'] = ('上海','北京','天津','广州')
cmb.pack()
wuya.mainloop()