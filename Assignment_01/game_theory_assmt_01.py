#!/usr/bin/python3

import Node



def main(args):

    game = Game(m=int(args[1]), n=int(args[2]))
    game.printGame()

if __name__ == "__main__":
    import sys
    main(sys.argv)
