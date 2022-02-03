'''
Execution code
'''
import board as b
import graphics
import cell as c


def main():
    "Main procedure"
    my_board = b.Board(1000,1000)
    for i in range(10):
        graphics.show(my_board,i)
        for x in range(my_board.get_x()):
            for y in range(my_board.get_y()):
                my_board.update_cell(x,y)
            
            

if __name__ == "__main__":
    main()