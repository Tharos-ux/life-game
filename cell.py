'''
Define a cell
'''
import random
from enum import Enum,auto
from my_checker import my_class_checker

class Etat(Enum):
    "Représentation d'un état cellulaire"
    # todo edit properties in consequence
    ALIVE = auto()
    DEAD = [0,0,0]

#@my_class_checker Ne pas utiliser de class check ici, car méthodes beaucoup appelées donc rajoute BEAUCOUP de temps d'exécution
class Cell:
    def __init__(self, color:list, state:Etat=Etat.DEAD, method:str="0", lifespan:int=10):
        '''
        Cell constructor

        Positionnal args:
        state (False) - living state of celle : False means dead, True means alive
        method (0) - way it interacts with her surroundings at each new iteration
        color - define its color it should be displayed to if its alive
        '''
        self.state = state
        self.color = color
        self.method = random.choice(["0","1","2"])
        self.lifespan = lifespan # to add to them a half-life after
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
        self.__color = color

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self,method:str) -> None:
        self.__method = method

    def half_life(self) -> float:
        "Probability = polygon"
        # TODO
        return float(0)

    def __str__(self) -> str:
        return "Alive" if self.state else "Dead"

    def mutation(self,contact):
        "contact is another cell it may get something from"
        if random.random()<0.001: # maybe add mutation factor inside cell def
            match random.randrange(0,3):
                case 0:
                    self.state = contact.state
                case 1:
                    self.color = contact.color
                case 2:
                    self.method = contact.method



    def new_state(self,origin,surroundings):
        """
        We call a specific developpement method by a name given in parameter ; each cell may have its own path
        """
        task = getattr(Tasks, 'Exec' + self.method)
        task(origin,surroundings)

class Tasks:
    "Each method must return new cell state (True/False)"

    def Exec0(origin,surroundings):
        # cellules qui vivent, qui meurent, et qui se battent un peu
        if random.random()<0.05: origin.state = Etat.DEAD
        if surroundings != []:
            for cell in surroundings:
                origin.mutation(cell)
                if cell.state == Etat.DEAD:
                    if random.random()<0.25:
                        cell.color = origin.color
                        cell.method = origin.method
                        cell.state = Etat.ALIVE
                else:
                    cell.color = origin.color if random.random()<0.01 else cell.color


    def Exec1(origin,surroundings):
        # cellules qui vivent, qui meurent, mais qui se battent BEAUCOUP
        if random.random()<0.05: origin.state = Etat.DEAD
        if surroundings != []:
            for cell in surroundings:
                origin.mutation(cell)
                if cell.state == Etat.DEAD:
                    if random.random()<0.25:
                        cell.color = origin.color
                        cell.method = origin.method
                        cell.state = Etat.ALIVE
                else:
                    cell.color = origin.color if random.random()<0.50 else cell.color

    def Exec2(origin,surroundings):
        # cellules qui mutent au contact de d'autres, et qui meurent
        if random.random()<0.05: origin.state = Etat.DEAD
        if surroundings != []:
            for cell in surroundings:
                origin.mutation(cell)
                if cell.state == Etat.DEAD:
                    if random.random()<0.25:
                        cell.color = origin.color
                        cell.method = origin.method
                        cell.state = Etat.ALIVE
                else:
                    cell.color = [int((origin.color[0]+cell.color[0])/2),int((origin.color[1]+cell.color[1])/2),int((origin.color[2]+cell.color[2])/2)]
