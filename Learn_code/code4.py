#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 16:28
# @Author  : dapengchiji！！
# @FileName: code4.py

'''
['a', 'b', 'c', 'd', 'e', 'f', 'g']
查询list其中元素，拼出一个字符串"adg"
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str.join(元组、列表、字典、字符串) 之后生成的只能是字符串。
'''
# list=['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print("拼出的字符中结果是:%s"%(list[0]+list[3]+list[-1]))
#
# print("拼出的字符中结果是:%s"%"".join(list[::3])) # "".join()
#
# seq = {'hello':'nihao','good':2,'boy':3,'dapeng':4}
# print('_'.join(seq)) # 字典只对键进行连接
#
#

'''
删除  del list[1]或者 del list[1:3]
更新 list[1:3]=[2,8] 或者 list[0]=1
1、strip() 处理的时候，如果不带参数，默认是清除两边的空白符，例如：/n, /r, /t, ' ')。
2、strip() 带有参数的时候，这个参数可以理解一个要删除的字符的列表，是否会删除的前提是从字符串最开头和最结尾是不是包含要删除的字符，
如果有就会继续处理，没有的话是不会删除中间的字符的。

程序说明
做一个小图书馆程序，图书馆的书放到一个list里面保存，
使用add命令：加一本书，
使用lend命令，减去一本存在的书
如果不存在，需要提示一下
输入"." ，退出程序
使用getall命令:可以查询所有没有借出去的书，
'''

library=[]
while 1:
    command = input("输入你想要操作的命令:")
    command =command.strip() # strip该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。主要是为了防止用户输入空格过滤掉
    if "add " in  command: # 增加
        library.append(command.split(" ")[1])
        print("图书添加成功！")
    elif "lend " in  command:# 判断借出
        if command.split(" ")[1] in library:
            library.remove(command.split(" ")[1])
            print("借出成功啦啦")
        else:
            print("这本书已被借走，不在啦")
            continue
    elif "getall" in command:  # 查询所有
        if len(library)>=1:
            for book in library:
                print(book)
        else:
            print("图书馆已经没有书籍了")
    elif "." ==command:  # 结束程序
              break
    else:
        print("您输入的命令不正确，请重新输入")

