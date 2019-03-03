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
                if (cell.down + i[0]) >= 0 and (cell.right + i[1]) >= 0:
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

        self.button = None
