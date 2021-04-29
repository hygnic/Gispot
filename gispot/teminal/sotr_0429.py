# -*- coding:utf-8 -*-
# -------------------------------------------
# Name:              sotr_0429
# Author:            Hygnic
# Created on:        2021/4/29 22:14
# Version:           
# Reference:         
"""
Description:         
Usage:               
"""
# -------------------------------------------
a_list = ["a","a","b","b","b","c","d","d","d"]
# a_list = ["r","v","a","a","b","b","b","c","d","d","d"]
b_list = []


cnt = "start_flag"
for a_item in a_list:
    if cnt == "start_flag":
        last_value = a_item
        cnt = 1
        b_list.append(cnt)
        
    else:
        if a_item == last_value:
            cnt+=1
            b_list.append(cnt)
            
        else:
            last_value = a_item
            b_list.append(1)
            cnt = 1
            
print b_list
