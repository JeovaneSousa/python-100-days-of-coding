from tkinter import *

LABEL_FONT = ('arial', 14, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password_data = {'website': website_entry.get(),
                     'email/username': email_entry.get(),
                     'password': password_entry.get()
                     }
    with open("password-vault.txt", mode='a') as vault:
        vault.write(f"{password_data.get('website')} | {password_data.get('email/username')} | {password_data.get('password')} \n\n")
    used_email = email_entry.get()

    def clear():
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, used_email)
        password_entry.delete(0, END)
        website_entry.focus()

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
password_generation_button = Button(text='Generate password', highlightthickness=0, fg='black', bg='white')
password_generation_button.grid(row=3, column=2)

add_password_button = Button(text='Add password', width=36, highlightthickness=0, fg='black', bg='white', command=save)
add_password_button.grid(row=4, column=1, columnspan=2)





window.mainloop()
