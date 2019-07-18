from enum import Enum
from typing import Type, TypeVar, Optional, Dict, List


class Player(Enum):
    one = 1
    two = 2
T = TypeVar('T')

class Game:
    '''
    Game
    ====
    An interface for implementing games with normal play.
    Generates a values for the game using zermelos algorithm.
    '''

    def options(self: T) -> Generator[T, None, None]:
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
    def nim_options(self) -> Generator[int, None, None]:
        for option in self.options():
            yield option.nim_value()

    @property()
    def nim_value(self) -> int:
        ...

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
    
    '''
    for option in game.options():

        if zermelo(option, toggle[player]) is player:

            return player

    return toggle[player]

