# Carlos Pedro Gonçalves (2015), Game Theory with Python
# Game Theory and Applied A.I. Classes
# Instituto Superior de Ciências Sociais e Políticas (ISCSP)
# University of Lisbon
# cgoncalves@iscsp.ulisboa.pt
#
# Two Person's Prisonners' Dilemma Game
#
# For more details see the user manual that comes with the package:
# Gonçalves, C.P. (2015) "Game Player User Manual - A Game Theory Analyzer With Python",
#     https://sites.google.com/site/autonomouscomputingsystems/game-player


import gamep # import game player main module

config = [] # setup the game configuration list

# add the alternative game configurations:
gamep.addAlternative(["Cooperate","Cooperate"],[2,2],config)
gamep.addAlternative(["Cooperate","Defect"],[0,4],config)
gamep.addAlternative(["Defect","Cooperate"],[4,0],config)
gamep.addAlternative(["Defect","Defect"],[1,1],config)

print("\nGame Configuration: ", config)

gamep.analyzeGame(config,True) # analyze the game
