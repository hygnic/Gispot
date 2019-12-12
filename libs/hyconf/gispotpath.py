# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

"""锚点文件"""

import os
import Tkinter as tk



_libs_hyconf = os.path.dirname(__file__)  # E:/move on move on/Gispot/libs/hyconf
_lib = os.path.dirname(_libs_hyconf)  # E:\move on move on\Gispot\libs
_Groot = os.path.dirname(_lib)  # E:\move on move on\Gispot
_bin_p = os.path.join(_Groot, "bin")
_docs_p = os.path.join(_Groot, "docs")
_GUIs_p = os.path.join(_Groot, "GUIs")
_Gispot_p = os.path.join(_Groot, "_Gispot_p")

# docs
# _explode_mulitp = os.path.join(_docs_p, r"explode_mulitp.gc")
# _gstrename = os.path.join(_docs_p, r"multip_ejpg.gc")
# _multip_ejpg = os.path.join(_docs_p, r"multip_ejpg.gc")



class GifPath():
	basepath = os.path.abspath(os.path.join(_GUIs_p,"Icons"))
	gif_forbid = os.path.join(basepath, "forbid.gif")
	



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
