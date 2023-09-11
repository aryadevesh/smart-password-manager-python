from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ----------------------------- Search -------------------------------------------#

def search():
    website_text = website_entry.get().lower()
    if len(website_text) == 0:
        messagebox.showinfo(title="error", message="Please fill up the website details.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data file exist\n")
        else:
            if website_text in data:
                email = data[website_text]["email"]
                password = data[website_text]["password"]
                messagebox.showinfo(title=website_text, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details exist with website: {website_text}\n")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    email_password_entry.delete(0, END)
    email_password_entry.insert(0, password)
    pyperclip.copy(text=password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": email_password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(email_password_entry.get()) == 0:
        var = messagebox.showerror(title="Oops", message="Please fill all the details.\n")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            email_password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, )
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)

website_entry = Entry(width=27)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, columnspan=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aryadevesh78@gmail.com")

email_password = Label(text="Password:")
email_password.grid(column=0, row=3)

email_password_entry = Entry(width=27)
email_password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=password_gen)
generate_pass_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
