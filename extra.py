# Minesweeper
# by Javad Hamidi
# Minesweeper.py 1.0.0
# 01/09/2017

from tkinter import *
from tkinter import ttk

root = Tk()  # Creates the GUI's main window
root.title("Minesweeper")
root.wm_iconbitmap('assets\ico\mine.ico')

frame = Frame(root)


class Cell:
    def __init__(self, mine, num, clicked):

        self.cell_numbers = []

        for icon in range(1, 9):
            self.cell_numbers.append(PhotoImage(file="assets/gif/1.gif"))  # must find way to import .ico

        self.mine = False
        self.num = 0
        self.clicked = False
        button = Button(root, height=1, width=2)

        if clicked:
            button = Button(root, text=num, height=1, width=2)

        button.pack()


""""""
Label(text="Minesweeper").pack()

a1 = Cell(True, 1, True)
a2 = Cell(True, 2, True)

frame.pack()

""""""

root.mainloop()  # Keeps window running until closed out
