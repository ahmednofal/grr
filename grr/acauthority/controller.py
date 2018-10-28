# This is the controller
# It is supposed to govern all interactions between the acauthority and client, and the acauthority and
# server


# Activity Diagram Flow

# Server sends acauthority a request for an access token for certain number of named resources
# on the
# client machine

# The acauthority uses the keycloak in the backend to verify the role of the server user and the
# access granted
# Access classes and roles will be heirarchical, meaning they will start out at the easiest
# config and then go down with more complexity and freedom of choice
# Assumed : Identity has been received

# Returns roles of the identity using the KeyCloak api
# args : identity is a certificate signed by a CA
import keycloak

class Token:
    pass

class ACAuthority:

    def receive_token_request(token_req):
        pass

    def identity_roles(server_IP):
        pass

    # cross checks the access requested with the supplied token
    def access_token_valid(token, access):
        pass

    # Send token to server
    def send_token(token):
        pass

    # returns created token
    def create_token():
        pass

    # Change the
    def invalidate_token(token):
        pass

    # Change the timestamp
    def refresh_token(token):
        pass
