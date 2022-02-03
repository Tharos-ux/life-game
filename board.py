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
        self.layout = [[cell.Cell([random.randrange(0, 254),random.randrange(0, 254),random.randrange(0, 254)],True if random.random()<0.1 else False) for _ in range(x)] for _ in range(y)]
        #TODO add some things to this poor board :(


    def get_surroundings(self,x,y):
        '''
        returns all existing cells around a position
        '''
        cells,tries,maxX,maxY = [],[(x-1,y-1),(x+1,y+1),(x,y+1),(x+1,y),(x-1,y+1),(x+1,y-1),(x-1,y),(x,y-1)],self.get_x(),self.get_y()
        for e in tries:
            if (e[0]<1 or e[1]<1 or e[0]>999 or e[1]>999):
                tries.remove(e)
        print(tries)
        for (x,y) in tries:
            cells.append(self.get_cell(x,y))
        return cells

    def get_cell(self,x,y):
        '''
        getter; cell in (x,y)
        ''' 
        return self.layout[x][y]

    def update_cell(self,x,y):
        my_cell = self.get_cell(x,y)
        my_cell.new_state(self.get_surroundings(x,y))
      

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
