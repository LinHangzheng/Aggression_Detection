
# -*- coding: utf-8 -*-
import os
#设定文件路径
path='video_image/Real_Life_Violence_Dataset/fight'   
i=1
#对目录下的文件进行遍历
for category in os.listdir(path):
#判断是否是文件
    if os.path.isdir(os.path.join(path,category))==True:
#设置新文件名
        new_name=category.replace(category,"V_%d.mp4"%i)
#重命名
        os.rename(os.path.join(path,category),os.path.join(path,new_name))
        i+=1
#结束
print ("End")