#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
将标准输出改为到文件输出
'''
def cmp(a,b):
    if not isinstance(a,(int,float)):
        raise TypeError
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
print(cmp(2,5))			

print("*"*30)
'''
把一个字符串中的所有数字删除
'''
s='a1b2c3d4f5'
result=[]

for i in s:
    if i not in '0123456789':
        # result.append(i)  # 插入
        result+=i
print("".join(result))


print("*"*30)
#列表推导式
print("".join([i for i in 'a1b32322cw3423243d4f5' if i not in '0123456789']))

'''
查找列表最大值和最小值，不使用函数
'''
ls = [1,3,4,6,9,666]
max_number = 0
for i in ls:
    if i > max_number:
        max_number=i  
print(max_number) 

''''给3个数排序'''
l = [8,20,200]
def l_sort(l):
    '''找到列表最大值'''
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    return max_number                    
print("找到列表最大值:",l_sort(l)) 







