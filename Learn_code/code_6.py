#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 18:48
# @Author  : dapengchiji！！
# @FileName: file_code6.py

'''
1.os.path.join() 将分离的部分合成一个整体
2.os.path.splitext()将文件名和扩展名分开
3.os.path.split（）返回文件的路径和文件名

'''

import  os
#os.path.join() 将分离的部分合成一个整体
filename=os.path.join('/Users/macbook/awesome','Learn_code')
print (filename)
#
#
#os.path.splitext()将文件名和扩展名分开
fname,fename=os.path.splitext('/Users/macbook/awesome/Learn_code/*.py')
print('fname is:',fname)
print('fname is:',fename)


#os.path.split（）返回文件的路径和文件名
dirname,filename=os.path.split('/home/ubuntu/python_coding/split_func/split_function.py')
print (dirname,filename)

可以封装成函数，方便 Python 的程序调用




'''
除法函数，需要处理除数不能为0
'''
def div(a,b):
    if not isinstance(a,(int,float,complex)):
        return None
    if not isinstance(b,(int,float,complex)):
        return None
    if b==0:
        print("除数不能为0")
        return None
    return a/b

print(div(10,6))


'''
1.写一个函数，统计一下这一句话中的数字个数
You very beautiful I like very you 666! I am 20 years old!
2.统计一下字母的个数
3.统计一下字母和数字个数
4.统计一下非字母和非数字的个数
'''
s='You very 666 beautiful I like very you 666! I am 20 years old!'
def count_digit(s):
    if not isinstance(s,str):
        print("这不是一个unicode字符串")
        return 0
    result=0
    for i in s:
        # if i in "0123456789":
        if ord(i)>=48 and ord(i)<=57:
            result+=1
    return result
print("字符串中的出现数字的个数为:%d个"%count_digit(s))


#2统计一下字母的个数
def count_letters(s):
    # if not isinstance(s,str):
    #     print("这不是一个unicode字符串")
    #     return 0
    result=0
    for i in s:
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):# 大写字母''小写字母
           result += 1
    return result
print("字符串中的字母的个数为:%d个"%count_letters(s))


#3统计一下字母和数字个数
print("数字和字符串一共:%d个"%(count_digit(s)+count_letters(s)))

#4统计一下非字母和非数字的个数

def count_sum(s):
    count=len(s)
    return count-(count_digit(s)+count_letters(s))
print(count_sum(s))




'''
ord() 函数
返回对应的 ASCII 数值，或者 Unicode 数值
'''
s='i like you 666'

#统计数字个数
count_number=0
for i in s:
    if i in '0123456789':
        count_number+=1
print(count_number)

#统计字母个数
count_str=0
for i in s:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        count_str+=1
print(count_str)

#统计非字母和非数字个数
print(len(s)-(count_number+count_str))


