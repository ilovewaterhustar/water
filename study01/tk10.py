from tkinter import *

window=Tk()

counter=0

def clicked():
    global counter
    counter+=1
    label["text"]='how many push ur button:' +str(counter)
    
label =Label(window, text="not yet push")
label.pack()
button = Button(window,text="increase",command=clicked).pack()

window.mainloop()    