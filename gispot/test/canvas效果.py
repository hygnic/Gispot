#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/21 11:22
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------

import time
from Tkinter import *

# 　配置
# 　要打开的图像
image1 = "handou.gif"

# 初始坐标
x0 = 50.0
y0 = 50.0

# 列表将包含所有的x和y坐标.到目前为止，他们只包含初始坐标
x = [x0]
y = [y0]

# 每次移动的速度或距离
vx = 1.0  # x 速度
vy = 0.5  # y 速度

# 边界，这里要考虑到图片的大小，要预留一半的长和宽
x_min = 46.0
y_min = 46.0
x_max = 754.0
y_max = 554.0

# 图片间隔时间,要动画效果，此处设为每秒４０帧
sleep_time = 0.025

# 运行步数
range_min = 1
range_max = 2000

# 创建500次的x和y坐标
for t in range(range_min, range_max):
	# 新坐标等于旧坐标加每次移动的距离
	new_x = x[t - 1] + vx
	new_y = y[t - 1] + vy
	
	# 如果已经越过边界，反转方向
	if new_x >= x_max or new_x <= x_min:
		vx = vx * -1.0
	
	if new_y >= y_max or new_y <= y_min:
		vy = vy * -1.0
	
	# 添加新的值到列表
	x.append(new_x)
	y.append(new_y)

# 开始使用ｔｋ绘图
root = Tk()
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack()

photo1 = PhotoImage(file=image1)
width1 = photo1.width()
height1 = photo1.height()
image_x = (width1) / 2.0
image_y = (height1) / 2.0

# 每次的移动
for t in range(range_min, range_max):
	canvas.create_image(x[t], y[t], image=photo1, tag="pic")
	canvas.update()
	
	# 暂停0.05妙，然后删除图像
	time.sleep(sleep_time)
	canvas.delete("pic")

root.mainloop()

# 上述代码修改自：http: // pastebin.com / BZ9XRg8Z
# 改动的幅度不是很大，源代码：
# """
# Endlessly bouncing ball - demonstrates animation using Python and TKinter
# """
# import time
#
# # Initial coordinates
# x0 = 10.0
# y0 = 30.0
#
# ball_diameter = 30
#
# # Get TKinter ready to go
# from Tkinter import *
#
# window = Tk()
# canvas = Canvas(window, width=400, height=300, bg='white')
# canvas.pack()
#
# # Lists which will contain all the x and y coordinates. So far they just
# # contain the initial coordinate
# x = [x0]
# y = [y0]
#
# # The velocity, or distance moved per time step
# vx = 10.0  # x velocity
# vy = 5.0  # y velocity
#
# # Boundaries
# x_min = 0.0
# y_min = 0.0
# x_max = 400.0
# y_max = 300.0
#
# # Generate x and y coordinates for 500 timesteps
# for t in range(1, 500):
#
# 	# New coordinate equals old coordinate plus distance-per-timestep
# 	new_x = x[t - 1] + vx
# 	new_y = y[t - 1] + vy
#
# 	# If a boundary has been crossed, reverse the direction
# 	if new_x >= x_max or new_x <= x_min:
# 		vx = vx * -1.0
#
# 	if new_y >= y_max or new_y <= y_min:
# 		vy = vy * -1.0
#
# 	# Append the new values to the list
# 	x.append(new_x)
# 	y.append(new_y)
#
# # For each timestep
# for t in range(1, 500):
# 	# Create an circle which is in an (invisible) box whose top left corner is at (x[t], y[t])
# 	canvas.create_oval(x[t], y[t], x[t] + ball_diameter, y[t] + ball_diameter,
# 					   fill="blue", tag='blueball')
# 	canvas.update()
#
# 	# Pause for 0.05 seconds, then delete the image
# 	time.sleep(0.05)
# 	canvas.delete('blueball')
#
# # I don't know what this does but the script won't run without it.
# window.mainloop()