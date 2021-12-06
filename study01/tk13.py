from tkinter import *

window =Tk()
window.geometry("600x200")

def callback(event):
    print(event.x, event.y,"mouse event from") 
    
window.bind("<Button-1>",callback)
window.mainloop()