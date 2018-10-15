#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.设定一个用户名和密码，输入正确提示登录成功，否则失败，但是失败次数最多3次，否则退出程序（可以使用for或者while 循环）

'''

# 1.次数
import sys
username = 'dapeng'
password = 'test123'

#for 循环
# for i in range(3):
# 	if username == input("输入你的用户名:") and  password == input("输入你的密码:"):
# 		print("Login Successful!")
# 		break
# 	else:
# 		print("用户名或者密码错误")
# 	i +=1  # 循环次数累加
# print ("错误次数超过限制，程序退出")
# 	# if i ==2:
# 	# 	print ("错误次数超过限制，程序退出")
#
#
# # while 循环
# count = 0
# while count < 3:
# 	if username == input("输入你的用户名:") and  password == input("输入你的密码:"):
# 			print("Login Successful!")
# 			break
# 	else:
# 		print("用户名或者密码错误")
# 	count += 1
# print ("错误次数超过限制，程序退出")


'''	
2.自己实现一个函数，在一句话中查找某个单词的算法，存在返回索引号，否则返回False
(1) 使用句子中的坐标遍历句子的每一个位置
(2) 使用查找单词的长度结合使用切片来查找单词
例如:s[i:i+len(单词)]

遍历字符串 （1）基于位置遍历 （2）基于字符来遍历
'''
# 查找单词
#方法1 内置方法
import re
word = 'Like'
str_word = 'I Like You But I hope know You Where are you from?'
print([i.start() for i in re.finditer(word,str_word)]) #finditer 返回一个可迭代对象。

#find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
print(str_word.find('Like'))
print(str_word.rfind('Like')) # rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。


#写的方法1
strs_word = 'I Like You But I hope know You Where are you from?'
def find_word(strs_word,words):
    index_list=[]
    words_length=len(words)
    for i in range(len(strs_word)-words_length+1):
        if strs_word[i:i+words_length] == words:
            index_list.append(i)
    return index_list
print(find_word(strs_word,'Like'))


#按照学习教程写的方法2  循环嵌套
strs_word = 'I Like You But I hope know You Where are you from?'
def find_word(strs_word,words):
    index_list=[]
    words_length=len(words)
    for i in range(len(strs_word)-words_length+1):
        for j in range(words_length):
            if strs_word[i+j] != words[j]:
                break
        else:
            index_list.append(i)
    return index_list
print(find_word(strs_word,'Like'))
    


