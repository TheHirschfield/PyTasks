"""
                                       
   Business - U08007                   
   Calender, Schedule, Planner.        
                                       
   Authors: Oliver Hirschfield, Curtis Geddes, Christian Rojas,
   Francesca Ayeni, Fayosi Olukoya, Kieran St Louis.

   File: GUI Management
                                       
"""

#IMPORTS
from tkinter import *

#GUI Management
class windowManagement(Frame):

    #GUI Setup
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    #Main Window Creation
    def initUI(self):

        #Add Window Title
        self.parent.title("U08007")
        
        #Menu Bar
        guiMenuBar = Menu(self.parent)
        self.parent.config(menu=guiMenuBar)

        #Drop Down Menu -FILE
        guiMenuBarFile = Menu(guiMenuBar)

        #Action Menu - NEW
        guiMenuBarFileNew = Menu(guiMenuBarFile)
        
        #Add Options For NEW Menu
        guiMenuBarFileNew.add_command(label="Event", command=self.onNewEvent) #New Event
        guiMenuBarFileNew.add_command(label="Tag", command=self.onNewTag) #New Tag
        guiMenuBarFile.add_cascade(label="New", menu=guiMenuBarFileNew, underline=0)
        
        #Add Separator to Dropdown
        guiMenuBarFile.add_separator()

        #Quit Option
        guiMenuBarFile.add_command(label="Quit", command=self.onExit)
        guiMenuBar.add_cascade(label="File", menu=guiMenuBarFile)


    #New Event
    def onNewEvent(self):
        print("This Will Allow The User To Create An Event.")

    #New Tag
    def onNewTag(self):
        print("This Will Allow The User To Create A Tag.")
    
    #Close Window & Quit Program
    def onExit(self):
        self.parent.destroy()
        self.quit()
   
