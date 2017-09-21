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
mines = 1

cells = {}

img_nums = []
img_mine = PhotoImage(file="assets/gif/mine.gif")
img_flag = PhotoImage(file="assets/gif/flag.gif")
for img in range(9):
    img_nums.append(PhotoImage(file="assets/gif/" + str(img) + ".gif"))


class Cell:
    def __init__(self, position_x, position_y, mine, name):
        self.has_mine = mine
        self.number = 0
        self.clicked = False
        self.x = position_x
        self.y = position_y

        def click():
            pass

        button = Button(root, command=click)

        button.grid(row=position_x, column=position_y)
        print(position_x)
        print(position_y)

        global assign_num

        def assign_num():
            if self.has_mine:
                button.config(image=img_mine)
            else:
                button.config(image=img_nums[self.number])


def new_game():
    locations = []

    for i in range(1, (y + 1)):
        locations += list(range(int(str(i) + str(1)), int(str(i + 1) + str(0))))

    mine_locations = random.sample(locations, mines)

    for row in range(1, (x + 1)):
        for cell in range(1, (y + 1)):
            if int(str(row) + str(cell)) in mine_locations:
                cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, True, f"cell{row}{cell}")
            else:
                cells["cell{0}{1}".format(row, cell)] = Cell(row, cell, False, f"cell{row}{cell}")

            place_numbers()


def place_numbers():
    for i in cells:
        if cells[i].has_mine:
            try:
                cells["cell{0}".format(str(int(cells[i].x)) + str(int(cells[i].y) + 1))].number += 1  # right
                # cells["cell{0}".format(str(int(cells[i].x)) + str(int(cells[i].y) - 1))].number += 1  # left
                cells["cell{0}".format(str(int(cells[i].x) + 1) + str(int(cells[i].y)))].number += 1  # bottom
                # cells["cell{0}".format(str(int(cells[i].x) - 1) + str(int(cells[i].y)))].number += 1  # top

                # cells["cell{0}".format(str(int(cells[i].x) - 1)) + str(int(cells[i].y) + 1)].number += 1  # top right
                # cells["cell{0}".format(str(int(cells[i].x) - 1)) + str(int(cells[i].y) - 1)].number += 1  # top left

                cells["cell{0}".format(str(int(cells[i].x) + 1)) + str(int(cells[i].y) + 1)].number += 1  # bottom right
                cells["cell{0}".format(str(int(cells[i].x) + 1)) + str(int(cells[i].y) - 1)].number += 1  # bottom left

            except KeyError:
                print("cell does not exist")

        assign_num()


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

