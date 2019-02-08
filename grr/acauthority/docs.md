THIS IS NOT UPDATED
===================
INFORMATION IS WRONG
====================
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


in 

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/client/grr_response_client/grr_fs_client.py


flags.DEFINE_bool("install", False, "Specify this to install the client.")

flags.DEFINE_bool(
    "break_on_start", False,
    "If True break into a pdb shell immediately on startup. This"
    " can be used for debugging the client manually.")



Check /home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/worker_lib.py


Check 
/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/bin/worker.py

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/server_startup.py


/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flow.py
def StartFlow(client_id=None,
              cpu_limit=None,
              creator=None,
              flow_args=None,
              flow_cls=None,
              network_bytes_limit=None,
              original_flow=None,
              output_plugins=None,
              start_at=None,
              parent_flow_obj=None,
              parent_hunt_id=None,
              **kwargs):
  """The main factory function for creating and executing a new flow.

  Args:
    client_id: ID of the client this flow should run on.


also for the ac authority we can use the function

  flow_args.Validate()

  when we try to validate the flows and roles used by the client to create roles in the client side

  check 

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flows/general/webhistory.py




def StartFlow(client_id=None,
              cpu_limit=None,
              creator=None,
              flow_args=None,
              flow_cls=None,
              network_bytes_limit=None,
              original_flow=None,
              output_plugins=None,
              start_at=None,
              parent_flow_obj=None,
              parent_hunt_id=None,
              **kwargs):

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flow.py


very promising

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/client/grr_response_client/comms.py
▼ GRRClientWorker : class
   +ChargeBytesToSession : function
   +Drain : function
   +HandleMessage : function



