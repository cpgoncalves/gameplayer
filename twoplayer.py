"""
Created on Sat Mar  8 11:25:59 2025

Two-player game analyzer for two player games using Strategy Analyzer

The software model imports a two-person game matrix from Excel and 
performs the following analyses:
    1. Finds the pure strategies Nash equilibria for the simultaneous game
    2. Analyzes two sequential games alternatives
    3. Calculates the probability scenarios in case of a single mixed
       strategy equilibrium


@author: Carlos Pedro Gonçalves
@institution: Lusophone University Lisbon, University Center
@school: School of Economic Sciences and Organizations
@department: Department of Management on Civil Aviation and Airports


"""

import pandas as pd
import numpy as np
from numpy.linalg import matrix_rank as mrank
from numpy.linalg import inv
import gamep as gp
import ast



def read_file(filename):
    # Get the Excel file as a Pandas dataframe object
    GF = pd.read_excel(filename, header=0, index_col=0) 
    return GF



def game_analysis(GF):
    
    # Print the game dataframe and the strategies for each player
    
    print("\nGame Matrix:")
    print(GF)
    
    print("\nRow Player Strategies:")
    Row = list(GF.index)
    print(Row)
    
    print("\nColumn Player Strategies:")
    Column = list(GF.columns.values)
    print(Column)
    
    lRow= len(Row)
    lColumn = len(Column)
    
    # Extract the numpy array for the game matrix
    
    GM = np.array(GF,dtype=tuple)
    
    
    config = [] # configuration for simultaneous game
    tree_row = [] # decision tree for sequential game starting with row player
    tree_column = [] # decision tree for sequential game starting with column player
    
    # Payoff matrices for R (row) and C (column) players to be used in mixed
    # strategies analysis
    R = np.zeros((lRow,lColumn))
    C = np.zeros((lRow,lColumn))
    
    # For each row and column...
    for i in range(0,lRow):
        for j in range(0,lColumn):
            
            # extract the strategies for the simultaneous game and for
            # the sequential game with the row player playing first
            strategy=[Row[i],Column[j]]
            
            # extract the strategies for the sequential game with the
            # column player playing first
            strategy_seq_column=[Column[j],Row[i]]
            
            # extract the payoffs for the simultaneous game and for the 
            # sequential game with the row player playing first
            payoffs=ast.literal_eval(GM[i][j])
            
            # extract the payoffs for the sequential game with the column
            # player playing first
            payoffs_seq_column=ast.literal_eval(GM[j][i])
            
            # extract the row and column player payoff matrices for the
            # mixed strategies equilibrium calculation
            R[i,j]=payoffs[0]
            C[i,j]=payoffs[1]
            
            # add alternative strategic configurations for the simultaneous
            # game
            gp.addAlternative(strategy,payoffs,config)
            
            # add the tree paths for the alternative sequential games
            gp.createPath(strategy,payoffs,tree_row)
            gp.createPath(strategy_seq_column,payoffs_seq_column,tree_column)
            
    
    # Print the game scenarios for the simultaneous game in the A.I.'s
    # working memory
    print("\nGame Scenarios for Simultaneous Game:")
    for scenario in config:
        print(scenario)
    
    # Calculate the Nash equilibria for the simultaneous game
    equilibria=gp.analyzeGame(config,False)
    
    # Get the row and column matrices for mixed strategies evaluation
    R=np.matrix(R)
    R=R.T
    C=np.matrix(C)
    
    
    # Sequential analysis if the row and column player plays first
    print("\nPerforming Sequential Analysis")
    plays = [0,1]
    
    print("\nRow player plays first")
    
    gp.showTree(tree_row)
    RTree = gp.evaluateTree(tree_row,plays)
    
    
    print("\nColumn player plays first")
    gp.showTree(tree_column)
    gp.evaluateTree(tree_column,plays)
    CTree = gp.evaluateTree(tree_column,plays)
    
    
    
    # Return the payoff matrices the row and column player's strategies lists
    # and the Nash equilibria
    return R, C, Row, Column, equilibria, RTree, CTree



def analyze_matrix(GF):
    
    # Perform the game analysis from the game dataframe
    R, C, Row, Column, equilibria, RTree, CTree = game_analysis(GF)
    
       
    # Number of columns in the row and column player's strategies
    nR=R.shape[1]
    nC=C.shape[1]
    
    
    # If the mixed strategies' analysis is requested for scenario probability
    # calculations
    if equilibria == None or len(equilibria) != 1:
        print("\nAnalyzing Mixed Strategies")
        
        # Get the linear equation system's matrices for the row and column
        # players' equilibrium probabilities
        MR = []
        MC = []
        
        # Row player uses column player's payofss while column player uses
        # row player's payoffs
        for i in range(1,nC):
            MR.append(list(np.array(C[:,0].T-C[:,i].T)[0])+[0.0])
        for i in range(1,nR):
            MC.append(list(np.array(R[:,0].T-R[:,i].T)[0])+[0.0])
            
        MR.append(list(np.ones(nC))+[1.0])
        MC.append(list(np.ones(nR))+[1.0])
        
        MR = np.matrix(MR)
        MC = np.matrix(MC)
        
        # Print the row and column player's matrices for the system's of
        # linear equations
        print(MR)
        print(MC)
        
        
        # Analyze the system of linear equations
        if mrank(MR[:,:-1]) == mrank(MR) == C.shape[1]:
            print("\nThere is a single solution for row player probabilities")
            gR='PDS'
        elif mrank(MR[:,:-1]) == mrank(MR) < C.shape[1]:
            print("\nThere is more than one solution for row player probabilities")
            gR='IPS'
        elif mrank(MR[:,:-1]) < mrank(MR):
            print("\nThere is no solution for row player probabilities")
            gR='IS'
        
        if mrank(MC[:,:-1]) == mrank(MC) == R.shape[1]:
            print("\nThere is a single solution for column player probabilities")
            gC='PDS'
        elif mrank(MC[:,:-1]) == mrank(MC) < R.shape[1]:
            print("\nThere is more than one solution for column player probabilities")
            gC='IPS'
        elif mrank(MC[:,:-1]) < mrank(MC):
            print("\nThere is no solution for column player probabilities")
            gC='IS'
        
        
        # If the system is possible definite...
        if gR == 'PDS' and gC=='PDS':
            print("\nThere is a single solution for linear equations")
            
            p_valid=True # logical control for valid solution analysis
            
            # calculate the row player's equilibrium probabilities
            print("\nCalculating row player probabilities:")
            print("\nFull system's matrix")
            print(MR)
            print("\nProbabilities values")
            P_row = np.dot(inv(MR[:,:-1]),MR[:,-1])
            P_row=list(np.array(P_row.T)[0])
            for i in range(0,len(Row)):
                print("\nRow player strategy:", Row[i])
                print("Probability:", P_row[i])
                if P_row[i] < 0 or P_row[i] > 1:
                    print("WARNING: PROBABILITY OUTSIDE OF DOMAIN BOUNDS")
                    print("NO MIXED STRATEGIES EQUILIBRIUM IS PRESENT")
                    p_valid = False
            
            # calculate the column player's equilibrium probabilities
            print("\nCalculating column player probabilities:")
            print("\nFull system's matrix")
            print(MC)
            print("\nProbabilities values")
            P_column = np.dot(inv(MC[:,:-1]),MC[:,-1])
            P_column = list(np.array(P_column.T)[0])
            print(P_column)
            for i in range(0,len(Row)):
                print("\nColumn player strategy:", Column[i])
                print("Probability:", P_column[i])
                if P_column[i] < 0 or P_column[i] > 1:
                    print("\nWARNING: PROBABILITY OUTSIDE OF DOMAIN BOUNDS")
                    print("NO MIXED STRATEGIES EQUILIBRIUM IS PRESENT")
                    p_valid = False
            
            
            
            # extract the scenarios with the strategic configurations
            # and probabilities if the solution provides for valid
            # probabilities:
            if p_valid == True:
                scenarios = []
                
                for i in range(0,len(Row)):
                    for j in range(0,len(Column)):
                        scenario=[]
                        scenario.append(Row[i])
                        scenario.append(Column[j])
                        scenario.append(P_row[i]*P_column[j])
                        scenarios.append(scenario)
                
                # place the scenarios as a Pandas dataframe
                scenarios_df=pd.DataFrame(data=scenarios,columns=['Row Player','Column Player','Probability'])
                
                # save the scenarios to Excel file
                scenarios_df.to_excel('Scenarios.xlsx')
            else:
                print("\nNo valid mixed strategies equilibrium was found!")
    
    print("\nPure Strategies Synthesis:")
    print("\nSimultaneous Game Equilibrium:")
    if len(equilibria) != 0:
        for element in equilibria:
            print(element)
    print("\nSequential Game:")
    print("\nIf row player plays first:")
    gp.showTree(RTree)
    print("\nIf column player plays first:")
    gp.showTree(CTree)
    
    
    
