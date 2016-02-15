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
from tkinter import ttk

import calendar

from Events import *

#GUI Management
class windowManagement(Frame):

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta
    
    #GUI Setup
    def __init__(self, parent):
        Frame.__init__(self, parent)

        #Get Current Calender States
        firstDay = calendar.MONDAY
        year = self.datetime.now().year
        month = self.datetime.now().month
        
        
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
        guiMenubarCalendar = Menu(guiMenubar)
        guiMenubarHelp = Menu(guiMenubar)

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

        #Calendar Dropdown
        guiMenubarCalendar.add_command(label="Import", command=self.onSave)
        guiMenubar.add_cascade(label="Calendar", menu=guiMenubarCalendar)
        
        #Help Dropdown
        guiMenubarHelp.add_command(label="Contents...", command=self.onExit)
        guiMenubar.add_cascade(label="Help", menu=guiMenubarHelp)

        #TOOLBAR
        guiToolbar = Frame(self.parent, bd=1, relief=RAISED)

        #New Event Button
        self.img = Image.open("resources/new.png")
        newImage = ImageTk.PhotoImage(self.img)
        
        #Save Button
        self.img = Image.open("resources/save.png")
        saveImage = ImageTk.PhotoImage(self.img)

        #Load Button
        self.img = Image.open("resources/load.png")
        loadImage = ImageTk.PhotoImage(self.img)
        
        #Add New Event Button to Toolbar
        newButton = Button(guiToolbar, image=newImage, relief=FLAT, command=self.onNewEvent)
        newButton.image = newImage
        newButton.pack(side=LEFT, padx=2,pady=2)

        #Add Save Button to Toolbar
        saveButton = Button(guiToolbar, image=saveImage, relief=FLAT, command=self.onSave)
        saveButton.image = saveImage
        saveButton.pack(side=LEFT, padx=2,pady=2)

        #Add Load Button to Toolbar
        loadButton = Button(guiToolbar, image=loadImage, relief=FLAT, command=self.onLoad)
        loadButton.image = loadImage
        loadButton.pack(side=LEFT, padx=2,pady=2)

        guiToolbar.pack(side=TOP, fill=X)

        self.calenderStyleWidget()
        self.calenderPlaceWidget()

        self.calenderMake()
        
        self.pack()
    
    def calenderMake(self):
        calenderHeader = "Month"

    #Set Styling For Buttons
    def calenderStyleWidget(self):
        style = ttk.Style(self.master)
        styleArrowLayout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', styleArrowLayout('left'))
        style.layout('R.TButton', styleArrowLayout('right'))
    
    def calenderPlaceWidget(self):
        #Header Frame
        calenderFrame = ttk.Frame(self)
        leftMonthChangeButton = ttk.Button(calenderFrame, style='L.TButton', command=self.onSave)
        rightMonthChangeButton = ttk.Button(calenderFrame, style='R.TButton', command=self.onSave)
        self.calenderHeader = ttk.Label(calenderFrame, text="Test", width=15, anchor='center')
        self.calenderMainView = ttk.Treeview(show='', selectmode='none', height=7)
        
        #Pack Header
        calenderFrame.pack(in_=self, side='top', pady=4, anchor='center')
        leftMonthChangeButton.grid(in_=calenderFrame)
        self.calenderHeader.grid(in_=calenderFrame, column=1, row=0, padx=12)
        rightMonthChangeButton.grid(in_=calenderFrame, column=2, row=0)
        self.calenderMainView.pack(in_=self, expand=1, fill='both', side='bottom')
        
    ''' Main GUI Callbacks '''
    
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
   
