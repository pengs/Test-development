#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''生成器'''

# g=(x*x for x in range(5)) #列表生成式
# for i in g:
#     print(i),
#
# print("\n"+"--分割线--"+"--"*20)


#for x循环
def fibonacci():
    a, b = 0, 1
    for i in range(10):
        yield b
        a, b = b, a + b
for i in fibonacci(1):
        print(i),


print("\n"+"--分割线--"+"--"*20)

#while循环方式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fib(11):
    print(n),




