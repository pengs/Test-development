#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 21:51
# @Author  : dapeng！！
# @FileName: huatian.py
#


import requests
import json

# url='https://love.163.com/api/relation/followersByCursor'# 喜欢人
url ='https://love.163.com/api/visitor/latestvisitor' # 谁访问
# url='https://love.163.com/api/messages/noticeByCursor' # 消息中心
# url='https://love.163.com/open/api/recommend/v1/encounter/list'
# url ='https://love.163.com/api/praise'
header = {'Content-Type':'application/json'
    ,'Authorization':'OAuth2 25d403b175dc568e22c6a4d8e4b123d3'}
data ={}
re=requests.post(url,headers=header,params=data)
if re.status_code==200:
    print('接口是正确')
else:
    print("接通不通")
result=re.json()
r=re.text
print(json.dumps(result,indent=4,ensure_ascii=False))






