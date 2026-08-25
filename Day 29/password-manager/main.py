import tkinter as tk
from json import JSONDecodeError
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        #
        # if is_ok:
        try:
            with open("./data.json", mode="r", encoding="utf-8") as file:
                # Reading the current saved data from data.json
                current_data = json.load(file)

        except FileNotFoundError, JSONDecodeError:
            with open("./data.json", mode="w", encoding="utf-8") as file:
                # Creating the data.json file and adding data for the first time
                json.dump(new_data, file, indent=4)
        else:
            # Updating current data with the new data
            current_data.update(new_data)

            with open("./data.json", mode="w", encoding="utf-8") as file:

                # Saving the updated data into the data.json
                json.dump(current_data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            email_entry.insert(0, "aumsoni2002@gmail.com")
            password_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    if len(website.strip()) == 0:
        messagebox.showinfo(title="Error", message="Please enter a website name")
    else:
        try:
            with open("./data.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        except JSONDecodeError:
            messagebox.showinfo(title="Error", message="The Data File is empty")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CANVAS(displays an image), Location: column=1, row=0, shows the image './logo.png'
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABEL(displays text), Location: column=0, row=1, shows the text 'Website:'
website_label = tk.Label(window, text="Website:")
website_label.grid(column=0, row=1)

# ENTRY(single line text input), Location: column=1, row=1, User enters website name
website_entry = tk.Entry(window, width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# BUTTON(runs a function to search for a website name from data.json file), Location: column=2, row=1, shows the button 'Search'
search_button = tk.Button(window, text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

# LABEL(displays text), Location: column=0, row=2, shows the text 'Email/Username:'
email_label = tk.Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)

# ENTRY(single line text input), Location: column=1, row=2, User enters email or username
email_entry = tk.Entry(window, width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aumsoni2002@gmail.com")

# LABEL(displays text), Location: column=0, row=3, shows the text 'Password:'
password_label = tk.Label(window, text="Password:")
password_label.grid(column=0, row=3)

# ENTRY(single line text input), Location: column=1, row=3, User enters password
password_entry = tk.Entry(window, width=21)
password_entry.grid(column=1, row=3)

# BUTTON(runs a function to generate password when clicked), Location: column=2, row=3, shows the button 'Generate Password'
generate_password_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# BUTTON(runs a function to add password to a file when clicked), Location: column=1, row=4, shows the button 'Generate Password'
add_button = tk.Button(window, text="Add", width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
