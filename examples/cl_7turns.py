#!/usr/bin/env python
"""
cl_7turns.py

Created by Tim Wilson on 2009-09-03.
Copyright 2009, This software is distributed under the terms of the 
GNU General Public License (http://www.gnu.org/licenses/gpl.html).
"""


import cl


def main():
    """
    Use the Chutes and Ladders library (cl.py) to run these simulations.

    The shortest possible Chutes and Ladders game is 7 turns. Let's see how
    many different ways you can win in 7 turns.

    """
    numSims = int(input("How many game simulations? "))
    minTurns = 1000
    maxTurns = 0
    totalRounds = 0
    uniqueSpinHistory = []
    board = cl.Board()
    f = open("spinHistory.log", "w")
    for i in range(numSims):
        p = cl.Player("Tim")
        g = cl.Game([p], board)
        winner = g.play()
        if len(winner.spinHistory) == 7:
            history = ", ".join(winner.spinHistory)
            if history not in uniqueSpinHistory:
                uniqueSpinHistory.append(history)
            f.write(f"{history}\n")
        totalRounds += g.rounds
        if g.rounds > maxTurns:
            maxTurns = g.rounds
        if g.rounds < minTurns:
            minTurns = g.rounds
        p.position = 0
        p.turns = 0
    f.close()
    avgRounds = float(totalRounds) / numSims
    print(f"Min: {minTurns}  Max: {maxTurns}  Avg: {avgRounds:.2f}")


if __name__ == "__main__":
    main()
