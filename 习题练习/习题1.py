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
随机数在1~20之间产生，要求记录一下产生的随机数以及最后的和，以及随机数的个数
'''
import random

result_sum = 0
random_num_list = [] 

while True: # 条件为真，一直执行
	random_num = random.randint(1,20) # 生产 1~20之间的整数
	random_num_list.append(random_num) # 生产随机数的列表
	result_sum += random_num  # 数据累加
	if result_sum > 100:  # 判断对应条件
		break
		
print("随机数的和为:",result_sum)		
print("生产的随机数一共为:%s个"%len(random_num_list))
print("随机数的列表为",random_num_list)


		
	
'''1+2+3+4+...+100之间偶数和'''
result_sum = 0
for i in range(1,101):
	if i % 2 == 0:
		result_sum += i	
print("1~100之间偶数的和为:",result_sum)

print("*" * 30)
'''
遍历一个字符串（基于字符遍历和基于位置遍历）
遍历一个列表 
'''
# 基于字符的遍历

for i in 'hello world':	
	print(i)

print("*" * 30)
# 基于位置遍历
str_s = 'hello world'
for i in range(len(str_s)):
	print(str_s[i])	

	
print("*" * 30)
# 遍历一个列表
list_num = [1,2,4,90]
for i in list_num:
	print(i)
	
print("*" * 30)
'''
遍历一个列表中嵌套列表和元祖的所有元素，将1~12的数字进行输出
'''
ls = [[[1,2,3],4,5],7,8,(9,10,(11,12))]
for i in ls:
	if isinstance(i,(list,tuple)):  # isinstance() 函数来判断一个对象是否是一个已知的类型
		for j in i:
			if isinstance(j,(list,tuple)):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)					
