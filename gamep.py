# Carlos Pedro Goncalves 2015
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
# University of Lisbon
# E-mail: cgoncalves@iscsp.ulisboa.pt
#
# Game Player - Game Theory Analyzer
#
# Copyright (c) 2015 Carlos Pedro Goncalves


######################
# SIMULTANEOUS GAMES #
######################

import gameAI

def addAlternative(strategies,payoffs,config):
    configuration = (strategies,payoffs) # a game configuration code corresponds to a Python list of names of the strategies
                                         # played plus the associated payoff system 
    config.append(configuration) # append the configuration of the strategies plus the corresponding payoffs

def analyzeGame(config,showReasoning):
    AI = gameAI.GameAI(config,[],[]) # instantiate the game AI
    AI.evaluateGame(showReasoning) # evaluate the game




####################
# SEQUENTIAL GAMES #
####################

import sequential


def createPath(code,payoffs,tree):
    x = (code,payoffs) # a tree path node list plus the associated payoff system
    tree.append(x) # append the path to the tree (the tree is a list of tuples of paths and respective payoffs)


def pathDescription(path):
    p = '' # reset the auxiliary variable to empty string
    for node in path[0]: # for each node name in the path code
        p = p + node + '->' # add the node name plus the arrow ->
    p = p[:-2] # remove the final arrow that points nowhere
    return p
    

def showTree(tree):
    for path in tree: # for each path
        p = pathDescription(path) # implement the describePath function
        p = p + ': ' + str(path[1]) # add the payoff
        print(p) # print the path with the payoff

def treeDepth(tree):
    pathDepths = [] # list to store the depth of each path
    for path in tree:
        pathDepths.append(len(path[0])) # add the depth of each path (the length of the path code string)
    maxDepth = max(pathDepths) # calculate the maximum depth
    return maxDepth # return the maximum depth


def evaluateTree(tree,plays):
    # this function will print out each player's strategic reasoning and final choices
    maxDepth = treeDepth(tree) # store the tree's maximum depth (number of levels)
    players = [] # we will need multiple instances of the class Player
    lastLevel = maxDepth - 1 # the last level of the tree
    for level in range(0,maxDepth):
        # the instances of the class Player correspond to software agents that
        # have an ID corresponding to the ID of the player that plays at a certain
        # level of the tree, a level to which the software agent  is associated and
        # the player's plan
        players = players + [sequential.Player(plays[level],level,[])]
    for i in range(0,maxDepth):
        activeLevel = lastLevel - i
        print("\nEvaluating Level", activeLevel)
        if activeLevel == lastLevel:
            # the last level player plays first
            nextPlan = []
            LastPlayer = players[activeLevel]
            LastPlayer.planResponse(lastLevel,tree,nextPlan)
            # the player's plan becomes the next plan for the subsequent level:
            nextPlan = LastPlayer.myPlan
        else:
            # the other players play next in sequence from the end of the tree
            # to the beginning
            for Agent in players:
                if Agent.level == activeLevel:
                    Agent.planResponse(lastLevel,tree,nextPlan)
                    nextPlan = []
                    # each player's adaptive plan becomes the next plan for
                    # the subsequent level:
                    nextPlan = Agent.myPlan
    # the first player's plan now has the final pruned tree configuration
    # that comes out of the other player's choices:
    FirstPlayer = players[0]
    finalTree = FirstPlayer.myPlan
    print("\nFinal Choices:\n")
    showTree(finalTree)
    return finalTree
