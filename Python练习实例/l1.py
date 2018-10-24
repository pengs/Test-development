#!/usr/bin/python3
# -*- coding: utf-8 -*-

for n in range(100,1000):# 遍历所有三位数
	a = n% 10 # 取余找出个位数
	b = int(n/100)  # 求商找出百位数
	c = int(n/100) % 10 # 通过求商取整找出百位和十位，然后求商找出十位
	if n == a**3 + b**3 + c**3:
		print("%d"%n)


def isIpV4AddrLegal(ipStr):
    '''切割IP地址为一个列表'''
    ip_split_list = ipStr.strip().split('.')
    # 切割后列表必须有4个元素
    if 4 != len(ip_split_list):
        return False
    for i in range(4):
        try:
            # 每个元素必须为数字
            ip_split_list[i] = int(ip_split_list[i])
        except:
            print("IP invalid:" + ipStr)
            return False
    for i in range(4):
        # 每个元素值必须在0-255之间
        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:
            pass
        else:
            print("IP invalid:" + ipStr)
            return False
    return True

print(isIpV4AddrLegal('12.0.2.1'))
print(isIpV4AddrLegal('0.0.2.1'))



