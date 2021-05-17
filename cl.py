#!/usr/bin/env python
"""
cl.py

Created by Tim Wilson <tim@timwilson.info> on 2009-09-02.
Copyright 2009, This software is distributed under the terms of the 
GNU General Public License (http://www.gnu.org/licenses/gpl.html).
"""

import random


class Game:
    """
    This class describes the game of Chutes and Ladders including the actual
    play of the game.
    """

    def __init__(self, players, board, debug=False, summary=False, logging=False):
        """
        At a minimum, you'll need to pass a list of one or more Player objects and
        a Board object to instantiate a Game object. The debug, summary, and logging
        parameters simply provide more information to a log file or the screen. Also,
        keep track of the number of rounds it takes to win.
        """

        self.players = players
        self.board = board
        self.debug = debug
        self.summary = summary
        self.logging = logging
        self.rounds = 0

    def play(self):
        """Run the simulation"""

        # Set up the logging file
        if self.logging:
            f = open("clgame.log", "w")

        s = Spinner()  # Create a spinner with six numbers
        while 1:
            for p in self.players:
                currentPosition = p.position
                spin = s.spin()
                p.spinHistory.append(str(spin))
                p.turns += 1
                self.rounds += 1

                # Make sure that the player hasn't rolled a number that would
                # put him beyond 100. Else, look to the board list and find
                # where the player's position should be.
                if currentPosition + spin > 100:
                    p.position = currentPosition
                else:
                    # Here's the key to the whole thing
                    p.position = self.board.squares[p.position + spin]

                # Print debug information to the screen
                if self.debug:
                    status = ""
                    if p.position < currentPosition:
                        status = "*CHUTE*"
                    elif p.position - currentPosition - spin > 1:
                        status = "*LADDER*"
                    print(
                        f"{p.name}  Prev: {currentPosition}  Spin: {spin}  New: {p.position}   {status}"
                    )

                # Write turn details to logging file
                if self.logging:
                    f.write(f"{p.name},{spin},{p.turns},{self.rounds}")

                # Check to see if we have a winner
                if p.position == self.board.finalSquare:
                    if self.summary:
                        print(f"Game winner: {p.name} in {p.turns} turns")
                    if self.logging:
                        f.close()
                    return p


class Board:
    """
    The Board class is really just a python list containing 100 items corresponding
    the squares where each player's piece should land. The player's piece starts off
    the board (self.squares[0]). If the player rolls a 4 on the spinner, the player's
    new position is found at self.squares[4].

    """

    def __init__(self):
        self.squares = [
            0,
            38,
            2,
            3,
            14,
            5,
            6,
            7,
            8,
            31,
            10,
            11,
            12,
            13,
            14,
            15,
            6,
            17,
            18,
            19,
            20,
            42,
            22,
            23,
            24,
            25,
            26,
            27,
            84,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            44,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            26,
            11,
            50,
            67,
            52,
            53,
            54,
            55,
            53,
            57,
            58,
            59,
            60,
            61,
            19,
            63,
            60,
            65,
            66,
            67,
            68,
            69,
            70,
            91,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            100,
            81,
            82,
            83,
            84,
            85,
            86,
            24,
            88,
            89,
            90,
            91,
            92,
            73,
            94,
            75,
            96,
            97,
            78,
            99,
            100,
        ]
        self.finalSquare = 100


class Player:
    """
    The Player class tracks the player's name, position on the board, total number
    of turns taken, and a list containing each of the player's spins during the game.

    """

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.turns = 0
        self.spinHistory = []


class Spinner:
    """
    A simple Spinner class that returns a random number from a Chutes and Ladders
    spinner. The default spinner has six numbers.

    """

    def __init__(self, numChoices=6):
        self.numChoices = numChoices

    def spin(self):
        number = random.choice(range(self.numChoices)) + 1
        return number


if __name__ == "__main__":
    # Here's a little piece of code that will actually run a game. Most of the time
    # you'll need to import cl.py to do something interesting with it.
    b = Board()
    p1 = Player("Joey")
    p2 = Player("Susie")
    players = [p1, p2]
    g = Game(players, b, 1, 1)
    g.play()
