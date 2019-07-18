#!/usr/bin/python3
'''
domino.py
========================================
This script prints out the tree view of the domino game.

The domino game is simple. On a recangular board of dimensions n x m
players take turns 

'''
import sys

class Tile:

    def __init__(self, content = None):
        self.content = content

    def __eq__(self, other):
        return self.content == other.content

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        if self.content == None:
            return '\u25A1'
        else:
            return str(self.content)

    def __bool__(self):
        return not (self.content is None)


class Board:
    def __init__(self, m, n):

        self.m, self.n = m, n
        self.tiles = []

        for i in range(m):
            self.tiles.append([])
            for j in range(n):
                self.tiles[i].append(Tile())

    def __eq__(self, other):

        if self.m != other.m or self.n != other.n:
            return False
        # compare them tile by tile
        for i in range(self.m):
            for j in range(self.n):
                if self.tiles[i][j] != other.tiles[i][j]:
                    return False
        return True

    @staticmethod
    def copyBoard(board):

        boardCopy = Board(board.m, board.n)

        for i in range(boardCopy.m):

            for j in range(boardCopy.n):

                boardCopy.tiles[i][j] = board.tiles[i][j]

        return boardCopy
    def __isPlayable(self, i, j):

        return i < self.m and j < self.n and not bool(self.tiles[i][j])

    def playDomino(self, a, b, c):

        m, n = self.m, self.n
        a0, a1 = a[0], a[1]
        b0, b1 = b[0], b[1]
        tiles = self.tiles

        # if index is out of range, or a tile is occupied
        if self.__isPlayable(a0, a1) and self.__isPlayable(b0, b1):

            self.tiles[a0][a1] = Tile(c)
            self.tiles[b0][b1] = Tile(c)
            return True

        return False


class Node:
    def __init__(self, parent = None, game = None):

        self.parent = parent
        self.game = game

        if not parent is None:

            m, n = parent.board.m, parent.board.n
            self.board = Board.copyBoard(parent.board)
            self.player = 2 if parent.player ==  1 else 1

        else:

            m, n = game.m, game.n
            self.board = Board(m, n)
            self.player = 1

        self.children = []

        # alternate the player

        # "NONE" is a transitive game state, "WIN" is p1 win "LOSE" is p1 loss
        self.__nlines = None

    def populate(self):

        m, n = self.board.m, self.board.n
        tiles = self.board.tiles
        child = Node(self, self.game)
        domino = '\u25a0' if self.player == 1 else '\u25a8'
        for i in range(m):

            for j in range(n):

                if child.board.playDomino((i, j), (i+1, j), domino):

                    self.children.append(child)
                    child.populate()
                    child = Node(self, self.game)


                if child.board.playDomino((i, j), (i, j+1), domino):

                    self.children.append(child)
                    child.populate()
                    child = Node(self, self.game)

        return

    def printNode(self):
        # while the line is not all spaces
        for i in range(self.__numLines()):
            if i % self.board.m == 0:
                print()
            s = self.__getLine(i);
            print(s)

    def __getLine(self, lineNum):

        if lineNum > self.__numLines():
            return ''

        s = ''
        m, n = self.board.m, self.board.n
        tiles = self.board.tiles
        if lineNum < m:
            for j in range(n):
                s += str(tiles[lineNum][j])
        else:
            s += ''.rjust(self.board.n)
        s += ' '.rjust(4)

        for i in range(len(self.children)):

            child = self.children[i]

            if child.__numLines() > lineNum:

                s += child.__getLine(lineNum)
                break

            else:
                lineNum -= child.__numLines()
        if len(self.children) == 0 and lineNum % m == 0:
            s +=  "   W" if self.player == 2 else "   L"
        return s

    def __numLines(self):

        if self.__nlines is None:

            sum = 0
            for child in self.children:
                sum += child.__numLines()
            m = self.board.m
            self.__nlines = m if m > sum else sum

        return self.__nlines


class Game:

    def __init__(self, m, n):

        self.m, self.n = m, n

        self.root = Node(None, self)
        self.root.populate()


    def printGame(self):
        self.root.printNode()

def main(args):
    game = Game(int(args[1]), int(args[2]))
    game.printGame()

if __name__ == "__main__":
    main(sys.argv)
