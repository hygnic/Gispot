#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/6/9 18:27
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------

# !/usr/bin/python2.7

# ! -*- coding: utf-8 -*-

from Tkinter import *

import os

import threading

pathDir = os.environ['HOMEPATH']

# print pathDir+'/hqzy/Demo/OCR_demo/'


root = Tk()

root.title("hello")

root.geometry('1000x480')

lock_my = 0


def printhello():
	print "hello"


def ocr_demo():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/OCR_demo/')
		
		status = os.system('python ocr_demo.py')
		
		lock_my = 0


# print "hello"


def ocr_demo_process():
	th = threading.Thread(target=ocr_demo)
	
	th.setDaemon(True)
	
	th.start()


# print "hello11111"


def lightweight_demo():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/lightweight_model/')
		
		status = os.system('python lightweight_demo.py')
		
		lock_my = 0


# print "hello"


def lightweight_demo_process():
	th = threading.Thread(target=lightweight_demo)
	
	th.setDaemon(True)
	
	th.start()


def super_resolution():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/super_resolution/')
		
		status = os.system('sh run.sh')
		
		lock_my = 0


def super_resolution_process():
	th = threading.Thread(target=super_resolution)
	
	th.setDaemon(True)
	
	th.start()


def style_transfer():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/style_transfer/')
		
		status = os.system('sh run.sh')
		
		lock_my = 0


def style_transfer_process():
	th = threading.Thread(target=style_transfer)
	
	th.setDaemon(True)
	
	th.start()


def voice_demo():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/voice_demo/')
		
		status = os.system('python voice_demo.py')
		
		lock_my = 0


def voice_demo_process():
	th = threading.Thread(target=voice_demo)
	
	th.setDaemon(True)
	
	th.start()


def voice_demo_with_spectrum():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/voice_demo/')
		
		status = os.system('python voice_demo_with_spectrum.py')
		
		lock_my = 0


def voice_demo_with_spectrum_process():
	th = threading.Thread(target=voice_demo_with_spectrum)
	
	th.setDaemon(True)
	
	th.start()


def voiceDemos_new():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/VoiceDemos_new/src/')
		
		status = os.system('python EchoMain.py')
		
		lock_my = 0


def voiceDemos_new_process():
	th = threading.Thread(target=voiceDemos_new)
	
	th.setDaemon(True)
	
	th.start()


def face_demo():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/face_demo/code/')
		
		status = os.system('python run_demo.py')
		
		lock_my = 0


def face_demo_process():
	th = threading.Thread(target=face_demo)
	
	th.setDaemon(True)
	
	th.start()


def cnnDemo():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/v2.6/')
		
		status = os.system('./cnnDemo')
		
		lock_my = 0


def cnnDemo_process():
	th = threading.Thread(target=cnnDemo)
	
	th.setDaemon(True)
	
	th.start()


def Video_Hierarchy():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		# os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('input_test.py')
		
		lock_my = 0


def Video_Hierarchy_process():
	th = threading.Thread(target=Video_Hierarchy)
	
	th.setDaemon(True)
	
	th.start()


def Test_CNN_speed():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Test_CNN_speed')
		
		lock_my = 0


def Test_CNN_speed_process():
	th = threading.Thread(target=Test_CNN_speed)
	
	th.setDaemon(True)
	
	th.start()


def Multi_Chips():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Multi_Chips')
		
		lock_my = 0


def Multi_Chips_process():
	th = threading.Thread(target=Multi_Chips)
	
	th.setDaemon(True)
	
	th.start()


def Web_camera():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Web_camera')
		
		lock_my = 0


def Web_camera_process():
	th = threading.Thread(target=Web_camera)
	
	th.setDaemon(True)
	
	th.start()


def Single_picture_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Web_camera')
		
		lock_my = 0


def Single_picture_input_process():
	th = threading.Thread(target=Single_picture_input)
	
	th.setDaemon(True)
	
	th.start()


def Single_video_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Single_video_input')
		
		lock_my = 0


def Single_video_input_process():
	th = threading.Thread(target=Single_video_input)
	
	th.setDaemon(True)
	
	th.start()


def Web_camera_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Web_camera_input')
		
		lock_my = 0


def Web_camera_input_process():
	th = threading.Thread(target=Web_camera_input)
	
	th.setDaemon(True)
	
	th.start()


def Picture_slide_show_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Web_camera_input')
		
		lock_my = 0


def Picture_slide_show_input_process():
	th = threading.Thread(target=Picture_slide_show_input)
	
	th.setDaemon(True)
	
	th.start()


def Multiple_chips_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Multiple_chips_input')
		
		lock_my = 0


def Multiple_chips_input_process():
	th = threading.Thread(target=Multiple_chips_input)
	
	th.setDaemon(True)
	
	th.start()


def Test_CNN_speed_input():
	global lock_my
	
	if (lock_my == 0):
		lock_my = 1
		
		os.chdir(pathDir + '/hqzy/Demo/')
		
		status = os.system('./Test_CNN_speed_input')
		
		lock_my = 0


def Test_CNN_speed_input_process():
	th = threading.Thread(target=Test_CNN_speed_input)
	
	th.setDaemon(True)
	
	th.start()


label = Label(root, text='sdkdemo', width=20, height=2, font=18).grid(padx=20,
																	  pady=10,
																	  row=0,
																	  column=0)

Button(root, text="分类测速", command=Video_Hierarchy_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=1, column=0)

Button(root, text="卷积测速", command=Test_CNN_speed_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=2, column=0)

Button(root, text="多块芯片应用", command=Multi_Chips_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=3, column=0)

Button(root, text="摄像头分类识别", command=Web_camera_input_process, width=20,
	   height=2, font=18).grid(padx=20, pady=0, row=4, column=0)

label = Label(root, text='交互式sdkdemo', width=20, height=2, font=18).grid(
	padx=20, pady=10, row=0, column=1)

Button(root, text="图片分类识别（input）", command=Single_picture_input_process,
	   width=20, height=2, font=18).grid(padx=20, pady=0, row=1, column=1)

Button(root, text="视频分类识别（input）", command=Single_video_input_process, width=20,
	   height=2, font=18).grid(padx=20, pady=0, row=2, column=1)

Button(root, text="摄像头分类识别（input）", command=Web_camera_input_process, width=20,
	   height=2, font=18).grid(padx=20, pady=0, row=3, column=1)

Button(root, text="图片幻灯片放映", command=Picture_slide_show_input_process, width=20,
	   height=2, font=18).grid(padx=20, pady=0, row=4, column=1)

Button(root, text="多块芯片应用（input）", command=Multiple_chips_input_process,
	   width=20, height=2, font=18).grid(padx=20, pady=0, row=5, column=1)

Button(root, text="分类测速（input）", command=Test_CNN_speed_input_process, width=20,
	   height=2, font=18).grid(padx=20, pady=0, row=6, column=1)

label = Label(root, text='图像处理', width=20, height=2, font=18).grid(padx=20,
																   pady=10,
																   row=0,
																   column=2)

Button(root, text="手写字识别", command=ocr_demo_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=1, column=2)

Button(root, text="图像增强", command=super_resolution_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=2, column=2)

Button(root, text="风格转换", command=style_transfer_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=3, column=2)

Button(root, text="人脸识别", command=face_demo_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=4, column=2)

label = Label(root, text='语音处理', width=20, height=2, font=18).grid(padx=20,
																   pady=10,
																   row=0,
																   column=3)

Button(root, text="语音识别", command=voice_demo_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=1, column=3)

Button(root, text="语音识别（频谱图）", command=voice_demo_with_spectrum_process,
	   width=20, height=2, font=18).grid(padx=20, pady=0, row=2, column=3)

Button(root, text="声纹识别", command=voiceDemos_new_process, width=20, height=2,
	   font=18).grid(padx=20, pady=0, row=3, column=3)

root.mainloop()
