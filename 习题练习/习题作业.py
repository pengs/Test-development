#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.设定一个用户名和密码，输入正确提示登录成功，否则失败，但是失败次数最多3次，否则退出程序（可以使用for或者while 循环）

2.自己实现一个函数，在一句话中查找某个单词的算法，存在返回索引号，否则返回False
'''

# 1.次数
import sys
username = 'dapeng'
password = 'test123'

#for 循环
for i in range(3):
	if username == input("输入你的用户名:") and  password == input("输入你的密码:"):
		print("Login Successful!")
		break
	else:
		print("用户名或者密码错误")
	i +=1  # 循环次数累加
print ("错误次数超过限制，程序退出")		
#	if i ==2:
#		print ("错误次数超过限制，程序退出")

			
# while 循环
count = 0 
while count < 3:
	if username == input("输入你的用户名:") and  password == input("输入你的密码:"):
			print("Login Successful!")
			break
	else:
		print("用户名或者密码错误")
	count += 1	
print ("错误次数超过限制，程序退出")		
				
	
	
	


		
			
			 
