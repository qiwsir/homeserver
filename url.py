#coding:utf-8

from handler.index import MainHandler
from handler.index import LoginHandler

url=[
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    ]
