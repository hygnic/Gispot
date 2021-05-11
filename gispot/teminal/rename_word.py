# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              rename_word
# Author:            Hygnic
# Created on:        2021/5/10 9:12
# Version:           
# Reference:         
"""
Description:         重命名word文件
Usage:               
"""
# -------------------------------------------
import os



def rename_word(dir):
    
    save_dir = os.path.abspath(os.path.dirname(dir)+os.path.sep+"word_save")
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    print save_dir
    for a_word in os.listdir(dir):
        old_name = a_word
        new_name = old_name.replace(
            u"审查的村民（代表）会议记录", "")
        print new_name
        os.rename(os.path.join(dir,old_name),
                  os.path.join(save_dir, new_name))
        
    
    
if __name__ == '__main__':
    dirs = ur"G:\成员资格"
    rename_word(dirs)