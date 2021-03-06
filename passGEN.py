import random
from tkinter import *
import string
from tkinter import messagebox
from tkinter.ttk import *

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
# root.iconbitmap("D:/CODE/PasGEN/logo.ico")    # logo
# Entry and Label
random_password = Label(root, text="Password")
random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# password Label
c_label = Label(root, text="Lengh")
c_label.grid(row=1)

# Password Major Functions
def low ():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh
ijklmnopqrstuvwxyz0123456789@#"""
    password = ""
    # low Password
    if var.get() == 1:
        for i in range(length):
            password += random.choice(lower)
        return password
    # medium Password
    elif var.get() == 0:
        for i in range(length):
            password += random.choice(upper)
        return password
    # strong Password
    elif var.get() == 3:
        for i in range(length):
            password += random.choice(digits)
        return password
    else:
        messagebox.showwarning('Python says', 'First Select a Option')

# Generate Function
def generate():
    password1 = low()
    entry.insert(10, password1)

# Copy to clipboard
def clipboard():
    random_pass = entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_pass)

# Major Button
copy_btn = Button(root, text="Copy", command=clipboard)
copy_btn.grid(row=0, column=2)
generate_btn = Button(root, text="Generate", command=generate)
generate_btn.grid(row=0, column=3)
exit_btn = Button(root, text="Exit", command=root.quit)
exit_btn.grid(row=0, column=4)
# Radio Button
low_Rbtn = Radiobutton(root, text="Low", variable=var, value=1)
low_Rbtn.grid(row=1, column=2, sticky="E")
medium_Rbtn = Radiobutton(root, text="Medium", variable=var, value=0)
medium_Rbtn.grid(row=1, column=3, sticky="E")
strong_Rbtn = Radiobutton(root, text="Strong", variable=var, value=3)
strong_Rbtn.grid(row=1, column=4, sticky="E")
# combo box for length
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                    17, 18, 19, 20, 21, 22, 23, 24, 
                    25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(row=1, column=1)

root.mainloop()
