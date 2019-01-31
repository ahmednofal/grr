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


# New Architecture
#  The acauthority is inlined
# Which means it acts as the server in the past architecture
# We need to check the role
# And the action(s) acquired by that role and if the action required is included in the actions acquired
# No more tokens

# The deployment Implementation of the acauthority will not follow the same as the server
# To be examined is the server-client communication because it should be cloned for the server-ac-client
# Architecture
# import keycloak
# x = KeyCloak.client
# keycloak.KeycloakAdmin.create_client(x)


import keycloak

class Token:
    pass

class ACAuthority:
    def __init__(self):
        # AC Authority initialization
        # It should firstly get access to the admin account of keycloak

        self.admin_user_name = "admin"
        self.admin_password = "9437618525"
        # self.adminobj = keycloak.keycloak_admin.KeycloakAdmin("http://localhost:8080/auth/", self.admin_user_name, self.admin_password)
        self.adminobj = keycloak.keycloak_admin.KeycloakAdmin("http://localhost:8080/auth/", self.admin_user_name, self.admin_password)
        pass
    def get_identity(self, request):
        self.adminobj.get_client(request.identity)

    def facilitate_roles(self, request):
        identity = self.get_identity(request);
    def identity_roles(server_IP):
        pass

    # cross checks the access requested with the supplied token
    def access_token_valid(token, access):
        pass


