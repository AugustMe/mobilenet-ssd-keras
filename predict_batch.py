# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:30:52 2020

@author: zqq
"""

import os
from ssd import SSD
from PIL import Image
import glob

def detect_img(indir,outdir):
    ssd = SSD()
    #遍历该目录下的所有图片文件
    for filename in glob.glob(indir):
        print("Start, the detect image is:",filename)
        img = Image.open(filename)
        img = ssd.detect_image(img)
        #img.show() # 显示图片
        img.save(os.path.join(outdir,os.path.basename(filename)))
        print("End, the detection of this image")
        print('---------------------------------')
    
if __name__ == '__main__':
    indir = "img/*.jpg"      # 待检测图片路径
    outdir = "img_res"       # 检测后图片的保存路径
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    detect_img(indir,outdir) # 调用检测函数