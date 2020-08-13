#-*-coding:utf-8-*-
'''
@File    : PictureCapture.py
@Time    : 2020/08/10
@Author  : Coco Xu
@Version : 1.0
@Desc    : Take picture from usb camera and save into local folder, per TimeInveral by using OpenCV.
'''


import cv2
import os

import utility

TimeInveral = 10  #视频帧计数间隔频率
imageFolder = 'image'
Count = 1

utility.mkdir(imageFolder)
        
vc = cv2.VideoCapture(0)  #读入视频文件,将视频文件地址写入即可 ('Test.avi')

    
if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
else:
    rval = False
    
timeF = TimeInveral
    
while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(Count % timeF == 0): #每隔timeF帧进行存储操作
        cv2.imwrite(imageFolder + '/' + str(Count) + '.jpg', frame) #存储为图像
    Count = Count + 1
    cv2.waitKey(1)
vc.release()
