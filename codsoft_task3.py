from tkinter import *
import tkinter as tk
import random
import string

pw = Tk()
pw.title('Password Generator')
pw.geometry('300x300')

def option():
    option = choice.get()

choice = IntVar()
btn1 = Radiobutton(pw, text="Poor Password", variable=choice, value=1,command = option, font=("Arial",12))
btn1.pack()

btn2 = Radiobutton(pw, text="Average Password", variable=choice, value=2,command = option, font=("Arial",12))
btn2.pack()

btn3 = Radiobutton(pw, text="Strong Password", variable=choice, value=3,command = option, font=("Arial",12))
btn3.pack()

label_space = Label(pw)
label_space.pack()

label_len = Label(pw, text="Give Strength of Password:", font=("Gintronic",12))
label_len.pack()

num=IntVar()
label_entry = Spinbox(pw, from_= 8, to_=15, textvariable=num, width=18, font=10)
label_entry.pack()

def callback():
    output.config(text=genpass())

label_space = Label(pw)
label_space.pack()

btn4 = Button(pw, text="Generate Password", font=("Arial",12), command=callback)
btn4.pack()

output = Message(pw, text="",relief=RAISED, width=180,font=20)
output.pack(side=BOTTOM)

poor = string.ascii_lowercase + string.ascii_uppercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
strong = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.ascii_letters

def genpass():
    if choice.get() == 1:
        return "".join(random.sample(poor, num.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, num.get()))
    elif choice.get() == 3:
        return "".join(random.sample(strong, num.get()))

pw.mainloop()





