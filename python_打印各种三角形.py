#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 直角三角形
rows = int(input('输入列数：'))
for i in range(1,rows):
	print('*'*i)

for i in range(1,rows):
	for j in range(i):
		print("*",end="")
	print("")
	 
## 等腰直角三角形
rows = int(input('输入列数：'))
for i in range(1, rows):
	print(' * '*i)

for  i in range(1,rows):
	for j in range(1,i+1):
		print(" * ",end="")
	print("")
	
	
# 打印等腰三角形
rows = int(input('输入列数：'))
for i in range(1,rows):
	if i%2!=0:
		str=('*'*i)
		print(str.center(9,' '))


for i in range(rows): 
	for j in range(0,rows-i):
		print(end=' ')
	for k in range(rows-i,rows):
		print('*',end=' ')
	print('')
		

		

# 正方形
rows = int(input('输入列数：'))
for i in range(0, rows):
	print(" * "*rows)


for i in range(0,rows):
	for j in range(0,rows):
		print(" * ",end="")
	print(" ")


# 打印倒立直角三角形
for x in range(10):
	for i in range(x,10):
		print('*',end='')
	print('')


print('同一行打印直角三角形')
for j in range(10):
	for x in range(0,j):
		print('*',end='')
	for n in range(j,19-j):
		print(' ',end='')
	for k in range(0,j):
		print('*',end='')
	print('')


print('直角三角形拼装心形')
for j in range(8):
    for x in range(0, j):
        print('*', end='')
    for n in range(j, 19 - j):
        print(' ', end='')
    for k in range(0, j):
        print('*', end='')
    print('')
for i in range(10):
    for j in range(0, 0 + i):
        print(end=' ')
    for k in range(0 + i, 10):
        print('*', end=' ')
    print('')

print('打印倒立等腰三角形1')
for j in range(10):
	for x in range(0,j):
		print(end=' ')
	for n in range(j,15-j):
		print('*',end='')

	print('')


print('打印倒立等腰三角形2')
for i in range(10):
	for j in range(0,0 + i):
		print(end=' ')
	for k in range(0 + i,10):
		print('*',end=' ')
	print('')


print('同一行打印两个等腰三角形')
for i in range(10):
	for j in range(0,10 - i):
		print(end=' ')
	for k in range(10 - i,10):
		print('*',end=' ')
	for n in range(0,0 ):
		print(end=' ')
	for m in range(0 + i,10):
		print(' ',end=' ')
	for jj in range(10,10):
		print(end=' ')
	for kk in range(10 - i,10):
		print('*',end=' ')
	print('')

print('等腰三角形拼装心形')
for i in range(10):
    for j in range(0, 10 - i):
        print(end=' ')
    for k in range(10 - i, 10):
        print('*', end=' ')
    for n in range(0, 0):
        print(end=' ')
    for m in range(0 + i, 10):
        print(' ', end=' ')
    for jj in range(10, 10):
        print(end=' ')
    for kk in range(10 - i, 10):
        print('*', end=' ')
    print('')
for i in range(20):
    for j in range(0, 0 + i):
        print(end=' ')
    for k in range(0 + i, 20):
        print('*', end=' ')
    print('')

print('打印正方形')
for i in range(10):
    for j in range(0, 10 - i):
        print(end=' ')
    for n in range(0, 0 + i):
        print(end=' ')
    for m in range(0 + i, 10):
        print('*', end=' ')
    for k in range(10 - i, 10):
        print('*', end=' ')
    print('')