# -*- encoding=utf8 -*-A
__author__ = "szh"
"""
梦幻西游手游龙宫师门任务自动化脚本
"""

from airtest.core.api import *
import os

mission_location = (2284,445)  # 任务位置：第一格284,445；第二格284,630
while True:
    sleep(3)
    touch(mission_location, times=2)  # 有时送信任务会有对话框，双击可关闭对话框并领任务
    sleep(10)
    if exists(Template(r"tpl1548578645561.png", threshold=0.9, record_pos=(0.355, 0.104), resolution=(2560, 1440))):
        touch(Template(r"use.png", record_pos=(0.355, 0.104), resolution=(2560, 1440)))
        sleep(5.0)
        print("**********************收集灵气")
        continue
    if exists(Template(r"chilun.png", record_pos=(0.457, 0.225), resolution=(2560, 1440))):# 进入战斗有齿轮，检测不到齿轮就是战斗结束
        while True:
            sleep(10)
            if not exists(Template(r"chilun.png", record_pos=(0.457, 0.225), resolution=(2560, 1440))):
                break
        print ('**********************战斗')
        continue
    if exists(Template(r"buy.png", record_pos=(0.259, 0.175), resolution=(2560, 1440))):
        touch(Template(r"tpl1548171560497.png", record_pos=(0.259, 0.175), resolution=(2560, 1440))) # 购买后自动回师门
        sleep(2)
        if exists(Template(r"buy.png", record_pos=(0.259, 0.175), resolution=(2560, 1440))):
            while True:  # 有时准备买的物品会被别人买走，循环尝试购买
                if exists(Template(r"buy.png", record_pos=(0.259, 0.175), resolution=(2560, 1440))):
                    touch((1100,445))  # 点击第一个物品
                    touch(Template(r"tpl1548171560497.png", record_pos=(0.259, 0.175), resolution=(2560, 1440))) # 购买后自动回师门
                else:
                    break
        while True:
            sleep(5.0)
            if exists(Template(r"tpl1548171602691.png", record_pos=(0.32, 0.171), resolution=(2560, 1440))):
                touch(Template(r"tpl1548171602691.png", record_pos=(0.32, 0.171), resolution=(2560, 1440))) # 购买后自动回师门，并上交，上交后有对话
                sleep(2)
                touch(mission_location)  # 点击一下关闭对话
                break
        print ('**********************购买')
        continue
    if exists(Template(r"tpl1548504872233.png", record_pos=(0.34, -0.073), resolution=(2560, 1440))):  # 有的NPC有多种对门，选师门
        touch(Template(r"tpl1548504872233.png", record_pos=(0.34, -0.073), resolution=(2560, 1440)))
        sleep(3)
        touch(mission_location)  # 点击关闭对话
        continue
    if exists(Template(r"tpl1548171602691.png", record_pos=(0.32, 0.171), resolution=(2560, 1440))):  # 有时需要上次的东西正好本身有，不用购买
        touch(Template(r"tpl1548171602691.png", record_pos=(0.32, 0.171), resolution=(2560, 1440))) 
        sleep(3)

    if exists(Template(r"tpl1548172409253.png", threshold=0.9, record_pos=(0.082, 0.053), resolution=(2560, 1440))):  # 出现确定表示20次师门做完
        os.system("D:\\mp3.mp3")  # 放首音乐提醒一下
        break
