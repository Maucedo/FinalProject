import numpy as np
from IPython.display import clear_output
a = np.zeros((8,8), str)
a[1, 0:]  = "p"
a[6, 0:] = "P"
a[2:6, :] = " "
a[7, 0], a[7, 7] = "R", "R"
a[0, 0], a[0,7] = "r", "r"
a[0, 1], a[0, 6] = "h", "h"
a[0, 2], a[0, 5] = "b", "b"
a[0, 3], a[0,4] = "k", "q"
a[7, 1], a[7,6] = "H", "H"
a[7,2], a[7,5] = "B", "B"
a[7,3], a[7,4] = "K", "Q"

def printer():
    print("    a   b   c   d   e   f   g   h")
    for i in range(8):
        print(i + 1, a[i])
values = ["a", "b", "c", "d", "e", "f", "g", "h"]
pieces = ["h", "p", "k", "b", "q", "r"]
Bpieces = ["H", "P", "K", "Q", "B", "R"]
b = 1
#def chosenp():
    
def pawnmoveB():
    if movpie == "P":
        if index1 == 1:
            if nindex ==  index1 - 1 or index1 - 2:
                if a[nindex2, nindex1] == " ":
                    Move = True
                else:
                    Move = False
Move = False

while True:
    b += 1
    clear_output(wait=True)
    print("Player 1" if b % 2 == 0 else "Player2")
    printer()
    play = input("type c to capitulate or any other button to move")
    if play == "c":
        print("You surrendered")
        break
    else:
        test = True
        while test:
            move = input("what to move")
            index1 = values.index(move[0])
            index2 = int(move[1]) - 1
            movpie = a[index2, index1]
            if b % 2 == 0:
                if movpie in pieces:
                    # då kan vi flytta
                    where = input("where to move")
                    nindex1 = values.index(where[0])
                    nindex2 = int(where[1]) - 1
                    a[nindex2, nindex1] = movpie
                    a[index2, index1] = " "
                    printer()
                    test = False
                else:
                    pass # då kan vi inte flytta
            elif b % 2 != 0:
                    if movpie in Bpieces:
                        where = input("where to move")
                        nindex1 = values.index(where[0])
                        nindex2 = int(where[1]) - 1
                        a[nindex2, nindex1] = movpie
                        a[index2, index1] = " "
                        printer()
                        test = False
                                    