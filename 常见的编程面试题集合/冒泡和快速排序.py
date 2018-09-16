#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''冒泡排序'''

#使用for循环
list=[1,3,5,18,20,90]

for i in range(len(list)):
    for j in range(i):
        if list[j] >list[i]:
            list[i],list[j] = list[j],list[i]
print(list)

#Python内嵌函数sort()
list.sort()
print(list)



'''快速排序'''

def QuickSort(l,left,right):
    # 判断left是否小于right,如果为false,直接返回
    if left < right:
        i = left
        j = right
        #设置基准数
        key = l[i]
        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (l[j] >= key):
                j = j - 1
            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            l[i] = l[j]
            #同样的方式比较前半区
            while (i < j) and (l[i] <= key):
                i = i + 1
                #交换
            l[j] = l[i]
            # print("-----"%l)
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回key
        l[i] = key
        #递归前后半区
        QuickSort(l, left, i - 1)
        QuickSort(l, j + 1, right)

l = [12, 90, 4, 22, 5, 89, 100, 90]
QuickSort(l,0,len(l)-1)
print("Quick Sort: ")
print(l)

