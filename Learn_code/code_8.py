#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 21:47
# @Author  : dapengchiji！！
# @FileName: code8.py

'''
函数传入的参数为不可变的，对外部的变量就没有影响 如 数字、字典
按值传--传入的不是变量对应的内存地址
函数传入的参数为可变的，对外部的变量就有影响
按引用传--传入的变量对应的内存地址
'''
a=111
def f():
     global a
     a = 11
     b = a+1
     print(b)
print (f())

# args可变参数
def f(a,b,*args):
    for i in args:
        print(i)
print(f(1,2,3,4,5,6))

'''
写一个函数，使用可变参数，计算函数所有参数之和
'''
#计算函数传入参数之和  *args 表示吧可变的多个非命名参数，转换成一个元祖
def f(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(f(1,2,3,4,10))

#**kw  表示把可变的多个命名参数，转换为一个字典
def dict(a,b,**kw):
    for k,v in kw.items():
        print (k,v)
print(dict(1,2,m=1,n=1,w=1))
'''
使用**kw，把可变的所有参数 算一个乘积
同时使用*arg 和**kw，算一下字母的长度之和，注意所有参数均使用字符串
字符串都是字母
'''

def fun(**kw):
    global mult
    for k,w in kw.items():
        mult=w*w
        return None

print(fun(a=1,b=2,c=3))





