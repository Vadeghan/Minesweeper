# Minesweeper
# by Javad Hamidi
# Minesweeper.py 1.0.0
# 01/09/2017

from tkinter import *
from tkinter import ttk

import random

root = Tk()  # Creates the GUI's main window
root.resizable(0, 0)  # disables resizing
root.title("Minesweeper")
root.wm_iconbitmap('assets\ico\mine.ico')

Label(root, text="Minesweeper").grid(row=0, column=0, columnspan=10)

x = 9
y = 9
mines = 10

random.sample(range(mines), x)
random.sample(range(mines), y)

cells = {}


class Cell:
    blank_img = PhotoImage(file=r"assets\gif\blank.gif")
    mine_img = PhotoImage(file="assets\gif\mine.gif")
    flag_img = PhotoImage(file=r"assets\gif\flag.gif")

    def __init__(self, width, height, mine, num, clicked):
        self.mine = False
        self.num = 0
        self.clicked = False

        def click():
            pass

        button = Button(root, command=click)
        button.config(image=self.blank_img)
        button.grid(row=width, column=height)


def new_game():
    for row in range(1, (x + 1)):
        for cell in range(1, (y + 1)):
            cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, False, 0, False)


def options():
    options_menu = Toplevel()
    options_menu.wm_iconbitmap(r'assets\ico\blank.ico')
    options_menu.title("Options")

    Label(options_menu, text="Height (9-24):").pack(side=LEFT, padx=5, pady=5)
    Label(options_menu, text="Width (9-30):").pack(side=LEFT, padx=5, pady=5)
    Label(options_menu, text="Mines (10-67):").pack(side=LEFT, padx=5, pady=5)

    e1 = Entry(options_menu)
    e2 = Entry(options_menu)
    e3 = Entry(options_menu)

    e1.delete(0, END)
    e1.insert(0, x)

    e2.delete(0, END)
    e2.insert(0, y)

    e3.delete(0, END)
    e3.insert(0, mines)

    e1.pack(side=LEFT, padx=5, pady=5)
    e2.pack(side=LEFT, padx=5, pady=5)
    e3.pack(side=LEFT, padx=5, pady=5)

    def save():
        global x
        x = int(e1.get())
        global y
        y = int(e2.get())
        global mines
        mines = int(e3.get())

        new_game()
        options_menu.destroy()

    Button(options_menu, text="Save", command=save).pack()


menu = Menu(root)

game_menu = Menu(menu, tearoff=0)
game_menu.add_command(label="New Game", command=new_game)
game_menu.add_command(label="Options", command=options)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)


about_menu = Menu(menu, tearoff=0)
about_menu.add_command(label="About")


menu.add_cascade(label="Game", menu=game_menu)
menu.add_cascade(label="Help", menu=about_menu)
root.config(menu=menu)

new_game()
root.mainloop()  # Keeps window running until closed out
