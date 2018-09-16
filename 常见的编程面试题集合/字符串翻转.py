#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''字符串翻转的多种写法'''

string = 'abcdef'

s=[1,3,4,5,6]
def string_reverse1(string):
    return string[::-1]
s.reverse()
print(s)


def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i, j in zip(range(l - 1, 0, -1), range(l // 2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)


def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]


from collections import deque


def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)


def string_reverse5(string):
    return ''.join(string[i]
    for i in range(len(string) - 1, -1, -1))



print(string_reverse1(string))
print(string_reverse2(string))
print(string_reverse3(string))
print(string_reverse4(string))
print(string_reverse5(string))

