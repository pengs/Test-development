#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
输入多个数字，当输入偶数的时候求和，输入奇数不求和，输入.的时候结束求和 打印求和结果
不知道循环次数，则使用while循环
'''

result=0
while 1:
	input_data = input("请输入数字:")
	if input_data=='.':		
		break
	else:
		if int(input_data) % 2 == 0:			
			result+=int(input_data)		
print(result)		
		

'''嵌套循环，输出10-50个位带有1-5的所有数字
如 11，12，13，14，15
'''
# 取余数
for i in range(10,50):
	if 0 < i%10 <=5:	
		print(i)

# for 循环嵌套
for i in '1234':
	for j in '12345':
		print(int(i+j))
		
# 将数字转换为字符串，取个位的字符判断是否在1-5之间		
for i in range(10,51):
	if str(i)[1] in '12345':
		print(i)

