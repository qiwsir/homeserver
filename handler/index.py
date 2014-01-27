#coding:utf-8

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.write("hello")
