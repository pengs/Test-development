#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 22:56
# @Author  : dapengchiji！！
# @FileName: code2.py


import unittest
import requests


host = 'https://jingleapp.uccc.cc'

#定义一个HomePage类，这个类继承于unittest下的TestCase
class HomePage(unittest.TestCase):

    def setUp(self):
        print('开始测试，在这里做环境初始化')
    # @classmethod
    def tearDown(self):
        print('测试结束，在这里做数据还原')

    def test_case_01(self):

        str_main = '/api/v2.3/customer/salescluesPool/tasks?limit=20&offset=0&type=2'
        # par = ''
        test_url = host + str_main
        header = {
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdWNjYy5jYyIsInRlbmFudElkIjo1MzY3LCJ1aWQiOjIwMDIzLCJleHAiOjM2ODQ4NTIxNzMsImlhdCI6MTUzNzM2ODUyNn0.6Bht27m7hRM21rvyDPxVefD8SWryWpoES2dSC_vta7I'}

        response = requests.get(test_url,params=header)
        result = response.text
        print (test_url)
        print ('case1_run')
        #这里使用assertIn方法断言，判断result中是否包含关键词centos7
        self.assertIn(' "templateId" : 409',result,msg='断言失败')

        '''
        以下是常用的一些断言方法
        1.assertEqual(self, first, second, msg=None)

        --判断两个参数相等：first == second

        2.assertNotEqual(self, first, second, msg=None)

        --判断两个参数不相等：first ！= second

        3.assertIn(self, member, container, msg=None)

        --判断是字符串是否包含：member in container

        4.assertNotIn(self, member, container, msg=None)

        --判断是字符串是否不包含：member not in container

        5.assertTrue(self, expr, msg=None)

        --判断是否为真：expr is True

        6.assertFalse(self, expr, msg=None)

        --判断是否为假：expr is False

        7.assertIsNone(self, obj, msg=None)

        --判断是否为None：obj is None

        8.assertIsNotNone(self, obj, msg=None)
        --判断是否不为None：obj is not None
        '''


if __name__ == '__main__':
    unittest.main()


