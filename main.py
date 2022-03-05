'''
Execution code
'''
import board as b
import graphics
import cell as c
import random
import numpy as np
import datetime
import os

# constantes
GENERATIONS:int = 30
BOARD_SIZE:int = 300


def main():
    "Main procedure"
    simulate()
    
            
def simulate() -> None:
    my_start_time:str = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S')
    os.mkdir(my_start_time) # create foler to store output

    print(" INITIALISATION ".center(80,'o'))
    print(f"Plateau de {BOARD_SIZE} x {BOARD_SIZE} cellules".center(80))

    my_board = b.Board(BOARD_SIZE,BOARD_SIZE) # initialisation du plateau

    print(" GENERATIONS ".center(80,'o'))
    print(f">>> Lancement à {datetime.datetime.today()} de {GENERATIONS} générations <<<".center(80))

    for i in range(GENERATIONS):
        #print(f"Génération {i} en cours de calcul...")
        graphics.show(my_board,my_start_time,i)

        # pour update sans avantager des cellules sur d'autres
        liste_update = my_board.get_updatables()
        random.shuffle(liste_update)

        for cell in liste_update:
            my_board.get_cell(cell[0],cell[1]).new_state(my_board.get_cell(cell[0],cell[1]),my_board.get_surroundings(cell[0],cell[1]))

    print(f">>> Fin à {datetime.datetime.today()} <<<".center(80))


if __name__ == "__main__":
    main()