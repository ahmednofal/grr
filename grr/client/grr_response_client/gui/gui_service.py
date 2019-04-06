from __future__ import absolute_import
from Tkinter import *
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
        self.chkbtns_list = []
        Frame.__init__(self, parent)
        row_idx = 1
        col_idx = 0
        col_no = 3
        row_no = 10
        for action_entry, accessible in self.actions_whitelist.items():
            chk = Checkbutton(self,
                    text=action_entry,
                    variable=accessible,
                    command=gui_obj.UpdatePersistentActionsList)
            chk.grid(row=row_idx, column=col_idx, sticky=W)
            self.chkbtns_list.append(chk)
            if row_idx > row_no:
                col_idx += 1
                row_idx = 0
            row_idx += 1

    @property
    def actions_whitelist(self):
        return self.__actions_whitelist

    @property
    def chkbtns_list(self):
        return self.__chkbtns_list

    @actions_whitelist.setter
    def actions_whitelist(self, actions_whitelist_dict):
        for action, accessible in actions_whitelist_dict.items():
            self.__actions_whitelist[action].set(accessible)

class GUIAgent:
    def __init__(self):
        self.root = Tk()
        actions_whitelist_dict = self.PersistentActionsWhitelistDict()
        actions_whitelist_dict = {anaction: BooleanVar(self.root) for anaction in actions_whitelist_dict.keys()}
        self.actions_list_gui = Checklist(self, self.root,
                actions_whitelist_dict)
        self.actions_list_gui.pack(side=TOP,  fill=X)
        self.actions_list_gui.config(relief=GROOVE, bd=2)
        Button(self.root, text='all', command=self.SelectAll).pack()
        Button(self.root, text='none', command=self.DeselectAll).pack()
        while True:
            self.UpdateActionsList()
            self.root.update()

    def ChangeActionsListVals(self, func):
        func()
        self.UpdatePersistentActionsList()

    def ChangeAll(self, func):
        for abtn in self.actions_list_gui.chkbtns_list:
            func(abtn) # either select or deselect

    def SelectAll(self):
        def aux():
            self.ChangeAll(Checkbutton.select)
        self.ChangeActionsListVals(aux)

    def DeselectAll(self):
        def aux():
            self.ChangeAll(Checkbutton.deselect)
        self.ChangeActionsListVals(aux)

    def PersistentActionsWhitelistDict(self):
        with open(actions_whitelist_json_file, 'r') as f:
            return json.load(f)

    def UpdateActionsList(self):
        # The file has to exist
        # Read JSON file
        with open(actions_whitelist_json_file, 'r') as f:
            try:
                actions_whitelist_dict = json.load(f)
            except:
                self.UpdatePersistentActionsList()
        for action_entry, accessible in actions_whitelist_dict.items():
            self.actions_list_gui.actions_whitelist[action_entry].set(accessible)
        return self

    def UpdatePersistentActionsList(self):
        with open(actions_whitelist_json_file, 'w') as f:
            dict_tob_dumped = {action_entry: accessible_boolvar.get()
                    for action_entry, accessible_boolvar in
                    self.actions_list_gui.actions_whitelist.items()}
            json.dump(dict_tob_dumped, f)
        return self

gui_agent = GUIAgent()

