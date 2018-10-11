#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
冒泡排序算法的运作如下：
	比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
	对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
	针对所有的元素重复以上的步骤，除了最后一个。
	持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
l1 = [54,26,93,17,77,31,44,55,20]
for i in range(len(l1)):
	for j in range(i+1):
		if l1[j] > l1[i]:
			l1[i],l1[j] = l1[j],l1[i]
print("冒泡排序后的列表为1:",l1)

print("*" * 30)	
#定义一个函数
def bubble_sort(alist):
	for i in range(0,len(alist)):
		for j in range(i+1):
			if alist[j] > alist[i]:
				alist[i], alist[j] = alist[j], alist[i]
if __name__=='__main__':				
	li = [54,26,93,17,77,31,44,55,20]
	bubble_sort(li)
	print("使用函数方法冒泡排序后的列表为2:",li)	
		
print("*" * 30)	
#内置函数sort
li = [54,26,93,17,77,31,44,55,20]
li.sort()
print("使用内置函数冒泡排序后3:",li)

			

#选择排序
'''
选择排序（Selection sort）是一种简单直观的排序算法。
	首先在待排序序列中找到最小（大）元素，存放到排序序列的起始位置，
	然后，再从剩余未序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
'''
print("*" * 30)	
alist = [54,26,93,17,77,31,44,55,20]
n=len(alist)
for i in range(n-1): # 需要进行n-1次选择操作
	min_index = i # 记录最小位置
	for j in range(i,n):  # 从i+1位置到末尾选择出最小数据
		if alist[min_index] > alist[j] :
			min_index = j
	if min_index != i: # 如果选择出的数据不在正确位置，进行交换
		alist[i], alist[min_index] = alist[min_index], alist[i]
print("选择排序后的列表:",alist)				


#快速排序
'''
快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''


