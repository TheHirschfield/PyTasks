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
import tkinter.font
import calendar

from Events import *
from Notes import *

def getCalendar(locale, fd):
    if locale is None:
        return calendar.TextCalendar(fd)
    else:
        return calendar.LocaleTextCalendar(fd, locale)

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
        selectedBg = '#9bc0d9' # Previous - 84b5d3
        selectedFg = '#ffffff'
        
        self.date = self.datetime(year,month,1)
        self.selected = None
        self.currentTime = ""

    
        self.cal = getCalendar(None,firstDay)
        
        self.parent = parent
        self.initUI()

        #Main Calender Widget
        self.calenderStyleWidget()
        self.calenderPlaceWidget()
        self.calenderConfig()

        self.setupSelected(selectedBg, selectedFg)
        
        self.items = [self.calenderMainView.insert('', 'end', values='') for _ in range(6)]
        
        self.calenderMake()
        self.calenderMainView.bind('<Map>',self.minsize)

        #Add Events Listing Tabs
        self.eventViewerPlace()
        
    #Main Window Creation
    def initUI(self):

        #Add Window Title
        self.parent.title("Personal Organiser")
        
        #MENU BAR
        guiMenubar = Menu(self.parent)
        self.parent.config(menu=guiMenubar)

        #Drop Down Menu -FILE
        guiMenubarFile = Menu(guiMenubar)
        guiMenubarEdit = Menu(guiMenubar)
        guiMenubarCalendar = Menu(guiMenubar)
        guiMenubarHelp = Menu(guiMenubar)

        #Action Menu - NEW
        guiMenubarFileNew = Menu(guiMenubarFile)
        guiMenubarFileExport = Menu(guiMenubarFile)
        
        #Add Options For NEW Menu
        guiMenubarFileNew.add_command(label="Task", command=self.onNewTask) #New Task
        guiMenubarFileNew.add_command(label="Tag", command=self.onNewTag) #New Tag
        guiMenubarFile.add_cascade(label="New", menu=guiMenubarFileNew, underline=0)

        guiMenubarFile.add_command(label="Save", command=self.onSave)
        guiMenubarFile.add_command(label="Load", command=self.onLoad)

        guiMenubarFileExport.add_command(label="Notes", command=self.exportNotes)
        guiMenubarFileExport.add_command(label="Tasks", command = self.exportTasks)
        guiMenubarFile.add_cascade(label="Export", menu=guiMenubarFileExport, underline=0)
        
        #Add Separator to Dropdown
        guiMenubarFile.add_separator()

        #Quit Option
        guiMenubarFile.add_command(label="Quit", command=self.onExit)
        guiMenubar.add_cascade(label="File", menu=guiMenubarFile)

        #Edit Dropdown
        guiMenubarEdit.add_command(label="Clear Note", command=self.clearNote)
        guiMenubarEdit.add_command(label="Clear Event On Day", command=self.clearEventOnDay)
        guiMenubar.add_cascade(label="Edit", menu=guiMenubarEdit)
        
        #Calendar Dropdown
        guiMenubarCalendar.add_command(label="Next Month", command=self.setNextMonth)
        guiMenubarCalendar.add_command(label="Previous Month", command=self.setPreviousMonth)
        guiMenubar.add_cascade(label="View", menu=guiMenubarCalendar)
        
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
        newButton = Button(guiToolbar, image=newImage, relief=FLAT, command=self.onNewTask)
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
        
        self.pack(expand=1, fill='both')

    #Set Styling For Buttons
    def calenderStyleWidget(self):
        style = ttk.Style(self.master)
        styleArrowLayout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', styleArrowLayout('left'))
        style.layout('R.TButton', styleArrowLayout('right'))
        style.configure('Calendar.Treeview', rowheight=40)
    
    def calenderPlaceWidget(self):
        #Header Frame
        calenderFrame = ttk.Frame(self)
        leftMonthChangeButton = ttk.Button(calenderFrame, style='L.TButton', command=self.setPreviousMonth)
        rightMonthChangeButton = ttk.Button(calenderFrame, style='R.TButton', command=self.setNextMonth)
        self.calenderHeader = ttk.Label(calenderFrame, width=15, anchor='center')
        self.calenderMainView = ttk.Treeview(show='', selectmode='none', height=7, style='Calendar.Treeview')
        
        #Pack Header
        calenderFrame.pack(in_=self, side='top', pady=4, anchor='center')
        leftMonthChangeButton.grid(in_=calenderFrame)
        self.calenderHeader.grid(in_=calenderFrame, column=1, row=0, padx=12)
        rightMonthChangeButton.grid(in_=calenderFrame, column=2, row=0)
        self.calenderMainView.pack(in_=self, fill='x', side='top')

    def calenderConfig(self):
        cols = self.cal.formatweekheader(3).split()
        self.calenderMainView['columns'] = cols
        self.calenderMainView.tag_configure('header',background='grey90')
        self.calenderMainView.insert('','end', values=cols, tag='header')

        font = tkinter.font.Font()

        maxwidth = max(font.measure(col) for col in cols)*5
        for col in cols:
            self.calenderMainView.column(col, width=maxwidth, minwidth=maxwidth, anchor='c')
 
    def calenderMake(self):
        year, month = self.date.year, self.date.month

        #Update Calender Month Listing
        calHeader = self.cal.formatmonthname(year, month, 0)
        self.calenderHeader['text'] =  calHeader.title()

        _cal = self.cal.monthdayscalendar(year,month)
        for indx, i in enumerate(self.items):
            week = _cal[indx] if indx < len(_cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self.calenderMainView.item(i, values=fmt_week)

        self.eventRegisteredPlace()
    
    def minsize(self,evt):
        width, height = self.calenderMainView.master.geometry().split('x')
        height = height[:height.index('+')]
        self.calenderMainView.master.minsize(width, height)


    def setupSelected(self, selectedBg, selectedFg):
        self.font = tkinter.font.Font()
        self.canvas = canvas = tkinter.Canvas(self.calenderMainView, background=selectedBg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0,0,fil=selectedFg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self.calenderMainView.bind('<Configure>', lambda evt: canvas.place_forget())
        self.calenderMainView.bind('<ButtonPress-1>', self.selectedDate)

    def eventRegisteredPlace(self):

        for x in range (0,len(events)):

            temp_date = events[x][1]
            
            print("Preparing To Highlight: ",getTask(events[x][1]))

            if str(self.date.year) == temp_date.split( )[2]:

                if(self.date.month < 10):
                    temp_month = str(self.date.month)
                else:
                    temp_month = self.date.month
                
                if str(temp_month) == temp_date.split( )[1]:
                    print("Task Rendering Will Take Place for",getTask(events[x][1]))
                else:
                    print("Date", temp_month, "Does Not Fit Criteria For:",getTask(events[x][1]))

            else:
                print("Date", temp_date, "Does Not Fit Criteria For:",getTask(events[x][1]))
    
    def eventViewerPlace(self):
        eventViewerFrame = ttk.Frame(self)               
        eventViewerFrame.pack(in_=self, side='top',fill='both', expand='Y')
        
        self.eventMainView = ttk.Notebook(eventViewerFrame, name='notebook')

        #Event Tab Text Box - Tab 0
        tab0 = ttk.Frame(self.eventMainView)
        self.eventMainView.add(tab0, text="Tasks")

        self.eventMainView.pack(fill='both', expand=Y, side='top')

        self.eventsBox = Text(tab0, wrap=WORD, width=40, height=10)
        self.eventsBox.pack(fill=BOTH, expand=Y)

        #self.eventsBox.config(state=DISABLED)
        

        #Note Tab Text Box - Tab 1
        tab1 = ttk.Frame(self.eventMainView)
        self.eventMainView.add(tab1, text="Notes")

        self.eventMainView.pack(fill='both', expand=Y, side='top')

        self.notesBox = Text(tab1, wrap=WORD, width=40, height=10)
        vscroll = ttk.Scrollbar(tab1, orient=VERTICAL, command=self.notesBox.yview)
        self.notesBox['yscroll'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)
        self.notesBox.pack(fill=BOTH, expand=Y)


    def showSelected(self, text, bbox):

        x, y, width, height = bbox

        textw = self.font.measure(text)

        canvas = self.canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width/2 - textw/4, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self.calenderMainView, x=x, y=y)
    
    #User Input Calls
    def selectedDate(self, evt):
        #Save Old Date
        if self.currentTime != "" and self.getFromNotes() != "":
            if getNote(self.currentTime) != "":
                removeNote(self.currentTime)
            addNote(self.currentTime, self.getFromNotes())

        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self.items:
            return

        itemValues = widget.item(item)['values']
        if not len(itemValues):
            return

        text = itemValues[int(column[1]) - 1]
        if not text:
            return

        bbox = widget.bbox(item, column)
        if not bbox:
            return

        text = '%02d' % text
        self.selected = (text, item, column)
        self.showSelected(text, bbox)
        self.currentTime = text + " " + str(self.date.month) + " " + str(self.date.year)

        self.addToTasks(getTask(self.currentTime))
        self.addToNotes(getNote(self.currentTime))

        

    #Tasks Box Add
    def addToTasks(self,txt):
        self.tasksBox.delete(1.0, END)
        self.tasksBox.insert(END, txt)
        print(txt)
    
    #Notes Box Add
    def addToNotes(self,txt):
        self.notesBox.delete(1.0, END)
        self.notesBox.insert(END, txt)
    
    def getFromNotes(self):
        return self.notesBox.get("1.0",'end-1c')
    
    ### Main GUI Callbacks ###
    
    #New Event
    def onNewTask(self):
        print("This Will Allow The User To Create An Task.")

        self.taskWindows = Toplevel(self)
        self.taskWindows.wm_title("New Task")

        Label(self.taskWindows, text="Task Name").grid(row=0)
        Label(self.taskWindows, text="Task Day:").grid(row=1)
        Label(self.taskWindows, text="Task Month:").grid(row=2)
        Label(self.taskWindows, text="Task Year:").grid(row=3)

        self.taskGrid1 = Entry(self.taskWindows)
        self.taskGrid2 = Entry(self.taskWindows)
        self.taskGrid3 = Entry(self.taskWindows)
        self.taskGrid4 = Entry(self.taskWindows)

        self.taskGrid1.grid(row=0, column=1)
        self.taskGrid2.grid(row=1, column=1)
        self.taskGrid3.grid(row=2, column=1)
        self.taskGrid4.grid(row=3, column=1)
        
        Button(self.taskWindows, text='Add', command=self.taskWindowAdd).grid(row=5, column=0, sticky=W, pady=4)
        Button(self.taskWindows, text='Cancel', command=self.taskWindowClose).grid(row=5, column=1, sticky=W, pady=4)

    def taskWindowAdd(self):
        print("Task Name: " + self.taskGrid1.get())
        print("Task Day: " + self.taskGrid2.get())
        print("Task Month: " + self.taskGrid3.get())
        print("Task Year: " + self.taskGrid4.get())

        dateTime = self.taskGrid2.get() + " " + self.taskGrid3.get() + " " + self.taskGrid4.get();

        addTask(self.taskGrid1.get(),dateTime,"unknown")
        
        self.taskWindowClose()

    def clearEventOnDay(self):
        if self.currentTime != "":
            removeTask(self.currentTime)
    
    def taskWindowClose(self):
        self.taskWindows.destroy()

    def addToTasks(self,txt):
        self.eventsBox.delete(1.0, END)
        self.eventsBox.insert(END, txt)
    
    #New Tag
    def onNewTag(self):
        print("This Will Allow The User To Create A Tag.")

    #Save Calender
    def onSave(self):
        print("This Will Save The Calender To File.")

    #Load Calender
    def onLoad(self):
        print("This Will Load The Calender From File.")

    def clearNote(self):
        self.canvas.place_forget()
        if self.currentTime != "" and self.getFromNotes() != "":
            if getNote(self.currentTime) != "":
                removeNote(self.currentTime)

        self.addToNotes("")

    def exportNotes(self):
        exportNoteToFile()

    def exportTasks(self):
        saveTasks(self)
            
    #Change To Previous Month View
    def setPreviousMonth(self):
        #Remove Overlay Location
        self.canvas.place_forget()

        #Save Current Note
        if self.currentTime != "" and self.getFromNotes() != "":
            if getNote(self.currentTime) != "":
                removeNote(self.currentTime)
            addNote(self.currentTime, self.getFromNotes())

        #Wipe Note
        self.addToNotes("")
            
        self.date = self.date - self.timedelta(days=1)
        self.date = self.datetime(self.date.year, self.date.month, 1)
        self.calenderMake()

    #Change To Next Month View
    def setNextMonth(self):
        #Remove Overlay Location
        self.canvas.place_forget()

        #Save Current Note
        if self.currentTime != "" and self.getFromNotes() != "":
            if getNote(self.currentTime) != "":
                removeNote(self.currentTime)
            addNote(self.currentTime, self.getFromNotes())

        #Wipe Note
        self.addToNotes("")
        
        year, month = self.date.year, self.date.month
        self.date = self.date + self.timedelta(days=calendar.monthrange(year, month)[1] + 1)
        self.date = self.datetime(self.date.year, self.date.month, 1)
        self.calenderMake()
        
    #Close Window & Quit Program
    def onExit(self):
        self.parent.destroy()
        self.quit()

    
   
