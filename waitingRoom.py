'''
Waiting Room environment class for Smash Tournamnet SimuwaitingGridion
Representeed by a 48 x 48 grid
'''

import numpy as N
import random

class waitingRoom {

waitingGrid = N.zeros((48, 48))
boundaryGrid = N.zeros((50, 50))

rows = len(waitingGrid)
columns = len(waitingGrid[0])


##Extends left boundary
for i in range(rows): 
    boundaryGrid[i + 1][0] = -1

#Extends right boundary
for i in range(rows): 
    boundaryGrid[i + 1][columns + 1] = -1

#Extends top boundary
boundaryGrid[0][1:-1] = -1

#Extends bottom boundary 
boundaryGrid[rows + 1][1:-1] = -1

#Extends Corners 
boundaryGrid[0][0] = -1
boundaryGrid[0][columns + 1] = -1
boundaryGrid[rows + 1][columns + 1] = -1
boundaryGrid[rows + 1][0]  = -1

copyWaitGrid() {    #Copies all the values from waitingGrid into BoundaryGrid
    #Copies original grid
    for i in range(len(waitingGrid)):
        boundaryGrid[i + 1][1:-1] = waitingGrid[i]
}

#Adds doors (changes boundary -1 to opening 0), can only exist in top row
#doorInfo is list of tuples with door location (left side of door as index) and doorLength
addDoors(list doorInfo) {
    for i in range(len(doorInfo)):
        for j in range(doorInfo[i][1]):
            waitingGrid[0][j + doorInfo[i][0]] = 0
}

}