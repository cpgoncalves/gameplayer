# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:19:32 2025

Application of two-player game analyzer to the Ultimatum game.

The analysis finds performs the analysis for the simultaneous and sequential
games.

@author: Carlos Pedro Gonçalves
@institution: Lusophone University Lisbon, University Center
@school: School of Economic Sciences and Organizations
@department: Department of Management on Civil Aviation and Airports



"""

import twoplayer as tp

X = tp.read_file("Ultimatum.xlsx")


tp.analyze_matrix(X)
