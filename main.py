from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password():
    entry_password.delete(0,END)
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    r_password = ''.join(random.choice(characters) for _ in range(12))

    entry_password.insert(0, r_password)
    return r_password

def copy_pw():
    pyperclip.copy(generate_random_password())


# # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get().title()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password,
        }    
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Error", message="You left some fields empty")
    else:
        is_ok =  messagebox.askokcancel(title=website, message=f"These are the deatials entered: \n"
        f"Email: {email} \nPassword:{password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                     data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                     json.dump(new_data, data_file, indent=4)
            else:               
                data.update(new_data)
                with open("data.json", "w") as data_file:
                     json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0,END)

# Search Function yo find login details
def search():
    website = entry_website.get().title()
    try:
        with open("data.json","r") as data_file:
             data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no data file existing")
    else:
       if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
       else:
            messagebox.showinfo(title="Error", message=f"No details for website '{website}' found. ")


# # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
 
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
 
entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus_set()
 
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
entry_email = Entry()
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")
 
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons

generate_btn = Button(text="Generate Password", command=generate_random_password)
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, command= save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

copy_btn = Button(text="Copy Password",width=35, command=copy_pw)
copy_btn.grid(row=5, column=1, columnspan=2, sticky="EW")

search_btn = Button(text="Search", command=search )
search_btn.grid(column=2, row=1, sticky="EW")
 
mainloop()
