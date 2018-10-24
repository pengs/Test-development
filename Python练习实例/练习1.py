#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 10:25
# @Author  : dapeng！！
# @FileName: 练习1.py

# 1、题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

result = 0 # 统计一共有多少个互不相同且无重复数字
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i!=j and j!=k and k!=i:
				result += 1				
				print(i,j,k)
print("共有%d个互不相同且无重复数字的三位数"%result)
				

# 2、题目：企业发放的奖金根据利润提成。

'''利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

def award(I):
	awards = 0
	if I<=10:
		awards = I*0.1
	elif (I > 10) and (I <= 20):
		awards = (I - 10) * 0.075 + award(10)
	elif 20< I <= 40:
		awards = (I - 20) * 0.05 + award(20)			
	elif 40 < I <= 60:
		awards = (I - 40) * 0.03 + award(40)			
	elif 60 < I <= 100:
		awards = (I - 60) * 0.015 + award(60)
	else:
		awards = award(100) + (I - 100) * 0.01
	return awards
		
if __name__ == '__main__':
	i = int(input("请输入当月利润:"))
	print("净利润:", i)
	print("发放的奖金为：", award(i/10000)*10000)



# 3、题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
分析 x + 100 = n**2, x + 100 + 168 = m**2		
设 m+n=i,m-n=j,则m=(i+j)/2;n=(i-j)/2 有 i*j=168, 因为 m,n 都是整数且 m!=n, 所以 j,i!=0, 因为i*j是正数，
故abs(i)>=1,abs(j)>=1。所以i和j的上限可以取 168。因此m和n的上限也是168,下限可以取-168
（注意，m,n的取值范围可以放得很大，不影响结果，因为限制条件可以自己去约束，但所取的范围一定要比真实范围大）
'''
result =[]
for m in range(168):
	for n in range(m):
		if (m+n)*(m-n) == 168:
			x = n**2-100
			result.append(x)	
print("所求的整数为：",result)	

# 列表推导式			
print([n**2-100 for m in range(168) for n in range(m) if(m+n)*(m-n)==168])	


		
# 4、题目：输入某年某月某日，判断这一天是这一年的第几天？

# 内置函数

import time
D=input("请输入年份，格式如XXXX-XX-XX：")
d=time.strptime( D,'%Y-%m-%d').tm_yday # 将字符串转为时间元组
print ("今天是一年中的第{}天 !".format(d))



year = int(input('请输入年份：'))
month = int(input('请输入月份:'))
day = int(input('请输入日期:'))
months = [31,28,31,30,31,30,31,31,30,31,30,31]
d = 0
if 1<=month<=12: # 判断月份
	if 1<day<=31: # 判断日期
		d += day 
		if month > 2:
			if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)): # 判断闰年
				d += 1 #如果是闰年 则多加一天
		for i in range(1，12):
			if i < month:
				d += months[i]
				i += 1
		print("您输入的日期是本年的第:%d天"%d)
	else:
		print('输入的日期有错误')
else:
	print('输入的月份有错误')
	
	
# 5、输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input("请输入数字："))	
y = int(input("请输入数字："))	
z = int(input("请输入数字："))	

l = [x,y,z]
l.sort()	  # 内置函数		
print("这三个数由小到大输出:",l) 
# 冒泡排序
for i in range(len(l)):
	j=0
	for j in range(i):
		if l[j] > l[i]:
			l[i],l[j] = l[j],l[i]
print("这三个数由小到大输出:",l) 	

# 6、 斐波那契数列。

#计算斐波那契数列，通过循环来实现
num=int(input("请输入您要显示的项数："))
print("-------循环-------");
n=3
a=[1,2]
if(num==1):
	print(a[0],end=" ")
elif(num==2):
	print(a[num-2],a[num-1],end=" ")
else:
	while(n<=num):
		temp=a[n-2]+a[n-3]
		a.append(temp)
		n+=1
	for i in a:
		print(i,end=' ')
print()


# 7、将一个列表的数据复制到另一个列表中。

l1=[1,2,3,4,5]
l2=[]
for i in l1:
	if i not in l2:
		l2.append(i)
print(l2)	

l3=l1[:]
print(l3)

l4=l1.copy()
print(l4)

l5=[i for i in l1]
print(l5)

l6=l1*1
print(l6)

#8、 输出 9*9 乘法口诀表。

for i in range(1,10):
	for j in range(1,10):
		print(j,"*",i,"=",i*j,"\t",end="")
		if i==j:
			print("")
			break

for i in range(1,10):
	for j in range(1,i+1):
		k=i*j
		print('{}*{}={}'.format(j, i, k), end=" ")	
	print("")
	
	
# 9、暂停1秒输出

import time

l1=[1,2,3,4,5]
for i in l1:
	time.sleep(1)
	print(i)
	
# 10、暂停一秒输出，并格式化当前时间。

import time
 
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# 暂停一秒
time.sleep(1)
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))	