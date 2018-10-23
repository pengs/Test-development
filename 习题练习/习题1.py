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




print("*" * 30)
'''把列表的数字6打印出来'''
l1 = [[1,2,3,[4,5,6]]]

#通过切片的方式
print(l1[0][3][2])

# 通过循环递归的查找
for i in l1:
	if isinstance(i, (list,tuple)): # isinstance() 函数来判断一个对象是否是一个已知的类型
		print(i)
		for j in i:
			if isinstance(j, (list,tuple)):
				for k in j:
					if k==6:
						print(k)
# 循环递归+切片					
for i in l1:
	if isinstance(i, (list,tuple)): # isinstance() 函数来判断一个对象是否是一个已知的类型
		for j in i[3]:
			if j == 6:
				print(j)



print("*" * 30)						
'''每个元素+1'''
l = [1, 2, 3, 4, 5]
l1 = []

for i in l:
	l1.append(i+1)
print(l1)



'''
1.遍历列表中嵌套的列表和元祖的所有元素
2.打印出10
'''
for  i  in ls:
	if isinstance(i, (list,tuple)):
		for j in i:
			if j == 10:
					print("按照需求打印出数字：",j)	

'''
求100以内的素数
一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数，如2，3，5，7，11，13
打印出来
'''
		
num=[]
i=2
for i in range(2,100):
	j=2
	for j in range(2,i):
		if i % j == 0:
			break
	else:
		num.append(i)
print("100以内的素数列表为:",num)								

in_num= int(input("请输入数字："))
if in_num == 1:
	print(in_num,"不是一个素数")
for i in range(2,in_num):
	if in_num %i == 0:
		print(in_num,"不是一个素数")
		break
	if i == in_num-1:
		print(in_num,"是一个素数")	
