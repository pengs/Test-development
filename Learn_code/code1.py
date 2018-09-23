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
# a=list(range(10))
# b=(1,2,3,4)
# c={'m':49,'n':50}
# d = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#
# print("这是一个列表，值是可以进行操作修改:",a)
# print(type(a))
# print("这是一个元祖，数据不可修改:",b)
# print(type(b))
# print("这是一个字典，字典的值是可以操作修改:",c)
# print(type(c))
# # 集合（set）是一个无序不重复元素的序列。
# print("这是一个集合:",d)
# print(set(d))

# 只输出10-5
for i in range(10,-1,-1):
    if i <5:
        break
    print(i)

for i in range(10,-1,-1):
    if i>=5:
        print(i)

#只输出5
for i in range(10,-1,-1):
    if i>5 or i<5:
        continue
    else:
        print(i)

for i in range(10,-1,-1):
    if i==5:
     print(i)
     break

#打印8次停止
# for i in range(10):
#     if i==8:
#         break
#     else:
#         print("no break!!!")

#continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
#for。。。else循环
# for i in range(10):
#     continue
# else:
#     print("no break")
#
#打印偶数  打印0-10之间的奇数，可以用continue语句跳过某些循环：
# for i in range(10):
#     if i %2==0:
#         continue
#     print(i)



# n=5
# while n>=1:
# 	print(n)# 	n-=1
#

# n=5
# while n>=1:
#     if n>2:
#      print(n)
#     else:
#       break
#     n-=1



'''
把一个字符串"abcdefgh",插入到一个list每一个字母站一个list中的一个元素位置
'''
str = 'abcdefgh'
#最便捷
print(list(str))

#2
list1=[]
for i in str:
   list1.append(i)
print(list1)


#3钟
str1=""
for i in str:
    str1=str1+i+" "
print(str1.strip( ))
print(str1.split(" "))


