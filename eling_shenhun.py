# -*- coding: UTF-8 -*- 
import os
#import cv2
#import numpy as np
import time
import random
#coding=utf-8

# 使用的Python库及对应版本：
# python 3.6
# opencv-python 3.3.0
# numpy 1.13.3
# 用到了opencv库中的模板匹配和边缘检测功能
import sys   
reload(sys) 
sys.setdefaultencoding('gb18030')

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
    print('上古巨龙已苏醒，人类将面临空前危机，你是拯救人类的唯一人选。去霍斯加高峰吧，孩子，去找灰胡子们学习猎魂之力吧，然后去拯救这个支离破碎的世界吧~'.decode('utf-8').encode('gbk'))
    print('经过一段时间的学习，你已经掌握了许多能力，技能发动：打开万华轮！！！！'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(3)
    print('嘿！呀！猎魂开始！！！！'.decode('utf-8').encode('gbk'))
    cmd = ('adb shell input tap %i %i' % (239, 515)) #239 515 猎魂
    os.system(cmd)
    print(cmd)
    time.sleep(3)
    
def lvye_shenshe():
    count = 7 #祈福7次
    for i in range(count):
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (455, 970, 456, 971) #455,970 
        print('妈咪妈咪哄，看我祈福第%i百次，祈到头皮发昏！'.decode('utf-8').encode('gbk') % (i+1))
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(1.0, 2))
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (519, 1242, 521, 1243) #确定
        print('看看我们的收获！好多能量碎片！哈哈哈哈~'.decode('utf-8').encode('gbk'))
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.2, 0.3))
def beibao():
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (519, 1625, 521, 1626) #519 1625 背包
    print('满了满了！打开背包整理一下~可伶可伶可伶'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(3, 3.5)) #手机显示背包效率有点低
    
def suipian_combin():
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (129, 507, 131, 508) #129 507 第一个碎片
    print('就是你了！我要把所有的碎片能量加注在你的身上！！！！'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(1, 1.2))
    for i in range(20):
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (523, 1324, 524, 1325) #523 1324 一键添加
        print('第 %i 颗七龙珠出现吧！'.decode('utf-8').encode('gbk') % (i+1))
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.2, 0.3))
        cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
            % (534, 1327, 535, 1328) #534 1327 强化
        print('七龙珠玉碎，能量灌输！'.decode('utf-8').encode('gbk'))
        os.system(cmd)
        print(cmd)
        time.sleep(random.uniform(0.5, 0.6))
    print('祈福的过程中，会出现许多特异的珠子，它们往往会逃避召唤，让我们捡取它们吧！'.decode('utf-8').encode('gbk'))
    combinedZiorCheng()
    combinedZiorCheng()
    combinedZiorCheng()
    combinedZiorCheng()
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (1002, 564, 1003, 565) #1002 564 关掉小窗口
    print('能量灌输完成！啊，这最终的珠子充满了力量，闪瞎了我的眼睛~~~'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(random.uniform(0.5, 0.6))   
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (519, 1625, 519, 1626) #519 1625 裂魂
    print('但是，打败巨龙的能量远远不够，少年继续努力祈福吧！！！！！！！！！！'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(2)      


#更新紫色碎片合并

def combinedZiorCheng():
    cmd = ('adb shell input tap %i %i' % (170, 1080)) #170 1080 选择碎片
    print('寻找背包的角落，看看我们发现了什么~'.decode('utf-8').encode('gbk'))
    os.system(cmd)
    print(cmd)
    time.sleep(1)
    cmd = ('adb shell input tap %i %i' % (947, 402)) #947 402 默认第一个紫色碎片  
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (947, 616)) #第2个紫色碎片 
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (947, 822)) #第3个紫色碎片 
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (947, 1021)) #第4个紫色碎片  
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (947, 1227)) #第5个紫色碎片 
    os.system(cmd)
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (947, 1423)) #第6个紫色碎片 
    os.system(cmd)
    print('嗯，这个角落已经收集完毕！'.decode('utf-8').encode('gbk'))
    print(cmd)
    cmd = ('adb shell input tap %i %i' % (540, 1653)) #540 1653 确定
    os.system(cmd)
    print(cmd)
    time.sleep(0.1)
    cmd = ('adb shell input tap %i %i' % (534, 1327)) #534 1327 强化 
    os.system(cmd)
    print('把这些特异的珠子粉碎吧，它们具有更大的能量！'.decode('utf-8').encode('gbk'))
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
    print('新的故事开始了 %i'.decode('utf-8').encode('gbk') % (i+1))
