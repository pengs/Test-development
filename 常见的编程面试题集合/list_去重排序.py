#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素'''
#
ids=[1,23,44,33,22,33,44,55,22,33]
l=list(set(ids))#消除重复元素
# l.sort(ids.index)  #不改变原有顺序
print(l)


print("\n"+"--分割线--"+"--"*20)

# #通过for循环来实现且不改变原有顺序
l1 = [1,4,3,3,4,2,3,4,5,6,1]
l2 = []
for i in l1:#for循环
    if not i in l2:
        l2.append(i)
print (l2)


print("\n"+"--分割线--"+"--"*20)

# 通过生成器方式实现且不改变原有顺序
ids=[1,23,44,33,22,33,44,55,22,33]
l2 = []
[l2.append(i) for i in ids if not i in l2]  #列表生成式
print(l2)



#求一有序列表[1,2,3,,4,4,4,5,6]中4的区间，代码实现
class list():
    def get_all_index(arr, target):
        return [i for i, a in enumerate(arr) if a == target]

    if __name__ == "__main__":
       arr = [1,2,3,4,4,4,5,6]
       target = 4
       s = get_all_index(arr, target)
       print(s[0], s[-1])

