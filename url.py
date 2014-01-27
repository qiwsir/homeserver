#coding:utf-8

from handler.index import MainHandler
from handler.index2 import MainHandler2

url=[
    (r'/',MainHandler),
    (r'/2',MainHandler2),
    ]
