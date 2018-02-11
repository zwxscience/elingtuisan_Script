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
#1066 798 功能选择

#239 515 猎魂
#882 1057 封印
#455,970 祈福十次
#519 1242 确定
#519 1625 背包
#129 507 第一个碎片
#一下8次循环
#523 1324 一键添加
#534 1327 强化

#1002 564 关掉小窗口
#519 1625 裂魂 
# 祈福十次 循环

#更新紫色碎片合并
#170 1080 选择碎片
#947 402 默认第一个紫色碎片
#540 1653 确定
#534 1327 强化

def prepare_game():
    cmd = ('adb shell input tap %i %i' % (1066, 798)) #1066 798 功能选择
    os.system(cmd)
    print(cmd)
    time.sleep(3)
    cmd = ('adb shell input tap %i %i' % (239, 515)) #239 515 猎魂
    os.system(cmd)
    print(cmd)
    time.sleep(3)
    
def lvye_shenshe():
    for i in range(20):
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (455, 970, 456, 971) #455,970 祈福20次
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(1.0, 2))
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (519, 1242, 521, 1243) #确定
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.2, 0.3))
def beibao():
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (519, 1625, 521, 1626) #519 1625 背包
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(3, 3.5)) #手机显示背包效率有点低
    
def suipian_combin():
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (129, 507, 131, 508) #129 507 第一个碎片
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.2))
    for i in range(7):
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (523, 1324, 524, 1325) #523 1324 一键添加
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.2, 0.3))
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (534, 1327, 535, 1328) #534 1327 强化
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.5, 0.6))
    combinedZiorCheng()
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (1002, 564, 1003, 565) #1002 564 关掉小窗口
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(0.5, 0.6))   
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (519, 1625, 519, 1626) #519 1625 裂魂
    os.system(cmd)
    print(cmd)
    time.sleep(2)      


#更新紫色碎片合并

def combinedZiorCheng():
    cmd = ('adb shell input tap %i %i' % (170, 1080)) #170 1080 选择碎片
    os.system(cmd)
    print(cmd)
    time.sleep(1)
    cmd = ('adb shell input tap %i %i' % (947, 402)) #947 402 默认第一个紫色碎片
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (540, 1653)) #540 1653 确定
    os.system(cmd)
    print(cmd)
    time.sleep(0.1)
    cmd = ('adb shell input tap %i %i' % (534, 1327)) #534 1327 强化 
    os.system(cmd)
    print(cmd)
    time.sleep(0.1)

# 循环直到游戏失败结束
prepare_game()
for i in range(100000):
    #get_screenshot(0)
    #img_rgb = cv2.imread('%s.png' % 0, 0)
    #cv2.imwrite('last.png', img_rgb)
    lvye_shenshe()
    beibao()
    suipian_combin()
    print('times %i' % (i))
