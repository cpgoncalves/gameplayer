# Carlos Pedro Gonçalves (2015), Game Theory with Python
# Game Theory and Applied A.I. Classes
# Instituto Superior de Ciências Sociais e Políticas (ISCSP)
# University of Lisbon
# cgoncalves@iscsp.ulisboa.pt
#
# Two Company's Game (Simultaneous) (payoffs correspond to expected Return On Sales)
#
# For more details see the user manual that comes with the package:
# Gonçalves, C.P. (2015) "Game Player User Manual - A Game Theory Analyzer With Python",
#     https://sites.google.com/site/autonomouscomputingsystems/game-player

import gamep

config = []

gamep.addAlternative(["Lower price","Lower price"],[3,5],config)
gamep.addAlternative(["Lower price","Raise price"],[6,5],config)
gamep.addAlternative(["Raise price","Lower price"],[4,8],config)
gamep.addAlternative(["Raise price","Raise price"],[5,6],config)

gamep.analyzeGame(config,False)
