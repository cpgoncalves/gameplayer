# Carlos Pedro Gonçalves (2015), Game Theory with Python
# Game Theory and Applied A.I. Classes
# Instituto Superior de Ciências Sociais e Políticas (ISCSP)
# University of Lisbon
# cgoncalves@iscsp.ulisboa.pt
#
# New Entrant vs Market Leader (payoffs correspond to strategic value)
#
# For more details see the user manual that comes with the package:
# Gonçalves, C.P. (2015) "Game Player User Manual - A Game Theory Analyzer With Python",
#     https://sites.google.com/site/autonomouscomputingsystems/game-player

import gamep # import the game player main module

tree = [] # setup the game tree

# design the tree in accordance with the problem:
# the "No move" is added at a given level whenever the player has no alternative choice
# this allows us to deal with a tree with different branch lengths
gamep.createPath(["Enter","Propose partnership","Accept partnership","No move"], [5,3],tree)
gamep.createPath(["Enter","Propose partnership","Reject partnership","Fight"], [-2,3.5],tree)
gamep.createPath(["Enter","Propose partnership","Reject partnership","Do not fight"], [4,2],tree)
gamep.createPath(["Enter","Do not propose partnership","Fight","No move"], [-1,3],tree)
gamep.createPath(["Enter","Do not propose partnership","Do not fight","No move"], [4,2],tree)
gamep.createPath(["Do not enter","No move","No move","No move"],[0,5],tree)
gamep.showTree(tree)

# play sequence New Entrant plays in the first two levels then the Market Leader plays
# in the next two levels 
plays = [0,0,1,1]

gamep.evaluateTree(tree,plays) # evaluate the game tree
