
# Carlos Pedro Gonçalves (2015), Game Theory with Python
# Game Theory and Applied A.I. Classes
# Instituto Superior de Ciências Sociais e Políticas (ISCSP)
# University of Lisbon
# cgoncalves@iscsp.ulisboa.pt
#
# Three Person's Prisonners' Dilemma Game
#
# For more details see the user manual that comes with the package:
# Gonçalves, C.P. (2015) "Game Player User Manual - A Game Theory Analyzer With Python",
#     https://sites.google.com/site/autonomouscomputingsystems/game-player

import gamep

config = []

gamep.addAlternative(["Cooperate","Cooperate","Cooperate"],[2,2,2],config)
gamep.addAlternative(["Cooperate","Cooperate","Defect"],[2.5,2.5,1],config)
gamep.addAlternative(["Cooperate","Defect","Cooperate"],[2.5,1,2.5],config)
gamep.addAlternative(["Cooperate","Defect","Defect"],[0,2,2],config)

gamep.addAlternative(["Defect","Cooperate","Cooperate"],[1,2.5,2.5],config)
gamep.addAlternative(["Defect","Cooperate","Defect"],[2,0,2],config)
gamep.addAlternative(["Defect","Defect","Cooperate"],[2,2,0],config)
gamep.addAlternative(["Defect","Defect","Defect"],[1,1,1],config)


gamep.analyzeGame(config,True)
