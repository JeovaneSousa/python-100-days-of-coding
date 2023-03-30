from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler app")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text=f"Question here", 
            fill=THEME_COLOR, 
            font=FONT
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        TRUE_IMAGE = PhotoImage(file="images/true.png")
        self.true_button = Button(image=TRUE_IMAGE, height=100, width=100, highlightthickness=0,command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)

        FALSE_IMAGE = PhotoImage(file="images/false.png")
        self.false_button = Button(image=FALSE_IMAGE, height=100, width=100, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)

        self.next_question()
        
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You`ve reached the end of the Quiz")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.quiz.check_answer(user_answer=True)
        self.give_feedback(is_right)
        
    def false_button_pressed(self):
        is_right = self.quiz.check_answer(user_answer=False)
        self.give_feedback(is_right)
    
    def give_feedback(self, outcome: bool):
        self.scoreLabel.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")

        if outcome:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
    
        self.window.after(ms=1000, func=self.next_question)
        