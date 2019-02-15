from config import ACSERVER, GRRSERVER


class ACServerCommunicator:
    """Handles all communication with the ac server and
    keeps track of contest of the communication """

    def __init__(self, hostname = None port = None)
        """
        This is just a function to connect to the ac server and the rest of the
        connection info will be stored as instance member
        """
        # Get configs from the config file
        self.user_registered = False
        if not hostname:
            self.ac_hostname = ACSERVER['hostname']
        if not port
            self.port = ACSERVER['port']

        self.ac_hostname = hostname
        self.port = port
        pass

    def register_keycloak_user(self):
        self.ac_hostname = ACSERVER['hostname']
        self.ac_port = ACSERVER['port']
        pass

    def request_role_token(flow_type, server_resolve):
        """
        requests a role token from the AC server (keycloak based)

        :flow_type: The flow type that is to be executed on the client
        side
        :server_resolve: The server host resolved into IP and port
        :returns: access token
        :raises: access denied error
        """

        self.connect_to_ac_server()
        if not self.user_registered:
            self.register_keycloak_user()
        pass
