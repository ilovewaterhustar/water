from tkinter import *

window =Tk()
f = Frame(window)

b1=Button(f, text="box#1",bg="red", fg="white")
b2=Button(f, text="box#2",bg="green", fg="black")
b3=Button(f, text="box#3",bg="orange", fg="white")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l=Label(window, text="this")

l.pack()
f.pack()

window.mainloop()