'''
Execution code
'''
import board
import graphics

def main():
    "Main procedure"
    my_board =  board.Board(1000,1000)
    graphics.show(my_board)

if __name__ == "__main__":
    main()