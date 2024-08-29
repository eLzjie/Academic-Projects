from tkinter import *
import datetime as dt

# function for date and time
def update(root):
    now = dt.datetime.now()
    formatted_date = now.strftime("%A, %B %d, %I:%M %p")
    datetime.set(formatted_date)
    root.after(1000, update, root)

def clock(top_frame):
    global datetime
    # adding the date and time
    datetime = StringVar()
    datetime_label = Label(top_frame, textvariable=datetime, font=("Arial 12 bold"), fg="#C9D8CC", bg="#3B5A64")
    datetime_label.pack(side=RIGHT)

