# Minesweeper
# by Javad Hamidi
# Minesweeper.py 4.2.7
# 01/09/2017

from tkinter import *  # imports the whole tkinter library for GUI making

import webbrowser  # lets you open websites from within a python function
import random

root = Tk()  # Creates the GUI's main window
root.resizable(0, 0)  # disables any resizing of the window
root.title("Minesweeper")  # sets the window title
root.wm_iconbitmap('assets\ico\mine.ico')  # sets the window icon in corner

# creates a heading labeled 'Minesweeper' above the game
Label(root, text="Minesweeper").grid(row=0, column=0, columnspan=10)

# sets initial height, width and number of mines
x = 9
y = 9
mines = 10

# 'cells' dictionary stores every instance of the cell class
cells = {}

# 'positions' represent the x and y coordinates in all eight positions around a cell
# [0, 1] is up, because the if you change the x by 0 and the y by one, you go one up
positions = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [1, 0]]

# imports all image assets and assigns them to variables
img_blank = PhotoImage(file="assets/gif/blank.gif")
img_mine = PhotoImage(file="assets/gif/mine.gif")
img_fail_mine = PhotoImage(file="assets/gif/fail_mine.gif")
img_not_mine = PhotoImage(file="assets/gif/not_mine.gif")
img_flag = PhotoImage(file="assets/gif/flag.gif")

# stores all the numbers in a single list in order; img_nums[0] = 0.gif, img_nums[1] = 1.gif, etc.
img_nums = []
for img in range(9): 
    img_nums.append(PhotoImage(file="assets/gif/" + str(img) + ".gif"))


# creates an object called 'Cell'
class Cell:
    def __init__(self, position_x, position_y, mine, name):
        # sets default values to all used variables based on parameters given on instance creation
        self.name = name
        self.has_mine = mine
        self.number = 0
        self.flagged = False
        self.x = position_x
        self.y = position_y
        self.clicked = False

        def flood_click(position):
            if not position.flagged:
                position.button.config(image=img_nums[cells[position.name].number], relief=RIDGE)
                self.clicked = True

        def flood_neighbours(selected_cell, cell_positions):
            for i in cell_positions:
                # if a cell is on an edge or corner, without all 8 surrounding cells, this will catch any errors caused by the program looking for the non-existent cells
                try:
                    flood_click(cells["cell{0}{1}".format(selected_cell.x + i[0], selected_cell.y + i[1])])
                except KeyError:
                    pass

        def click():  # this function is called when a user clicks on a cell to decide what happens
            if not self.clicked:  # prevents already clicked cells from being clicked on again
                """
                if the user clicks on a cell with a mine, the program will then scan through all cells to see weather or not
                any others have mines. If a cell has a mine, it will check to see if it has been flagged. If it has been
                flagged, the program will pass that cell. If it has not been flagged, that cell will show the mine (img_mine).
                If the cell has been flagged but does not have a mine, it will show img_not_mine. Finally, the initially 
                selected cell it will set itself to img_fail_mine. Any other cells will remain the same as before.
                """

                self.clicked = True

                if self.flagged:  # prevents cell from being clicked if it has been flagged already by setting flagged to False
                    self.clicked = False

                elif self.has_mine:
                    for l in cells:
                        cells[l].clicked = True  # sets all cells on the board as clicked -- comment out this line for bug testing
                        if cells[l].has_mine:
                            if cells[l].flagged:
                                pass
                            else:
                                cells[l].button.config(image=img_mine, relief=RIDGE)
                        elif cells[l].flagged:
                            cells[l].button.config(image=img_not_mine, relief=RIDGE)
                    self.button.config(image=img_fail_mine, relief=RIDGE)

                elif self.number > 0:  # if the cell isn't blank (does not have a 0 value), it will reveal itself
                    self.button.config(image=img_nums[self.number], relief=RIDGE)

                else:  # if the cell is blank, it will reveal itself and all its neighbours by calling the 'flood_neighbours' function
                    self.button.config(image=img_nums[self.number], relief=RIDGE)
                    flood_neighbours(self, positions)

        self.button = Button(root, command=click)  # creates a button using the tkinter 'Button' function, and assigns it to a variable
        self.button.grid(row=position_x, column=position_y)  # uses the grid positioning method to place buttons in the correct places

        def flag(event):  # method called when right mouse button is clicked. The 'event' parameter is passed by tkinter but not used in the method
            if not self.clicked:  # if the cell hasn't been already clicked
                if self.flagged:
                    self.button.config(image=img_blank, relief=RAISED)
                    self.flagged = False
                else:
                    self.button.config(image=img_flag, relief=RAISED)
                    self.flagged = True

        def reveal_adjacent(event, cell_positions):
            """
            if you middle-click a number, and it is surrounded by exactly that many flags (as indicated by the number),
            all covered tiles become uncovered﻿
            """

            if self.number > 0:
                for i in cell_positions:
                    if cells["cell{0}{1}".format(self.x + i[0], self.y + i[1])].flagged:
                        try:
                            flood_click(cells["cell{0}{1}".format(self.x + i[0], self.y + i[1])])
                        except KeyError:
                            pass

        self.button.bind('<Button-3>', flag, positions)  # binds the right mouse click to the 'reveal_adjacent' method
        self.button.bind('<Button-2>', reveal_adjacent)  # binds the middle mouse button to the 'reveal_adjacent' method


# 'place_numbers' scans every cell on the board, and for each mine, its adjacent cells' number is is increased by one
def place_numbers(coordinates):  # coordinates is 'positions' taken as the function's parameter
    for i in cells:
        if cells[i].has_mine:
            for j in coordinates:
                try:
                    cells["cell{0}{1}".format(cells[i].x + j[0], cells[i].y + j[1])].number += 1
                except KeyError:
                    pass

    # set each cell as blank when the game starts
    for i in cells:
        cells[i].button.config(image=img_blank)


def new_game():
    # creates a list that stores all the potential instance positions on the grid
    locations = []
    for i in range(1, (y + 1)):
        locations += list(range(int(str(i) + str(1)), int(str(i + 1) + str(0))))

    # depending on the number of mines chosen, 'random.sample' selects random 'locations' and assigns them to a variable ('mine_locations') in a list
    # this serve as the list of random coordinates for the cells with mines
    mine_locations = random.sample(locations, mines)

    # this loop creates all the cell instances based on the provided height and width of grid and stores them in the 'Cells' dictionary
    for cell in range(1, (x + 1)):
        for row in range(1, (y + 1)):
            # on creation, cells are checked for whether their coordinates match those in 'mine_locations'; whether it should be a mine
            if int(str(cell) + str(row)) in mine_locations:
                cells["cell{0}{1}".format(cell, row)] = Cell(cell, row, True, f"cell{cell}{row}")
            else:
                cells["cell{0}{1}".format(cell, row)] = Cell(cell, row, False, f"cell{cell}{row}")

    place_numbers(positions)  # after the cells are created and the mines are placed, the 'place_numbers' function is called to place the numbers


def options():  # this function displays and opens the minesweeper's option menu
    options_menu = Toplevel()  # creates a 'Toplevel' menu (a pop-up window in tkinter) stored in the options_menu variable
    options_menu.wm_iconbitmap(r'assets\ico\blank.ico')  # sets the window's icon as a blank image
    options_menu.title("Options")  # sets the window title as 'Options'

    # creates three lines of text next to the three entry boxes to label them
    Label(options_menu, text="Height (9-24):").pack(side=LEFT, padx=5, pady=5)
    Label(options_menu, text="Width (9-30):").pack(side=LEFT, padx=5, pady=5)
    Label(options_menu, text="Mines (10-67):").pack(side=LEFT, padx=5, pady=5)

    # creates three text entry boxes
    e1 = Entry(options_menu)
    e2 = Entry(options_menu)
    e3 = Entry(options_menu)

    # puts the currently assigned values as default text in each entry box
    e1.insert(0, x)
    e2.insert(0, y)
    e3.insert(0, mines)

    # pack is what tkinter uses to place the entry box widgets
    e1.pack(side=LEFT, padx=5, pady=5)
    e2.pack(side=LEFT, padx=5, pady=5)
    e3.pack(side=LEFT, padx=5, pady=5)

    def save():  # establishes the function of the 'Save' button
        # sets the x, y and mines variables outside of the function to the given values in the entry boxes
        global x
        x = int(e1.get())
        global y
        y = int(e2.get())
        global mines
        mines = int(e3.get())

        new_game()  # restarts the game with the new parameters
        options_menu.destroy()  # closes the options menu

    Button(options_menu, text="Save", command=save).pack()  # creates and displays the 'Save' button


def about():  # when the about button is pressed, this function opens the appropriate external website
    webbrowser.open("https://github.com/Vadeghan/Minesweeper")

menu = Menu(root)  # creates a tkinter 'Menu' stored in the menu variable

game_menu = Menu(menu, tearoff=0)  # within 'menu' a sub-menu is created stored in 'game_menu'
game_menu.add_command(label="New Game", command=new_game)
game_menu.add_command(label="Options", command=options)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)


about_menu = Menu(menu, tearoff=0)
about_menu.add_command(label="About", command=about)

# the sub-menus 'game_menu' and 'about_menu are made accessable through a button on the cascade, created by the 'add_cascade' method
menu.add_cascade(label="Game", menu=game_menu)
menu.add_cascade(label="Help", menu=about_menu)

root.config(menu=menu)  # establishes that the GUI's menu is stored in the 'menu' variable

new_game()  # starts the program by creating a new game

root.mainloop()  # keeps the main window running until closed out by user
