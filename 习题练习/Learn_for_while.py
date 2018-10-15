#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 21:39
# @Author  : dapengchiji！！
# @FileName: Learn_for_while.py

'''
for循环输出打印倒三角形
'''
# 打印上半部分
rows =int(input("请输入打印的行数:"))
for i in range(1,rows):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
# 打印下半部分
for i in range(0, rows):
    for k in range(0, rows-i):
        print ("*",end=" ")
    print ("\n")


'''
While循环输出打印倒三角形
'''
print("^"*30)
# while 打印三角形 #打印上半部分
#rows =int(input("请输入打印的行数:"))
count = 1
while count <= rows:
    count1 = 1
    while count1 <= count:
        print("*",end=" ")
        count1 += 1
    print("\n")
    count += 1
# 打印下半部分
counts = 1
while counts <= rows:
    count2=1
    while count2 <= (rows-counts):
        print("*", end=" ")
        count2 += 1
    print("\n")
    counts += 1


print("^"*30)
# 打印实心正方形

for  i in range(5):
    for j in range(4):
        print("*",end=" ")
    print("*")


