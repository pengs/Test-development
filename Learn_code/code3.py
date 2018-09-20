#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 21:56
# @Author  : dapengchiji！！
# @FileName: code3.py

'''
if 判断练习
'''

month=9
birth_month=int(input("您输入生日月只能是1~12的数字:"))
if 1<=birth_month<=12:
    print(" ")
    if birth_month == month:
        print("输入的生日月:%d月,恭喜是你的生日月"%birth_month)
    elif birth_month < month:
        print("输入的生日月:%d月,小于你的生日月"%birth_month)
    else:
        print("输入的生日月:%d月,大于你的生日月"%birth_month)
else:
      print("输入的生日月:%d月\n输入错误，请重新输入......"%birth_month)






