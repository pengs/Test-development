#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/1 18:42
# @Author  : dapeng！！
# @FileName: randoms.py
''''''
import random


#random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
for i in range(3):
    print(random.random())


print("*"*20+"\n")
'''random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
# 如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。'''
print(random.uniform(10,20))
print(random.uniform(20,10))



print("*"*20+"\n")
'''random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b'''
print(random.randint(10,20)) # 生成的随机数n: 10 <= n <= 20
print(random.randint(20,20)) # 永远是20
# print(random.randint(20,10)) # 会报错，下限必须小于上限



print("*"*20+"\n")
'''
random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
'''
print(random.randrange(10,100,2)) # 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。


print("*"*20+"\n")
'''
random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
'''
print(random.choice("学习Python"))
print(random.choice(["JGood", "is", "a", "handsome", "boy"]))
print(random.choice(("Tuple", "List", "Dict")))


print("*"*20+"\n")
'''
random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。
'''
p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
print (p)


print("*"*20+"\n")
'''
random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  # 从list中随机获取5个元素，作为一个片断返回
print (slice)
print (list)  # 原有序列并没有改变。

