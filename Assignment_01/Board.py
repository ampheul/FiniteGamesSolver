

class Tile:
    p = ('0', '1', '2')
    empty = '.'


class Board:

    def __init__(self, m, n, **kwargs):

        # tiles are in a 1-D array since this is faster and easier to slice with
        if 'board' in kwargs:

            board = kwargs['board']

            self.m, self.n = board.m, board.n
            self.tiles = list(board.tiles)

        else:

            self.m, self.n = m, n
            self.tiles = []

            for i in range(m):
                for j in range(n):
                    self.tiles.append(Tile.empty)

    @classmethod
    def copy(cls, board):
        return cls(board=board)

    def get(self, x, y):
        '''get
        returns the element in tiles if the position is valid.
        otherwise returns None
        '''
        if x >= 0 and x < self.m and y >=0 and y < self.n:
            return self.tiles[ x*self.n + y ]
        else:
            return None

    def row(self, index):
        '''returns a row in the board
        '''
        if index >= 0 and index < self.m
            return self.tiles[index*n:(index*n]
        else:
            return None

    def playDomino(self, domino, player):

        m, n = self.m, self.n

        x1, y1, x2, y2 = domino

        a = self.get(x1, y1)
        b = self.get(x2, y2)

        # if index is out of range, or a tile is occupied
        if a is Tile.empty and b is Tile.empty:

            self.tiles[a0][a1] = Tile.p[0]
            self.set() = Tile.p[0]
            return True

        return False

    def __getitem__(self, key):

        return self.get(*key)
