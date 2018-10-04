#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 17:52
# @Author  : dapeng！！
# @FileName: code11.py

'''
1、求1+2+3+4+5+......+100
'''
sum=0
for i in range(1,101):
    sum+=i
print("1+2+3+4+5+......+100的和:%d"%sum)

'''
2、交换2个变量的值
'''
a=10
b=2
a,b=b,a
print("交换后的值为:%d,%d"%(a,b))

'''
3、一个足球队寻找年龄在10-12岁的小女孩(包括10岁和12岁)加入，编写一个程序，询问用户的性别（m是男性，f是女性）和年龄，然后显示一条消息
指出这个人是否可以加入球队；询问10次后，输出满足条件的总人数
'''

'''
4、输入1-127的ascii码的并输出对应的字符
解决问题的步骤：输入1-127之间的数字--将数字转换为ASCII码 chr()--打印输出 print
# '''
number=int(input("请输入1-127之间的数字:"))
if number>=1 and number<=127:
    print("输入的数字:%d,转换成ASCII码后的字符:%s"%(number,chr(number)))
else:
    print("你输入的数字不在需求的范围，请重新输入吧")



'''
5、输入a,b,c,d4个整数，计算a+b-c*d的结果
'''

a=int(input("请输入第一个整数: "))
b=int(input("请输入第二个整数: "))
c=int(input("请输入第三个整数: "))
d=int(input("请输入第四个整数: "))

if a>0  and b>0 and c>0 and d>0:
  result=a+b-c*d
  print(result)
else:
    print("输入结果为空")



'''6、计算一周有多少分钟，多少秒钟
解决问题的步骤 一周7天--每天24小时--1小时=60分钟--1分钟==60s
# '''
week=7*24*60 # 一周有多少分钟
weeks=week*60 # 一周有多少秒钟
print("一周有:%d分"%week)
print("一周有:%d秒"%weeks)

'''
7、3个人在餐厅吃饭，想分摊餐费，总共消费了$35.27；他们还想给15%的小费，每个人咋付钱
1.人数3人；2、平均消费（总消费/3）3、
'''
money=35.27*(1+0.15)
person_money=money/3
print("每个人需要支付的钱数为:%d$"%person_money)

'''
8、计算一个12.5*16.7的矩形房间的面积和周长
面积 S=a*b(a,b为长和宽)
周长 L=2*(a+b)
'''
a=12.5
b=16.7
S=a*b
L=2*(a+b)
print("矩形的面积为:%dm"%S)
print("矩形的周长为:%dm"%L)

'''
9、判断一个数n能否同时被3和5整除
'''

n=int(input("输入一个整数:"))
if n % 3 == 0 and n % 5 == 0:
    print("输入的%d，能同时被3和5整除" % n)
else:
    print("输入的%d，无法同时被3和5整除" % n)





