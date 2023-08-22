from tkinter import *
import math
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(numbers) for char in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    entry2.insert(0, "".join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = entry.get()
    email = entry1.get()
    password = entry2.get()
    new_data = {website: {
            "email": email,
            "password": password,}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)
            with open("data.json", mode="w") as file:
                #saving updated data
                json.dump(data, file, indent= 4)

                entry.delete(0, END)
                entry2.delete(0, END)
        except json.JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent= 4)
                entry.delete(0, END)
                entry2.delete(0, END)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent= 4)
                entry.delete(0, END)
                entry2.delete(0, END)

def search():
    website = entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.config(padx=100, pady=50)


window.title("Password Manager")


canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=mypass_image)

canvas.grid(column=1, row=1)

label = Label(text="Website:")
label.grid(column=0, row=2)
entry = Entry(width=30)
entry.grid(column=1, row=2)
entry.focus()
seach_button = Button(text="Search", width=15, command = search)
seach_button.grid(column=2, row=2)


label1 = Label(text="Email/Username:")
label1.grid(column=0, row=3)
entry1 = Entry(width=30)
entry1.grid(column=1, row=3)
entry1.insert(END, string="jm31934@gmail.com")


label2 = Label(text="Password:")   
label2.grid(column=0, row=4)
entry2 = Entry(width=30)
entry2.grid(column=1, row=4)
button = Button(text="Generate Password", width=36, command = generate_password)
button.grid(column=2, row=4, columnspan= 1)

button1 = Button(text="Add", width=36, command = save_to_file)
button1.grid(column = 0, row=5, columnspan=2)







window.mainloop()