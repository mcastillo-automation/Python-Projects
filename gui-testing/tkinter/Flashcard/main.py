from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------- Random Word -------
try:
    fr_en_data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    fr_en_data = pandas.read_csv('data/french_words.csv')
finally:
    to_learn = fr_en_data.to_dict(orient='records')
card_object = {}


def next_card():
    global card_object, flip_timer
    window.after_cancel(flip_timer)
    card_object = random.choice(to_learn)
    fr_word = card_object['French']
    canvas.itemconfig(card_bg, image=card_front_image)
    canvas.itemconfig(card_lang, text='French', fill='black')
    canvas.itemconfig(card_word, text=fr_word, fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    en_word = card_object['English']
    canvas.itemconfig(card_bg, image=card_back_image)
    canvas.itemconfig(card_lang, text='English', fill='white')
    canvas.itemconfig(card_word, text=en_word, fill='white')


def is_known():
    to_learn.remove(card_object)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# --------- UI Setup ----------

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title('Flashy')

flip_timer = window.after(3000, flip_card)

# Images
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
wrong_button_image = PhotoImage(file='images/wrong.png')
right_button_image = PhotoImage(file='images/right.png')

# Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 264, image=card_front_image, tags='card_image')
card_lang = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
