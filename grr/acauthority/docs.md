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

# res start

flags.DEFINE_bool("install", False, "Specify this to install the client.")

flags.DEFINE_bool(
    "break_on_start", False,
    "If True break into a pdb shell immediately on startup. This"
    " can be used for debugging the client manually.")

in

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/client/grr_response_client/grr_fs_client.py

# res done

# res start
Check

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

"""
also for the ac authority we can use the function

  flow_args.Validate()

  when we try to validate the flows and roles used by the client to create roles in the client side

in

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flow.py
# res end

# res start
▼ GRRClientWorker : class
   +ChargeBytesToSession : function
   +Drain : function
   +HandleMessage : function

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/client/grr_response_client/comms.py
# res end

# res start
For the server entry point


The entry point is
  def CallFlow(self,
               flow_name=None,
               next_state=None,
               request_data=None,
               client_id=None,
               base_session_id=None,
               **kwargs):
    """Creates a new flow and send its responses to a state.

    This creates a new flow. The flow may send back many responses which will be

    also
    client_messages instance member data in flow_base file classes
"""
    also
  def CallState(self, next_state="", start_time=None):
    """This method is used to schedule a new state on a different worker.

    This is basically the same as CallFlow() except we are calling
    ourselves. The state will be invoked at a later time.

    Args:
       next_state: The state in this flow to be invoked.
       start_time: Start the flow at this time. This delays notification for
         flow processing into the future. Note that the flow may still be
         processed earlier if there are client responses waiting.

    Raises:
       FlowRunnerError: if the next state is not valid.
    """

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flow_base.py

also
FlowRunner like FlowBase can CallClient CallFlow CallState and
CallStateInLine

# res end

# res start 
    self.QueueResponse(msg, start_time)

    # Notify the worker about it.
    self.QueueNotification(session_id=self.session_id, timestamp=start_time)



4. The child flow calls CallClient() which schedules some messages for the client. Since its runner has a parent runner, the messages are queued on the
   parent runner's message queues.

also
FlowRunner like FlowBase can CallClient CallFlow CallState and
CallStateInLine

  def _QueueRequest(self, request, timestamp=None):
    if request.HasField("request") and request.request.name:
      # This message contains a client request as well.
      self.queue_manager.QueueClientMessage(
          request.request, timestamp=timestamp)

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flow_runner.py

# res end






# res start
  def Start(self):

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flows/general/webhistory.py


# res end




Confusing stuffffff


# res start

▶ imports

▼ PoolGRRClient : class
   +Run : function

   +Stop : function

   +__init__ : function

   +run : function


 +CheckLocation : function

 +CreateClientPool : function

 +main : function

 edited

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/client/grr_response_client/poolclient.py

# res end



# Information extracted from looking at the code


1.
"""
FlowBase and FlowRunner have the exact same functions almost,we need to check
which of the them is the entry point to the server,
and inject the ac code in it
TODO: check which to use between FLowRunner and FlowBase
"""

2.
"""
almost all flows have a Start() method that calls CallFlow() method
"""

"""
grr_api_client folder has flow.py which contains FlowBase class
"""

"""
The cronjob flow get executed using the Start() method and the
cron job gets executed using the Run method
"""

"""
grr_api_client is the entry point for the flow definition engine
particularly the flow.py file
"""
# Good paths to consider in general for server


/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/worker_lib.py

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/bin/worker.py

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/server_startup.py

/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flows/general/webhistory.py


# Good paths to consider in general for the client


/home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/api_client/python/grr_api_client/flow.py
