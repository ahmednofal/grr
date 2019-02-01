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


# abstractions
# keycloak clients are apps generally but they are the server analysts
# Just to assign to each of them a role
# Then a user account is managed by the client with the available role

# The server analyst will be the client trying to access the users with certain roles
# The roles will be just a database of tags, the tags will be analyzed using the controller
# TODO: Check what would happend when there are non conventional roles, where to check the roles actions
# TODO: adopt the grr terminology when dealing with clients in keycloak and refer to them as analysts
# TODO: Figure out a way to be able to keep the connection open with the underlying keycloak server
# TODO: Problem, the current client : analyst abstraction does not offer a relationship to the user
# TODO: might be it a good idea to switch for client to actually be the client machine and the user would be the server
# analyst, but then still we donot have an association between each client and each user and the roles assumed
# TODO: we can always go back to groups being the client machines in which users are existant and can assume roles
# TODO: Might it not be a good idea to keep track of the machines and just keep track of the server analysts ids


# Flow
# client -> action -> acauth -> databases -> client role -> approve/deny role ->

import keycloak
import requests
class ACAuthority:
    # Needed because the server apparently kicks us out every few ms
    def auth(self):
        self.adminobj = keycloak.keycloak_admin.KeycloakAdmin("http://localhost:8080/auth/", self.admin_user_name, self.admin_password)

    # This should be remove in favor of an initialization and installation script
    def __init__(self):
        # AC Authority initialization
        # It should firstly get access to the admin account of keycloak
        self.admin_user_name = "admin"
        self.admin_password = "9437618525"
        # self.adminobj = keycloak.keycloak_admin.KeycloakAdmin("http://localhost:8080/auth/", self.admin_user_name, self.admin_password)
        self.auth()

    def request_action(self,request):
        self.auth()
        return request.action

    def request_analyst(self, request):
        self.auth()
        return request.analyst

    def request_client_machine(self, request):
        self.auth()
        return request.request_machine

    def lookup_role(self, request):
        self.auth()
        analyst = self.request_analyst(request)
        return self.adminobj.get_client_roles(analyst)

    def lookup_action(self, request):
        self.auth()
        action = self.request_action(request)

    def identity_as_db_entry(self,identity):
        self.auth()

    def get_identity(self, request):
        self.auth()
        current_users = self.adminobj.get_users()
        db_entry = self.identity_as_db_entry(self.request)

    def facilitate_roles(self, request):
        self.auth()
        identity = self.get_identity(request);

    # DEPRECATED or is it ?
    def identity_roles(self,server_IP):
        self.auth()
        realm_groups = self.adminobj.get_groups()
        # The single group is a client in our definition and the users in the group are the server analysts
        # subscribed to roles to be used analyzing the client machine

        for group in realm_groups:
            pass
        pass





