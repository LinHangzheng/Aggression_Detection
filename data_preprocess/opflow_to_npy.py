# -*- coding: utf-8 -*-
"""opflow_to_csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FtjJvuzj2xBrGxB59JVhwkvRwvHEWBrb
"""

import glob
import cv2
import numpy as np
import os
import re
import gc
from tqdm import tqdm

os.environ['CUDA_VISIBLE_DEVICES'] = "0,1"
# get the work path
path = os.getcwd()

os.chdir(path)
os.listdir(path)

# cur_path = os.path.dirname(os.path.abspath("__file__"))
# par_path = os.path.abspath(os.path.join(cur_path,os.path.pardir))
# print (cur_path)
# print (par_path)
# data_kind = "Movie Dataset"
# data_path = par_path+"/"+ data_kind + " opflow"
# os.listdir(data_path)

# name list of all dataset 

data_kind_list = ["SC_nodelete_MP4","uniform_SC_MP4","SC_delete_MP4","uniform_youtube_MP4","Real_Life_Violence_Dataset"]
data_kind = data_kind_list[4]

data_path = path+"/video_image"+ "/"+ data_kind + " opflow"
print ("data path:",data_path)
os.listdir(data_path)

file_kind = data_kind+' opflow'
fight_files = glob.glob(data_path+'/fight'+'/*mp4')
noFight_files = glob.glob(data_path+'/noFight'+'/*mp4')
total_files = fight_files + noFight_files
print ("fight files:", len(fight_files))
print ("noFight files:",len(noFight_files))
# size for potical flow batch
L = 5

# key for the string sort, it will get the digit 
# from the string and then sort it 
def sort_key(s):
    if s:
        try:
            c = re.findall(r"\d+", s)[-1]

        except:
            c = -1
        return int(c)

# generator function for the images
def generator(list1, lits2):
    '''
    Auxiliar generator: returns the ith element of both given list with
         each call to next() 
    '''
    for x,y in zip(list1,lits2):
        yield x, y

# convert the optical flow into the csv file
def convert_data_to_npy(file,file_kind):
    count = 0
    for video_path in tqdm(file):
        print (video_path)
        count+=1
        x_images = glob.glob(video_path + '/x_*.jpg')
        x_images.sort(key=sort_key)
        y_images = glob.glob(video_path + '/y_*.jpg')
        y_images.sort(key=sort_key)
        nb_stacks = len(x_images)-L+1
        flow = np.zeros(shape=(224,224,2*L,nb_stacks), dtype=np.float64)
        gen = generator(x_images,y_images)
        # print(video_path)
        # print(np.shape(x_images),np.shape(y_images))
        for i in range(len(x_images)):
            flow_x_file, flow_y_file = next(gen)
            img_x = cv2.imread(flow_x_file, cv2.IMREAD_GRAYSCALE)
            img_y = cv2.imread(flow_y_file, cv2.IMREAD_GRAYSCALE)
            # Assign an image i to the jth stack in the kth position, but also
            # in the j+1th stack in the k+1th position and so on
            # (for sliding window) 
            for s in list(reversed(range(min(L,i+1)))):
                if i-s < nb_stacks:
                    flow[:,:,2*s,i-s] = img_x
                    flow[:,:,2*s+1,i-s] = img_y
            del img_x,img_y
            gc.collect()                
        flow = np.transpose(flow, (3, 0, 1, 2))
        
        file_name = re.search(r'ght/(.*?)(\.mp4)',video_path).group(1)
        
        if "noFight" in video_path:
            outPutDirName=path+'/npy_'+str(L)+'/'+file_kind+'/noFight/'
            if not os.path.exists(outPutDirName):
                # If it doesn't exit, create it
                os.makedirs(outPutDirName)
            out_path = '%s.npy'%os.path.join(outPutDirName,file_name)
        else :
            outPutDirName=path+'/npy_'+str(L)+'/'+file_kind+'/fight/'
            if not os.path.exists(outPutDirName):
                # If it doesn't exit, create it
                os.makedirs(outPutDirName)
            out_path = '%s.npy'%os.path.join(outPutDirName,file_name)
        print('%i/%i'%(count,len(file)))
        # np.savetxt(out_path, flow, fmt="%d",delimiter = ',')
        np.save(file = out_path,arr = flow) 

if __name__ == "main":
    convert_data_to_npy(total_files,file_kind)
