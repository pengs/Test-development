#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 17:07
# @Author  : dapeng！！
# @FileName: test.py

# rows = int(input("please input number:"))
#
# for i in range(rows):
#     for space in range(0, rows - i):
#         print(end=' ')
#     for star in range(rows - i, rows):
#         print("*", end=' ')
#     print('')


try:
    for i in range(1,5):
        for j in range(1,5):
            if i==3 and j ==3:
                raise
            print(i)
except:
    pass