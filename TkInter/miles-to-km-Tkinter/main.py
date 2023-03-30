from tkinter import *

FONT_PATTERN = ("arial", 24, "bold")
def button_click():
    miles = float(input.get())
    if miles != 0:
        total_in_km = miles * 1.609
        label_4.config(text=f"{total_in_km}")


window = Tk()
window.title("Miles to KM Converter")
window.config(height=300, width=400)
window.config(pady=20, padx=20)

input = Entry(width=8)
input.grid(row=0, column=1)

label_1 = Label(text="Miles", font=FONT_PATTERN)
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to", font=FONT_PATTERN)
label_2.grid(row=1, column=0)

label_3 = Label(text="Km", font=FONT_PATTERN)
label_3.grid(row=1, column=2)

label_4 = Label(text=0, font=FONT_PATTERN)
label_4.grid(row=1, column=1)

button = Button(text="Do the magic!", command=button_click)
button.grid(row=2, column=1)

window.mainloop()
