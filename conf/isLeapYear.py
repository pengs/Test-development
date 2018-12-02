#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 10:51
# @Author  : dapeng！！
# @FileName: isLeapYear.py

class Solution():
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isleapyear(self,n):

        if (n % 100) != 0 and (n % 400) == 0:
            return  True
        elif  (n % 4) == 0:
            return True
        else:
            return False

n=int(input("请输入需要判断的年份:"))
Leapyear = Solution().isleapyear(n)
print(Leapyear)




