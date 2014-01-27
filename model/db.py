#!/usr/bin/evn python
#coding:utf-8

import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='123123', db='jiazhengfuwu',charset='utf8')

cur = con.cursor()
