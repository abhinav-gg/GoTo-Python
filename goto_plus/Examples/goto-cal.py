###PLACE ME AT THE TOP OF YOUR CODE### (this function can not be imported as it requires the __file__ var of the specific file it is used in)
def goto(line):
    with open(__import__("os").path.abspath(__file__), "r") as f: content = [i.replace("    ", "\t") for i in f.readlines()]
    try: exec("".join(content[(line-1):]), globals())
    except SystemExit: raise __import__("sys").exit()       
    except RecursionError: raise __import__("sys").exit("GoTo Exception - GoTo has formed a loop.")
    except IndentationError:
        while any([i.isalpha() for i in content[(line-1)]]) == False: line += 1
        editout = content[(line-1):]
        for j, i in enumerate(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), ""))):
            editout.insert(0, "{}if True:\n".format('\t' * (len(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), "")))-j-1)))
        exec("".join(editout))
    raise __import__("sys").exit()
######################################
from datetime import datetime, timedelta
import os, sys
from tkinter import *
from tkcalendar import Calendar
import json
input("~~~~~~~~~~~~~~\nDISCLAIMER\n~~~~~~~~~~~~~~\nTHE CODE FOR THE HOMEWORK TASK IS INTACT BETWEEN LINES 37 AND 68\nTHIS TOOK A LOT OF TIME TO COMPLETE AND DOES ACTUALLY WORK DESPITE\nTHE CODE LOOKING HORENDOUS AND USING GLOBAL VARIABLES WITH GOTO >:)\nI WOULD APPRECIATE YOU RUNNING IT TO SEE WHAT IT DOES\n~~~~~~~~~~~~~~\nPRESS [ENTER] TO BEING\n~~~~~~~~~~~~~~\n")
events = []
sys.tracebacklimit = -1
global today, returnstring 
today, returnstring = "", ""
Tk.report_callback_exception = lambda *args : None
print("WELCOME TO CALENDAR APPLICATION:")
goto(174) # Load from file
#Not Needed due to GUI but is needed for regular homework
#while True:
#    try:
#        date = datetime.strptime(input("Enter date (format dd/mm/yyyy); "), "%d/%m/%Y")
#        break
#    except: 
#        print("Invalid input")

date = today
while True:
    try:
        inp = input("Enter start time (format hh:mm) or (A) if the event lasts all day; ")
        starttime = datetime.strptime(inp, "%H:%M")
        duration = datetime.strptime(input("Enter duration (format hh:mm); "), "%H:%M")

        break
    except:

        if inp == "A":
            starttime = datetime.strptime("00:01", "%H:%M")
            duration = datetime.strptime("23:59", "%H:%M")
            break
        print("Invalid input")
        

starttimetimedelta = timedelta(hours=duration.hour, minutes=duration.minute)

durationtimedelta = timedelta(hours=duration.hour, minutes=duration.minute)

start = date + starttimetimedelta

endtime = start + durationtimedelta

title = input("Enter a summary for this event; ")

tempjson = { 
  "start": { "dateTime": start.strftime("%A %d %B %Y at %I:%M %p") }, 
  "end": { "dateTime": endtime.strftime("%d/%m/%Y %H:%M") }, 
  "summary": title, 
}
events.append(tempjson)
returnstring = json.dumps(tempjson, sort_keys=False, indent=4) + "\nADDED\n"
print("Event has been ADDED\n\n")
goto(183) # SET END
########### HERE TO GET
todaysevents = []
_ = -1
_ += 1
if _ < len(events):
    event = events[_]
    tempdate = datetime.strptime(event["start"]["dateTime"], "%A %d %B %Y at %I:%M %p")
    if tempdate.date() == today.date():
        todaysevents.append(event)
    #print(tempdate.date(), today.date(), todaysevents)
    goto(75) # line to iter _

returnstring = json.dumps(todaysevents, sort_keys=False, indent=4)
goto(183) # GET END
########### HERE TO DEL
todaysevents = []
_ = -1
_ += 1
if _ < len(events):
    event = events[_]
    tempdate = datetime.strptime(event["start"]["dateTime"], "%A %d %B %Y at %I:%M %p")
    if tempdate.date() == today.date():
        todaysevents.append(event)
    #print(todaysevents)
    goto(89) # line to iter _
if len(todaysevents) == 0: returnstring = "No Events To Delete On This Date"; goto(183)
print(json.dumps(todaysevents, sort_keys=False, indent=4), "\nEnter the number of the event you would like to remove:")
_ = -1
_ += 1
if _ < len(todaysevents):
    print(f"{_ + 1}) {todaysevents[_]['summary']}")
    goto(100)
while True:
    try:
        k = int(input("Enter Number; "))
        if k not in range(1, len(todaysevents) + 1):
            raise
        break
    except:
        print("Invalid input")
events.remove(todaysevents[k-1])
print("Event has been DELETED\n\n")
returnstring = json.dumps(todaysevents[k-1], sort_keys=False, indent=4) + "\nDELETED"
goto(183) # DEL END
##################################################

root = Tk()
root.geometry("600x1500")
root.title('Close me to save the calendar')
temptoday = datetime.today()

cal = Calendar(root, selectmode = 'day',
               year = temptoday.year, month = temptoday.month,
               day = temptoday.day)
 
cal.pack(pady = 20)
 
def EVENT_get():
    global today, returnstring
    t = [i.rjust(2, "0") for i in cal.get_date().split("/")]
    today = datetime.strptime("/".join(t), "%m/%d/%y")
    goto(72) # get code after set code

def EVENT_set():
    global today, returnstring
    t = [i.rjust(2, "0") for i in cal.get_date().split("/")]
    today = datetime.strptime("/".join(t), "%m/%d/%y")
    goto(35) # set code at beginning

def EVENT_del():
    global today, returnstring
    t = [i.rjust(2, "0") for i in cal.get_date().split("/")]
    today = datetime.strptime("/".join(t), "%m/%d/%y")
    goto(86) # del code after get code

    dateLabel.config(text=returnstring)
    raise Exception("This isnt working")#
 
Button(root, text = "Get Event",
       command = EVENT_get).pack(pady = 0)

Button(root, text = "Set Event",
       command = EVENT_set).pack(pady = 0)
 
Button(root, text = "Del Event",
       command = EVENT_del).pack(pady = 0)
 
dateLabel = Label(root, text = "")
dateLabel.pack(pady = 5)

def on_closing():
    print("SAVED CALENDAR")
    root.destroy()
    goto(169)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

storefile = open("calendar.json", "w")
storefile.write(json.dumps(events, sort_keys=False, indent=4))
storefile.close()
goto(117)#make new window

try:
    storefile = open("calendar.json", "r")
    events = json.loads("".join(storefile.readlines()))
    storefile.close()
except:  
    print("Could not load previous Calendar...")
    events = []
goto(117)

dateLabel.config(text=returnstring)
raise Exception("This isnt working")

