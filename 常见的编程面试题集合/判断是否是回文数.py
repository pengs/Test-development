#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午5:24
# @Author  : dapengchiji！！
# @FileName: 判断是否是回文数.py

def is_palindrome(n):
    return str(n)==str(n)[::-1]  #str()将整数转化成字符串
output=filter(is_palindrome, range(1,1001))#利用filter()函数筛选出1~1000中的回数
print(list(output))