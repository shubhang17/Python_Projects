from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox
from random import shuffle,randint,choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for char in range(randint(8, 10))]
    password_symbols=[choice(symbols) for char in range(randint(2, 4))]
    password_numbers=[choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password= "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website= website_entry.get()
    email= email_entry.get()
    password=password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't Leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading Old Data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            #Updating Old data with new data
            data.update(new_data)
            with open("data.json","w") as data_file:
                #Saving Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No Deatils for {website} exists.")






# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Canvas
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column= 1, row= 0)

#label
website_label = Label(text="Website:")
website_label.grid(column= 0, row= 1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column= 0, row= 2)

password_label = Label(text="Password:")
password_label.grid(column= 0, row= 3)

#Entry
website_entry = Entry(width=17)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"shubhangagarwal1710@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(row=3,column=1)

#Button
generate_password_button = Button(text="Generate Password",command=password_generator)
generate_password_button.grid(column=2,row=3)

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)

add_button = Button(text="Add",width=30,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()