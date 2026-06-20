from tkinter import *
from tkinter import messagebox

# Main Window
root = Tk()
root.title("To-Do List Manager")
root.state("zoomed")  # Maximize window
root.configure(bg="#1e1e2f")

tasks = []

# Add Task
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        tasks.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)

# Delete Task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Update Task
def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task == "":
            messagebox.showwarning("Warning", "Enter updated task!")
        else:
            tasks[selected] = new_task
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            task_entry.delete(0, END)

    except:
        messagebox.showwarning("Warning", "Select a task to update!")

# Clear All Tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, END)
        tasks.clear()

# Title
title = Label(
    root,
    text="TO-DO LIST MANAGER",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Entry Frame
entry_frame = Frame(root, bg="#1e1e2f")
entry_frame.pack(pady=10)

task_entry = Entry(
    entry_frame,
    width=40,
    font=("Arial", 16),
    bd=3
)
task_entry.pack()

# Button Frame
frame = Frame(root, bg="#1e1e2f")
frame.pack(pady=15)

add_btn = Button(
    frame,
    text="Add Task",
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=add_task
)
add_btn.grid(row=0, column=0, padx=10)

update_btn = Button(
    frame,
    text="Update Task",
    bg="orange",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=update_task
)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = Button(
    frame,
    text="Delete Task",
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=delete_task
)
delete_btn.grid(row=0, column=2, padx=10)

# Listbox Frame
list_frame = Frame(root)
list_frame.pack(pady=20)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    list_frame,
    width=60,
    height=18,
    font=("Arial", 14),
    bg="white",
    fg="black",
    selectbackground="#4a90e2",
    yscrollcommand=scrollbar.set
)

listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)

# Clear Button
clear_btn = Button(
    root,
    text="Clear All Tasks",
    bg="purple",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    command=clear_tasks
)
clear_btn.pack(pady=15)

# Footer
footer = Label(
    root,
    text="Python GUI Based To-Do List Application",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="lightgray"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()