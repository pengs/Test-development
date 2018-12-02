#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 18:14
# @Author  : dapeng！！
# @FileName: parse.py

import re
from pprint import pprint

with open('/Users/macbook/Test-development/Learn_code/stations.html', 'r') as f:
     text = f.read()
     stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
     pprint(dict(stations),indent=4)