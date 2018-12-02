#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/3 11:16
# @Author  : dapeng！！
# @FileName: tongji.py

import os

class StatLines(object):
    def __init__(self,path):
        self.path = path

    def stat_lines(self):
        in_multi_comment = False
        total = 0
        file_list = os.listdir(self.path)
        os.chdir(self.path)
        for file in file_list:
            if file.endswith('.py'):
                lines = open(file, encoding='utf-8').readlines()
                count = 0
                for line in lines:
                    if line == '\n':
                        continue
                    elif line.startswith("#") or \
                         (line.startswith('"""') and line.endswith('"""')):
                        continue
                    elif (line.startswith("'''") and line.endswith("'''")):
                        continue
                    else:
                        count += 1

                total += count
                print('%s has %d lines' %(file,count))
        print('total lines is: %d' %total)

if __name__ == '__main__':
    sl = StatLines('/Users/macbook/Test-development/Learn_code')
    sl.stat_lines()



