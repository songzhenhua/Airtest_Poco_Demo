# -*- encoding=utf8 -*-
__author__ = "szh"
"""
com.netease.poco.u3d.tutorial.apk demo
"""

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

poco("btn_start").click()  # 点击start按钮
poco("basic").click()  # 点击basic按钮
poco("star_single").long_click(duration=3)  # 长按五角星
poco("pos_input").set_text('测试输入文字')  # 输入文字
sleep(3)
poco("btn_back").click()  # 点击back按钮 
sleep(1.0)

poco("drag_and_drop").click()  # 点击drag drop按钮
shell = poco("shell").focus('center')  # 定义贝壳对象
for star in poco("star"):
    star.drag_to(shell)  # 循环将五角星拖到贝壳
poco("btn_back").click()  # 点击back按钮 

poco("list_view").click()  # 点击list view按钮 
poco("Scroll View").swipe([0, -1])  # 将列表向上滑动
sleep(2.0)
poco("Text (12)").click()  # 选中列表最后一项
poco("btn_back").click()  # 点击back按钮 

poco("wait_ui").click()  # 点击Wait UI按钮 
count = 0
while True:    
    yellow_fish = poco("yellow")  # 定义黄鱼
    blue_fish = poco("blue")  # 定义蓝鱼
    fish = poco.wait_for_any([yellow_fish, blue_fish])  # 等待鱼出现
    fish.click()
    sleep(1.0)
