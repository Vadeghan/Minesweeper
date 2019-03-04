# Minesweeper
# by Javad Hamidi
# Minesweeper.py 4.2.7
# 01/09/2017

#from ui import *
#from core import *

from tkinter import *  # imports the whole tkinter library for GUI making
import random
import webbrowser  # lets you open websites from within a python function

# set default height, width and number of mines
x = 9
y = 9
mines = 10

# 'grid' array stores every instance of the Cell class
grid = []

# 'positions' represent the x and y coordinates in all eight positions around a cell
# [0, 1] is up, because the if you change the x by 0 and the y by one, you go one up
positions = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 1], [-1, -1], [-1, 0]]

root = Tk()  # Creates the GUI's main window
root.resizable(0, 0)  # disables any resizing of the window
root.title("Minesweeper")  # sets the window title
root.wm_iconbitmap('assets/ico/mine.ico')  # sets the window icon in corner

# creates a heading labeled 'Minesweeper' above the game
Label(root, text="Minesweeper").grid(row=0, column=0, columnspan=10)

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




cell_buttons = []

def click(cell):
    if cell.clicked == False:
        if cell.has_mine:
            cell.button.config(image=img_mine, relief=RIDGE)

        if cell.number > 0:
            cell.button.config(image=img_nums[cell.number], relief=RIDGE)
            
        if cell.number == 0 and cell.has_mine == False:
            flood_fill(cell)

            for i in grid:
                for j in i:
                    if j.clicked == True and j.number == 0:
                        for k in positions:
                            try:
                                if (j.down + k[0]) >= 0 and (j.right + k[1]) >= 0:
                                    grid[j.down + k[0]][j.right + k[1]].clicked = True
                            except IndexError:
                                pass
            for i in grid:
                for j in i:
                    if j.clicked == True:
                        j.button.config(image=img_nums[j.number], relief=RIDGE)
        cell.clicked == True

def show_grid():
    count_i = 0
    for i in grid:
        count_j = 0
        for j in i:
            j.button = Button(root, command=lambda j=j: click(j))
            j.button.grid(row=j.down, column=j.right)
            j.button.config(image=img_blank)
            count_j += 1
        count_i += 1
            



def print_grid():
    for i in grid:
        line = []
        for j in i:
            if j.has_mine:
                line.append("x")
            else:
                line.append(str(j.number))
        print(str(line))

create_grid(x, y, mines)

place_numbers()

print_grid()

show_grid()







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
    webbrowser.open("https://github.com/javadhamidi/minsweeper-windows")

menu = Menu(root)  # creates a tkinter 'Menu' stored in the menu variable

game_menu = Menu(menu, tearoff=0)  # within 'menu' a sub-menu is created stored in 'game_menu'
#TODO game_menu.add_command(label="New Game", command=new_game)
game_menu.add_command(label="Options", command=options)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)


about_menu = Menu(menu, tearoff=0)
about_menu.add_command(label="About", command=about)

# the sub-menus 'game_menu' and 'about_menu are made accessable through a button on the cascade, created by the 'add_cascade' method
menu.add_cascade(label="Game", menu=game_menu)
menu.add_cascade(label="Help", menu=about_menu)

root.config(menu=menu)  # establishes that the GUI's menu is stored in the 'menu' variable


root.mainloop()  # keeps the main window running until closed out by user
