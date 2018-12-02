#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 18:07
# @Author  : dapeng！！
# @FileName: tickets.py


"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达cd

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""
import requests
from  docopt import  docopt
from stations import stations
from prettytable import PrettyTable
def cli():

    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    data = arguments['<date>']

    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-11-01&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'

    r = requests.get(url,verify=False) # 添加verify=False参数, 不验证证书
    print(r.json())
    r = requests.get(url)
    rows = r.json()['data']['result']
    headers = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)
    for row in rows:
       pt.add_row(row)
    print(pt)





if __name__=='__main__':
    cli()

