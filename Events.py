"""
                                       
   Business - U08007                   
   Calender, Schedule, Planner.        
                                       
   Authors: Oliver Hirschfield, Curtis Geddes, Christian Rojas,
   Francesca Ayeni, Fayosi Olukoya, Kieran St Louis.

   File: Event Storage
                                       
"""

#Import Time Packages
import time
import datetime
import csv

#Main Event Storage
events = []

#Add Event to Storage
def addTask(title, timestamp, location):

    #Create Temp New Event List
    temp = [title, timestamp, location]

    #Add To Main Storage
    events.append(temp)

    #Debug Notify
    print("Task Added: ", temp)

#Remove an Event from Storage
def removeTask(time):
    print ("Attempting to remove task at: ", time)
    if len(events) > 0:
        for n in range(0, len(events)):
            if events[n][1] == time:
                del events[n]
                print ("Event Removed: ", time)
                return True
    return False

#Get Note For Date
def getTask(time):
    for n in range(0, len(events)):
        if events[n][0] == time:
            return events[n][1]

    return ""

#Convert Timestamp To Readable Form
def convertEventTimestamp(date):
    return datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')


addTask("Birthday", "15 03 2016","Home")
removeTask("15 03 2016")
