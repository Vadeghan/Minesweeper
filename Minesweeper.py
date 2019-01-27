# Minesweeper
# by Javad Hamidi
# Minesweeper.py 4.2.7
# 01/09/2017

#from ui import *
from core import *

import random

# set default height, width and number of mines
x = 9
y = 9
mines = 10

# 'cells' dictionary stores every instance of the cell class
# cells = {}

# 'positions' represent the x and y coordinates in all eight positions around a cell
# [0, 1] is up, because the if you change the x by 0 and the y by one, you go one up
positions = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [1, 0]]



create_grid(x, y, mines)

place_numbers()

for i in grid:
    line = []
    for j in i:
        line.append(j.number)
    print(line)


"""
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
                pass
                #cells["cell{0}{1}".format(cell, row)] = Cell(cell, row, True, f"cell{cell}{row}")
            else:
                cells["cell{0}{1}".format(cell, row)] = Cell(cell, row, False, "cell{cell}{row}")

    place_numbers(positions)  # after the cells are created and the mines are placed, the 'place_numbers' function is called to place the numbers
"""

#new_game()  # starts the program by creating a new game

