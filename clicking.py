from tkinter import *
root = Tk()


def click(event):
    print(event)
    print(event.num)
    print(event.state)
    print('')

button = Button(root)
button.bind('<Button-3>', click)
button.bind('<Button-1>', click)
button.bind('<Button-2>', click)
button.bind('<Button-4>', click)


button.pack()
mainloop()
