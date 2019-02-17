KEYCLOAK_CONFIG = {
    'admin_user_name' : 'admin',
    'admin_password' : '9437618525',
    'admin_auth_endpoint' : 'http://localhost:8080/auth/',
    'keycloak_server_port': '8080',
}

RPCSERVER_CONFIG = {
    'hostname' : 'localhost',
    'port' : '4000'
}

ACSERVER_protocol = "http://"
ACSERVER_hostname = "localhost"
ACSERVER_port = '8090'
ACSERVER =
{
    'hostname' :ACSERVER_hostname,
    'port': ACSERVER_port,
    'server_url':ACSERVER_protocol+ACSERVER_hostname+':'+ACSERVER_port+'/auth/'
    'realm':'grr'
    'public_key':''
    'encryption_algorithm':''
}
