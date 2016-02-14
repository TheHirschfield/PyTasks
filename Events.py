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

def addEvent(title, timestamp, location):

    
    temp = [title, timestamp, location]

    #Add To Main Storage
    events.append(temp)

    print("New Event Added: ", temp)

addEvent("Birthday", time.time(),"Home")

