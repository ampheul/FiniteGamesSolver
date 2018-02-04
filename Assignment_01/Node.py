from board import Board


class Node:
    def __init__(self, parent = None, game = None, **kwargs):

        self.parent = parent
        self.game = game

        try:

            m, n = parent.board.m, parent.board.n
            self.board = Board(board= parent.board)
            self.player = 2 if parent.player ==  1 else 1

        except AttributeError:

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
