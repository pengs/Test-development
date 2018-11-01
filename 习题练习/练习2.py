#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1、找出小于1000的正整数中，是3或5的倍数的数，并计算其和
'''
result = 0
for i in range(0,100):
    if i % 3 == 0 or i % 5 == 0:
        result+=i
print("数字加起来的和为:",result)    
            

'''
2、0~9这10个数字可以组成多少不重复的3位数？
'''
result1 = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (i!=j) and (j!=k) and (k!=i):
                result1+=1
print(result1)                  
#                        
'''
3、程序执行后，输入一串字符，然后把它反转后打印出来，如果敲击回车，则终止
'''    
import sys
if True:
     s = input("请输入字符串:")
     if isinstance(s, (str)):
         print(s[::-1])
     else:
         sys.exit()

'''
4、要审查的帖子在这个文本文档里，要求将所有的和谐，三个代表，言论自由，64替换为*号
'''
 

'''
5、遍历并打印0到100，如果数字能被3整除，显示Fizz；
如果数字能被5整除，显示Buzz；
如果能同时被3和5整除，就显示FizzBuzz。
结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……
'''

for i in range(0,101):
   if i % 3 == 0 and  i %5==0:
       print("FizzBuzz")
   elif i % 3 ==0:
       print("Fizz")
   elif i % 5==0 :
       print("Buzz")
   else:
       print(i)


'''
6、水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。 例如：1^3+5^3+3^3=153。
水仙花数只是自幂数的一种，严格来说3位数的3次幂数才称为水仙花数
'''
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i*100+j*10+k == i**3+j**3+k**3:
                print(i*100+j*10+k)
            else:
                print('no')
                
                


'''
7、输入某年某月某日，判断这一天是这一年的第几天？

解题思路  
闰年 2月28天
平年 2月29天
'''
year = int(input('请输入年份：\n'))
month = int(input('请输入月份:\n'))
day = int(input('请输入日期:\n'))
months = [31,28,31,30,31,30,31,31,30,31,30,31] # 每个月的天数 闰年2月需要加一天
sumday = day
for m in range(0, month-1):
    sumday += months[m]
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        if (month > 2):# 此处要考虑若输入的月份没有超过2,就不用加1
            sumday +=1
            print("这是第 %d 天" % sumday)
        else:
            print("这是第 %d 天" % sumday)
else:
    print("这是第 %d 天" % sumday)




'''
8、题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
string = input("请输入5个字符:")
def re(string):
    if len(string) == 0:
        return string
    return re(string[1:])+string[0]
print(re(string))

