#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/05 16:30
# @Author  : dapengchiji！！
# @FileName: code14.py

'''
1.生成所有的小写字母
2.生成所有的大写字母
3.所有的大小写字母
4.所有的大小写字母和数字
'''
#生成所有的小写字母
for i in range(97,123):
	print(chr(i))
	
print('*'*30)
#生成所有的大写字母
for i in range(65,91):
	print(chr(i))
	
print('*'*30)	
#所有的数字
for i in range(48,58):
	print(chr(i))

print('*'*30)
import string
#所有数字
print(string.digits)
#大小写字母
print(string.ascii_letters) 
#所有的大小写字母和数字
print(string.digits+string.ascii_letters)


print('*'*30)
#生成字符串 a1b2c3d4...j10
result = ""
first_ascii_code = 97  # 定义一个初始值
for  i  in  range(1,11):
	result+=chr(first_ascii_code+i-1)+str(i)
print(result)

print('*'*30)
#生成a1B2d3...J10
result = ''
first_ascii_code = 97 # 定义一个初始值
for i in range(1,11): 
    if i %2==0:
       result+= chr(first_ascii_code+i-32-1)+str(i)
    else:
        result+= chr(first_ascii_code+i-1) + str(i)
print(result)


