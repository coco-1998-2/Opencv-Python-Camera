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
import datetime

import utility


TIME_INTERVAL = 10*60 # 视频帧计数间隔频率
IMAGE_FOLDER = 'images'
Count = 1

utility.mkdir(IMAGE_FOLDER)
     
vc = cv2.VideoCapture(1)  # 读入视频文件,将视频文件地址写入即可 ('Test.avi')
# vc.NamedWindow("Face detection", 1)

if vc.isOpened(): # 判断是否正常打开
    rval , frame = vc.read()
    print("===========================\r\nCamera Opened Successfully.\r\n===========================\r\n")
else:
    rval = False
    print("===========================\r\nWARNING : No Video Source\r\n===========================\r\n")
    
timeF = TIME_INTERVAL
    
while rval:   # 循环读取视频帧
    cv2.imshow("usb camera", frame)
    rval, frame = vc.read()
    
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC key
        break

    if(Count % timeF == 0): # 每隔timeF帧进行存储操作
        print("\ncount %s\n" % str(Count) )
        current_time_str = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d-%H-%M-%S')
        cv2.imwrite(IMAGE_FOLDER + '/' + current_time_str + '.jpg', frame) # 存储为图像
        Count = Count + 1
    
vc.release()
cv2.destroyWindow("usb camera")