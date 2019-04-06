from collections import OrderedDict
from grr_response_client.ac.config import actions_whitelist_json_file
from grr_response_client.actions import ActionPlugin
from tkinter import *
import thread
import json
import os

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
        if self.PersistentActionsListExist():
            self.UpdateActionsList()
        else:
            self.InitializePersistentActionsList()

    def PersistentActionsListExist(self):
        return os.path.exists(actions_whitelist_json_file)

    def ActionAccessible(self,action):
        """
        checks if the action exists in the whitelisted
        actions
        """
        # updateInternalList
        self.UpdateActionsList()
        # actionlist_updated
        return self.actions_whitelist[action]

    def InitializePersistentActionsList(self):
        # Only run when presistent storage is not there
        # or if somethings goes wrong
        self.actions_whitelist = OrderedDict().fromkeys(
                ActionPlugin.classes.keys()
                ,False)
        with open(actions_whitelist_json_file, 'w') as f:
            json.dump(self.actions_whitelist, f)
        return self

    def UpdateActionsList(self):
        # The file has to exist
        # Read JSON file
        with open(actions_whitelist_json_file, 'r') as f:
            try:
                self.actions_whitelist = json.load(f)
            except:
                self.InitializePersistentActionsList()
                self.UpdateActionsList()
        return self

    def UpdatePersistentActionsList(self):
        # Write JSON file
        with open(actions_whitelist_json_file, 'w') as f:
            json.dump(self.actions_whitelist, f)
        return self

access_control_manager = AccessControlManager()






