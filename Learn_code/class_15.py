#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
类和对象
'''
class Student(object): # 定义一个Student的类
      def __init__(self,name,sex,age,score):  # 类实例
            self.name=name
            self.sex=sex
            self.age=age
            self.score=score

    
p1=Student("dapeng", "男", 29, 90)    # 实例化属性
p2=Student("xiaoxu", "女", 38, 89)

print("性别为:%s," %p1.sex, "年龄是:%d" % p1.age)  # 调用方法输出
print("名字是:%s," % p2.name, "分数为:%d" % p2.score)

s='哈哈'
print(s)



#自定义函数，统计字母出现次数
print("*" * 30)	
def count_occurence(s,letter):  # 定义一个函数，统计出现的次数
      if isinstance(s,str) or isinstance(letter, str):
            return 0
            times=0
      if letter not in s:
            return 0
      else: 
            for i in s:
                  if i == letter:
                        times+=1
      return times          
print(count_occurence("aaa","aaa"))
print(count_occurence("aaa","b"))
print(count_occurence("2",2))
