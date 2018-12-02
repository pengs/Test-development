#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests
import unittest
import json
from pubulic_way.get_token import getSession
 
class testlogin(unittest.TestCase):
 
	def test_getIdentify(self):
		'''调用test_listCollectInfoByCreditId(self)响应数据中的taxid参数'''
		result = self.get_listCollectInfoByCreditId()
		json_result=json.loads(result)
		p1 = json_result["polygons"][0]["ENTERPRISETAXID"]
		data = {"lyname":"COL_WPOLYGON_3206","id":"8f34969c-ea5e-489c-94bc-37e54ad40660","taxid":p1}
		url = "http://10.17.17.31:8080/LandTaxSys/search/getLayerAlianame"
		headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		cookies = self.get_cookies()
		r = requests.post(url,data=data,headers=headers,cookies=cookies)
		# print(p1)
		# print(r.status_code)
		# print(r.text)
		# return r.text
		checkpoint = '91320612MA1UYCL59U'
		if r.status_code == 200:
			if checkpoint in r.text:
				print('测试结果:Passed,断言成功。响应状态码:{}。响应数据【json】:{}'.format(r.status_code,r.text))
			else:
				print('测试结果:Failed,断言失败。响应状态码:{}。断言内容为：{}。响应数据【json】:{}'.format(r.status_code,checkpoint,r.text))
		else:
			print('测试结果:Failed,接口不通。响应状态码:{}。响应数据【json】:{}'.format(r.status_code,r.text))
 
	def get_listCollectInfoByCreditId(self):
		'''获取响应数据中的taxid参数'''
		url = "http://10.17.17.31:8080/LandTaxSys/dataEdit/listCollectInfoByCreditId"
		data = {"start":"1","end":"8","targetTaxId":"91320612MA1UYCL59U","nearbyTaxId":"","swjgDm":"23206","userId":"32060100033"}
		headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		cookies = self.get_cookies()
		r = requests.post(url,data=data,headers=headers,cookies=cookies)
		return r.text
 
	def get_cookies(self):
		cookies = getSession()
		return cookies

if __name__ == '__main__':
	unittest.main()

