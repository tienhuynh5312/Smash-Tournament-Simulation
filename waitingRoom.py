'''
Environment class for Smash Tournament Simulation
Representeed by a 73 x 48 grid
'''

import numpy as N
import random

class Environment:

    def __init__(self):

        #Game room is 24 x 48, waiting room is 48 x 48, + 1 for wall in the middle. 24 + 48 + 1 = 73
        self.environmentGrid = N.zeros((73, 48))
        self.boundaryGrid = N.zeros((75, 50))

        self.rows = len(self.environmentGrid)
        self.columns = len(self.environmentGrid[0])


    def init_boundary(self):
        ##Extends left boundary
        for i in range(rows): 
            self.boundaryGrid[i + 1][0] = -1

        #Extends right boundary
        for i in range(rows): 
            self.boundaryGrid[i + 1][columns + 1] = -1

        #Extends top boundary
        self.boundaryGrid[0][1:-1] = -1

        #Extends bottom boundary 
        self.boundaryGrid[rows + 1][1:-1] = -1

        #Extends Corners 
        self.boundaryGrid[0][0] = -1
        self.boundaryGrid[0][columns + 1] = -1
        self.boundaryGrid[rows + 1][columns + 1] = -1
        self.boundaryGrid[rows + 1][0]  = -1


    def copyWaitGrid():    #Copies all the values from environmentGrid into BoundaryGrid
        #Copies original grid
        for i in range(len(self.environmentGrid)):
            boundaryGrid[i + 1][1:-1] = self.environmentGrid[i]


    #Adds doors (changes boundary -1 to opening 0), can only exist in top row
    #doorInfo is list of tuples with door location (left side of door as index) and doorLength
    def addDoors(list doorInfo):
        for i in range(len(doorInfo)):
            for j in range(doorInfo[i][1]):
                self.environmentGrid[0][j + doorInfo[i][0]] = 0


    def addBooth(int coord):



