"""
                                       
   Business - U08007                   
   Calender, Schedule, Planner.        
                                       
   Authors: Oliver Hirschfield, Curtis Geddes, Christian Rojas,
   Francesca Ayeni, Fayosi Olukoya, Kieran St Louis.

   File: Notes Managements
                                       
"""

#Import Time Packages
import csv

#Main Note Storage
notes = []

def addNote(time, note):
    #Create Temp New Note List
    temp = [time, note]

    #Add To Main Storage
    notes.append(temp)

    #Debug Notify
    print("Event Added: ", temp)

#Remove Saved Note
def removeNote(time):
    if len(notes) > 0:
        for n in range(0, len(notes)):
            if notes[n][0] == time:
                del notes[n]
                print ("Note Removed: ", time)
                return True
    return False


#Get Note For Date
def getNote(time):
    for n in range(0, len(notes)):
        if notes[n][0] == time:
            return notes[n][1]

    return ""
        
