# ---------------------------- IMPORT LIBRARIES -------------------------#
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json

# ---------------------------- DEFINE CONSTANTS -------------------------#
PATH_TO_PROJECT = "./Projects/Intermediate/SimplePasswordManager/"
MAX_LETTERS = 13
MAX_NUMBERS = 4
MAX_SYMBOLS = 3

# ---------------------------- GLOBAL VARIABLES -------------------------#
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_dict = {}

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(num_letters, num_numbers, num_symbols):
    """Generates a hard password"""
    password_list = []
    password_letters = []
    password_numbers = []
    password_symbols = []

    if num_letters > 0:
        password_letters = [choice(letters) for _ in range(num_letters)]
    if num_symbols > 0:
        password_symbols = [choice(symbols) for _ in range(num_symbols)]
    if num_numbers > 0:
        password_numbers = [choice(numbers) for _ in range(num_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    # Convert the list to string
    new_password_list = "".join(map(str,password_list))

    # Copy new password to the clipboard
    pyperclip.copy(new_password_list)

    return new_password_list


# ---------------------------- LOAD PASSWORD ------------------------------- #
def search_passwords(website):
    try:
        with open(PATH_TO_PROJECT+"data.json","r") as file:
            json_doc = json.load(file)
    except FileNotFoundError:
        return {}
    else:
        try:
            found = json_doc[website]
        except KeyError:
            return {}
        else:
            return found

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Incomplete information")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Credentials provided...\n\nUsername: {username}\nPassword: {password}\n\nContinue?")

        if is_ok:
            new_data = {
                website: {
                    "username": username,
                    "password": password,
                }
            }

            try:
                with open(PATH_TO_PROJECT+"data.json","r") as file:
                    # Read old data
                    old_data = json.load(file)
            except FileNotFoundError:
                old_data = {}
            finally:
                # Update old data with new data
                old_data.update(new_data)

            with open(PATH_TO_PROJECT+"data.json","w") as file:
                # Save Updated data
                json.dump(old_data, file, indent=2)
    
                # clean up entries
                website_input.delete(0,END)
                password_input.delete(0,END)

    website_input.focus()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Simple Passord Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=PATH_TO_PROJECT+"logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

# --- Website
website_label = Label(text="Website :")
website_label.grid(row=1,column=0)

website_input = Entry(width=42)
website_input.grid(row=1,column=1, columnspan=2)
website_input.focus()

#Buttons
def search_action():
    search_result = search_passwords(website_input.get())
    if search_result == {}:
        messagebox.showinfo(title=website_input.get(), message="No information found.")
        password_input.delete(0,END)
    else:
        messagebox.showinfo(title=website_input.get(), message=f"Username: {search_result["username"]}\nPassword: {search_result["password"]}")

        # Clear password_input (Entry value)
        password_input.delete(0,END)
        password_input.insert(0, search_result["password"])

        # Copy new password to the clipboard
        pyperclip.copy(search_result["password"])

#calls action() when pressed
search_password_button = Button(text="Search Password", command=search_action)
search_password_button.grid(row=1,column=2)

# --- User Name/email
username_label = Label(text="Username/Email :")
username_label.grid(row=2,column=0)

username_input = Entry(width=42)
#Add sdefault email to begin with
username_input.insert(END, string="mymail@mail.com")
username_input.grid(row=2,column=1, columnspan=2)

# --- Password
password_label = Label(text="Password :")
password_label.grid(row=3,column=0)

password_input = Entry(width=24)
password_input.grid(row=3,column=1)

#Buttons
def action():
    # Clear password_input (Entry value)
    password_input.delete(0,END)
    password_input.insert(0, generate_password(MAX_LETTERS,MAX_NUMBERS,MAX_SYMBOLS))

#calls action() when pressed
generate_password_button = Button(text="Generate Password", command=action)
generate_password_button.grid(row=3,column=2)

# --- Add Button ---
#Buttons
def add_action():
    save_password()

#calls action() when pressed
add_button = Button(text="Add", width=30, command=add_action)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()