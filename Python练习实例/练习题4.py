#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 找到列表中第二大的数，可以使用多种方法解决

l=[1,23,33,22,45,9]

## 排好序找倒数第二个
#for i in range(len(l)):
#	for j in range(i):
#		if l[j] > l[i]:
#			l[i],l[j] = l[j],l[i]			
#print(l[-2])
#print(l[::-1][1])
#l.sort()
#print(l[-2])
# 找到最大，删除，再找最大

#max_num = max(l)
#l.remove(max_num)
#print(max(l))
	
# 遍历，声明2个变量，一个存最大，一个存第二大，再比较
max_n = l[0]
sen_n = l[0]

for i in l:
	if i >= max_n:
		sen_n = max_n
		max_n = i
print(sen_n)	



'''
编写一个计算器，开始提示选择运算符，输入1/2/3/4,之回车，继续输入要进行运算的两个数字
后回车，打印出运算结果


'''
		
			
#def parse(path):
# in_multi_comment = False # 多行注释符标识符号
# comments = 0
# blanks = 0
# codes = 0
# with open(path, encoding="utf-8") as f:
# for line in f.readlines():
#	line = line.strip()
#	# 多行注释中的空行当做注释处理
#	if line == "" and not in_multi_comment:
#	blanks += 1
#	# 注释有4种
#	# 1. # 井号开头的单行注释
#	# 2. 多行注释符在同一行的情况
#	# 3. 多行注释符之间的行
#	elif line.startswith("#") or \
#		(line.startswith('"""') and line.endswith('"""') and len(line)) > 3 or \
#	 (line.startswith("'''") and line.endswith("'''") and len(line) > 3) or \
#	 (in_multi_comment and not (line.startswith('"""') or line.startswith("'''"))):
#	comments += 1
#	# 4. 多行注释符的开始行和结束行
#	elif line.startswith('"""') or line.startswith("'''"):
#	in_multi_comment = not in_multi_comment
#	comments += 1
#	else:
#	codes += 1
# return {"comments": comments, "blanks": blanks, "codes": codes}
#if __name__ == '__main__':
# print(parse("xxx.py"))		