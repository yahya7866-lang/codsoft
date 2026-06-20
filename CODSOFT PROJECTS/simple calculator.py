from tkinter import *

# Main Window
root = Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Display
display = Entry(root, font=("Arial", 24), bd=10, relief=RIDGE, justify="right")
display.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def click(value):
    display.insert(END, value)

def clear():
    display.delete(0, END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")

# Button Frame
frame = Frame(root)
frame.pack()

# Button Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create Buttons
for row in buttons:
    row_frame = Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "C":
            Button(
                row_frame,
                text=btn,
                font=("Arial", 18),
                width=5,
                height=2,
                command=clear
            ).pack(side=LEFT, expand=True, fill="both")
        elif btn == "=":
            Button(
                row_frame,
                text=btn,
                font=("Arial", 18),
                width=5,
                height=2,
                command=calculate
            ).pack(side=LEFT, expand=True, fill="both")
        else:
            Button(
                row_frame,
                text=btn,
                font=("Arial", 18),
                width=5,
                height=2,
                command=lambda b=btn: click(b)
            ).pack(side=LEFT, expand=True, fill="both")

root.mainloop()