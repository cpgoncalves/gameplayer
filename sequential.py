# Carlos Pedro Goncalves 2015
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
# University of Lisbon
# E-mail: cgoncalves@iscsp.ulisboa.pt
#
# Game Player - Game Theory Analyzer
#
# sequential.py contains Player class file: supporting game tree analysis
#
# Copyright (c) 2015 Carlos Pedro Goncalves


class Player:

    def __init__(self,playerID,level,myPlan):
        self.playerID = playerID
        self.level = level
        self.myPlan = myPlan

    def describePath(self,path):
        p = ''
        for node in path[0]:
            p = p + node + '->'
        p = p[:-2]
        print(p, ":", path[1])

    def communicateChoices(self):
        if len(self.myPlan) == 1:
            print("\nMy choice is:\n")
        else:
            print("\nMy choices are:\n")
        for alternative in self.myPlan:
            self.describePath(alternative)

    def describeClasses(self,strategyClasses):
        countClass = 0
        for strategyClass in strategyClasses:
            countClass += 1
            print("\nClass", countClass)
            for alternative in strategyClass:
                self.describePath(alternative)

    def evaluateClasses(self,strategyClasses):
        minPayoffs = []
        for strategyClass in strategyClasses:
            myPayoffs = []
            for configuration in strategyClass:
                payoff = configuration[1]
                myPayoffs.append(payoff[self.playerID])
            minPayoffs.append(min(myPayoffs))
        maxMin = max(minPayoffs)
        print("\nFor these classes, the MaxMin of my payoffs is", maxMin)
        preferred = []
        for i in range(0,len(strategyClasses)):
            if minPayoffs[i] == maxMin:
                preferred.append(strategyClasses[i])
        print("\nThe alternatives whose lowest payoff is highest")
        for strategyClass in preferred:
            for alternative in strategyClass:
                self.describePath(alternative)                
        return preferred

    def makeChoice(self,preferred):
        maxPayoffs = []
        for strategyClass in preferred:
            myPayoffs = []
            for configuration in strategyClass:
                payoff = configuration[1]
                myPayoffs.append(payoff[self.playerID])
            maxPayoffs.append(max(myPayoffs))
        print("\nThe above are the preferred alternatives")
        maxPayoffPreferred = max(maxPayoffs)
        for j in range(0,len(preferred)):
            if maxPayoffs[j] == maxPayoffPreferred:
                self.myPlan = self.myPlan + preferred[j]

    def returnClassBranch(self,strategyClass):
        path = strategyClass[0]
        fullBranch = path[0]
        branch = fullBranch[:self.level]
        return branch
    
    def planResponse(self,lastLevel,tree,nextPlan):
        print("\nI'm player", self.playerID, "playing at level", self.level)
        alreadyChecked = []
        if self.level == lastLevel:
            for pathA in tree:
                if pathA not in alreadyChecked:
                    alternatives = []
                    branchA = pathA[0]
                    alternatives.append(pathA)
                    alreadyChecked.append(pathA)
                    for pathB in tree:
                        if pathB not in alreadyChecked:
                            branchB = pathB[0]
                            if branchA[:self.level] == branchB[:self.level]:
                                alternatives.append(pathB)
                                alreadyChecked.append(pathB)
                    print("\nLooking at alternatives:\n")
                    for alternative in alternatives:
                        self.describePath(alternative)
                    payoffs = []
                    for alternative in alternatives:
                        alternativePayoffs = alternative[1]
                        myPayoff = alternativePayoffs[self.playerID]
                        payoffs.append(myPayoff)
                    maxPayoff = max(payoffs)
                    print("\nFor these alternatives my highest payoff is", maxPayoff)
                    for alternative in alternatives:
                        alternativePayoffs = alternative[1]
                        myPayoff = alternativePayoffs[self.playerID]
                        if myPayoff == maxPayoff:
                            self.myPlan = self.myPlan + [alternative]
            self.communicateChoices()
        else:
            strategyClasses = []
            for pathA in nextPlan:
                if pathA not in alreadyChecked:
                    alternatives = []
                    alternatives.append(pathA)
                    alreadyChecked.append(pathA)
                    for pathB in nextPlan:
                        if pathB not in alreadyChecked:
                            movesA = pathA[0]
                            movesB = pathB[0]
                            if movesA[:(self.level + 1)] == movesB[:(self.level + 1)]:
                                alternatives.append(pathB)
                                alreadyChecked.append(pathB)
                    strategyClasses.append(alternatives)
            print("\nI have the following strategy classes:")
            self.describeClasses(strategyClasses)
            if self.level == 0:
                preferred = self.evaluateClasses(strategyClasses)
                self.makeChoice(preferred)
                self.communicateChoices()
            else:
                comparison = []
                alreadyChecked = []
                for strategyClass in strategyClasses:
                    if strategyClass not in alreadyChecked:
                        branch = self.returnClassBranch(strategyClass)
                        alreadyChecked.append(strategyClass)
                        alternatives = []
                        alternatives.append(strategyClass)
                        for otherClass in strategyClasses:
                            if otherClass not in alreadyChecked:
                                otherBranch = self.returnClassBranch(otherClass)
                                if otherBranch == branch:
                                    alternatives.append(otherClass)
                                    alreadyChecked.append(otherClass)
                        comparison.append(alternatives)
                for alternativeClasses in comparison:
                    print("\nAnalyzing the strategy classes")
                    self.describeClasses(alternativeClasses)
                    preferred = self.evaluateClasses(alternativeClasses)
                    self.makeChoice(preferred)
                self.communicateChoices()
