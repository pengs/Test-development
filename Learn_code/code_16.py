#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 14:36
# @Author  : dapeng！！
# @FileName: code_16.py

# 计算字母和数字出现的次数
s = 'abcAAA123abcDDD456aa'
d = {}
for i in s:
	if i not in d:# 判断字符串的值是否存在字典中
		d[i]=1 # 不存在就生成一个值 {'a':1}
	else:
		d[i]+=1 # 循环判断，累积计算字母出现的次数
print(d) # 打印输出字典


print("*" * 30)
'''
给定一个字符串str=”aAsmr3idd4bgs7Dlsf9eAF”，请统计str 字符串中每个字母的出现 
次数（忽略大小写，a 与A 是同一个字母），并输出成一个字典，例如： {‘a’:3,’b’:1}
'''

s1 = "aAsmr3idd4bgs7Dlsf9eAF"
d1 = {}
for i in s1.lower(): # lower() 方法转换字符串中所有大写字符为小写。
    if i not in d1: # 判断字符串的值是否存在字典中
        d1[i] = 1 # 不存在就生成一个值 {'a':1}
    else:
        d1[i] += 1 # 循环判断，累积计算字母出现的次数
print(d1)


print("*" * 30)
# 网上其他人写的方法
s2 = "aAsmr3idd4bgs7Dlsf9eAF"
s2 = s2.lower() # 将大写字母转换成小写字母
s2_list=list(s2) # 将字符串转换成一个列表；不清楚为什么这么做的意义在哪里?看代码后面参数也没用到
char_dict = {}
for i in s2:
	if i in char_dict:
		count=char_dict[i]
	else:
		count=0
	count=count+1
	char_dict[i]=count
print(char_dict)
