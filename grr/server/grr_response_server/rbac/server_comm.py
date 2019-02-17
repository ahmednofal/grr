from config import GRRSERVER
from acauthority.config import ACSERVER
from keycloak import KeycloakOpenID
import requests



# TODO: Figure out a way to better memory manage the
# huge number of ACServerCommunicator objects created for each message
# TODO: Make sure client ID is the same in GRR so that messages do not get
# confusing
class ACServerCommunicator:
    """Handles all communication with the ac server and
    keeps track of contest of the communication """

    def __init__(self, grr_client_id, hostname = None port = None):
        """
        This is just a function to connect to the ac server and the rest of the
        connection info will be stored as instance member
        """
        # Get configs from the config file
        # just to get the rest api far easier than encoding them
        # Choosing the client to connect to
        keycloak_openid = KeycloakOpenID(
            server_url=ACSERVER['server_url'],
            realm_name=ACSERVER['realm'],
            # Client id to connect to, we need it to access client roles in the
            # ac and to assume those roles
            grr_client_id,
            "") # client secret no need
        config_well_know = keycloak_openid.well_know()
        self.user_registered = False
        if not hostname:
            self.ac_hostname = ACSERVER['hostname']
        else:
            self.ac_hostname = hostname
        if not port:
            self.ac_port = ACSERVER['port']
        else:
            self.ac_port = port
        self.ac_bearer_token = ACSERVER['ac_bearer_token']
        if not self.user_registered:
            if self.register_keycloak_user():
                # registration successful
                self.user_registered = True
            else:
                self.user_registered = False

    def register_keycloak_user():
        # using requests and rest-api
        # bearer token is manual
        # TODO: Make it automated via installation automation
        requests.post()




    def authenticate_to_ac_server(self):
        if self.register_keycloak_user():
            pass
        # using the Admin-REST API to connect to keycloak server
        # object to the ACServerCommunicator
        # with the admin_rest api you do not need to be authenticated
        # self.token_obj
        pass

    def request_role_token(self, client_id, action_type):
        """
        requests a role token from the AC server (keycloak based)

        :flow_type: The flow type that is to be executed on the client
        side
        :server_resolve: The server host resolved into IP and port
        :returns: access token
        :raises: access denied error
        """
        self.authenticate_to_ac_server()
        self.token_obj.token(ACSERVER['username'], ACSERVER['password'])
        pass
