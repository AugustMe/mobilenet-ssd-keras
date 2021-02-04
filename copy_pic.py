# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:10:11 2020

@author: zqq
"""

import os
import shutil

# 读取图片的路径
read_path = "VOCdevkit/VOC2007/JPEGImages/"
# 存放图片的路径
save_path = "img"
if not os.path.exists(save_path):
    os.mkdir(save_path)
fileType = '.jpg'
num = 0
# 读取并遍历读取txt中的每行
with open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'r') as f:
    for name in f:
        fileName = name.strip()  # 去除末尾的换行
        # print(fileName)
        # print(type(fileName)) # 查看文件类型

        # 读取并遍历文件夹中的图片
        for file in os.listdir(read_path):
            # print(file)
            # print(type(file))

            if fileName + fileType == file:
                num += 1
                shutil.copy(os.path.join(read_path, fileName + fileType), save_path)
                print("%s Copy successfully" % (fileName + fileType))
    print("Copy complete!")
    print("Total pictures copied:", num)


### 测试
# shutil.copy('img_res/000001.jpg',save_path)
# fileName = '000001'
# shutil.copy(os.path.join(read_path,fileName+fileType),save_path)



# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 21 17:10:11 2020
#
# @author: zqq
# """
#
# import os
# import shutil
#
# # 读取图片的路径
# read_path = "VOCdevkit/VOC2007/JPEGImages/"
# # 存放图片的路径
# save_path = "img"
# if not os.path.exists(save_path):
#     os.mkdir(save_path)
# fileType = '.jpg'
# num = 0
# # 读取并遍历读取txt中的每行
# with open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'r') as f:
#     for name in f:
#         fileName = name.strip()  # 去除末尾的换行
#         # print(fileName)
#         # print(type(fileName)) # 查看文件类型
#         shutil.copy(os.path.join(read_path, fileName + fileType), save_path)
#         print("%s Copy successfully" % (fileName + fileType))
#         num+=1
#     print("Copy complete!")
#     print("Total pictures copied:", num)
#
# ### 测试
# # shutil.copy('img_res/000001.jpg',save_path)
# # fileName = '000001'
# # shutil.copy(os.path.join(read_path,fileName+fileType),save_path)






