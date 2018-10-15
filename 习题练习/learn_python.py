#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 13:54
# @Author  : dapeng！！
# @FileName: learn_python.py


# 1. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
result = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (i != k):
                result += 1
                print(i, j, k)
print("能组成多少个互不相同且无重复数字的三位数:%d个"%result)

print("*"*30)
d=[]
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j)and (j!=k)and(i!=k):
				d.append(int(str(i)+str(j)+str(k)))
print ("能组成多少个互不相同且无重复数字的三位数:%s"%d)
print("能组成多少个互不相同且无重复数字的三位数:%d个"%len(d))                

print("*"*30)
# 2. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
'''

for i in range(1,86):
	if 168 % i == 0:
		j = 168 / i
		if i > j and (i * j) % 2==0 and (i - j ) % 2==0:
			m =(i + j) / 2
			n = (i - j) / 2
			x = n * n - 100
			print('符合条件的整数有:',x)
			
print("*" * 30)
# 参考其他人写的
t = []
for m in range(168):
	for n in range(m):
		if m**2 - n**2 == 168:
			x = n**2 - 100
			t.append(x)
print('符合条件的整数有：',t )		

print("*" * 30)
# 3.26个字母大小写成对打印，如Aa,Bb，。。。
for i in range(65,91):
	print(chr(i)+chr(i+32),end=",")
	
print("*" * 30)	
# 4.1个list包含10个数字，然后生成新的list，新的list比之前的数多1
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = []
for i in l1:
	if isinstance(i,(int,float)):
		l2.append(i+1)
	else:
		l2.append(i)
print("原来的list列表数值是:",l1)		
print("新生成的list列表数值是:",l2)

print("*" * 30)
# 5.倒序取出每个单词的第一个字母
s ='I Like You,I Love You,give two  money'
result = []
for i in s.split()[::-1]: # 倒序截取拆分
	result.append(i[0])  # 获取第一个字母
print(result)

# 先切割 拆分，再翻转；最后通过序列打印
s ='I Like You,I Love You,give two  money'
s=s.split()
s.reverse()
result = []
for i in s:
	result.append(i[0])
print(result)	

print("*" * 30)	
# 6.请找出字符串中出现次数最多的字母（出现次数重复）

s1='aaabbbccccddddxxxxxfffwwwww'
max_occurence_times_letters = [] # 创建空列表
max_occurence_times = 0 # 初始化出现的次数
for i in s1:
	if s1.count(i) > max_occurence_times:  
		max_occurence_times_letters=[]
		max_occurence_times_letters.append(i)
		max_occurence_times = s1.count(i)
	elif s1.count(i) == max_occurence_times:  # 如果出现次数相同，也需要存入到列表中
		max_occurence_times_letters.append(i)
print(list(set(max_occurence_times_letters)))  #打印输出 出现次数最多的字母--排重--转列表


print("*" * 30)
# 7.请找出字符串中出现次数最多的字母(出现的次数不重复)
s = 'aabbbccccddeeddffffff'
max_occurence_times_letter = " "  # 定义出现次数最多的字母
max_occurence_times = 0  # 定义出现最多的次数
for i in s: 
	if s.count(i) > max_occurence_times:  
		max_occurence_times_letter = i
		max_occurence_times = s.count(i)
print("出现次数最多的字母是:",max_occurence_times_letter,"出现的次数是:",max_occurence_times)	

print("*" * 30)
'''
str.count(sub, start= 0,end=len(string))
'''
# count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
print (s1.count("x",0,27)) 


print("*" * 30)
# 8.如何找到字典中最大值(值重复)
d={'a':1,'b':2,'c':3,'d':4,'e':4}
max_value = d['a']
result = [] # 创建空列表
for k,v in d.items():  # 以列表返回可遍历的(键, 值) 元组数组
	if v > max_value:
		max_value = v 
		result = [] # 清空列表
		result.append(k) # 将字典的键值插入到列表中
	elif v == max_value: # 确保 是否还有其他值也等于最大值
		result.append(k) # 添加最大的键值到列表中
print("字典中最大值",result)		 # 打印最后结果

print("*" * 30)		
#另一种写法使用内置函数（max）
d1={'a':1,'b':2,'c':3,'d':4,'e':4}
max_value = max(d1.values())
result = [] # 创建空列表
for k,v in d1.items():
	if v == max_value:
		result.append(k)
print("字典中最大值",result)

