# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

"""
锚点文件,
从__file__改用sys.args[0]
"""
import os
import sys

# 不使用该方法
_paths_gispot = os.path.abspath(sys.argv[0])  # G:\MoveOn\Gispot_copy\bin\Gispot.py
# print "_paths_gispot:",_paths_gispot
_paths_bin = os.path.dirname(_paths_gispot)  # G:\MoveOn\Gispot_copy\bin
_Groot = os.path.dirname(_paths_bin)  # E:\move on move on\gispot
_GUIs_p = os.path.join(_Groot, "GUIs")
_Docs_p = os.path.join(_Groot, "docs")
_base_icons_path = os.path.abspath(os.path.join(_GUIs_p, "Icons")) # E:\move on move on\gispot\GUIs\Icons

# G:\MoveOn\GUIs\Icons\GitHub_32.gif
# docs

# root = os.path.abspath(os.path.dirname(sys.argv[0]))
# _docs_p = os.path.join(root,"docs")
# _explode_mulitp = os.path.join(_docs_p, r"explode_mulitp.gc")
# _gstrename = os.path.join(_docs_p, r"multiplexport.gc")
# _multip_ejpg = os.path.join(_docs_p, r"multiplexport.gc")
# _path_bin = os.path.dirname(sys.argv[0])  # G:\MoveOn\Gispot\bin
# _path_root = os.path.dirname(_path_bin)  # G:\MoveOn\Gispot
# _GUIs_p = os.path.join(_path_root, "GUIs")
# _base_icons_path = os.path.abspath(os.path.join(_GUIs_p, "Icons"))

def code2exe():
	"""配置doc文件和图片，用于py2exe封装"""
	global _base_icons_path
	global _Docs_p
	# py2exe_path = "images"
	_base_icons_path = "images"
	_Docs_p = "gisdocs"
# 不封装时关闭该函数
# code2exe()



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
	# gif_github= os.path.join(ur"G:\MoveOn\Gispot_copy\bin\dist\images", "GitHub_32.gif")
	# gif_github= os.path.join(ur"images", "GitHub_32.gif")
	
	gif_empty1 =os.path.join(_base_icons_path, "empty.gif")
	# gif_test= os.path.join(_base_icons_path, "folder_1.gif")
	
	# 应用于toolbar中的按钮图标
	gif_dos = os.path.join(_base_icons_path, "dos.gif")
	gif_editor = os.path.join(_base_icons_path, "editor.gif")
	gif_tool = os.path.join(_base_icons_path,"toolbox.gif")
	
	# 应用于toolbar_viewer中的按钮图标
	gif_python = os.path.join(_base_icons_path, "python_48.gif")
	gif_python32 = os.path.join(_base_icons_path, "python_32.gif")

# G:\MoveOn\Gispot\docs
class DocPath(object):
	doc_me = os.path.join(_Docs_p, "multiplexport.gc")
	doc_em = os.path.join(_Docs_p, "explode_mulitp.gc")
	doc_trans_fbt = os.path.join(_Docs_p, "trans_fbt.gc")
	doc_trans_gst = os.path.join(_Docs_p, "trans_gst.gc")
	doc_gstrename = os.path.join(_Docs_p, "gstrename.gc")
	doc_task_dispatch = os.path.join(_Docs_p, "task_dispatch.gc")
	doc_saveacopy = os.path.join(_Docs_p, "save_acopy.gc")



	
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
