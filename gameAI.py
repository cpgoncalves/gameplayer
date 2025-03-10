# Carlos Pedro Goncalves 2015
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
# University of Lisbon
# E-mail: cgoncalves@iscsp.ulisboa.pt
#
# Game Player - Game Theory Analyzer
#
# gameAI.py class file: supports the analysis of simultaneous games
#
# Copyright (c) 2015 Carlos Pedro Goncalves



class GameAI:

    def __init__(self,game,notChosen,checked):
        self.game = game
        self.notChosen = notChosen
        self.checked = checked

    def evaluateGame(self,showReasoning):
        for i in range(0,len(self.game) - 1):
            configuration = self.game[i]
            if showReasoning == True:
                print("\nAnalyzing", configuration, "\n")
            for possibleAlternative in self.game:
                if possibleAlternative not in self.checked:
                    counter = 0
                    if possibleAlternative[0] != configuration[0]:
                        if showReasoning == True:
                            print("Comparing with", possibleAlternative)
                        strategyA = configuration[0]
                        strategyB = possibleAlternative[0]
                        for i in range(0,len(strategyA)):
                            if strategyA[i] != strategyB[i]:
                                counter += 1
                        if counter == 1:
                            if showReasoning == True:
                                print("Matches a single switch alternative\n")
                            payoffsA = configuration[1]
                            payoffsB = possibleAlternative[1]
                            for j in range(0,len(strategyA)):
                                if strategyA[j] != strategyB[j]:
                                    if payoffsA[j] < payoffsB[j]:
                                        if showReasoning == True:
                                            print(configuration, "is suboptimal")
                                            print("Player", j, "prefers to play", strategyB[j], "\n")
                                        if configuration not in self.notChosen:
                                            self.notChosen = self.notChosen + [configuration]
                                    elif payoffsA[j] > payoffsB[j]:
                                        if showReasoning == True:
                                            print(possibleAlternative, "is suboptimal")
                                            print("Player", j, "prefers to play", strategyA[j], "\n")
                                        if possibleAlternative not in self.notChosen:
                                            self.notChosen = self.notChosen + [possibleAlternative]
                                    else:
                                        if showReasoning == True:
                                            print("Player", j, "is indifferent between the two alternatives\n")
                                    break
                            
                        else:
                            if showReasoning == True:
                                print("Does not match a single switch alternative\n")
            self.checked = self.checked + [configuration]
        if showReasoning == True:
            print("\nNot Chosen: ", self.notChosen)
        equilibria = []
        for configuration in self.game:
            if configuration not in self.notChosen:
                equilibria.append(configuration)
        if len(equilibria) == 0:
            print("\nThis game has no pure strategies Nash equilibria!")
        else:
            if len(equilibria) == 1:
                print("\nThe pure strategies Nash equilibrium is:")
            else:
                print("\nThe pure strategies Nash equilibria are:")
            for element in equilibria:
                print(element[0], "| payoff:", element[1])
            print("\n")
        return equilibria                    
