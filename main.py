
# User Interface Creation with Python - Python GUI - Price Tracking Application with Python Tkinter and Price Tracking Application

from tkinter import *
from app import check_price
#@Lolita
root = Tk()
root.title('KK Price Tracking')
root.geometry('500x250')

status = False
timeloop = 1000

def scanning():
    if status:
        print('Checking')
        url = urlEntry.get()
        target = float(targetEntry.get())
        check = check_price(url, target)
        if check:
            stopApp()
    root.after(timeloop, scanning)

def startApp():
    global status
    status = True
    exeButton.config(text='STOP', command=stopApp)

def stopApp():
    global status
    status = False
    exeButton.config(text='START', command=startApp)

urllabel = Label(root, text='TARGET LINK')
urllabel.pack(pady=10)

urlEntry = Entry(root, width=40)
urlEntry.pack()

targetlabel = Label(root, text='TARGET PRICE')
targetlabel.pack(pady=10)

targetEntry = Entry(root, width=40)
targetEntry.pack()

exeButton = Button(root, text='START', command=startApp, width=20, height=2)
exeButton.pack(pady=10)

root.after(timeloop, scanning)
root.mainloop()
