#!/usr/bin/python3
'''
knight.py
=========
A knight moves on an nxn board. 
Players take turn moving the knight.
All knight moves must be towards the top left of the board.
The player who can not move loses.

This is an impartial game with normal play 
therefore we can calcluate nim equivalency and print it out,
precisely what this program does.

Takes a single command line argument n and prints the knight game on an
'''

import Game

class KnightGame(Game.Nim):
    state : Tuple[int, int, int] # x, y, boardsize
    
    def __init__(self, state : Tuple[int, int, int]):
        self.state = state
    
    def options(self):
        
        # the potential moves knight will take from current positon
        moves = [(-2, -1), (-2, 1), (-1, -2), (1, -2)]
        
        x, y, boardsize = self.state

        for i, j in moves:
            if 0 <= x+i and x + i < boardsize and 0 <= y + j and y + j < boardsize:
                yield (x + i, y + j)

if __name__ == '__main__':
    import sys

    n = int(sys.argv[1])

    init_state = (n-1, n-1, n)

    knight_game = KnightGame(init_state)

    nim_values  = [ None :  for i in range(n*n) ]
    nim_values[0] = 0
    
    def matrix_to_diagonal(i : int, j: int) -> Tuple[int, int]:
        return if i + j < n then (i + j, j) else (i + j, j + n - (i+j))

    def diagonal_to_matrix(i : int, j: int) -> Tuple[int, int]:
        return if a < n then (a - b, b) else (a-b + a-n, b + a-n)
    
    def flat_to_matrix(i : int) -> Tuple[int, int]:
        return divmod(i, n)
    
    def matrix_to_flat(i : int, j : int) -> int:
    
    def flat_to_diagonal() -> Tuple[int,int]:


    # iterate through the square using diagonal coordinates
    # the diagonal is a decreasing invariant in the knight game, so if we
    # find nim values for increasing i in diagonal coordinates, then we
    for a, b in map(flat_to_diagonal, range(n*n)):
        x, y = diagonal_to_matrix(a, b)
        KnightGame(x, y, n)
            