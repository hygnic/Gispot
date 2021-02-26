#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/2/19 15:26
# Reference: https://pythonprogramming.altervista.org/png-to-gif/
"""
Description: 将图片导出未gif图
Usage:
"""
# ---------------------------------------------------------------------------
import PIL.Image as Image
import os
import glob


def togif():
    # Create the frames
    frames = []
    imgs = glob.glob("*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    frames[0].save('png_to_gif.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=1000, loop=0)


if __name__ == '__main__':
    path = r"G:\MoveOn\Gispot\gispot\teminal\img"
    os.chdir(path)
    imagess = [u"带描边_wanzheng.jpg", u"无描边.jpg", u"无描边.jpg"]
    
    togif()