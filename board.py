'''
Code how the display is done
'''
import cell
import random

class Board:
    def __init__(self,x,y):
        '''
        Board constructor

        Keywords args:
        x - number of cols
        y - number of rows
        '''
        self.layout = [[cell.Cell(True if random.random()>0.3 else False) for _ in range(x)] for _ in range(y)]
        #TODO add some things to this poor board :(