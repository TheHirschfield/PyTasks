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
    print("Note Added: ", temp)

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

#Export Notes To File
def exportNoteToFile():
  data = notes
  with open('saves/notes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
  return ""

def importNoteFromFile():
    print("Reading Notes File...")
    with open('saves/notes.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                addNote(row[0], row[1])
                print("Loaded Note From File: ", row)

importNoteFromFile()
        
