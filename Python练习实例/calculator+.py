#!/usr/bin/python3
# -*- coding: utf-8 -*-

# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 编写一个calculator，提示选择运算符，输入对应数据，继续输入数字，打印出最终计算结果
def add(num1, num2):  # 加法
    return num1 + num2

def minus(num1, num2):  # 减法
    return num1 - num2

def multiply(num1, num2):  # 乘法
    return num1 * num2

def divide(num1, num2):  # 除法
    return num1 / num2

operator = input('''选择运算符:
1 is +
2 is -
3 is x
4 is ÷
输入你的选择（1/2/3/4）:
''')

if operator not in '1234':
    print("运算符选择输入错误，请重新输入")

else:
    num1 = int(input("请输入第一个数字:"))
    num2 = int(input("请输入第二个数字:"))
    if (operator == "1"):
        print("两数相加结果:{}".format(add(num1, num2)))
    elif (operator == "2"):
        print("两数相减结果:{}".format(minus(num1, num2)))
    elif (operator == "3"):
        print("两数相乘结果:{}".format(multiply(num1, num2)))
    elif (operator == "4"):
        print("两数相除结果:{}".format(divide(num1, num2)))

