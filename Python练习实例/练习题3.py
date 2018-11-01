#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 1 输入1~127的ASCII码并输出对应的字符
num = int(input("请输入1~127的ASCII码："))

if isinstance(num,int):
	nums=chr(num)
	print("输入的数字是:{},对应的ASCII码:{}".format(num, nums))
	
# 2、输入a,b,c,d4个整数，计算a+b-c*d	
#
a = int(input("请输入一个整数："))
b = int(input("请输入一个整数："))
c = int(input("请输入一个整数："))
d = int(input("请输入一个整数："))
#
result = a+b-c*d
if isinstance(result,int):
	print("结果为：%d"%result)
else:
	print("请输入整数")	

# 3、计算一个12.5m16.7m的矩形房间的面积和周长

length = eval(input("Please input length of the room:"))
width = eval(input("Please input width of the room:"))
area = length * width
perimeter = 2 * (length + width)
print("The room's area is %.2f and perimeter is %.2f"%(area,perimeter))	

# 4、怎么得到9/2的小数结果

print(9/2)
n = 9/2
print(float(n))

# 5、python计算中7*7*7*7可以有多少种写法

print(7*7*7*7)
print(7**4)
print(pow(7,4))  # pow() 方法返回 xy（x的y次方） 的值
print(eval('pow(7,4)')) # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(eval('*'.join(['7']*4)))
# 循环
a=1
for i in range(4):
	a =a*7
print(a)

# 6、写程序将温度从华氏转换为摄氏温度 C=5/9*(F-32)

F =int(input("请输入华氏摄氏度:"))
C =5/9*(F-32)

print("转换摄氏温度{}".format(C))

#7、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
price = float(input("请输入你购买物品的价格："))
result_price = 0
if price >= 50 and price <= 100:
	result_price = price*0.9
	print("你输入的价格:{}元,享受对应的折扣10%,因此打折后的价格为:{}元".format(price,result_price))
elif int(price) > 100:
	result_price = price*0.8
	print("你输入的价格:{}元,享受对应的折扣20%,因此打折后的价格为:{}元".format(price,result_price))
else:
	print("你购买物品的价格:%d"%price)	
	
# 8、判断一个n数能否同时被3和5整除，打印出这个数

n = eval(input("请输入需要判断的数字："))
if n % 3 ==	0 and n % 5 ==	0:
	print("输入的数字:{}，能同时被3和5整除".format(n))
else:
	print("输入的数字:{}，无法同时被3和5整除".format(n))	
	
# 9、求1+2+3+...+100的和
result = 0
for i in range(1,101):
	result += i
print("1+2+3+...+100的和为:%d"%result)	

i =1
result1 = 0
while i <=100:
	result1 += i
	i += 1
print("1+2+3+...+100的和为:%d"%result1)	
	

	
#10 、交换2个变量的值
a = 1
b = 2
a,b = b,a
print("交换后2个变量的值{},{}".format(a,b))

