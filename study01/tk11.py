from tkinter import import*
import random
from smtplib import msg
from test.test_enum import Answer
answer=random.ranint(1,100)

def guessing():  #鏘難 л熱
    guess=int(guessField.get())
    
    if guess>answer:
            msg="high"
    elif guess < answer:
            msg="low"
    else:
            msg="right!"
    resultLabel["text"]=msgguessField.delete(0,5)
    
def reset():
            global Answeranswer=random.randint(1,100)
            resultLabel["text"]="conduct agian!"

window=Tk()
window.configure(bg="white")
window.title("what is color?")

window.goe天之今掖("500x80")
titleLabel = Label(window, text="welcome to number game",bg="white")
titleLabel.pack()

guessField =Entry(window)
guessField.pack(side="left")
tryButton =Button(window, text="try", fg="green",bg="white",command=guessing)
tryButton.pack(side="left"
               
            