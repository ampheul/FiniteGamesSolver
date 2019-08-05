from enum import Enum
from typing import Type, Tuple, TypeVar, Generator, Iterable, Dict, List
from typing_extensions import Protocol

import operator
import functools


class Player(Enum):
    one = 1
    two = 2

T = TypeVar('T')

class Game(Protocol):
    '''
    Game
    ====
    An interface for implementing games with normal play.
    Generates a values for the game using zermelos algorithm.
    '''

    def options(self: T) -> Iterable[T]:
        ...


class NormalPlay(Game):
    '''
    NormalPlay
    ==========
    The type of game that the basic zermelo's algorithm applies to.
    '''
    pass

class Nim(NormalPlay):
    '''
    Nim
    ===
    The type of game that has a nim equivalence.
    '''
    pass

def mex(values : Iterable[int]) -> int:
    '''
    mex
    ===
    Provides the minimal excluded value in a list of non-negative integers.

    Parameters
    ----------
    values : Iterable[int]

    Returns
    -------
    int
        returns the minimal excluded integer among values.

    '''
    unique_values = sorted(set(values))

    if len(unique_values) == 0:
        return 0

    def binary_search(start: int, end: int) -> int:
        if start >= end:
            return start
        
        middle = ( start + end ) // 2
        
        if unique_values[middle] <= middle:
            return binary_search(middle, end)
        else:
            return binary_search(start, middle)
    
    return 1 + binary_search(0, len(unique_values))


nim_sum = functools.partial(functools.reduce, operator.xor)

toggle = {
    Player.one : Player.two,
    Player.two : Player.one
} # Dict[Player, Player]


def zermelo(game : NormalPlay, player : Player) -> Player:
    '''
    Zermelo
    =======
    Applies zermelo's algorithm on a game with normal play 
    and starting player to determine a winner.

    Parameters
    ----------
    game : NormalPlay
        A game with normal play condition. i.e, the player who cannot make a move loses.
    
    player : Player
        The player who plays first.
    
    Returns
    -------
    Player
        returns the player who has a winning strategy.
    '''
    for option in game.options():

        if zermelo(option, toggle[player]) is player:

            return player

    return toggle[player]

