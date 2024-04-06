from tkinter import Tk                          #Tk and label are the functions
from tkinter import Label                         #Tk are used for window label is used for labeling
import time
import sys 

root = Tk()              #root is the variable in which we store window
root.title("Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("arial",60),bg="black",fg="white")
digi_clock.pack()

present_time()

root.mainloop()              # mainloop is used for displaying the window
