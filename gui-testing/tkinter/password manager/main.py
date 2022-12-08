from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website_entry = website_field.get().strip()
    email_entry = email_field.get().strip()
    password_entry = password_field.get().strip()

    if website_entry == "" or email_entry == "" or password_entry == "":
        messagebox.showerror(message="Please don't leave any fields empty!")

    else:
        confirmation = messagebox.askokcancel(
            message=f"Is the below info accurate?\nEmail: {email_entry}\nPassword: {password_entry}",
            icon='question',
            title="Confirmation"
        )
        if confirmation is True:
            with open("data.txt", mode='a') as file:
                file.write(f"{website_entry} | {email_entry} | {password_entry}\n")
            messagebox.showinfo(message="Password Saved")

        website_field.delete(0, 'end')
        email_field.delete(0, 'end')
        password_field.delete(0, 'end')
        website_field.focus()


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
generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36, command=save_entry)

# Grids
website_label.grid(row=1, column=0, sticky="e")
website_field.grid(row=1, column=1, columnspan=2, sticky="we")
email_label.grid(row=2, column=0, sticky="e")
email_field.grid(row=2, column=1, columnspan=2, sticky="we")
password_label.grid(row=3, column=0, sticky="e")
password_field.grid(row=3, column=1, sticky="we")
generate_button.grid(row=3, column=2, sticky="e")
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
