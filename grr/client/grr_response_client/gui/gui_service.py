from tkinter import *
from collections import OrderedDict
from grr_response_client.actions import ActionPlugin
from multiprocessing.connection import Listener

class Checklist(Frame):
    def __init__(self, parent, actions_whitelist_dict, side=LEFT, anchor=W):
        self._actions_whitelist_dict = actions_whitelist_dict
        Frame.__init__(self, parent)
        row_idx = 0
        for action_entry, accessible in self._actions_whitelist_dict.items():
            chk = Checkbutton(self, text=action_entry, variable=accessible)
            chk.select()
            chk.grid(row=row_idx, sticky=W)
            row_idx += 1
    @property
    def actions_whitelist(self):
        return self._actions_whitelist_dict

    @actions_whitelist.setter
    def actions_whitelist(self, actions_whitelist_dict):
        for action, accessible in actions_whitelist_dict.items():
            self._actions_whitelist_dict[action].set(accessible)

class GUIAgent:
    def __init__(self):

        self.address = ('localhost', 6001)
        self.listener = Listener(self.address)
        self.conn = self.listener.accept()
        self.root = Tk()
        # A list of actions
        self.actions_whitelist = ActionPlugin.classes.keys()
        # this is a dict
        # TODO(ahmednofal): This should be derived from the comms.py via
        # connecting to it and polling it
        self.actions_whitelist = {anaction: BooleanVar(self.root) for anaction in self.actions_whitelist}
        self.actions_list_gui = Checklist(self.root,
                self.actions_whitelist)
        self.actions_list_gui.pack(side=LEFT)
        self.actions_list_gui.config(relief=GROOVE, bd=2)
        self.actions_list_gui.pack(side=TOP,  fill=X)

    def update(self):
        try:
            # retrieved dict to update the existing gui
            actions_whitelist = self.conn.recv()
            self.actions_list_gui.actions_whitelist(actions_whitelist)
            self.root.update()
        except:
            # means the pipe receive end is clear
            # get the white_list the next update
            pass

    def actions_white_list(self):
        return self.actions_list_gui.actions_whitelist()

gui_agent = GUIAgent()



