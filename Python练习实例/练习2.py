#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
'''
#n, m = list(map(int, input().split(' ')))
#li = []
#  
#def f(n, m, l, k):
#	if m == 0:
#		print(' '.join(l))
#	for i in range(k, n+1):
#		if i > m:
#			break
#		l.append(str(i))
#		f(n, m-i, l, i+1)
#		l.pop()
#		  
#f(5, 5, li, 1)

'''
提示用户进行输入数据
获取用户的数据数据（需要获取2个）
对获取的两个数字进行加减法运行，并输出相应的结果
'''
def add(num1,num2):
	return num1+num2

def minus(num1,num2):
	return num1-num2
	
operate = input('''请选择想要计算的程序：
1 是 +
2 是 -
请选择你输入的操作(1/2):
''')	
while 1:
	if  operate not in '12':
		print("你输入的选项不存在，请重新输入")
		break
	else:
		num1=int(input("请输入第一个数字:"))
		num2=int(input("请输入第二个数字:"))
		if operate =='1':
			print('输入的数字相加的结果为:{}'.format(add(num1, num2)))
			break
		elif operate =='2':
			print('输入的数字相减的结果为:{}'.format(minus(num1,num2)))
			break
	

'''
编写程序，从键盘获取一个人的信息，然后按照下面格式显示

	==================================
	姓名: dongGe    
	QQ:xxxxxxx
	手机号:131xxxxxx
	公司地址:北京市xxxx
	==================================
'''

username = input("请输入你的姓名:")
num_QQ = input("请输入你的QQ号码:")
phone = input("请输入你的手机号码:")
address = input("请输入公司地址:")

if isinstance(num_QQ,int):
	if int(phone)>11 or int(phone)<11:
		print("手机号码不符合规范:")
		
	
print('姓名:{};QQ:{};手机号:{};公司地址:{}'.format(username, num_QQ,phone,address))





s = [-1,1,-2,2,3,-3]
s1 = [1,2,3,4,5,6,7]
result = []
result1 = []

#求交集
for i in s:
	if i in s1:
		result.append(i)
print('交集为:{}'.format(result))

#求差集
for i in s:
	if i not in s1:
		result1.append(i)
for i in s1:
	if i not in s:
		result1.append(i)
			
print('差集为:{}'.format(result1) )



#差集2实现方法
result1 = []
result2 = []

for i in s:
	if i in s1:
		result1.append(i)

s = list(set(s+s1))
for i in s:
	if i not in result1:
		result2.append(i)
print('差集为:{}'.format(result2) )
		



