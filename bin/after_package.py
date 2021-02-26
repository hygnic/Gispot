# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/2/22 0:22
# Reference:https://www.cnblogs.com/rongge95500/p/11271764.html
"""
Description: 在完成打包后执行的脚本，作用是解压缩文件，创建快捷方式等
Usage:
"""
# ---------------------------------------------------------------------------
from __future__ import absolute_import
import os
import zipfile
import random
import time
import ConfigParser



"""
import sys
# 希望导入gpconfig这个自定义包，但是报错
root_gispot =  os.path.abspath(os.path.dirname(os.path.dirname(sys.argv[0]))) # G:\MoveOn\Gispot
gpconfig_path = os.path.abspath(os.path.join(root_gispot, "Lib", "gpconfig")) # G:\MoveOn\Gispot\Lib\gpconfig
print gpconfig_path
sys.path.append(gpconfig_path)
sys.path.append(r"G:\MoveOn\Gispot\Lib\gpconfig")
sys.path.append(r"G:\MoveOn\Gispot\GUIs")
for i in sys.path:
    print i
# from gpconfig import gppath
from gpconfig import gppath
"""

def unzip(my_zip, unzip_folder):
    """
    unzip file function
    :param my_zip: zip file
    :param unzip_folder: 解压缩后文件的存放路径
    :return:
    """
    if not os.path.isdir(unzip_folder):
        os.makedirs(unzip_folder)
    with zipfile.ZipFile(my_zip, 'r') as f:
        for a_file in f.namelist():
            f.extract(a_file, path=unzip_folder)
    os.remove(my_zip)


if __name__ == '__main__':
    use_ttktheme_module = True

    print "Current WorkSpace: <{}>".format(os.getcwd())
    """______________________________________________________________________"""
    """______________________________________________________________________"""

    if not os.path.isdir("dist"):
        raise OSError("dist file does not exists")

    if use_ttktheme_module: # 如果要将ttkthemes打包进去
        unzip("dist/library.zip", "dist/library")
        time.sleep(0.3)
        os.renames("dist/library", "dist/library.zip")
        os.renames("dist/ttkthemes/ttkthemes_patch.zip", "dist/library.zip/ttkthemes/ttkthemes_patch.zip")
        time.sleep(1)
        unzip("dist/library.zip/ttkthemes/ttkthemes_patch.zip",
                   "dist/library.zip/ttkthemes")
        time.sleep(1)
    new_name = "Gisopt{}{}".format(random.randint(10000, 99999), time.strftime("%m%d"))  # Gisopt189090222
    os.renames("dist",new_name)
    #