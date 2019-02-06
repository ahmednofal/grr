# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from tornado.options import define, options
# from tornado.web import Application
# from tornado.web import RequestHandler
from controller import ACAuthority
from config import KEYCLOAK_CONFIG, RPCSERVER_CONFIG
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher



# TODO: This should not include the registration functionality otherwise it is not an ac, ie exclude the
# keycloak functions that can register clients

# TODO: Even if we protect against deletion and creation of clients, other clients can modify other clients roles
# if any client is allowed access to the rpc

# TODO: There is no way in python-keycloak or python-keycloak-client to actually let the client
# create roles for itself without the admin privileges, through opendid-connect

# TODO: I give up, I am using the admin-api and exposing everything, after that we will try and restrict
# the access of client roles to each client on its own and currently we will settle for the exclusion of some
# client removal and addition functionality from the client and server side

# TODO: Also be aware that the application function running the rpc server must have a reauth function just as
# the acauthority, because keycloak times out on us

# TODO: Document that to access any admin functionality you have to call keycloakadmin.method_name

acauthority_object = ACAuthority()
def register_functions_in_jsonrpc():
    """This function will register the entire keycloak api in the rpc pool (the list of all the methods call
    able from rpc)
    :returns: nothing for the time being

    """
    dispatcher.add_object(acauthority_object.adminobj) # TODO: bad , restrict
    # TODO: Restrict Access to admin_obj api that can modify clients and users to clients in keycloak
    # TODO: Restiction will be in the image of whitelist/exposing certain api rather than blacklisting some

# @Request.application
def application(request):
    acauthority_object.auth_keycloak_admin()
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

application = Request.application(application)

def main():
    """This is function that will startup the server and serve the
    http requests coming from clients and servers
    :returns: nothing

    """
    register_functions_in_jsonrpc()
    run_simple( \
                RPCSERVER_CONFIG['hostname'],\
                RPCSERVER_CONFIG['port'],\
                application)

main()
