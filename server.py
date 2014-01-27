#coding:utf-8

import tornado.ioloop
import sys

from application import application

port="8888"

if __name__=="__main__":
    if len(sys.argv) > 1:
        port=sys.argv[1]

    application.listen(port)
    print 'Development server is running at http://127.0.0.1:%s/' % port
    print 'Quit the server with Control-C'

    tornado.ioloop.IOLoop.instance().start()
