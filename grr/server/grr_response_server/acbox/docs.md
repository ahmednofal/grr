Access Control Box
==============================

According to the proposed architecture ACBOX (Access Control Box) will be an intermediatry 
between the client and the server and delegates access control tokens from the server to the
client




It can be deployed as part of the client, server or neither of them and as a separate party

Philosophy
==========

The entire idea behind delegation is to keep the client as thin as possible, no resources to 
be spent on gathering files

Access Control Lists can be pretty heavy on disk usage, so as the methods and runtime over head
of checking and updating them

Requests Type
=============

The server sends a request to the acbox, the acbox will check the identity (certificate)
of the server and checks the access control list available

Access Control List
===================

The acbox has an ACL of the roles of the users on certain servers which the client approves of
So the access control list is kept at the acbox NOT in the client side, simply the acts are 
approved based on the tokens. The server sends the client the request, the requests is
forwarded to the acbox and checked for the identity of the server and the client and then the 
role in the acl


The api exists either thr


The token datastructure
=======================

Looking into current implementations of tokens, might have to serialize and deserialize 
internally 
