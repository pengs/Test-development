#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
'''
n, m = list(map(int, input().split(' ')))
li = []
  
def f(n, m, l, k):
	if m == 0:
		print(' '.join(l))
	for i in range(k, n+1):
		if i > m:
			break
		l.append(str(i))
		f(n, m-i, l, i+1)
		l.pop()
		  
f(5, 5, li, 1)
