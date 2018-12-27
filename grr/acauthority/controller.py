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

class Token:
    pass

class ACAuthority:

    def __init__(self):
        # AC Authority initialization
        # It should firstly get access to the admin account of keycloak

        self.admin_user_name = "admin"
        self.admin_password = "9437618525"
        self.adminobj = keycloak.keycloak_admin.KeycloakAdmin("http://localhost:8080/auth/", self.admin_user_name, self.admin_password)

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


# KEYCLOAK OPENID

from keycloak import KeycloakOpenID as KeyCloak

# Configure client
keycloak = KeyCloak(server_url="http://localhost:8080/auth/",
                    client_id="example_client",
                    realm_name="example_realm",
                    client_secret_key="secret")

# Get WellKnow
config_well_know = keycloak.well_know()

# Get Token
token = keycloak.token("user", "password")

# Get Userinfo
userinfo = keycloak.userinfo(token['access_token'])

# Refresh token
token = keycloak.refresh_token(token['refresh_token'])

# Logout
keycloak.logout(token['refresh_token'])

# Get Certs
certs = keycloak.certs()

# Get RPT (Entitlement)
token = keycloak.token("user", "password")
rpt = keycloak.entitlement(token['access_token'], "resource_id")

# Instropect RPT
token_rpt_info = keycloak.introspect(keycloak.introspect(token['access_token'], rpt=rpt['rpt'],
                                     token_type_hint="requesting_party_token"))

# Introspect Token
token_info = keycloak.introspect(token['access_token'])

# Decode Token
KEYCLOAK_PUBLIC_KEY = "secret"
options = {"verify_signature": True, "verify_aud": True, "exp": True}
token_info = keycloak.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)

# Get permissions by token
token = keycloak.token("user", "password")
keycloak.load_authorization_config("example-authz-config.json")
policies = keycloak.get_policies(token['access_token'], method_token_info='decode', key=KEYCLOAK_PUBLIC_KEY)
permissions = keycloak.get_permissions(token['access_token'], method_token_info='introspect')

# KEYCLOAK ADMIN

from keycloak import KeycloakAdmin

keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                               username='example-admin',
                               password='secret',
                               realm_name="example_realm",
                               verify=True)

# Add user
new_user = keycloak_admin.create_user({"email": "example@example.com",
                    "username": "example@example.com",
                    "enabled": True,
                    "firstName": "Example",
                    "lastName": "Example",
                    "realmRoles": ["user_default", ],
                    "attributes": {"example": "1,2,3,3,"}})


# Add user and set password
new_user = keycloak_admin.create_user({"email": "example@example.com",
                    "username": "example@example.com",
                    "enabled": True,
                    "firstName": "Example",
                    "lastName": "Example",
                    "credentials": [{"value": "secret","type": "password",}],
                    "realmRoles": ["user_default", ],
                    "attributes": {"example": "1,2,3,3,"}})

# User counter
count_users = keycloak_admin.users_count()

# Get users Returns a list of users, filtered according to query parameters
users = keycloak_admin.get_users({})

# Get user ID from name
user_id_keycloak = keycloak_admin.get_user_id("example@example.com")

# Get User
user = keycloak_admin.get_user("user_id_keycloak")

# Update User
response = keycloak_admin.update_user(user_id="user_id_keycloak",
                                      payload={'firstName': 'Example Update'})

# Update User Password
response = set_user_password(user_id="user_id_keycloak", password="secret", temporary=True)

# Delete User
response = keycloak_admin.delete_user(user_id="user_id_keycloak")

# Get consents granted by the user
consents = keycloak_admin.consents_user(user_id="user_id_keycloak")

# Send User Action
response = keycloak_admin.send_update_account(user_id="user_id_keycloak",
                                              payload=json.dumps(['UPDATE_PASSWORD']))

# Send Verify Email
response = keycloak_admin.send_verify_email(user_id="user_id_keycloak")

# Get sessions associated with the user
sessions = keycloak_admin.get_sessions(user_id="user_id_keycloak")

# Get themes, social providers, auth providers, and event listeners available on this server
server_info = keycloak_admin.get_server_info()

# Get clients belonging to the realm Returns a list of clients belonging to the realm
clients = keycloak_admin.get_clients()

# Get client - id (not client-id) from client by name
client_id=keycloak_admin.get_client_id("my-client")

# Get representation of the client - id of client (not client-id)
client = keycloak_admin.get_client(client_id="client_id")

# Get all roles for the realm or client
realm_roles = keycloak_admin.get_realm_roles()

# Get all roles for the client
client_roles = keycloak_admin.get_client_roles(client_id="client_id")

# Get client role
role = keycloak_admin.get_client_role(client_id="client_id", role_name="role_name")

# Warning: Deprecated
# Get client role id from name
role_id = keycloak_admin.get_client_role_id(client_id="client_id", role_name="test")

# Create client role
keycloak_admin.create_client_role(client_id, "test")

# Assign client role to user. Note that BOTH role_name and role_id appear to be required.
keycloak_admin.assign_client_role(client_id="client_id", user_id="user_id", role_id="role_id", role_name="test")

# Create new group
group = keycloak_admin.create_group(name="Example Group")

# Get all groups
groups = keycloak_admin.get_groups()

# Get group
group = keycloak_admin.get_group(group_id='group_id')

# Get group by name
group = keycloak_admin.get_group_by_name(name_or_path='group_id', search_in_subgroups=True)

# Function to trigger user sync from provider
sync_users(storage_id="storage_di", action="action")
