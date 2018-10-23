#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import requests
import json

class Jingle_login(unittest.TestCase):  # 定义一个类
    '''登录接口'''

    def setUp(self):  # 初始化
        self.post_url = 'https://uccc.bckefu.com'
        print("开始执行...")


    def tearDown(self):  # 与setUp()相对
        print("执行完毕")


    def test_login(self):
        '''测试登录'''

        self.post_headers = {"Content-Type":"application/x-www-form-urlencoded"}
        self.post_data = { "account": "MjAwMTA0MTAwMToyMDAxMDQxMDAx" }
        r = requests.post(self.post_url+'/api/v1.1/security/users/login',params=self.post_data,headers=self.post_headers)
        self.result=r.json()
        if r.status_code==200:
        # 断言 判断返回值是否符合预期一致
            self.assertEqual(self.result['code'],0)
            self.assertNotEqual(self.result['code'],500)
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.result['data']['username'],"2001041001")
        else:
            print(" 接口无法执行 ")
            

        # print(res)

        
    # def test_my_customer(self):



if __name__ == '__main__':
    unittest.main()





