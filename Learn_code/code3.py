#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 21:56
# @Author  : dapengchiji！！
# @FileName: code3.py

'''
if 判断练习
'''

# month=9
# birth_month=int(input("您输入生日月只能是1~12的数字:"))
# if 1<=birth_month<=12:
#     print(" ")
#     if birth_month == month:
#         print("输入的生日月:%d月,恭喜是你的生日月"%birth_month)
#     elif birth_month < month:
#         print("输入的生日月:%d月,小于你的生日月"%birth_month)
#     else:
#         print("输入的生日月:%d月,大于你的生日月"%birth_month)
# else:
#       print("输入的生日月:%d月\n输入错误，请重新输入......"%birth_month)


'''
输入3种字体 e,a,r
如果等于e，退出循环
输入a,执行continue
如果输入r，那么在读取一次字母，并打印
用死循环实现
'''
# n=3
# while 1:
#     str = input("三种字体:")
#     if str=="e":
#         break
#     elif str=="a":
#         continue
#     elif str=="r":
#          str = input("三种字体")
#          print(r)
#     n-=1


'''
1. 编程实现对一个元素全为数字的列表，求最大值、最小值

分析问题解决方案:
求最大值使用python的max()函数
求最小值使用python的mix()函数

'''
#作业1
list=[1,2,3,8,1,100]
print(max(list))
print(min(list))
print("=="*20)



'''
2.编写程序，完成以下要求：
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

分析问题解决方案：
统计计数，可以使用python的count()函数
'''
#作业2

# list=[1,2,3,4,11,2,3,4,"222"]
# for i in list:
#   print("11出现的次数:",i.count(list[]))

# print("=="*20)
# str="hello world"
# print("h出现的次数:",str.count("h"))
# print("e出现的次数:",str.count("e"))
# print("l出现的次数:",str.count("l"))
# print("o出现的次数:",str.count("o"))
# print("r出现的次数:",str.count("r"))
# print("d出现的次数:",str.count("d"))


''' 统计字符串中每个字符的个数
这里使用了python的内置函数，刚开始将ll写为列表，会报错TypeError: list indices must be integers or slices, not str
翻译一下，列表索引必须是整数或切片，而不是字符.  i是输入的字符串的每个字符，所以报错。改为字典的{}就OK了'''

# ss = input("请输入一串字符:")
# ll = {}
# '''错误示例：ll=[]'''
#
# for i in ss:
#     print(i)
#     ll[i] = ss.count(i)
#     '''ll[i]中i为字符，ll若为列表不允许，ll为字典表示该位置的值'''
# print(ll)



'''
3.编写程序，完成以下要求：
完成一个路径的组装
先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share

分析问题解决方式:通过字符串的相加可以实现
'''
#定义一个字符串
#
# for i in range(3):
#     filepath = input("请输入路径:")
#     if i==3:
#         break
#     print(filepath)

#
# filepath1='/Desktop'
# filepath2='/excel'




'''
4.编写程序，完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''



'''
5.在不用其他变量的情况下，交换a、b变量的值
'''
a=1
b=2
a,b=b,a
print(a)
print(b)