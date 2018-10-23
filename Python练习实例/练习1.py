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
		
	elif (I > 20) and (I <= 40):
		awards = (I - 20) * 0.05 + award(20)			

	elif (I > 40) and (I <= 60):
		awards = (I - 40) * 0.03 + award(40)			

	elif (I > 60) and (I <= 100):
		awards = (I - 60) * 0.015 + award(60)
			
	else:
		awards = award(100) + (I - 100) * 0.01
	
	return awards
		
if __name__ == '__main__':
	i = int(input("请输入当月利润:"))
	print("净利润:", i)
	print("发放的奖金为：", award(i/10000)*10000)






		
		




