import random
import tkinter
from tkinter import *

CHOICES = [
    'Да',
    'Нет',
    'Спроси об этом позже',
    'Может быть',
    'Вероятность 50/50',
    'Лучше не спрашивай',
    'Это плохая идея',
    'Конечно',
]


class App(object):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        photo = tkinter.PhotoImage(file="eye1.gif")

        self.answer_text = tkinter.StringVar()
        self.crystal_ball = tkinter.Label(frame, image=photo)

        self.answer = tkinter.Label(frame, font=("Helvetica", 16), textvariable=self.answer_text)
        self.crystal_ball.image = photo
        self.crystal_ball.pack()
        self.answer.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.quit_bottom = tkinter.Button(frame, text="QUIT", command=frame.quit)
        self.quit_bottom.pack(side=tkinter.RIGHT)

        self.ask_button = tkinter.Button(frame, text="ASK", command=self.get_answer)
        self.ask_button.pack(side=tkinter.LEFT)

    def get_answer(self):
        self.answer_text.set(random.choice(CHOICES))


root = Tk()
app = App(root)
root.mainloop()
root.destroy()
