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

def edit_task():
    try:
        selected = t_list.curselection()[0]
        previous_task_name = t_list.get(selected)
        task = t_entry.get()
        if task and previous_task_name != task:
            t_list.delete(selected)
            t_list.insert(selected, task)
            t_entry.delete(0, tk.END)
        elif previous_task_name == task:
            t_entry.delete(0, tk.END)
            messagebox.showwarning("Error", "Same Name!")
        else:
            messagebox.showwarning("Warning!", "The Task name can't be empty")
    except IndexError:
        messagebox.showwarning("Warning!", "Nothing is selected to edit")

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

btn_1 = tk.Button(app, text="Add Task", font=("JetBrains Mono",11), command=add_task, width=11, bg='#32CD32')
btn_1.place(x=10, y=90)

btn_2 = tk.Button(app, text="Delete Task", font=("JetBrains Mono",11),command=del_task, width=11, bg='#FF0000')
btn_2.place(x=125, y=90)

btn_3 = tk.Button(app, text="Update Task", font=("JetBrains Mono",11),command=edit_task, width=10, bg='#FFFF00')
btn_3.place(x=240, y=90)

t_list = Listbox(app, width = 36, height= 12, font=('JetBrains Mono',12))
t_list.place(x=10, y=140)

load_tasks()

app.mainloop()


