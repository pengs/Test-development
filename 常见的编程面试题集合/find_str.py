#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 23:15
# @Author  : dapengchiji！！
# @FileName: find_str.py

'''
从一个字符串查找统计字符串的个数以及数字的个数
'''

def count_s_a(s): # 定义一个统计函数
    count_s = count_z = 0  # 声明变量
    for i in s: #循环字符串
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):  # ord(c) 将字符串转换为ASCII码
            count_s+=1 # 自增
        elif i in "1234567890":  # 判断字符串 是否有数字
        # elif (ord(i) >= 48 and ord(i) <= 57):
            count_z +=1  # 自增
    print("数字个数：%d个" % count_z)
    print("字母个数：%d个" % count_s)

if __name__ == "__main__":
    s = 'You very 666 beautiful I like very you 666! I am 20 years old!'
    count_s_a(s)
