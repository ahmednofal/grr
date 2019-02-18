# This is the incoming action handler it will receive all the action requests from the servers
# And delegate them to the controller for the roles to be specified and then matched against
# The existing database entries
# This is merely a requests handler thread just to queue all requests and preprocess them in a manner
# such that the main controller does not get bothered by requests and just carry out the access control part
# on its own

# Signature
# listen_for_request
# check_valid_req
#

class IncomingActionHandler:
    def __init__(self):
        # this is supposed to initialize all possible internal data needed for communication
        pass
    def listen(self, port):

