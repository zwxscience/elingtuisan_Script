import os
import cv2
import numpy as np
import threading
import time
#import time
#import random

# 封印功能，命令的响应速度太慢，只能用来做辅助功能
# 使用的Python库及对应版本：
# python 3.6
# opencv-python 3.3.0
# numpy 1.13.3
# 用到了opencv库中的模板匹配和边缘检测功能
def get_screenshot(id):
    os.system('adb shell screencap -p /sdcard/%s.png' % str(id))
    os.system('adb pull /sdcard/%s.png .' % str(id)) 

#需要将一个橙色或者紫色神魂放到背包格子的第一位
#以下是1920×1080 分辨率的手机坐标，其他手机分辨率请自行适配
#1066 798 功能选择
#239 515 猎魂
#882 1057 封印
#538,1262 开始
#350 50 左上角
#750 50 右上角  
#780 1200 右下角
#316 1786 冻结
#536 1786 伤害加成
#770 1786 回复
def prepare_game():
    cmd = ('adb shell input tap %i %i' % (1066, 798)) #1066 798 功能选择
    os.system(cmd)
    print(cmd)
    time.sleep(3)
    cmd = ('adb shell input tap %i %i' % (882, 1057)) #1066 798 功能选择
    os.system(cmd)
    print(cmd)
    time.sleep(3)

def start_game():
    cmd = ('adb shell input tap %i %i' % (538, 1262)) #538,1262 开始
    os.system(cmd)
    print(cmd)
    #time.sleep(0.1)

def oneRound(arg,order):
    for i in range(60):
        if (order == 0):
            get_minggestone(arg)
        else :
            get_minggestone_re(arg)
    
def get_minggestone(arg):
    for y in range(100, 500, 100):
        for x in range(350, 750, 134):
            cmd = ('adb shell input tap %i %i' % (x+67, y+50)) #遍历点击
            #cmd = ('adb shell input swipe %i %i %i %i' % (x+50, y+57, x+50, y+57))
            os.system(cmd)
            print(cmd)
            print('the click thread is:%s\r' %arg)
            #time.sleep(0.01)
    #cmd = ('adb shell input tap %i %i' % (316, 1786)) #316 1786 冻结
    #os.system(cmd)
    #print(cmd)
    #time.sleep(0.01)
    cmd = ('adb shell input tap %i %i' % (536, 1786)) #536 1786 伤害加成
    os.system(cmd)
    print(cmd)
    #time.sleep(0.01)
    #cmd = ('adb shell input tap %i %i' % (770, 1786)) #770 1786 回复
    #os.system(cmd)
    #print(cmd)
    #time.sleep(0.01)

def get_minggestone_re(arg):
    for y in range(500, 100, -100):
        for x in range(750, 350, -134):
            cmd = ('adb shell input tap %i %i' % (x-67, y-50)) #遍历点击
            #cmd = ('adb shell input swipe %i %i %i %i' % (x+50, y+57, x+50, y+57))
            os.system(cmd)
            print(cmd)
            print('the click thread is:%s\r' %arg)
            #time.sleep(0.001)
    #cmd = ('adb shell input tap %i %i' % (316, 1786)) #316 1786 冻结
    #os.system(cmd)
    #print(cmd)
    #time.sleep(0.01)
    cmd = ('adb shell input tap %i %i' % (536, 1786)) #536 1786 伤害加成
    os.system(cmd)
    print(cmd)
    #time.sleep(0.01)
    #cmd = ('adb shell input tap %i %i' % (770, 1786)) #770 1786 回复
    #os.system(cmd)
    #print(cmd)
    #time.sleep(0.01)      

prepare_game()   
start_game() 
# 循环三次

# 下面是获取分辨率图片及坐标
#get_screenshot(0)
#img_rgb = cv2.imread('%s.png' % 0, 0)
#cv2.imwrite('last.png', img_rgb)
#get_minggestone()
for th in range(6):
    t =threading.Thread(target=oneRound,args=(th,th%2))
    t.start()
    time.sleep(0.5)
    
