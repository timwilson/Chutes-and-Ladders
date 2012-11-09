#!/usr/bin/env python
# encoding: utf-8
"""
cl_numTurns.py

Created by Tim Wilson on 2009-09-10.
Copyright 2009, This software is distributed under the terms of the 
GNU General Public License (http://www.gnu.org/licenses/gpl.html).
"""

import cl

def main():
	"""
	Use the Chutes and Ladders library (cl.py) to run these simulations.

	Let's discover the minimum, maximum, mean, and median number of turns required
	to win a Chutes and Ladders game.
		
	"""
	numSims = 1000000
	turnLog = []
	turnSum = 0
	f = open('clturns.log', 'w')
	for i in range(numSims):
		board = cl.Board()
		p1 = cl.Player("1")
		g = cl.Game([p1], board)
		winner = g.play()
		f.write("%s\n" % winner.turns)
		turnLog.append(winner.turns)
		turnSum += winner.turns
	f.close()
	turnLog.sort()
	mean = turnSum/float(numSims)
	minimum = turnLog[0]
	maximum = turnLog[-1]
	median = turnLog[numSims/2]
	print "Mean: %s" % mean
	print "Median: %s" % median
	print "Minimum: %s" % minimum
	print "Maximum: %s" % maximum

if __name__ == '__main__':
	main()

