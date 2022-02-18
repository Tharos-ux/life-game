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
        self.__state:Etat = state
        self.__color:str = color
        self.__method:str = method
        #TODO add some things to this poor cell :(

    @property
    def state(self) -> Etat:
        return self.__state

    @state.setter
    def state(self,state:Etat) -> None:
        self.__state = state

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self,color:str) -> None:
        self.__state = color

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self,method:str) -> None:
        self.__method = method

    def __str__(self) -> str:
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
