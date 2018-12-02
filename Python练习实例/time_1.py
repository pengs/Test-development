#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 写一个函数，函数要计算浮点数乘法的一万次相乘后的时间耗时，浮点数可以使用随机小数


#def add_end(L=[]):
#	L.append('END')
#	return L
#
#print(add_end([1,2,3])) # 调用正常
#print(add_end(['x','y']))
#print(add_end())
#print(add_end())
#print(add_end())
#	
#
#
#def add_end(L=None):
#	if L is None:
#		L = []
#	L.append('END')
#	return L
#
#print(add_end([1,2,3])) # 调用正常
#print(add_end(['x','y']))
#print(add_end())
#print(add_end())
#print(add_end())

# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
# str = "***Line1-abcdef \nLine2-abc \nLine4-abcd***";
# print (str.split())
# print (str.split(' ',1))
#
# # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# print(str.strip(" * "))


# 练习 求和函数
'''
要求有个值是 result 来存结果
如果是数字，相加
如果是字符串，当做字符串相加
如果是list ,就list相加
'''
def add(a,b):
	if isinstance(a,str) and isinstance (b,str):
		result =""
	elif isinstance(a,(int,float)) and isinstance(b,(int,float)):	
		result = 0
	elif isinstance(a,(list)) and isinstance(b,(list)):
		result = []
	else:
		return None	
	return 	a+b
	return result  # This code is unreachable

	
print(add("3","a"))
print(add(1,4))	
print(add([1,2],[2,3]))

