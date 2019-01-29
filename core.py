
import random

# set default height, width and number of mines
x = 9
y = 9
mines = 10

# 'grid' array stores every instance of the Cell class
grid = []

# 'positions' represent the x and y coordinates in all eight positions around a cell
# [0, 1] is up, because the if you change the x by 0 and the y by one, you go one up
positions = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [1, 0]]


def create_grid(x, y , mines):
    # creates a list that stores all the potential instance positions on the grid
    locations = []
    for i in range(1, (y + 1)):
        locations += list(range(int(str(i) + str(1)), int(str(i + 1) + str(0))))

    # depending on the number of mines chosen, 'random.sample' selects random 'locations' and assigns them to a variable ('mine_locations') in a list
    # this serve as the list of random coordinates for the cells with mines
    mine_locations = random.sample(locations, mines)

    # this loop creates all the cell instances based on the provided height and width of grid and stores them in the 'Cells' dictionary
    for cell in range(x):
        sub_array = []
        for row in range(y):
            # on creation, cells are checked for whether their coordinates match those in 'mine_locations'; whether it should be a mine
            if int(str(cell) + str(row)) in mine_locations:
                sub_array.append(Cell(row, cell, True))
            else:
                sub_array.append(Cell(row, cell, False))
        grid.append(sub_array)


# 'place_numbers' scans every cell on the board, and for each mine, its adjacent cells' number is is increased by one
def place_numbers():
    for i in range(x):
        for j in range(y):
            if grid[i][j].has_mine:
                for k in positions: # refering to the global variable
                    try:
                        grid[i + k[0]][j + k[1]].number += 1
                    except IndexError:
                        pass

def flood_fill(cell):
        # if a cell is on an edge or corner, without all 8 surrounding cells, this will catch any errors caused by the program looking for the non-existent cells
    if cell.clicked != True and cell.number == 0:
        cell.clicked = True

        for i in positions:
            try:
                flood_fill(grid[cell.down + i[0]][cell.right + i[1]])
            except IndexError:
                pass

# creates an object called 'Cell'
class Cell:
    def __init__(self, position_right, position_down, mine):
        # sets default values to all used variables based on parameters given on instance creation
        self.has_mine = mine
	self.number = 0
        self.right = position_right
        self.down = position_down

        self.flagged = False
        self.clicked = False

"""
	# __str__ is called when a user calls the print() function 
	# while __repr__ is called when a user just type the name of the instance

	# not really useful yet just experimenting at this stage
	def __repr__(self):
	    return 'mine' if self.has_mine else number
	    # could alternatively return position of cell on grid
"""
"""
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
                """"""
                if the user clicks on a cell with a mine, the program will then scan through all cells to see weather or not
                any others have mines. If a cell has a mine, it will check to see if it has been flagged. If it has been
                flagged, the program will pass that cell. If it has not been flagged, that cell will show the mine (img_mine).
                If the cell has been flagged but does not have a mine, it will show img_not_mine. Finally, the initially 
                selected cell it will set itself to img_fail_mine. Any other cells will remain the same as before.
                """"""

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
            """"""
            if you middle-click a number, and it is surrounded by exactly that many flags (as indicated by the number),
            all covered tiles become uncovered
            """"""

            if self.number > 0:
                for i in cell_positions:
                    if cells["cell{0}{1}".format(self.x + i[0], self.y + i[1])].flagged:
                        try:
                            flood_click(cells["cell{0}{1}".format(self.x + i[0], self.y + i[1])])
                        except KeyError:
                            pass

        self.button.bind('<Button-3>', flag, positions)  # binds the right mouse click to the 'reveal_adjacent' method
        self.button.bind('<Button-2>', reveal_adjacent)  # binds the middle mouse button to the 'reveal_adjacent' method
"""
