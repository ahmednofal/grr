#!/usr/bin/env python
from tkinter import *

# checkbar will take options and create booleans for them
class Checklist(Frame):
   def __init__(self, parent, actions_whitelist_dict, side=LEFT, anchor=W):
      self.actions_whitelist_dict = actions_whitelist_dict
      Frame.__init__(self, parent)
      row_idx = 0
      for action_entry, accessible in self.actions_whitelist_dict.items():
         chk = Checkbutton(self, text=action_entry, variable=accessible)
         chk.select()
         chk.grid(row=row_idx, sticky=W)
         # chk.pack(side=side, anchor=anchor, expand=YES)
         row_idx += 1

# class ACGUI():
#    def __init__(self, parent, )

# ACGUI(Tk(), actions_whitelist.values(), actions_whitelist.keys())
