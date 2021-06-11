#coding:gbk
"""
目标：RPSLS游戏（石头剪刀布蜥蜴史波克）
作者：马晶晶
日期：2021年6月5日
"""

import random
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0;
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    else:
        return 4

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "布"
    elif number==3:
        return "蜥蜴"
    else:
        return "剪刀"
    pass 

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    print("你的选择是：",player_choice)
    a=name_to_number(player_choice)
    b=random.randint(0,4)
    s1=number_to_name(b)
    print("机器的选择是：",s1)
    comp(a,b)
    
def comp(a,b):
    if a==b:
        print("您和计算机出的一样呢")
    if a==0 and (b==3 or b==4):
        print("恭喜你赢了！")
    if a==0 and (b==1 or b==2):
        print("不好意思机器赢了~")
    if a==1 and (b==0 or b==4):
        print("恭喜你赢了！")   
    if a==1 and (b==2 or b==3):
        print("不好意思机器赢了~")
    if a==2 and (b==0 or b==1):
        print("恭喜你赢了！")   
    if a==2 and (b==3 or b==4):
        print("不好意思机器赢了~")
    if a==3 and (b==1 or b==2):
        print("恭喜你赢了！")   
    if a==3 and (b==0 or b==4):
        print("不好意思机器赢了~")
    if a==4 and (b==2 or b==3):
        print("恭喜你赢了！")   
    if a==4 and (b==0 or b==1):
        print("不好意思机器赢了~")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
choice_name=input("请输入你的选择：")
rpsls(choice_name)
input()
