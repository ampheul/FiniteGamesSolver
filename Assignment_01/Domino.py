from Game import Game, SubGame
from Board import Board

class DominoBoard(Board):

class Domino(Game):
    '''an mxn domino game

    expresses tiles as sets of played positions
    allows playing of a domino if netiher of its edges are in the
    '''
    def __init__(self, m, n, *arr, **kwargs):

        super().__init__(self, *arr, **kwargs)
        self.board = Board(m,n)
        self.__group = SymmetryGroup.d8(n) if m == n else SymmetryGroup.z2xz2(m,n)


    def symmetric(self, other):

        for sigma in self.__group.elements:

            self.state == other.state

    @property
    def state(self):
        '''state is all played moves
        '''
        return self.__state

    @state.setter(self):
    def state(self):



    @property
    def options(self):
