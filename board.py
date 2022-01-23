'''
Code how the display is done
'''
import cell
import random

class Board:
    def __init__(self,x,y,alive=0.1):
        '''
        Board constructor

        Keywords args:
        x - number of cols
        y - number of rows

        Positionnal args:
        alive - from 0 to 1, probability of alive cell
        '''
        self.x = x
        self.y = y
        self.layout = [[cell.Cell(True if random.random()<0.1 else False) for _ in range(x)] for _ in range(y)]
        #TODO add some things to this poor board :(

    def get_cell(self,x,y):
        '''
        getter; cell in (x,y)
        ''' 
        return self.layout[x][y]       

    def get_x(self):
        '''
        getter; size in x
        '''
        return self.x
    
    def get_y(self):
        '''
        getter; size in y
        '''
        return self.y

    def __str__(self):
        ret = ""
        for row in self.layout:
            for cell in row:
                ret += cell.to_string()
            ret += "\n"
        return ret
