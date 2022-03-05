'''
Graphical interface
'''

import random
import board
import cell
import numpy as np
from PIL import Image as im
import IPython.display as display
from tkinter import *

def show(board,folder,gen=0):
    "show graphic representation of the life game"
    x,y = board.x,board.y
    data = np.zeros((x,y,3), dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            data[i,j] = board.get_cell(i,j).color if board.get_cell(i,j).state==cell.Etat.ALIVE else [0,0,0]
    img = im.fromarray(data)
    img.save(f"{folder}/visu{gen}.png")

"""

'''
Graphical interface
'''
import board
import cell
import numpy as np
from PIL import Image
from tkinter import *

def gen_img(board,x,y):
    "graphic representation of the life game"
    data = np.zeros((x,y,3), dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            data[i,j] = [254,0,0] if board.get_cell(i,j).get_state() else [0,0,0]
    img = Image.fromarray(data)
    return img

def show(board):
    "show the window"
    x,y = board.get_x(),board.get_y()
    win = Tk()
    win.title(f"Life game")
    win.geometry(f"{x}x{y}")
    cont = Canvas(win, bg="white", height=x, width=y)
    background_label = Label(win, image=gen_img(board,x,y))
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    cont.pack()

    win.mainloop()

"""