# Game theory stuff

Here is a repository which solves finite games as discussed in an undegrad course.

We solve 3 games. The solutions are provided as the output as knight.py, domino.py, and ttttg.py

## The Knight game:
Players take turns moving a knight from some initial position on an n by n chessboard. The knight is only allowed to two tiles upwards or two tiles to the left. The player who cannot play loses (the knight has moved to the top right). This is an impartial game with normal play and so we can calculate a nim equivalency for each tile. This program prints an ascii version of the board with each tile colored based on its nim equivalency.


## The Domino game
Given an nxm grid, players take turns placing 2x1 dominoes. The player cannot place a domino 

`lib/` contains a bunch of files which I intend to use in future projects.
