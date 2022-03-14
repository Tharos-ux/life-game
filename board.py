'''
Code how the display is done
'''
import cell
import random
import numpy as np

class Board:
    def __init__(self,x:int,y:int,alive:float=0.1):
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
        # numpy array 
        self.layout = np.empty((0, y), cell.Cell)
        for _ in range(y):
            self.layout = np.append(self.layout, np.array([[cell.Cell([random.choice([50,100,200]),random.choice([50,100,200]),random.choice([50,100,200])],cell.Etat.ALIVE if random.random()<0.001 else cell.Etat.DEAD) for _ in range(x)]]), axis=0)
        #TODO add some things to this poor board :(

    def get_updatables(self) -> list:
        return [(x,y) for x in range(self.x) for y in range(self.y) if self.get_cell(x,y).state == cell.Etat.ALIVE]

    def get_surroundings(self,x,y):
        '''
        returns all existing cells around a position
        '''
        # TODO vectorize
        if self.get_cell(x,y).state == cell.Etat.ALIVE:
            tries,maxX,maxY = [(x-1,y-1),(x+1,y+1),(x,y+1),(x+1,y),(x-1,y+1),(x+1,y-1),(x-1,y),(x,y-1),(x+2,y),(x-2,y),(x,y+2),(x,y-2)],self.x,self.y
            return [self.get_cell(e[0],e[1]) for e in tries if (e[0]>=0 and e[1]>=0 and e[0]<maxX and e[1]<maxY)]
        return []

    def get_cell(self,x,y):
        return self.layout[x,y]
      
    @property
    def x(self) -> int:
        '''
        getter; size in x
        '''
        return self.__x
    
    @property
    def y(self) -> int:
        '''
        getter; size in y
        '''
        return self.__y

    @x.setter
    def x(self,x:int) -> None:
        '''
        setter; size in x
        '''
        self.__x = x
    
    @y.setter
    def y(self,y:int) -> None:
        '''
        setter; size in y
        '''
        self.__y = y

    def __str__(self) -> str:
        ret = ""
        for row in self.layout:
            for cell in row:
                ret += cell.to_string()
            ret += "\n"
        return ret
