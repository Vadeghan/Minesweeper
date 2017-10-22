# Minesweeper
# by Javad Hamidi
# Minesweeper.py 1.0.0
# 01/09/2017

from tkinter import *
from tkinter import ttk

import webbrowser
import random

root = Tk()  # Creates the GUI's main window
root.resizable(0, 0)  # disables resizing
root.title("Minesweeper")
root.wm_iconbitmap('assets\ico\mine.ico')

Label(root, text="Minesweeper").grid(row=0, column=0, columnspan=10)

x = 9
y = 9
mines = 10

cells = {}

img_nums = []
img_blank = PhotoImage(file="assets/gif/blank.gif")
img_mine = PhotoImage(file="assets/gif/mine.gif")
img_fail_mine = PhotoImage(file="assets/gif/fail_mine.gif")
img_not_mine = PhotoImage(file="assets/gif/not_mine.gif")
img_flag = PhotoImage(file="assets/gif/flag.gif")
for img in range(9):
    img_nums.append(PhotoImage(file="assets/gif/" + str(img) + ".gif"))


class Cell:
    def __init__(self, position_x, position_y, mine, name):
        self.name = name
        self.has_mine = mine
        self.number = 0
        self.clicked = False
        self.flagged = False
        self.x = position_x
        self.y = position_y

        def flood_click(position):
            if position.flagged:
                position.button.config(image=img_flag)
                position.clicked = False
            else:
                position.clicked = True
                position.button.config(image=img_nums[cells[position.name].number], relief=RIDGE)
                flood_fill(position)

        def flood_fill(selected_cell):
            if selected_cell.number == 0 and not selected_cell.flagged:
                try:
                    flood_click(cells["cell{0}{1}".format(selected_cell.x, selected_cell.y + 1)])
                except KeyError:
                    pass

        def click():
            if self.has_mine:
                for l in cells:
                    if not cells[l].flagged:
                        if cells[l].has_mine:
                            cells[l].button.config(image=img_mine, relief=RIDGE)
                            cells[l].clicked = True
                    elif cells[l].flagged:
                        # cells[l].button.config(image=img_not_mine, relief=RIDGE)
                        cells[l].clicked = True
                self.button.config(image=img_fail_mine, relief=RIDGE)  # this doesn't make sense
                self.clicked = True
            elif self.flagged:
                pass
            elif self.number > 0:
                self.button.config(image=img_nums[self.number], relief=RIDGE)
                self.clicked = True

            else:
                self.clicked = True
                self.button.config(image=img_nums[self.number], relief=RIDGE)
                flood_fill(self)

        self.button = Button(root, command=click)
        self.button.grid(row=position_x, column=position_y)

        def flag(right_click):
            if not self.clicked:
                if self.flagged:
                    self.button.config(image=img_blank, relief=RAISED)
                    self.flagged = False
                else:
                    self.button.config(image=img_flag, relief=RAISED)
                    self.flagged = True

        def reveal_adjacent(middle_click):
            """
            if you middle-click a number, and it is surrounded by exactly that many flags (as indicated by the number),
            all covered tiles become uncovered﻿
            """

        self.button.bind('<Button-2>', reveal_adjacent)
        self.button.bind('<Button-3>', flag)  # bind right mouse click


def place_numbers():
    for i in cells:
        if cells[i].has_mine:
            try:
                cells["cell{0}{1}".format(cells[i].x, cells[i].y + 1)].number += 1  # right
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x, cells[i].y - 1)].number += 1  # left
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x + 1, cells[i].y)].number += 1  # bottom
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x - 1, cells[i].y)].number += 1  # top
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x - 1, cells[i].y + 1)].number += 1  # top right
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x - 1, cells[i].y - 1)].number += 1  # top left
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x + 1, cells[i].y + 1)].number += 1  # bottom right
            except KeyError:
                pass

            try:
                cells["cell{0}{1}".format(cells[i].x + 1, cells[i].y - 1)].number += 1  # bottom left
            except KeyError:
                pass

    for k in cells:
        cells[k].button.config(image=img_blank)


def new_game():
    locations = []

    for j in range(1, (y + 1)):
        locations += list(range(int(str(j) + str(1)), int(str(j + 1) + str(0))))

    mine_locations = random.sample(locations, mines)

    for row in range(1, (x + 1)):
        for cell in range(1, (y + 1)):
            if int(str(row) + str(cell)) in mine_locations:
                cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, True, f"cell{row}{cell}")
            else:
                cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, False, f"cell{row}{cell}")

    place_numbers()


def options():  # rewrite this in a more pythonic way
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


def about():
    webbrowser.open("https://github.com/Vadeghan/Minesweeper")

menu = Menu(root)

game_menu = Menu(menu, tearoff=0)
game_menu.add_command(label="New Game", command=new_game)
game_menu.add_command(label="Options", command=options)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)


about_menu = Menu(menu, tearoff=0)
about_menu.add_command(label="About", command=about)


menu.add_cascade(label="Game", menu=game_menu)
menu.add_cascade(label="Help", menu=about_menu)

root.config(menu=menu)

new_game()

root.mainloop()  # Keeps window running until closed out
