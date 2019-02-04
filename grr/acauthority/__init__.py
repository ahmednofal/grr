from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from tornado.web import RequestHandler

define('port', default=8888, help='port to listen on')

def main():
    """This is function that will startup the server and serve the
    http requests coming from clients and servers
    :returns: nothing

    """
    app = Application()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()

main()
