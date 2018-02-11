'''Board

    A class for simulating a board style data structure.
    Intended for use in games.
'''


class Board:
    '''A hashable board class.
    '''
    class Tile:
        empty = '.'
    def __init__(self, m, n, tiles=(), **kwargs):

        # tiles are in a 1-D array since this is faster and easier to slice with

        self.m, self.n = m, n
        self.tiles = tiles

    '''properties.
    these will make overriding functionality easier
    '''
    @property
    def m(self):
        return self.__m
    @property
    def n(self):
        return self.__n
    @property
    def tiles(self):
        return __tiles

    def row(self, index):
        '''returns a row in the board indexed 0 to m-1
        '''
        return self.tiles[index*n:(index+1)*n]

    def rows(self):
        '''rows
        returns a generator expression for the rows
        '''
        m, n = self.m, self.n

        return (self.tiles[i*n: (i+1)*n] for i in range(m) )

    def get(self, x, y):
        '''get
        returns the element in self.__tiles if the position is valid.
        otherwise returns None
        '''
        if x >= 0 and x < self.m and y >=0 and y < self.n:

            return self.tiles[ x*self.m + y ]

        else:

            return None

    def __getitem__(self, key):
        '''takes a key of tuple(int, int) type indexing a row and column of the
        board
        '''
        return self.get(*key)

    def __hash__(self):

        try:

            return self.hash

        except AttributeError:

            self.hash = hash(self.tiles)

            return self.hash



if __name__ == "__main__":

    def print_board(board):

        for row in board.rows():

            print(''.join(['x' if i == 0 else 'o' for i in row]))

        print(board[1,2])

    board = Board(4, 5, tiles= tuple(i % 2 for i in range(4*5)))
    print_board(board)
