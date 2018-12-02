#!/usr/bin/python3
# -*- coding: utf-8 -*-
s = [-1,1,-2,2,3,-3]
s1 = [1,2,3,4,5,6,7]
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

# 求一个字符串中的字母的个数函数

'''
问题解决步骤：
1.定义一个函数  
2.遍历字符串的每个值，判断是否是字母；（包括大写和小写，可以通过ord()函数来判断）
3.声明一个变量，接收字符串字母的个数
'''
#判断传入参数的类型 

def str_num(s):
	if not isinstance(s,str):
		return None
	result =0
	for i in s:
		if (65<=ord(i)<=90) or (97<=ord(i)<=122):  # ord() 返回对应的ASCII数值  65-90是大写字母 97-122是小写字母
			result +=1
	return result			
print('字符串包含字母的个数为:{}个'.format(str_num('hello world lalala 001')))







				
