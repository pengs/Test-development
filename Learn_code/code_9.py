#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 15:52
# @Author  : dapengchiji！！
# @FileName: flask_api.py

'''
list 增删改查
'''

a=[1,23,4,5,6,7,8]
#update
a[0]=90
print(a)
#插入
a.append(10)
print(a)
#增加
a.insert(2,80)
print(a)
#删除
a.remove(7)
print(a)
#增加
a.extend((1,2,3,4))
print(a)
#统计列表出现的次数
b=a.count(4)
print(b)
#pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
a.pop(8)
print(a)
#reverse() 函数用于反向列表中元素
a.reverse()
print(a)
#排序
a.sort()
print(a)
#去重
print(list(set(a)))
print("*"*50)

'''
元祖和列表的区别，列表可修改，元祖不可修改（对象不可修改）
'''

#元祖
tup1 = ('physics', 'chemistry', 1997, 2000,[10,100])
tup1[4].append(2000) #插入值
del tup1[4][0]  #删除值
tup1[4][1]=888  #修改元祖 对象的值

print(tup1)
#声明元祖的方式1
def func(a,b):
    return a,b
print(func(1,2))
print(type(func(1,2)))
#声明元祖的方式2
m=1,2
print(m)
print(type(m))

print("*"*50)

'''
字典无序;字典的key特点，不能重复
'''
#字典
d = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#增加一个字典
d['haha']=1112
#删除
del d['Cecil']
d.pop('Beth')
print(d)

#修改字典值
d['Alice']='www'

#查询
print(d['Alice'])
print(d.keys())
print(d.values())
print(d)

print("*"*50)
#遍历key值
for i in d.keys():
    print(i)
print("*"*50)
#遍历values
for i in d.values():
    print(i)

print("*"*50)

#遍历字典
for key,valuse in d.items():
    print(key,":",valuse)

print("*"*50)

#快速生成一个字典
d={}
print(d.fromkeys([1,2,3,4,5],"ab"))
print("*"*50)

#字典存取对应关系的
d["石鹏"]=['石头','石有','石石']
print(d)
print("*"*50)

#Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}
dict.update(dict2)
print("更新字典 dict : ", dict)
print("*"*50)

#按照 key 来给字典排序
dict = {200:'a',20:'b',610:'c'}
d1={}
for k in sorted(dict.keys()):
    d={k:dict[k]}
    d1.update(d)
print(d1)
print("*"*50)

#如果键值有重复，则 dict2 的内容更新替换到 dict 中，如上面的代码，会有下面的结果
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female','Age':9}
dict.update(dict2)
print("更新字典 dict : ", dict)
print("*"*50)


'''
统计一句话中，出现了多少个单词
如：how old are you,I fine thank you and you！
'''

s='How old are you,I fine thank you and you'
result = 0
for i in s:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):  # 大写字母''小写字母
       result += 1
print("一共出现:%d个单词"%result)



