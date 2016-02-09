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

        #File Drop Down Menu
        guiMenuBarFile = Menu(guiMenuBar)
        guiMenuBarFile.add_command(label="Quit", command=self.onExit)
        guiMenuBar.add_cascade(label="File", menu=guiMenuBarFile)

    #Close Window & Quit Program
    def onExit(self):
        self.parent.destroy()
        self.quit()
   
