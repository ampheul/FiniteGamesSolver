#!/usr/bin/python3
'''
Takes a single command line argument n and prints the knight game on an
nxn board. Players must move the knight so that the sum of coordinates
decreases (described with matrix coordinates). 

The player who can not move loses.

This is clearly an impartial game with normal play 
therefore we can calcluate nim equivalency and print it out

... so we do that.
'''
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

    def horsy_options(i, j):
        '''Get the options that a horse can move to starting from (i,j)
        Those are the values which have x+y strictly less than i+j
        '''
        if tiles.inTiles(i-2, j-1): 
        
            yield tiles[i-2, j-1]
        
        if tiles.inTiles(i-2, j+1):
            
            yield tiles[i-2, j+1]
        
        if tiles.inTiles(i-1, j-2):
            
            yield tiles[i-1, j-2]
        
        if tiles.inTiles(i+1, j-2):
            
            yield tiles[i+1, j-2]
        
        raise StopIteration
    
    def setTile(x,y):
        
        if not tiles.inTiles(x,y):
            return 
        
        options = {option for option in horsy_options(x,y)}
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
    
    # iterate along the diagonal and play horsy
    # since the invariant of the diagonal sum must decrease in horsy,
    # we can discover all moves in proper order, ensuring subgames are already evaluated
    for i in range(2*(n-1)+1):
         for j in range(i+1):
            if tiles.inTiles(i-j,j):
                setTile(i-j,j)

    symbols = ['.\u25A1','.\u25A5', '.\u25A6', '.\u25A3', '.\u25A0']
    for i in range(n):
        print( ''.join([ symbols[i] for i in tiles.tiles[n*i:n*(i+1)] ]) )

