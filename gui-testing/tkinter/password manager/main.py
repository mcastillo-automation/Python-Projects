import random
import string
import json
from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password_generator():
    accepted_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = ''.join(random.choices(string.ascii_letters + string.digits +
                                      ''.join(accepted_symbols), k=17))

    if password_field.get().strip() == '':
        password_field.insert(index=0, string=password)
        pyperclip.copy(password)

    else:
        password_field.delete(first=0, last='end')
        password_field.insert(index=0, string=password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website_entry = website_field.get().strip()
    email_entry = email_field.get().strip()
    password_entry = password_field.get().strip()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }
    if website_entry == "" or email_entry == "" or password_entry == "":
        messagebox.showerror(message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            messagebox.showinfo(message="Password Saved")
            website_field.delete(first=0, last='end')
            email_field.delete(first=0, last='end')
            password_field.delete(first=0, last='end')
            website_field.focus()


# ---------------------------- SEARCH --------------------------------- #

def search():
    website_entry = website_field.get().strip()

    if website_entry == "":
        messagebox.showerror(message="Unable to search without website!")

    else:
        try:
            with open("data.json", mode='r') as file:
                text = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
        else:
            try:
                messagebox.showinfo(
                    message=f"Email: {text[website_entry]['email']}\nPassword: {text[website_entry]['password']}")
            except KeyError as error_message:
                messagebox.showerror(message=f"No details for {error_message} exist.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create MyPass Canvas
canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Text-fields
website_field = Entry(width=35)
website_field.focus()
email_field = Entry(width=35)
password_field = Entry(width=21)

# Buttons
generate_button = Button(text="Generate Password", command=random_password_generator)
add_button = Button(text="Add", width=36, command=save_entry)
search_button = Button(text="Search", command=search)

# Grids
website_label.grid(row=1, column=0, sticky="e")
website_field.grid(row=1, column=1, columnspan=2, sticky="we")
search_button.grid(row=1, column=2, sticky="e")
email_label.grid(row=2, column=0, sticky="e")
email_field.grid(row=2, column=1, columnspan=2, sticky="we")
password_label.grid(row=3, column=0, sticky="e")
password_field.grid(row=3, column=1, sticky="we")
generate_button.grid(row=3, column=2, sticky="e")
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
