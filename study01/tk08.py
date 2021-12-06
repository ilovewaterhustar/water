from tkinter import *

window =Tk()
f = Frame(window)

b1=Button(f, text="picture store",bg="white", fg="black")
b2=Button(f, text="big",bg="white", fg="black")
b3=Button(f, text="cancel",bg="white", fg="black")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l=Label(window, text="this")

l.pack()
f.pack()

window.mainloop()