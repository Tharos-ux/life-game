'''
Execution code
'''
import board as b
import graphics
import cell as c
import random
import numpy as np

# constantes
GENERATIONS:int = 100
BOARD_SIZE:int = 300


def main():
    "Main procedure"
    simulate()
    
            
def simulate() -> None:
    my_board = b.Board(BOARD_SIZE,BOARD_SIZE) # initialisation du plateau

    for i in range(GENERATIONS):
        print(f"Génération {i} en cours de calcul...")
        graphics.show(my_board,i)

        # pour update sans avantager des cellules sur d'autres
        liste_update = my_board.get_updatables()
        random.shuffle(liste_update)

        for cell in liste_update:
            my_board.get_cell(cell[0],cell[1]).new_state(my_board.get_cell(cell[0],cell[1]),my_board.get_surroundings(cell[0],cell[1]))


if __name__ == "__main__":
    main()