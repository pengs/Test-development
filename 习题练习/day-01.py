#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 23:29
# @Author  : dapengchiji！！
# @FileName: day-01.py
'''
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，
然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

把@asyncio.coroutine替换为async；
把yield from替换为await。
'''

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time,async
from  aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Hello Webapp!</h1>')

# @asyncio.coroutine
async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    # srv=yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 1234)
    logging.info('server started at http://127.0.0.1:1234...')
    return  srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

