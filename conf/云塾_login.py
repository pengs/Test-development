#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import unittest
import json

class  testlogin(unittest.TestCase):
	
	def test_login(self):
		url = "http://meeting.docbook.com.cn/api/app/v2/profile/login"
		headers={'Content-Type': 'application/json'}
		data={"version": "2.6.8",
			"version_type": 1,
			"platform": 10,
			"sign": "35e47e0ea27cde10d273d966e6c9af66",
			"timestamp": 1540471114,
			"imei": "C00CAC7F-0A05-473C-ABC3-B1E405E819CE",
			"username": "17610420804",
			"password": "peng725033"
		}
		r = requests.post(url,headers=headers,data=data)
#		checkpoint='userid'
#		if r.status_code==200:
#			if checkpoint in r.text:
#				print('测试结果:Passed,断言成功。响应状态码:{}。响应数据【json】:{}'.format(r.status_code,r.text))
#			else:
#				print('测试结果:Failed,断言失败。响应状态码:{}。断言内容为：{}。响应数据【json】:{}'.format(r.status_code,checkpoint,r.text))
#		else:
#			print('测试结果:Failed,接口不通。响应状态码:{}。响应数据【json】:{}'.format(r.status_code,r.text))
		print(r.json())
#		
		def get_cookies(self):
			cookies= getSession()
			return cookies
			

if __name__=='__main__':
	unittest.main()