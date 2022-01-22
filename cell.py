'''
Define a cell
'''

class Cell:
    def __init__(self,state=False):
        '''
        Cell constructor

        Positionnal args:
        state (False) - living state of celle : False means dead, True means alive
        '''
        self.state = state
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

    def get_state(self):
        '''
        getter; true if cell is alive, false otherwise
        '''
        return self.state

    def __str__(self):
        return "O" if self.state else " "