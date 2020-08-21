# Copyright (c) All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

#-*-coding:utf-8-*-

"""
@File    : main.py
@Time    : 2020/08/10
@Author  : Coco Xu
@Version : 1.0
@Desc    : Take picture from usb camera using OpenCV, save into local folder,
           and upload into Azure Blob Storage.
"""

import os
import random
import sys
import time
import json

import PictureCapture
from PictureCapture import PictureCapture

import AppState

def main(
        imageFolderName = 'images',
        cameraIndex = 0,
        interval = 60,
        ):

    global pictureCapture

    try:
        # print("\nPython %s\n" % sys.version)
        print("Press Ctrl-C to exit.")

        with PictureCapture(imageFolderName, cameraIndex, interval) as pictureCapture:
            try:                
                pictureCapture.takePicture()
                pictureCapture.showVideoWindow()
            except KeyboardInterrupt:
                print("Camera capture module stopped")    
    except KeyboardInterrupt:
        print("Camera capture module stopped")

if __name__ == '__main__':
    main('images', 0, 60)