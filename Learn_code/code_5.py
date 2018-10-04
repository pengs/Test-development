#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 16:59
# @Author  : dapengchiji！！
# @FileName: code5.py

'''
（1）查找系统所有盘符，
（2）所有盘符查找.png的文件
（3）获取这些文件的MD5的值 保存一个文件中
'''

import os
import hashlib

# filter1=[".mpg"]

def all_path(dirname):
    result=[]
    for maindir,subdir,filenames in os.walk(dirname): # 遍历所有目录查找
        for filename in filenames:
            apath =os.path.join(maindir,filename)
            ext=os.path.splitext(apath)[1]

            if ext in filter1:
                result.append(apath)
    return result

# def md5sum(fname):
#     fd=open(fname,"r")
#     fcont=fd.read()
#     fd.close()
#     fmd51=hashlib.md5(fcont)
#     with open("123.txt", "w") as f2:
#         for i in allfiles:
#             fname = os.path.basename(i)
#             md5 = fmd51
#             f2.write('{}\n'.format(len(allfiles)))
#             f2.write(md5 + "  " + fname + "" + "\n")
#
#
# if __name__=='__main__':
#     dirs = "/Users/macbook/awesome"
#     allfiles = []
#     for i in dirs:
#         volumn_name = i + ":"
#         if os.path.exists(volumn_name):
#             local_files = all_path(volumn_name)
#             allfiles += local_files

# import os
# def all_path(dirname):
#     filelistlog = dirname + "/filelistlog.txt"  # 保存文件路径
#     postfix = set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式
#     for maindir, subdir, file_name_list in os.walk(dirname):
#         for filename in file_name_list:
#             apath = os.path.join(maindir, filename)
#             # if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
#             if apath.split('.')[-1] in postfix:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
#                 try:
#                     with open(filelistlog, 'a+') as fo:
#                         fo.writelines(apath)
#                         fo.write('\n')
#                 except:
#                     pass    # 所以异常全部忽略即可
#
#
# if __name__ == '__main__':
#     dirpath = "/Users/macbook/awesome"  # 指定根目录
#     all_path(dirpath)

