# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from tornado.options import define, options
# from tornado.web import Application
# from tornado.web import RequestHandler

define('port', default=8888, help='port to listen on')

# TODO: May be this should be moved into a different class, something in __init__.py, still needed

# TODO: This should not include the registration functionality otherwise it is not an ac, ie exclude the
# keycloak functions that can register clients
def register_functions_in_jsonrpc(self):
    """This function will register the entire keycloak api in the rpc pool (the list of all the methods call
    able from rpc)
    :returns: nothing for the time being

    """
    # keycloak_admin_methods = inspect.getmembers(self.adminobj, predicate=inspect.ismethod) # list
    # for amethod in keycloak_admin_methods:
    #     amethod[1] = dispatcher.add_method(amethod[1])
    # pass
    running_dispatcher = dispatcher.Dispatcher()
    running_dispatcher.add_object(acauthority_object)


def main():
    """This is function that will startup the server and serve the
    http requests coming from clients and servers
    :returns: nothing

    """
    # app = Application()
    # http_server = HTTPServer(app)
    # http_server.listen(options.port)
    # IOLoop.current().start()

main()
