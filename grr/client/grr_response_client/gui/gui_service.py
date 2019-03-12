from tkinter import *
from collections import OrderedDict
from grr_response_client.actions import ActionPlugin
from multiprocessing.connection import Listener
from grr_response_client.ac.config import actions_whitelist_json_file
import json

class Checklist(Frame):
    def __init__(self,
            gui_obj,
            parent,
            actions_whitelist_dict,
            side=LEFT,
            anchor=W):
        self.actions_whitelist = actions_whitelist_dict
        Frame.__init__(self, parent)
        row_idx = 0
        for action_entry, accessible in self.actions_whitelist.items():
            chk = Checkbutton(self,
                    text=action_entry,
                    variable=accessible,
                    command=gui_obj.UpdatePresistantActionsList)
            # chk.select()
            chk.grid(row=row_idx, sticky=W)
            row_idx += 1
    @property
    def actions_whitelist(self):
        return self.__actions_whitelist

    @actions_whitelist.setter
    def actions_whitelist(self, actions_whitelist_dict):
        for action, accessible in actions_whitelist_dict.items():
            self.__actions_whitelist[action].set(accessible)

class GUIAgent:
    def __init__(self):
        self.root = Tk()
        actions_whitelist_dict = self.PresistentActionsWhitelistDict()
        actions_whitelist_dict = {anaction: BooleanVar(self.root) for anaction in actions_whitelist_dict.keys()}
        print(actions_whitelist_dict)
        self.actions_list_gui = Checklist(self, self.root,
                actions_whitelist_dict)
        self.actions_list_gui.pack(side=TOP,  fill=X)
        self.actions_list_gui.config(relief=GROOVE, bd=2)
        print(self)
        while True:
            self.UpdateActionsList()
            self.root.update()

    def PresistentActionsWhitelistDict(self):
        with open(actions_whitelist_json_file, 'r') as f:
            return json.load(f)

    def UpdateActionsList(self):
        # The file has to exist
        # Read JSON file
        with open(actions_whitelist_json_file, 'r') as f:
            actions_whitelist_dict = json.load(f)
        for action_entry, accessible in actions_whitelist_dict.items():
            self.actions_list_gui.actions_whitelist[action_entry].set(accessible)
        return self

    def UpdatePresistantActionsList(self):
        with open(actions_whitelist_json_file, 'w') as f:
            dict_tob_dumped = {action_entry: accessible_boolvar.get() for action_entry, accessible_boolvar in self.actions_list_gui.actions_whitelist.items()}
            json.dump(dict_tob_dumped, f)
        return self

gui_agent = GUIAgent()



