#!/usr/bin/python3
# -*- coding: utf-8 -*-

num1 = input("请输入第一个数字:")
num2 = input("请输入第二个数字:")

print('两数之和为:{}'.format(int(num1)+int(num2)))

num3 = input("请输入数字:")


if int(num3) %2 ==0:
	print("您输入的:%d是偶数"%int(num3))
else:
	print("您输入的:%d是奇数"%int(num3))


'''
请输入3个数字，数字之间用空格隔开，输入3个数字回车后，打印出“您输入的最大数字为：三个数字中的数字
'''

str_num = input('请输入3个数字，数字之间用空格隔开:')
num1,num2,num3 = [int(i) for i in str_num.split()] # 列表生成式

#num1,num2,num3 = [int(i) for i in range(3,6)] # 列表生成式


if int(num1)>int(num2)  and  int(num1) > int(num3):
	print("您输入的最大是数字是:%d"%int(num1))
elif int(num2)>int(num1) and int(num2) > int(num3):
	print("您输入的最大是数字是:%d"%int(num2))
else:
	print("您输入的最大是数字是:%d"%int(num3))


#for
for i in range(1,101):
	if i %3 ==0:
		print("Fizz")
	elif i %5==0:
		print("Buzz")
	print(i)	
	
# while
print("*"*30)
i = 1
while i<=100:
	if i %3 ==0:
		print("Fizz")	
	elif i %5==0:
		print("Buzz")			
	print(i)
	i+=1			
		
				