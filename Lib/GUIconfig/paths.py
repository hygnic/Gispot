# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

"""锚点文件"""

import os


_libs_hyconf = os.path.dirname(__file__)  # E:/move on move on/gispot/Lib/GUIconfig
_lib = os.path.dirname(_libs_hyconf)  # E:\move on move on\gispot\Lib
_Groot = os.path.dirname(_lib)  # E:\move on move on\gispot
# _bin_p = os.path.join(_Groot, "bin")
# _docs_p = os.path.join(_Groot, "docs")
# _Gispot_p = os.path.join(_Groot, "_Gispot_p")

_GUIs_p = os.path.join(_Groot, "GUIs")


# E:\move on move on\gispot\GUIs\Icons
_base_icons_path = os.path.abspath(os.path.join(_GUIs_p, "Icons"))
# docs
# _explode_mulitp = os.path.join(_docs_p, r"explode_mulitp.gc")
# _gstrename = os.path.join(_docs_p, r"multiplexport.gc")
# _multip_ejpg = os.path.join(_docs_p, r"multiplexport.gc")



class GifPath(object):
	"""
	gif图片的路径
	"""
	# _base_icons_path
	gif_forbid = os.path.join(_base_icons_path, "forbit.gif")
	gif_close = os.path.join(_base_icons_path, "close30_4.gif")
	gif_folder = os.path.join(_base_icons_path, "folder1.gif")
	
	gif_textfile = os.path.join(_base_icons_path, "Text_File16.gif")
	gif_add_file = os.path.join(_base_icons_path, "file3.gif")
	
	gif_info = os.path.join(_base_icons_path, "help_info_3.gif")
	gif_confirm= os.path.join(_base_icons_path, "confirm32_9.gif")
	
	gif_github= os.path.join(_base_icons_path, "GitHub_32.gif")
	
	gif_empty1 =os.path.join(_base_icons_path, "empty.gif")
	# gif_test= os.path.join(_base_icons_path, "folder_1.gif")
	
	# 应用于toolbar中的按钮图标
	gif_dos = os.path.join(_base_icons_path, "dos.gif")
	gif_editor = os.path.join(_base_icons_path, "editor.gif")
	
	
	# 应用于toolbar_viewer中的按钮图标
	gif_python = os.path.join(_base_icons_path, "python_48.gif")
	
	
if __name__ == '__main__':
	aa = GifPath.gif_github
	print os.path.exists(aa)


# class Path_GC(object):
# 	"""
# 	GC帮助文档的配置地址
# 	"""
# 	@property
# 	def explode_mulitp(self):
# 		return _explode_mulitp
#
# 	@property
# 	def gstrename(self):
# 		return _gstrename
#
# 	@property
# 	def multip_ejpg(self):
# 		return _multip_ejpg
#
#
#
# if __name__ == '__main__':
# 	pass
