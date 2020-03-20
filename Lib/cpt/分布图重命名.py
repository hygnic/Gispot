# -*- coding: utf-8 -*-
# User: hygnic liaochen
# Date: 2019/9/17

import os

# 放置XJQYDM+乡镇名称的txt文档，注意编码
one_file_path = ur"G:\古蔺县\古蔺县分布图\成果\fbt.txt"
# 图片地址
path2 = ur'G:\古蔺县\古蔺县分布图\改名 1'

fd = open(one_file_path, mode="r")
list1 = fd.readlines()
list2 = os.listdir(path2)
# listphoto = []
# for l2 in list2:
#     i = l2.split('.')
#     print i[0]
#     listphoto.append(i[0])

# print len(listphoto[0])
for l2 in list2:
    if l2.endswith('jpg'):
        for l1 in list1:
            if l2.split('.')[0] == l1[9:].decode('utf8').split('\n')[0]:
                oldname = os.path.join(path2, l2)
                XJQYDM = l1[:9]
                newname1 = 'FBT'
                newname2 = '00007001.jpg'
                newfile = os.path.join(path2, newname1 + XJQYDM + newname2)
                os.rename(oldname, newfile)
                print 'ok'
