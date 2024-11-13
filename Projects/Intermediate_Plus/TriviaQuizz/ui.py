from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PATH_TO_PROJECT = "./Projects/Intermediate_Plus/TriviaQuizz/"

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quizz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text="Next Question....",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file=PATH_TO_PROJECT+"images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=PATH_TO_PROJECT+"images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz.still_has_questions():
            q_txt = self.quizz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)
        else:
            self.end_of_game()

    def true_clicked(self):
        is_right = self.quizz.check_answer("true")
        self.give_feedback(is_right)

    def false_clicked(self):
        is_right = self.quizz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            #set canvas green
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score : {self.quizz.score}")
        else:
            #set canvas red
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

    def end_of_game(self):
        eog = f"Final score : {self.quizz.score}/{self.quizz.question_number}"
        self.canvas.itemconfig(self.question_text, text=eog)
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

