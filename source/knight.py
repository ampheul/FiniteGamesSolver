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

import .Game

class KnightGame(Nim):
    state : Tuple[int, int]
    
    def __init__(self, state : Tuple[int, int]):
        self.state = state
    
    def options(self):
        return 

print(KnightGame().options() + 1)

class Tiles:
    '''Creates an nxn tile grid
    '''
    def __init__(self, n):
        # default to -1, to signal it has been unset
        self.tiles = [-1 for i in range(n*n)]
        self.n = n
    
    def __getitem__(self, index):
        '''return the element at coordinate (i, j) in the board
        '''
        (i,j) = index
        if not self.inTiles(i, j):
            raise Exception('(%d, %d) not in tiles' % (i,j))
        elif self.tiles[n*i+j] == -1:
            raise Exception("bad access (%d,%d). tile needs to be set" % (i, j))
        
        return self.tiles[n*i+j]
    
    def __setitem__(self, index, value):
        '''Set the item at coordinate (i, j) in self.tiles
        '''
        (i,j) = index
        if not self.inTiles(i, j):
            raise Exception('(%d, %d) not in tiles' % (i,j))
        
        self.tiles[n*i+j] = value
    
    def inTiles(self, i, j):
        '''Ensure that this coordinate is within the tile grid.
        '''
        return 0 <= i and i <self.n and 0 <=j and j < self.n

if __name__ == '__main__':
    import sys

    n = int(sys.argv[1])

    tiles = Tiles(n)

    def knight_options(i : int, j : int):
        '''
        knight_options
        ==============
        iterate over the knight's potential moves and return only the legal moves.

        Parameters
        ----------
        i : int
        j : int

        Return
        '''

        # possible knight moves
        knight_moves = [(-2,-1),(-2,1),(-1,-2),(1,-2)]
    
        for x,y in knight_moves:
            
            if tiles.inTiles(i+x,j+y):

                yield tiles[i+x,j+y]
    
    def setTile(x,y):
        
        if not tiles.inTiles(x,y):
            return 
        
        options = set(knight_options(x,y))
        print(str(options)+' tile: %d,%d' % (x, y))
        options = list(options)
        options.sort()

        #calculate mex
        mex = 0
        mexFound = False
        for i in range(len(options)):
            
            if i != options[i]:
                mex = i
                mexFound = True
                break
        tiles[x,y] = mex if mexFound else len(options)
        print('mex: %d, len: %d, tiles[%d,%d]: %d'% (mex, len(options), x, y, tiles[x,y]))
    
    # iterate along the diagonal and play the knight game
    # since the invariant of the diagonal sum must decrease in the knight game,
    # we can discover all moves in proper order, ensuring subgames are already evaluated
    for i in range(2*(n-1)+1):
         for j in range(i+1):
            if tiles.inTiles(i-j,j):
                setTile(i-j,j)

    #symbols = ['.\u25A1','.\u25A5', '.\u25A6', '.\u25A3', '.\u25A0']
    symbols = ['.'+str(i) for i in range(5)]
    for i in range(n):
        print( ''.join([ symbols[i] for i in tiles.tiles[n*i:n*(i+1)] ]) )

