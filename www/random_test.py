#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 10:47
# @Author  : dapengchiji！！
# @FileName: random_test.py

'''随机生成手机号码，写入到Excel'''

import random
def createPhone():

  # list=["123","133","134","135","136","137","138","139","147","176","130","131",
  #       "150","151","152","153","155","156","157","158","159","186","187","188"]
  ls=["123",'121','120']
  str='0123456789'  #0-9随机取

  try:
      with open("/Users/macbook/Desktop/120number.xls", "w") as f:#生成需要的文本格式
        for i in range(300):#循环生成
         number=(random.choice(ls)+"".join(random.choice(str) for i in range(8))+"\n")
         #random.choice() 从序列中随机选取一个元素;--将号段+随机数拼接起来；换行显示
         f.write(number)#写入到文件中
  except IOError:
      print("Error:数据生成失败")
  else:
      print("啦啦啦----数据生成成功")
      f.close()

if __name__=="__main__":
    createPhone()
