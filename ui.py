from Tkinter import *  # imports the whole tkinter library for GUI making

import webbrowser  # lets you open websites from within a python function


root = Tk()  # Creates the GUI's main window
#TODO root.resizable(0, 0)  # disables any resizing of the window
root.title("Minesweeper")  # sets the window title
root.wm_iconbitmap('@assets/linux/xbm/mine.xbm')  # sets the window icon in corner

# creates a heading labeled 'Minesweeper' above the game
Label(root, text="Minesweeper").grid(row=0, column=0, columnspan=10)

# imports all image assets and assigns them to variables
img_blank = PhotoImage(file="assets/linux/gif/blank.gif")
img_mine = PhotoImage(file="assets/linux/gif/mine.gif")
img_fail_mine = PhotoImage(file="assets/linux/gif/fail_mine.gif")
img_not_mine = PhotoImage(file="assets/linux/gif/not_mine.gif")
img_flag = PhotoImage(file="assets/linux/gif/flag.gif")

# stores all the numbers in a single list in order; img_nums[0] = 0.gif, img_nums[1] = 1.gif, etc.
img_nums = []
for img in range(9): 
    img_nums.append(PhotoImage(file="assets/linux/gif/" + str(img) + ".gif"))



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

