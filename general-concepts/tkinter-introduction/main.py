from tkinter import *

def tell_when_clicked():
    label["text"] = input.get()

window = Tk()
window.title("lala")
window.minsize(width= 300, height= 200)
window.config(padx=20, pady=20)

label = Label(text= "My first Label", font=("arial", 24))
label.grid(row=1, column=1)
label["text"] = "New Label"

button1 = Button(text="Click me", command=tell_when_clicked)
button1.grid(row= 2, column=2)

button2 = Button(text="New button")
button2.grid(row= 1, column=3)

input = Entry(width=10)
input.grid(row=3, column=4)










window.mainloop()

