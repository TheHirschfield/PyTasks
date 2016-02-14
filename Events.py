"""
                                       
   Business - U08007                   
   Calender, Schedule, Planner.        
                                       
   Authors: Oliver Hirschfield, Curtis Geddes, Christian Rojas,
   Francesca Ayeni, Fayosi Olukoya, Kieran St Louis.

   File: Event Storage
                                       
"""

import time
import datetime


#Main Event Storage
events = []

#Add Event to Storage
def addEvent(title, timestamp, location):

    
    temp = [title, timestamp, location]

    #Add To Main Storage
    events.append(temp)

    print("Event Added: ", temp)

#Remove an Event from Storage
def removeEvent(identity):
    print ("Event Removed: ", events[identity])
    del events[identity]


addEvent("Birthday", time.time(),"Home")
print(events)
removeEvent(0)

print(events)
