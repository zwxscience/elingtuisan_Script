# elingtuisan_Script
恶灵退散手游自动的脚本，手动太遭累，所以写了个脚本，解放双手！

#更新神魂自动刷新功能

#更新自动刷封印功能

#更新自动挑战以及挑逗封印娘的功能

# 配置条件
# 使用的Python库及对应版本：
# python 3.6
# opencv-python 3.3.0
# numpy 1.13.3
# 用到了opencv库中的模板匹配和边缘检测功能

# 需要手机连接电脑
# 需要电脑安装adb 程序
# 具体安装方式请参考python 安装及配件安装.docx

#默认经验合并到背包格子的第一位（所以最好先放个橙色或者紫色的碎片，当然不放也可以）
## 因为我的手机是小米Note2，所以以下是1920×1080 分辨率的手机坐标，其他手机分辨率请自行适配
### 猎魂相关坐标
#455,970 祈福十次
#519 1242 确定
#519 1625 背包
#129 507 第一个碎片
#一下8次循环
#523 1324 一键添加
#534 1327 强化

#1002 564 关掉小窗口
#519 1625 猎魂 
#祈福十次 循环进行

### 封印相关坐标
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


### 自动挑战以及挑逗封印娘的功能
#995,1784 神社按钮
#544 512 头部
#558 720 胸部
#566 1027 腰部
#517 1472 腿部
#499 1844 降妖
#977 289 挑战首领


# 方法步骤
# 打开手机恶灵退散手游，连接数据线，usb 调试模式
# 下载本脚本后运行 
## 自动刷神魂
`python eling_shenhun.py`
## 自动封印（目前小米Note2 测试 命令执行响应没有达到理想的状态，所以只能当个辅助）
`python eling_fengyin.py`
## 自动挑战以及挑逗封印娘的功能
`python eling_normal.py`
# 等待其自动刷即可
![image](https://github.com/zwxscience/elingtuisan_shenhunSCript/blob/master/example.png)
