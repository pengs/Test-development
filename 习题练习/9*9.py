#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 19:33
# @Author  : dapengchiji！！
# @FileName: 9*9.py

# # 输出 9*9 乘法口诀表。
for i in range(1,10):
    for j in range(1,10):
        print(j,"*",i,"=",i*j,"\t" ,end="")# 注意这里加上end = ''是防止换行.
        if(j==i):
            print("")
            break

#输出 9*9
for i in range(1, 10):
    for j in range(1, i + 1):
        k = i * j
        print('{}*{}={}'.format(j, i, k), end=' ')#注意这里加上end = ''是防止换行.
    print('')

#while 循环9*9
i=0
j=0
while i <9:
    i+=1
    while j<9:
        j+=1
        print(j, "*", i, "=", i * j, "\t", end="")
        if i == j:
            j=0
            print("")
            break

# 对10个数进行排序。
list=[2,3,34,12,89,11,9,8,200]

print(sorted(list))

for i in range(len(list)):
    for j in range(i):
        if list[j] > list[i]:
            list[i],list[j] = list[j],list[i]
print(list)            
    
    

# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

#if __name__ == '__main__':
#    from sys import stdout
#    filename = input('输入文件名:\n')
#    fp = open(filename,"w")
#    ch = input('输入字符串:\n')
#    while ch != '#':
#        fp.write(ch)
#        stdout.write(ch)
#        ch = input('')
#    fp.close()
#
# #利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
def function(score):
   if(score>=90):
       print("分数:%d,已达到了A，非常棒!!!"%score)
   elif(60<=score<=89):
       print("分数:%d,已达到了B，很不错继续加油哟!"%score)
   else:
    print("分数:%d,只是C，需要继续努力哟"%score)

if __name__=="__main__":
    function(int(input("请输入分数:")))
    
    

#将一个列表的数据复制到另一个列表
list1=[1,2,3,5,11]
list2=[]
for i in range(len(list1)):
      list2.append(list1[i])
print(list2)



