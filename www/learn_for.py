#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 21:39
# @Author  : dapengchiji！！
# @FileName: learn_for.py

'''
根据输出打印倒三角形
'''
#打印上半部分
rows =int(input("请输入打印的行数:"))

for i in range(1,rows):
    j=0
    for j in range(0,i-j):
        print(" * ",end="")
    print("\n")
#打印下半部分
for i in range(0, rows):
    for k in range(0, rows-i):
        print (" * ",end="")
        k += 1
    i += 1
    print ("\n ")

