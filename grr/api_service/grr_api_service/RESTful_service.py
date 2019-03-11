from flask import Flask
from grr_api_client import api
from grr_api_client import api_shell_lib
from grr_api_service import config

# supply grpc service for apps to connect to and send requests here
# requests are
# The slash command needs to connect to web services, this is shell based
# so what we need to do is to provide REST API for it
#
# using the --exec-command we will be able to execute commands
# what is left is to be able to actually get the flow execution
# command
# DONE
# Use the hunt with a single client ID in the huntrunnerargs
# REST API design

# POST Flow
# Fields :
    # Client ID
    # Flow name
    # Execution time
    # Output redirection (Optional)
# POST Hunt

grr_REST_api = Flask(__name__)

# run a flow on a client
# using client representation and flow name

def connect_to_grr_server(auth):
    """ This function connect_to_grr_server : connects to grr_server
    using the grr_client_api to return an object that can be used to
    issue grr commands like flows and hunts on the clients and
    retrieve output information from the flow
    :raises: failure_to_connect error
    :returns: a grr_api object
    """
    # TODO(ahmednofal): change the config to point to the default config
    # in grr instead of your custom one

  return api.InitHttp(
      api_endpoint=config.api_endpoint,
      page_size=config.page_size,
      auth=auth,
      verify=False) # TODO(ahmednofal): change to something dynamic


# TODO(ahmednofal): change flow_obj to flow_name mayb
# auth comes from the service connecting to the plugin
# most probably will have to be swapped out for managed
# tokens
@grr_REST_api.route('/grr_server/api/v1.0/clients/', methods=['GET'])
def get_flows(auth, client_id):
    pass
@grr_REST_api.route('/grr_server/api/v1.0/flows/', methods=['GET'])
def get_flow(auth, flow_id, client_id):
    pass
@grr_REST_api.route('/grr_server/api/v1.0/flow/', methods=['POST'])
def execute_flow(auth, flow_obj, client_id):
    grrapi = connect_to_grr_server(auth)
    # flags.exec_code is just the conde to be executed
    # it has to include in it "grrapi" object to be able
    # to access the current context of GRR
    if flow_obj.args:
        grrapi.Client().CreateFlow(flow_obj.name, flow_obj.runner_args)
    else:
        grrapi.Client().CreateFlow(flow_obj.name)
    pass


# grrapi.CreateHunt(flow_name=None, flow_args=None, hunt_runner_args=None)
# # Modift from here
# flow_args = grrapi.types.CreateFlowArgs("FileFinder")
# # FileFinderArgs.paths gets initialized with an example value,
# # we should get rid of it.
# flow_args.ClearField("paths")
# flow_args.paths.append("/var/log/*")
# flow_args.action.action_type = flow_args.action.DOWNLOAD

# # Initialize hunt runner args.
# hunt_runner_args = grrapi.types.CreateHuntRunnerArgs()
# rule = hunt_runner_args.client_rule_set.rules.add()
# rule.rule_type = rule.LABEL
# rule.label.label_names.append("suspicious")

# # Create a hunt and start it.
# hunt = grrapi.CreateHunt(flow_name="FileFinder", flow_args=flow_args,
#                          hunt_runner_args=hunt_runner_args)
# hunt = hunt.Start()
@grr_REST_api.route('/grr_server/api/v1.0/clients/', methods=['GET'])
def get_client_by_name(auth, client_name):
    clientsIter = grrapi.SearchClients(query="")
    for aclient in clientsiter:
        if aclient.name == client_name:
            return flask.jsonify(aclient)
        else:
            # TODO(ahmednofal): should we return or raise an error
            # or return a 404
            return flask.jsonify("")
    pass


if __name__ == '__main__':
    grr_REST_api.run(debug=True)
