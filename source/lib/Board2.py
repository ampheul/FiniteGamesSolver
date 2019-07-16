#!/usr/bin/python
from typing import TypeVar, List, Tuple, Iterator

Tile = TypeVar('Tile', int, str)

Board = Tuple[Tuple[Tile,...], int, int]

'''Board2
    A datatype and functions for a hashable board.
'''

def makeBoard(m : int, n : int) -> Board:
    '''makeBoard
        makes an empty board
    '''
    return ( tuple( 0 for i in range(m*n) ), m, n )

def rows(board: List[Tile], m : int, n : int) -> Iterator[ Tuple[Tile,...] ]:
    for i in range(m):
        yield tuple( board[ m*i + j ] for j in range(n) )

if __name__ == "__main__":
    board1 = makeBoard(10, 15) # type: Snoard
    board2 = makeBoard(10, 15)

