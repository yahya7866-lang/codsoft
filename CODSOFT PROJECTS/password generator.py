from tkinter import *
from tkinter import messagebox
import random
import string



def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid password length!")
            return

        chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")


def copy_password():
    password = result_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first!")


def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)




root = Tk()
root.title("Password Generator")


root.attributes("-fullscreen", True)


root.configure(bg="#f5f5f5")


title = Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 32, "bold"),
    bg="#f5f5f5",
    fg="#1f2937"
)
title.pack(pady=40)


desc = Label(
    root,
    text="Generate Strong and Random Passwords",
    font=("Arial", 18),
    bg="#f5f5f5"
)
desc.pack(pady=10)


frame = Frame(root, bg="white", bd=3, relief=RIDGE)
frame.pack(pady=50)


Label(
    frame,
    text="Enter Password Length",
    font=("Arial", 16, "bold"),
    bg="white"
).grid(row=0, column=0, padx=20, pady=20)


length_entry = Entry(
    frame,
    font=("Arial", 16),
    width=15,
    justify="center"
)
length_entry.grid(row=0, column=1, padx=20)


Button(
    frame,
    text="Generate Password",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_password
).grid(row=1, column=0, columnspan=2, pady=20)


result_var = StringVar()

Entry(
    frame,
    textvariable=result_var,
    font=("Consolas", 16),
    width=35,
    justify="center"
).grid(row=2, column=0, columnspan=2, pady=20)


Button(
    frame,
    text="Copy Password",
    font=("Arial", 14, "bold"),
    bg="#2196F3",
    fg="white",
    command=copy_password
).grid(row=3, column=0, columnspan=2, pady=15)


Label(
    root,
    text="Press ESC to Exit Full Screen",
    font=("Arial", 12),
    bg="#f5f5f5",
    fg="gray"
).pack(side=BOTTOM, pady=20)


root.bind("<Escape>", exit_fullscreen)

root.mainloop()