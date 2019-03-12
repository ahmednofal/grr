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
                    callback=gui_obj.UpdatePresistantActionsList)
            chk.select()
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
        # A list of actions
        # TODO(ahmednofal): try retrieving from storage first then
        actions_whitelist = ActionPlugin.classes.keys()
        # A dict
        actions_whitelist = {anaction: BooleanVar(self.root) for anaction in actions_whitelist}
        self.actions_list_gui = Checklist(self, self.root,
                actions_whitelist)
        self.actions_list_gui.pack(side=LEFT)
        self.actions_list_gui.config(relief=GROOVE, bd=2)
        self.actions_list_gui.pack(side=TOP,  fill=X)
        # self.count = 0
        while True:
            self.UpdateActionsList()
            self.root.update()

    def UpdateActionsList(self):
        # The file has to exist
        # Read JSON file
        print("here")
        with open(actions_whitelist_json_file, 'r') as f:
            actions_whitelist_dict = json.load(f)
        # print(type(self.actions_list_gui.actions_whitelist()))
        self.actions_list_gui.actions_whitelist = actions_whitelist_dict
        print(self.actions_list_gui.actions_whitelist)
        return self

    def UpdatePresistantActionsList(self):

        with open(actions_whitelist_json_file, 'w') as f:
            json.dump(self.actions_whitelist, f)
        return self
        return self.actions_list_gui.actions_whitelist()

gui_agent = GUIAgent()



