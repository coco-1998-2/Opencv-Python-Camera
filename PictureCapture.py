# Copyright (c) All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

#-*-coding:utf-8-*-

"""
@File    : PictureCapture.py
@Time    : 2020/08/10
@Author  : Coco Xu
@Version : 1.0
@Desc    : Take jpg image from usb camera and save into local folder, using OpenCV.
           Image is named by the time it was taken, eg:"2020-08-21-14-03-13.jpg"
"""

import cv2
import os
import datetime

import utility

class PictureCapture(object):
    def __init__(self, imageFolderName, cameraIndex, interval):
        print("============\rPictureCapture::__init__()")
        self.imageFolderName = imageFolderName
        self.cameraIndex = cameraIndex
        self.interval = interval
        self.count = 1
    
    def __enter__(self):
        utility.mkdir(self.imageFolderName)

        return self

    def __savePicture(self, frame):
        current_time_str = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d-%H-%M-%S')
        cv2.imwrite(self.imageFolderName + '/' + current_time_str + '.jpg', frame)  # 存储为图像
        print("===========\r\nImage "+ current_time_str +"saved Successfully.\r\n========\r\n")


    def takePicture(self):
        vc = cv2.VideoCapture(self.cameraIndex)  # 若读入视频文件,将视频文件地址写入('Test.avi')

        if vc.isOpened(): 
            print("===========\r\nCamera Opened Successfully.\r\n========\r\n")
            rval , frame = vc.read()
            self.__savePicture(frame)
        else:
            rval = False
            print("===========\r\nWARNING : No Video Source\r\n===========\r\n")
    
        vc.release()
        cv2.destroyWindow("usb camera")
    
    
    def showVideoWindow(self):
        timeF = self.interval
     
        vc = cv2.VideoCapture(self.cameraIndex)  # 若读入视频文件,将视频文件地址写入('Test.avi')

        if vc.isOpened(): 
            print("===========\r\nCamera Opened Successfully.\r\n========\r\n")
            rval , frame = vc.read()
        else:
            rval = False
            print("===========\r\nWARNING : No Video Source\r\n===========\r\n")

        while rval:   # 循环读取视频帧
            cv2.imshow("usb camera", frame)
            rval, frame = vc.read()
            
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC key
                break

            if(self.count % timeF == 0): # 每隔timeF帧进行存储操作
                print("\ncount %s\n" % str(self.count) )
                self.__savePicture(frame)
                self.count = self.count + 1
    
        vc.release()
        cv2.destroyWindow("usb camera")
        
    def __exit__(self, exception_type, exception_value, traceback):
        cv2.destroyAllWindows()    