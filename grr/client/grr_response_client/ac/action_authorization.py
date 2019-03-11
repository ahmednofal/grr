from collections import OrderedDict
from grr_response_ac import config
from grr_response_client.actions import ActionPlugin
from tkinter import *
import thread

from multiprocessing.connection import Client

import requests

# Need to be globally accessible for the current client context
# so the gui can access it
# whitelisted_actions init

# actions_whitelist = dict().fromkeys(ActionPlugin.classes.keys())


class AccessControlManager:
    """Communicates with the gui to make sure the access control
    list of the actions are synced in both directions"""
    def __init__(self):
        """
        initializes the communicator
        """
        self.address = ('localhost', 6001)
        # TODO (ahmednofal): This should be removed to when the update
        # is needed and the port is open
        self.actions_whitelist = OrderedDict().fromkeys(
                ActionPlugin.classes.keys()
                ,False)

    def ActionAccessible(self,action):
        """
        checks if the action exists in the whitelisted
        actions
        """
        # updateInternalList
        self.conn = Client(self.address)
        return actions_whitelist[action]

    def UpdateGui(self):
        self.conn.send(self.actions_whitelist)
        pass

access_control_manager = AccessControlManager()






