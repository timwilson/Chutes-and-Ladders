#!/usr/bin/env python
# encoding: utf-8
"""
winAnalyzer.py

Created by Tim Wilson on 2009-09-30.
Copyright 2009, This software is distributed under the terms of the 
GNU General Public License (http://www.gnu.org/licenses/gpl.html).
"""

def main():
	"""
	Use the Chutes and Ladders library (cl.py) to run these simulations.

	Analyze the results from the cl_7turns simulations to identify the unique set
	of 7-turn Chutes and Ladders wins.
	
	"""
	f = open('spinHistory.log', 'r')
	spinHistory = [x.strip() for x in f.readlines()]
	f.close()
	uniqueWins = {}
	for win in spinHistory:
		if not uniqueWins.has_key(win):
			uniqueWins[win] = 1
		else:
			uniqueWins[win] += 1
	winkeys = uniqueWins.keys()
	winkeys.sort()
	for k in winkeys:
		print "%s:%s" % (k, uniqueWins[k])

if __name__ == '__main__':
	main()

