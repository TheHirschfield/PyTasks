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

#Main Event Storage
events = []

#Add Event to Storage
def addEvent(title, timestamp, location):

    #Create Temp New Event List
    temp = [title, timestamp, location]

    #Add To Main Storage
    events.append(temp)

    #Debug Notify
    print("Event Added: ", temp)

#Remove an Event from Storage
def removeEvent(identity):
    print ("Event Removed: ", events[identity])
    del events[identity]

#Convert Timestamp To Readable Form
def convertEventTimestamp(date):
    return datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')


addEvent("Birthday", time.time(),"Home")
removeEvent(0)
