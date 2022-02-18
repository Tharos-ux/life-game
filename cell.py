'''
Define a cell
'''
import random
from enum import Enum,auto

class Etat(Enum):
    "Représentation d'un état cellulaire"
    # todo edit properties in consequence
    ALIVE = auto()
    DEAD = auto()


class Cell:
    def __init__(self, color:str, state:Etat=Etat.DEAD, method:str="0"):
        '''
        Cell constructor

        Positionnal args:
        state (False) - living state of celle : False means dead, True means alive
        method(0) - way it interacts with her surroundings at each new iteration
        color - define its color it should be displayed to if its alive
        '''
        self.state:Etat = state
        self.color:str = color
        self.method:str = method
        #TODO add some things to this poor cell :(

    def set_dead(self):
        '''
        setter ; cell status to dead
        '''
        self.state = False

    def set_alive(self):
        '''
        setter ; cell status to alive
        '''
        self.state = True

    def set_state(self,state):
        '''
        setter ; set cell status
        '''
        self.state = state

    def get_state(self):
        '''
        getter; true if cell is alive, false otherwise
        '''
        return self.state

    def to_string(self):
        return "O" if self.state else " "

    def __str__(self):
        return "Alive" if self.state else "Dead"

    def new_state(self,surroundings):
        """
        We call a specific developpement method by a name given in parameter ; each cell may have its own path
        """
        task = getattr(Tasks, 'Exec' + self.method)
        self.state = task(surroundings)

class Tasks:
    "Each method must return new cell state (True/False)"

    def Exec0(surroundings):
        random.choice(surroundings).state = True

    def Exec1(surroundings):
        pass #TODO
