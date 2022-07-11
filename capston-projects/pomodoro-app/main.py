import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    check_marks.config(text="")
    canvas.itemconfig(time_text,text= "00:00")
    title_label.config(text="Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        title_label.config(text= "Work Time!", fg= GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_label.config(text="Long break!!", fg=RED)
        count_down(long_break_sec)
    else:
        title_label.config(text="Quick rest", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    print(time_scale.get())
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks_to_write = reps / 2
        checks_text = ""
        if reps % 2 == 0:
            for check in range(int(checks_to_write)):
                checks_text += "✅"

            check_marks.config(text=checks_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0,command=start_timer)
start_button.grid(row=2, column=0)

check_marks = Label(text="", highlightthickness=0, bg=YELLOW)
check_marks.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

time_scale = Scale(from_=0, to=60, bg=GREEN)
time_scale.grid(row=1, column=0)

window.mainloop()
