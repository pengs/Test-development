#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 07:44
# @Author  : dapengchiji！！
# @FileName: config.py

'''
我们需要创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。
使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。
'''
import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time,async,aiomysql


@asyncio.coroutine
def create_pool(loop,**kw)
    logging.info('create database connection pool......')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs