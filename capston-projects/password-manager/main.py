from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
LABEL_FONT = ('arial', 14, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    n_letters = randint(8, 12)
    n_numbers = randint(2, 4)
    n_symbols = randint(2, 4)

    password_prep = []
    [password_prep.append(choice(letters)) for _ in range(n_letters)]
    [password_prep.append(choice(numbers)) for _ in range(n_numbers)]
    [password_prep.append(choice(symbols)) for _ in range(n_symbols)]
    shuffle(password_prep)

    password = "".join(password_prep)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title='Yay!', message='Password copied to Clipboard')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    used_email = email_entry.get()
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, used_email)
    password_entry.delete(0, END)
    website_entry.focus()


def save():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title='ooops', message="Please, fill in all the fields correctly")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Username: {username}\n '
                                                              f'Password: {password}\n Is it ok to save?')
        if is_ok:
            with open("password-vault.txt", mode='a') as file:
                file.write(
                    f"{website} | {username} | {password} \n\n")

            clear()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(pady=20, padx=20, bg='white')

canvas = Canvas(height=200, width=200, bg='white', highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Labels -----------------------------------
website_label = Label(text='Website:', width=18, font=LABEL_FONT, fg='black', bg='white')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=LABEL_FONT, fg='black', bg='white')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=LABEL_FONT, fg='black', bg='white')
password_label.grid(row=3, column=0)

# Entry's -----------------------------------

website_entry = Entry(width=38, bg='white', fg='black')
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=38, bg='white', fg='black')
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'your-email@icloud.com')

password_entry = Entry(width=21, bg='white', fg='black')
password_entry.grid(row=3, column=1)

# Buttons -----------------------------------
password_generation_button = Button(text='Generate password', highlightthickness=0, fg='black', bg='white', command=generate_password)
password_generation_button.grid(row=3, column=2)

add_password_button = Button(text='Add password', width=36, highlightthickness=0, fg='black', bg='white', command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
