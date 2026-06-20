from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Contact Book Management System")
root.geometry("1000x650")
root.config(bg="#f5f7fa")
root.resizable(False, False)

contacts = []

# ================= FUNCTIONS =================

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])

    contact_table.insert(
        "",
        END,
        values=(name, phone, email, address)
    )

    messagebox.showinfo("Success", "Contact Added Successfully")
    clear_fields()

def select_contact(event):
    selected = contact_table.focus()

    if selected:
        values = contact_table.item(selected, "values")

        name_var.set(values[0])
        phone_var.set(values[1])
        email_var.set(values[2])
        address_var.set(values[3])

def update_contact():
    selected = contact_table.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first")
        return

    contact_table.item(
        selected,
        values=(
            name_var.get(),
            phone_var.get(),
            email_var.get(),
            address_var.get()
        )
    )

    messagebox.showinfo("Updated", "Contact Updated Successfully")
    clear_fields()

def delete_contact():
    selected = contact_table.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first")
        return

    contact_table.delete(selected)

    messagebox.showinfo("Deleted", "Contact Deleted Successfully")
    clear_fields()

def search_contact():
    keyword = search_var.get().lower()

    for item in contact_table.get_children():
        contact_table.delete(item)

    for contact in contacts:
        if (keyword in contact[0].lower() or
                keyword in contact[1]):

            contact_table.insert(
                "",
                END,
                values=contact
            )

# ================= VARIABLES =================

name_var = StringVar()
phone_var = StringVar()
email_var = StringVar()
address_var = StringVar()
search_var = StringVar()

# ================= TITLE =================

title = Label(
    root,
    text="CONTACT BOOK MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=15
)

title.pack(fill=X)

# ================= FORM FRAME =================

form_frame = Frame(root, bg="white")
form_frame.place(x=20, y=80, width=350, height=520)

Label(form_frame, text="Name",
      font=("Arial", 12, "bold"),
      bg="white").place(x=20, y=30)

Entry(form_frame,
      textvariable=name_var,
      font=("Arial", 12),
      width=25).place(x=120, y=30)

Label(form_frame, text="Phone",
      font=("Arial", 12, "bold"),
      bg="white").place(x=20, y=90)

Entry(form_frame,
      textvariable=phone_var,
      font=("Arial", 12),
      width=25).place(x=120, y=90)

Label(form_frame, text="Email",
      font=("Arial", 12, "bold"),
      bg="white").place(x=20, y=150)

Entry(form_frame,
      textvariable=email_var,
      font=("Arial", 12),
      width=25).place(x=120, y=150)

Label(form_frame, text="Address",
      font=("Arial", 12, "bold"),
      bg="white").place(x=20, y=210)

Entry(form_frame,
      textvariable=address_var,
      font=("Arial", 12),
      width=25).place(x=120, y=210)

Button(form_frame,
       text="Add Contact",
       bg="#27ae60",
       fg="white",
       font=("Arial", 11, "bold"),
       command=add_contact).place(x=20, y=300)

Button(form_frame,
       text="Update",
       bg="#2980b9",
       fg="white",
       font=("Arial", 11, "bold"),
       command=update_contact).place(x=140, y=300)

Button(form_frame,
       text="Delete",
       bg="#c0392b",
       fg="white",
       font=("Arial", 11, "bold"),
       command=delete_contact).place(x=240, y=300)

Button(form_frame,
       text="Clear",
       bg="#7f8c8d",
       fg="white",
       font=("Arial", 11, "bold"),
       command=clear_fields).place(x=140, y=360)

# ================= SEARCH =================

Label(root,
      text="Search Contact",
      bg="#f5f7fa",
      font=("Arial", 12, "bold")
      ).place(x=420, y=90)

Entry(root,
      textvariable=search_var,
      font=("Arial", 12),
      width=30
      ).place(x=560, y=90)

Button(root,
       text="Search",
       bg="#8e44ad",
       fg="white",
       font=("Arial", 10, "bold"),
       command=search_contact
       ).place(x=830, y=86)

# ================= TABLE =================

table_frame = Frame(root)
table_frame.place(x=400, y=140,
                  width=570, height=450)

scroll_y = Scrollbar(table_frame,
                     orient=VERTICAL)

contact_table = ttk.Treeview(
    table_frame,
    columns=("Name",
             "Phone",
             "Email",
             "Address"),
    yscrollcommand=scroll_y.set
)

scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=contact_table.yview)

contact_table.heading("Name", text="Name")
contact_table.heading("Phone", text="Phone")
contact_table.heading("Email", text="Email")
contact_table.heading("Address", text="Address")

contact_table["show"] = "headings"

contact_table.column("Name", width=120)
contact_table.column("Phone", width=120)
contact_table.column("Email", width=150)
contact_table.column("Address", width=150)

contact_table.pack(fill=BOTH, expand=1)

contact_table.bind(
    "<ButtonRelease-1>",
    select_contact
)

root.mainloop()