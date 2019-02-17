import grpc
import time
import hashlib
import acservice_pb2
import acservice_pb2_grpc
from concurrent import futures
from config import RPCSERVER_CONFIG
from controller import ACAuthority

class ACServiceServicor(
        acservice_pb2_grpc.ACServiceServicor):
    """
    gRPC servicor for the acservice gRPC calls
    """
    def __init__(self, *args, **kwargs):
        self.server_port = \
            RPCSERVER_CONFIG['port']

        self.hostname = \
            RPCSERVER_CONFIG['hostname']

        self.acauthority_object = ACAuthority()

    def register_client(self,
                        request,
                        context):
        # we will need to check that bearer token if it exists
        # with the api of the python-keycloak
        # you always need to reauth the ac
        # request.ac_bearer_token
        try:
            self.acauthority_object.
            adminobj.create_client(payload={'clientId':request.client_id})
            return ACServerResponse.OK
        except:
            return ACServerResponse.FAILED
    def authenticate_client(self,
                            request,
                            context):
        # request.bearer_toke
        pass
    def add_role(self,
                 request,
                 context):
        self.authenticate_client(request, context)
        self.acauthority_object.adminobj.
        pass
    def delete_role(self,
                    request,
                    context):
        pass
    def modify_role(self,
                    request,
                    context):
        pass
