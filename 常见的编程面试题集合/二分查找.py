#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''给定一个排序的整数数组（升序）和一个要查找的整数target，
用O(logn)的时间查找到target第一次出现的下标（从0开始），
如果target不存在于数组中，返回-1。
如：在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
'''

def Search(array,t):
    target = 0
    height = len(array)-1
    while target < height:
        mid = (target+height)/2
        if array[mid] < t:
            target = mid + 1
        elif array[mid] > t:
            height = mid - 1
        else:
            return array[mid]
    return -1
if __name__ == "__main__":
    print(Search([1,5,6,8,10,15,18,25],5))

