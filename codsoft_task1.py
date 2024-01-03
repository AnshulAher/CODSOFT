from tkinter import *
from tkinter import messagebox
import tkinter as tk

app = Tk()
app.title('To-Do List')
app.geometry('350x400')
app.config(bg='#191970')

def add_task():
    task = t_entry.get()
    if task:
        t_list.insert(0,task)
        t_entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Enter a task')

def del_task():
    selected = t_list.curselection()
    if selected:
        t_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error','Choose a task first!')

def save_tasks():
    with open("tasks.txt","w") as f:
        tasks = t_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                t_list.insert(0,task.strip())
    except FileNotFoundError:
        pass

t_entry = tk.Entry(app, font='Hack', width = 28)
t_entry.place(x=20,y=40)

btn_1 = tk.Button(app, text="Add Task", font=("JetBrains Mono",12), command=add_task, width=12, bg='#32CD32')
btn_1.place(x=50, y=90)

btn_2 = tk.Button(app, text="Delete Task", font=("JetBrains Mono",12),command=del_task, width=12, bg='#FF0000')
btn_2.place(x=200, y=90)

t_list = Listbox(app, width = 36, height= 12, font=('JetBrains Mono',12))
t_list.place(x=10, y=140)

load_tasks()

app.mainloop()