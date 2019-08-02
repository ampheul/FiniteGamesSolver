Finite Games Solver
===================

This repository contains many examples of finite games and solutions.

We solve 3 games.

The Knight game:
----------------

Players take turns moving a knight on an nxn chessboard.
Valid knight moves are squares which bring the knight closer to the top left corner
The player who cannot play loses.
This is an impartial game with normal play and so we can calculate a nim
equivalency for each square. This program prints
an ascii version of the board with each tile colored based on its nim
equivalency.

The Domino game
---------------

Given an nxm grid, players take turns placing 2x1 dominoes. The player who
cannot place a domino loses. print out the

.. note::
    
    It is easy to generate very large graphs with domino.py, it is recommended that you do not use numbers greater than 5.

As discussed in MATH 3157B at Western University during spring 2018
