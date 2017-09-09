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
mines = 9


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

random.sample(range(x), mines)
random.sample(range(y), mines)

cells = {}

for row in range(1, (x + 1)):
    for cell in range(1, (y + 1)):
        cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, False, 0, False)

# Label(root, text="Minesweeper").grid()

root.mainloop()  # Keeps window running until closed out
