#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 08:36
# @Author  : dapeng！！
# @FileName: code_12.py



'''
找出文件中所有包含test的行数
'''

fp =open('/Users/macbook/Desktop/b.txt','r+',encoding='utf-8') # r+ 读写操作 打开一个文件用于读写。文件指针将会放在文件的开头。
data=fp.readlines()  # 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
for  i in range(10):
  fp.write(str(i)+'\n')
fp.close() # 关闭文件。关闭后文件不能再进行读写操作。
lines=0  #统计查询 多少行
for line in data:
    if 'test' in line:
        lines += 1
        print(line.strip())
print("包含test字符一共有:%d行"%lines)


'''
写一个文件，里面写入dapeng1--dapeng101，写入之后读出来
'''

with open('/Users/macbook/Desktop/c.txt','w',encoding='utf-8')as f:
    for i in range(102):
        f.write('dapeng'+str(i)+'\n')
with open('/Users/macbook/Desktop/c.txt','r',encoding='utf-8')as f:
    f.readline()
    f.seek(10,0)
    print(f.tell())
    print(f.readline())

'''
文件替换  将一个文件其中的test字符，修改为其他dapeng
'''
with open('/Users/macbook/Desktop/A.txt','r+') as fp1:
        for i in fp1.readlines():
            fp1.write(i)
            print(i.replace('test','dapeng'),end="")





