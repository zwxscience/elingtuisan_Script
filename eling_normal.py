import os
import cv2
import numpy as np
import time
import random


# 使用的Python库及对应版本：
# python 3.6
# opencv-python 3.3.0
# numpy 1.13.3
# 用到了opencv库中的模板匹配和边缘检测功能

press_time = 1
def get_screenshot(id):
    os.system('adb shell screencap -p /sdcard/%s.png' % str(id))
    os.system('adb pull /sdcard/%s.png .' % str(id)) 

#需要将一个橙色或者紫色神魂放到背包格子的第一位
#以下是1920×1080 分辨率的手机坐标，其他手机分辨率请自行适配
#995,1784 神社按钮
#544 512 头部
#558 720 胸部
#566 1027 腰部
#517 1472 腿部
#499 1844 降妖
#977 289 挑战首领

     
def xiangyao():
    cmd = ('adb shell input tap %i %i' % (499, 1844)) #499 1844 降妖
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.5))
    
def tiaozhan():
    cmd = ('adb shell input tap %i %i' % (977, 289)) #977 289 挑战首领
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(2.0, 3.0)) 
 
def shenshe():
    cmd = ('adb shell input tap %i %i' % (995, 1784)) #995,1784 神社按钮
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.5))
 
def tiaodou():
    cmd = ('adb shell input tap %i %i' % (544, 512)) 
    #544 512 头部
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(2, 2.5))
    cmd = ('adb shell input tap %i %i' % (558, 720)) 
    #558 720 胸部
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.5))    
    cmd = ('adb shell input tap %i %i' % (566, 1027)) 
    #566 1027 腰部
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.5))
    cmd = ('adb shell input tap %i %i' % (517, 1472)) 
    #517 1472 腿部
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.5))
    
# 循环直到游戏失败结束
while(True):
    #get_screenshot(0)
    #img_rgb = cv2.imread('%s.png' % 0, 0)
    #cv2.imwrite('last.png', img_rgb)
    
    xiangyao()
    tiaozhan()
    shenshe()
    tiaodou()
