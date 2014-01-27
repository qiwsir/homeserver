#coding:utf-8

import tornado.web

class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        self.render("index2.html")
