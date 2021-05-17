#!/usr/bin/env python
"""
cl_firstMoveAdvantage.py

Created by Tim Wilson on 2009-09-10.
Copyright 2009, This software is distributed under the terms of the 
GNU General Public License (http://www.gnu.org/licenses/gpl.html).
"""

import cl


def main():
    """
    Use the Chutes and Ladders library (cl.py) to run these simulations.

    Let's discover whether having the first turn produces a statistically significant
    advantage in winning the game. Note, this only produces the win/loss data. You'll
    need to analyze the results in a spreadsheet or other numerical tool.

    """
    numSims = 1000
    f = open("clwinners.log", "w")
    for i in range(numSims):
        board = cl.Board()
        p1 = cl.Player("1")
        p2 = cl.Player("2")
        g = cl.Game([p1, p2], board)
        winner = g.play()
        f.write(f"{winner.name}\n")
    f.close()


if __name__ == "__main__":
    main()
