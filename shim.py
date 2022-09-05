import tkinter
from tkinter import *
from tkinter import messagebox
import time
import threading
import sys


root = Tk()
root.geometry("800x1000")
root.title("The Shrimp Whisper Feeding Software 1.0 by Freddie")
img = tkinter.Image("photo", file="/users/fredrikrosenlowuhl/downloads/shrimp.gif")
root.tk.call('wm', 'iconphoto', root._w, img)


# Declare variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()
hourString_break = StringVar()
minuteString_break = StringVar()
secondString_break = StringVar()


# Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("00")
hourString_break.set("00")
minuteString_break.set("00")
secondString_break.set("00")


# Defining the timer for when the motor will be active
def runTimer():

    # Placeholder for Martins function
    #start_feeding_motor()

    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    # Storing the original inputted values
    old_hourString = int(hourString.get())
    old_minuteString = int(minuteString.get())
    old_secondString = int(secondString.get())

    # Counting down to 0
    while(clockTime > -1):

        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        # Update the interface
        root.update()
        time.sleep(1)

        # The countdown is finished
        if(clockTime == 0):

            # Set clock to the original value again
            hourString.set(old_hourString)
            minuteString.set(old_minuteString)
            secondString.set(old_secondString)

            # Start the timer for the break
            threading.Thread(target=runBreakTimer).start()

        clockTime -= 1

# Defining the timer for when the motor will be inactive
def runBreakTimer():

    try:
        clockTime = int(hourString_break.get())*3600 + int(minuteString_break.get())*60 + int(secondString_break.get())
    except:
        print("Incorrect values")

    # Storing the original inputted values
    old_hourString_break = int(hourString_break.get())
    old_minuteString_break = int(minuteString_break.get())
    old_secondString_break = int(secondString_break.get())

    while(clockTime > -1):

        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0

        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString_break.set("{0:2d}".format(totalHours))
        minuteString_break.set("{0:2d}".format(totalMinutes))
        secondString_break.set("{0:2d}".format(totalSeconds))

        # Update the interface
        root.update()
        time.sleep(1)

        # The countdown is finished
        if(clockTime == 0):

            # Set clock to the original value again
            hourString_break.set(old_hourString_break)
            minuteString_break.set(old_minuteString_break)
            secondString_break.set(old_secondString_break)

            # Start the timer for the motor again
            threading.Thread(target=runTimer).start()

        clockTime -= 1

def stopRunning():
    sys.exit()

#def start_feeding_motor():
    #print("The motor has started!")
    #insert function elements with minutes as parameter and then it will stop after X minutes, which is the entry from "insert_feeding_duration_entry"

# DEFINING ELEMENTS:
# HEADING
overskrift = Label(root, text="Welcome to the Shrimp Whisper!")

# INSERT FEEDING DURATION AREA
insert_feeding_duration_label = Label(root, text="Insert feeding duration: (HH : MM : SS)")
hour_insert_feeding_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=hourString)
minute_insert_feeding_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=minuteString)
second_insert_feeding_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=secondString)

# INSERT BREAK DURATION AREA
insert_break_duration_label = Label(root, text="Insert break duration: (HH : MM : SS)")
hour_insert_break_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=hourString_break)
minute_insert_break_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=minuteString_break)
second_insert_break_duration_entry = Entry(root, width=3, borderwidth=5, textvariable=secondString_break)

# BUTTONS
start_feeding_scheme_button = Button(root, text="START FEEDING SCHEME", padx=40, pady=20, command=lambda: threading.Thread(target=runTimer).start())
stop_feeding_scheme_button = Button(root, text="STOP FEEDING SCHEME", padx=40, pady=20, command=stopRunning)



# ELEMENT MATRIX:
overskrift.place(x=300, y=50)

insert_feeding_duration_label.place(x=100, y=160)
hour_insert_feeding_duration_entry.place(x=130, y=200)
minute_insert_feeding_duration_entry.place(x=180, y=200)
second_insert_feeding_duration_entry.place(x=230, y=200)

start_feeding_scheme_button.place(x=400, y=185)

insert_break_duration_label.place(x=100, y=400)
hour_insert_break_duration_entry.place(x=130, y=440)
minute_insert_break_duration_entry.place(x=180, y=440)
second_insert_break_duration_entry.place(x=230, y=440)

stop_feeding_scheme_button.place(x=400, y=425)

root.mainloop()