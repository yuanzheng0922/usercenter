# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import os
import sys
from webconfig import *

# 服务地址
HOST = '0.0.0.0'

# 服务端口
PORT = 6200

# 调试模式: True/False
# 生产环境必须为False
DEBUG = True

# 日志文件配置
LOGFILE = {'root':{'filename':'stdout', 'level':'DEBUG'}}

# 数据库配置
DATABASE = {
    'usercenter': {
        'engine':'pymysql',
        'db': 'usercenter',
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '654321',
        'charset': 'utf8',
        'conn': 10,
    },
}


SESSION = {
    'type':'SessionRedis', 
    'server':[{'addr':('127.0.0.1', 6379), 'timeout':1000}], 
    'expire':3600,
}
