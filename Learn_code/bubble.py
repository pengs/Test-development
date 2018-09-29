#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 16:31
# @Author  : dapengchiji！！
# @FileName: bubble.py

'''
1、面试手写冒泡排序，记录一下自己写的
'''

lists = [1,30,2,89,10,27,3]
for i in range(len(lists)):
    for j in range(i):
        if lists[j] > lists[i]:
            lists[i],lists[j] = lists[j],lists[i]
print(lists)



'''
2、编写一个字符串的算法，判断字符串是不包含另一个字符串
'''
a='abcdef'
b='ef'

for i in a:
  if i in b:
    print("a包含b")
else:
    print("b不在a里面")




'''
3、文件A,复制的文件B
'''
#自己写得比较low
with open("/Users/macbook/Desktop/A.txt","r") as f:
     fr = f.read()
with open("/Users/macbook/Desktop/B.txt","w") as f:
     for i in fr:
         f.write(i)
     print("写入复制完成")







'''
4、随机数排重
'''
