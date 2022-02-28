'''
Execution code
'''
import board as b
import graphics
import cell as c
import random


def main():
    "Main procedure"
    my_board = b.Board(200,200)
    for i in range(100):
        print(f"Génération {i} en cours de calcul...")
        graphics.show(my_board,i)
        liste_update = my_board.get_updatables()
        while len(liste_update)>0:
            cell = random.choice(liste_update)
            my_board.get_cell(cell[0],cell[1]).new_state(my_board.get_cell(cell[0],cell[1]),my_board.get_surroundings(cell[0],cell[1]))
            liste_update.remove(cell)
            
            

if __name__ == "__main__":
    main()