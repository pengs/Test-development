#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 20:20
# @Author  : dapengchiji！！
# @FileName: code7_count.py

def count(s):
    count_a = count_z = count_o = count_s = 0
    for i in s:
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
            count_a = count_a + 1
        elif ord(i) >= 48 and ord(i) <= 57:
            count_z = count_z + 1
        elif ord(i) == 32:
            count_s = count_s + 1
        else:
            count_o = count_o + 1
    print  ("英文字母个数：%d个" % count_a)
    print  ("数字个数：%d个" % count_z)
    print  ("其他字符个数：%d个" % count_o)
    print ("空格个数：%d个" % count_s)


if __name__ == "__main__":
    s = 'You very 666 beautiful I like very you 666! I am 20 years old!'
    count(s)
