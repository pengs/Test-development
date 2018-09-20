#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 22:46
# @Author  : dapengchiji！！
# @FileName: code1.py

'''python 数据结构

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组

Unicode
Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。

在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。

由于 Python3.X 源码文件默认使用utf-8编码，

str对象和bytes对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。

# '''
#
#列表
a=list(range(10))
b=(1,2,3,4)
c={'m':49,'n':50}
d = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print("这是一个列表，值是可以进行操作修改:",a)
print(type(a))
print("这是一个元祖，数据不可修改:",b)
print(type(b))
print("这是一个字典，字典的值是可以操作修改:",c)
print(type(c))
# 集合（set）是一个无序不重复元素的序列。
print("这是一个集合:",d)
print(set(d))


