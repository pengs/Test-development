#!/usr/byearn/python3
# -*- codyearng: utf-8 -*-

import math
def is_prime(num):
	if not isinstance(num,int):
		return False
	if num ==1:
		return False
	if num == 2:
		return True
	for i in range(2,int(math.sqrt(num)+1)):
		if num%i==0:
			return False
	return True
result = 0
for i in range(1,101):
	if is_prime(i):
		result+=i
print(result)
# for 循环的方式，求一下100以内奇数之和

# 输入3个数字，达到3个数字求和
result = 0
for i in range(3):
	result+=int(input("请输入数字:"))
print(result)

'''
用户输入不同数据，当输入的数据达到3个数字的时候，求和结束程序（数字可以是整数）
提示判断是否为整数，isdigit()，遍历所有输入数据，判断是否在
0-9的字符串范围内
'''
def isdigit(s):
	for i in s:
		if i not in '0123456789':
			return False
	return True

result =0
times=0
while times<=3:
	num = input("请输入数字：")
	if isdigit(num):
		result+=int(num)
		times+=1
		break
print(result)
#		
	
	
	

	
'''
嵌套列表，输出一个矩阵
如
1 2 3
4 5 6
7 8 9
'''	
#l = [[1,2,3],[4,5,6],[7,8,9]]
#for i in l:
#	for j in i:
#		print(j,end=' ')
#	print(' ')	
#
## 2
#for i in range(len(l)):
#	for j in range(len(l[i])):
#		print(l[i][j],end = ' ')
#	print(' ')	
#
#		
   
		
# 花田喜欢人			
import requests
import json

url='https://love.163.com/api/relation/followersByCursor'
header = {'Content-Type':'application/json'
	,'Authorization':'OAuth2 975e72fe614e1c01edf5beb937e46b9f'}	
data ={}
re=requests.post(url,headers=header,params=data)	
result=re.json()
r=re.text
print(json.dumps(result,indent=4,ensure_ascii=False))	

#with open('/Users/macbook/Desktop/2.txt','r')as f:
#	file=f.readlines()
#f2=open('/Users/macbook/Desktop/3.txt','wb')
#
#for i in file:
#	l=i.spilt('\t')[0]
#	if l =='https://lovepicture.nosdn.127.net/'+str(i)+'?imageView':
#		f2.write(i)
#f2.close()

			 
		
#with open('/Users/macbook/Desktop/2.txt','w')as f:
#	f.write(r)
#					

			
'''从文本读取指定的url，保存到另一个文本'''