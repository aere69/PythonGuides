from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
PATH_TO_PROJECT = "./Projects/Intermediate/FlashCardsApp/"
current_card = {}

#--- import card data
try:
    data = pandas.read_csv(PATH_TO_PROJECT+"data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(PATH_TO_PROJECT+"data/french_words.csv")

to_learn = data.to_dict(orient="records")

#---- next_card : button command
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

#---- flip_card : window timer function
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

#---- Known words should be removed from list next time.
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv(PATH_TO_PROJECT+"data/words_to_learn.csv", index=False)

#---- UI ----

#---- Create main program window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#---- Create a canvas for the cards
#---- Use card image width and heigh for the canvas
canvas = Canvas(width=800, height=526)

#---- Create Image resources
card_front_img = PhotoImage(file=PATH_TO_PROJECT+"images/card_front.png")
card_back_img = PhotoImage(file=PATH_TO_PROJECT+"images/card_back.png")
right_button_img = PhotoImage(file=PATH_TO_PROJECT+"images/right.png")
wrong_button_img = PhotoImage(file=PATH_TO_PROJECT+"images/wrong.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()


