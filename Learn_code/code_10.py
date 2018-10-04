#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 10:01
# @Author  : dapeng！！
# @FileName: code10.py

#两个列表转字典
list1 = ['key1','key2','key3']
list2 = ['1','2','3']
dict(zip(list1,list2))
# {'key1': '1', 'key2': '2', 'key3': '3'}

#嵌套列表转字典
list3 = [['key1','value1'],['key2','value2'],['key3','value3']]
dict(list3)
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 列表、元组转字符串
list2 = ['a', 'a', 'b']
''.join(list2)
# 'aab'

tup1 = ('a', 'a', 'b')
''.join(tup1)
# 'aab'

# 字典转换为字符串
dic1 = {'a':1,'b':2}
str(dic1)
# "{'a': 1, 'b': 2}"

# 字典key和value互转
dic2 = {'a': 1, 'b': 2, 'c': 3}
# {value:key for key, value in a_dict.items()}
# {1: 'a', 2: 'b', 3: 'c’}

# 字符串转列表
s = 'aabbcc'
list(s)
# ['a', 'a', 'b', 'b', 'c', 'c']

# 字符串转元组
tuple(s)
# ('a', 'a', 'b', 'b', 'c', 'c')

# 字符串转集合
set(s)
# {'a', 'b', 'c'}

# 字符串转字典
# dic2 = eval("{'name':'ljq', 'age':24}")

# 切分字符串
a = 'a b c'
a.split(' ')
# ['a', 'b', 'c']
