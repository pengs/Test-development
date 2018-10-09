#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/05 16:30
# @Author  : dapengchiji！！
# @FileName: code14.py

'''
1．chr()函数 
该函数用于将ASCII码值转化为字符串。//chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
string chr (int ascii);  
2．ord()函数 
该函数用于将字符串转化为ASCII码值。
ord（str ） 返回值是对应的十进制整数。
'''

'''
1.生成所有的小写字母
2.生成所有的大写字母
3.所有的大小写字母
4.所有的大小写字母和数字
'''
#生成所有的小写字母
for i in range(97,123):
	print(chr(i))
	
print('*'*30)
#生成所有的大写字母
for i in range(65,91):
	print(chr(i))
	
print('*'*30)	
#所有的数字
for i in range(48,58):
	print(chr(i))

print('*'*30)
import string
#所有数字
print(string.digits)
#大小写字母
print(string.ascii_letters) 
#所有的大小写字母和数字
print(string.digits+string.ascii_letters)


print('*'*30)
#生成字符串 a1b2c3d4...j10
result = ""
first_ascii_code = 97  # 定义一个初始值
for  i  in  range(1,11):
	result+=chr(first_ascii_code+i-1)+str(i)
print(result)

print('*'*30)
#生成a1B2d3...J10
result = ''
first_ascii_code = 97 # 定义一个初始值
for i in range(1,11): 
    if i %2 == 0: # 遇偶数转换
       result+= chr(first_ascii_code+i-32-1)+ str(i) #小写转换成大写
    else:
        result+= chr(first_ascii_code+i-1) + str(i) # 输出小写
print(result)

#输出奇数字母和偶数字母到两个列表中，，小写字母
l1=[]  # 存偶数字母
l2=[]  # 存奇数字母
for i  in range(97,123):
	if i %2==0:
		l1.append(chr(i))		
	else:
		l2.append(chr(i))
print("存储偶数字母的列表:%s"%l1)
print("存储奇数字母的列表:%s"%l2)
		

		

