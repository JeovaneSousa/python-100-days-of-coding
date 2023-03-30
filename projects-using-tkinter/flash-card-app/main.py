from tkinter import *
import pandas
import random

TITLE_FONT = ("Ariel", 40, "italic")
SUBTITLE_FONT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"


# ------------------------------------Helper Methods---------------------------------------#
def already_know():
    data_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title_text, text="French", fil="black")
    canvas.itemconfig(word_text, text=current_card["French"], fil="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fil="white")
    canvas.itemconfig(word_text, text=current_card["English"], fil="white")


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError as e:
    print(f"The following exception occurred: {e}")
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")

current_card = {}

# ------------------------------------UI Setup---------------------------------------#
window = Tk()
window.title("Flash Card Game")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT, )
word_text = canvas.create_text(400, 263, text="Word", font=SUBTITLE_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=already_know)
right_button.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)
next_card()

if __name__ == "__main__":
    window.mainloop()
