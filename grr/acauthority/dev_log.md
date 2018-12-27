[26-12-2018]

Checking how deployment will be executed
There is a server
There is a client
and there is the assumed non running and non installed ???? keycloak server
Deploymeny should be automated through the grr interface

NOTE : Any empty entry as a group creation using the create_group api in the key cloak server will result
in completely obliterating the database of groups and rendering it useless, and then you would have to 
remove the entire keycloak installation and reinstall it.

TODO: get the location of the database server used by keycloak to be able to reinitialize it when you 
corrupt the entire db
