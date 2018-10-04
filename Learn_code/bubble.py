#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 16:31
# @Author  : dapengchiji！！
# @FileName: bubble.py

'''
1、面试手写冒泡排序，记录一下自己写的
'''
#
lists = [1,30,2,89,10,27,3]
for i in range(len(lists)):
    for j in range(i):
        if lists[j] > lists[i]:
            lists[i],lists[j] = lists[j],lists[i]
print(lists)

#
#
# '''
# 2、编写一个字符串的算法，判断字符串是否包含另一个字符串
# '''
def strcontains(l,s):
    for i in l:
        if i in s:
             return True
    return False
if __name__=='__main__':
    l='nihaobeijing'
    s='2ni22'
    print(strcontains(l,s))


# '''
# 3、文件A,复制的文件B
# '''
# #自己写得比较low
with open("/Users/macbook/Desktop/A.txt","r") as f:
     fr = f.read()
with open("/Users/macbook/Desktop/B.txt","w") as f:
     for i in fr:
         f.write(i)
     print("写入复制完成")



'''
4、构造一个1，2，3，5，7...99的列表
'''
lists=[]
for i in range(100):
    if i%2!=0:
        lists.append(i)
print(lists)

#
#
lists1=[]
n=1
while n<=99:
    lists1.append(n)
    n+=2
print(lists1)
