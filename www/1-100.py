#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 22:09
# @Author  : dapengchiji！！
# @FileName: 1-100.py
'''
1.计算1~100的累积和（包含1和100）
2.计算1~100之间偶数的累积和（包含1和100）
'''

#第1题使用while循环
i=1
sum=0
while i<=100:
    sum += i
    i+=1
print("1~100的累积和为:%d" % sum)

#第2题使用while循环

i=1
sum=0
while i<=100:
    if(i%2==0):
     sum += i
    i+=1
print("1~100的累积和为:%d" % sum)



#第1题使用for循环
sum =0
for i in range(1,101):
    sum+=i
print("1~100的累积和为:%d" % sum)

#第2题使用for循环
sum =0
for i in range(1,101):
    if(i%2==0):
     sum+=i
print("1~100的累积和为:%d" % sum)