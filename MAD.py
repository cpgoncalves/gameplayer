# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:19:32 2025

Application of two-player game analyzer to the Mutually Assured 
destruction game with payoffs on a scale of -10 to 10.

The analysis finds performs the analysis for the simultaneous and sequential
games.

In this example, for the simultaneous game the A.I. finds the absence of
pure strategies' equilibrium but does find the mixed strategies Nash
equilibrium.

It also stores the scenarios in an Excel file with the respective probabilities
extracted from the mixed strategies equilibrium.

@author: Carlos Pedro Gonçalves
@institution: Lusophone University Lisbon, University Center
@school: School of Economic Sciences and Organizations
@department: Department of Management on Civil Aviation and Airports



"""

import twoplayer as tp

PD = tp.read_file("MAD.xlsx")

tp.analyze_matrix(PD)