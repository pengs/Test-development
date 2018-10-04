#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:41
# @Author  : dapeng！！
# @FileName: code_list_13.py

'''
一个列表排重,多种实践方法
'''
list1 = [7,1,2,3,4,5,5,6,7,9,8,9]

# 常规通过循环排重
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print("")
print(list2)

# 内置函数set去重
print(list(set(list1)))

# 使用字典中fromkeys()的方法来去重
lst2 = {}.fromkeys(list1).keys()
print(lst2)

# 列表推导式
temp = []
[temp.append(i) for i in list1 if i not in temp ]
print(temp)


# 使用sort函数来去重
list1 = [7,1,2,3,4,5,5,6,7,9,8,9]
list2.sort(key=list1.index)
print(list2)

# 使用sorted函数来去重
lst2 = sorted(set(list1), key=list1.index)
print(list2)

