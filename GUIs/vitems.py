# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2020/3/17
# python2 arcgis10.6

import tkinter as tk
from TkGUIconfig import newidgets
from TkGUIconfig import paths
from ccmd import export
"""viewer items
配置位于主界面右边的toolbar viewer中的部件"""

def test_0317(master):
	newidgets.ButtonFrame(
		master,
		tk.PhotoImage(file=paths.GifPath.gif_python),
		"test",command=export.export
	)