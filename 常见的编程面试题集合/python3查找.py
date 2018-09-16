#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''字典排序'''

from collections import OrderedDict
import json

d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4
d['apple']=5
#
# for key in d:
#     print(key,d[key])

print(json.dumps(d) )
