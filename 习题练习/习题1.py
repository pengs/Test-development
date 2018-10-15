#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
1.随机生成一个整数，1-100之间，你最多猜5次，如果大了，就提示，小了，提示小
猜对了就提示猜中了
5次都没有，就猜没猜中
'''
import random
number = random.randint(1,100)
for i in range(7):
	user_number = int(input("输入的数字:"))
	if number == user_number:
		print("你猜中了，数字是:",user_number)
		print("你猜了 %s 次"%i)
		break
	elif number > user_number:
		print("你输入的太小了")
	else:
		print("你输入的太大了")
	i+=1
print("次数已用完")	


'''
使用while,计算随机之和，超过100的时候，停止程序
'''
