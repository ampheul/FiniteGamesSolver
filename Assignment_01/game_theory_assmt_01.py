#!/usr/bin/python3

import node from Node

class Game:

    def __init__(self, m, n, **kwargs):

        self.m, self.n = m, n

        self.root = Node(None, self)
        self.root.populate()


    def printGame(self):
        self.root.printNode()

def main(args):

    game = Game(int(args[1]), int(args[2]))
    game.printGame()

if __name__ == "__main__":
    import sys
    main(sys.argv)
