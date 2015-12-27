# Carlos Pedro Gonçalves (2015), Game Theory with Python
# Game Theory and Applied A.I. Classes
# Instituto Superior de Ciências Sociais e Políticas (ISCSP)
# University of Lisbon
# cgoncalves@iscsp.ulisboa.pt
#
# Two Company's Game (Sequential) (payoffs correspond to expected Return On Sales)
#
# For more details see the user manual that comes with the package:
# Gonçalves, C.P. (2015) "Game Player User Manual - A Game Theory Analyzer With Python",
#     https://sites.google.com/site/autonomouscomputingsystems/game-player


import gamep # import the game player main module

tree = [] # setup the game tree

# design the tree in accordance with the problem:
gamep.createPath(["Lower price","Lower price"],[3,5],tree)
gamep.createPath(["Lower price","Raise price"],[6,5],tree)
gamep.createPath(["Raise price","Lower price"],[4,8],tree)
gamep.createPath(["Raise price","Raise price"],[5,6],tree)
gamep.showTree(tree)

plays = [0,1] # define the play sequence

finalTree = gamep.evaluateTree(tree,plays) # evaluate the game tree
