from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card={}


def select():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    select()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 265, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
un_no_button = Button(image=x_img, highlightthickness=0, command=select)
un_no_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
no_button = Button(image=right_img, highlightthickness=0, command=is_known)
no_button.grid(row=1, column=1)

select()





























window.mainloop()

