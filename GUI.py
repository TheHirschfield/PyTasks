"""
                                       
   Business - U08007                   
   Calender, Schedule, Planner.        
                                       
   Authors: Oliver Hirschfield, Curtis Geddes, Christian Rojas,
   Francesca Ayeni, Fayosi Olukoya, Kieran St Louis.

   File: GUI Management
                                       
"""

#IMPORTS
from tkinter import *
from PIL import Image, ImageTk

from Events import *

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
        
        #MENU BAR
        guiMenubar = Menu(self.parent)
        self.parent.config(menu=guiMenubar)

        #Drop Down Menu -FILE
        guiMenubarFile = Menu(guiMenubar)

        #Action Menu - NEW
        guiMenubarFileNew = Menu(guiMenubarFile)
        
        #Add Options For NEW Menu
        guiMenubarFileNew.add_command(label="Event", command=self.onNewEvent) #New Event
        guiMenubarFileNew.add_command(label="Tag", command=self.onNewTag) #New Tag
        guiMenubarFile.add_cascade(label="New", menu=guiMenubarFileNew, underline=0)

        guiMenubarFile.add_command(label="Save", command=self.onSave)
        guiMenubarFile.add_command(label="Load", command=self.onLoad)
        
        #Add Separator to Dropdown
        guiMenubarFile.add_separator()

        #Quit Option
        guiMenubarFile.add_command(label="Quit", command=self.onExit)
        guiMenubar.add_cascade(label="File", menu=guiMenubarFile)

        #TOOLBAR
        guiToolbar = Frame(self.parent, bd=1, relief=RAISED)

        #Save Button
        self.img = Image.open("resources/save.png")
        saveImage = ImageTk.PhotoImage(self.img)

        #Add Save Button to Toolbar
        saveButton = Button(guiToolbar, image=saveImage, relief=FLAT, command=self.onSave)
        saveButton.image = saveImage
        saveButton.pack(side=LEFT, padx=2,pady=2)

        guiToolbar.pack(side=TOP, fill=X)
        self.pack()

    #New Event
    def onNewEvent(self):
        print("This Will Allow The User To Create An Event.")

    #New Tag
    def onNewTag(self):
        print("This Will Allow The User To Create A Tag.")

    #Save Calender
    def onSave(self):
        print("This Will Save The Calender To File.")

    #Load Calender
    def onLoad(self):
        print("This Will Load The Calender From File.")
    
    #Close Window & Quit Program
    def onExit(self):
        self.parent.destroy()
        self.quit()
   
