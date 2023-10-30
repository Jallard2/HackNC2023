import pygame
from crop import Crop, DoneCrops
#creates the farmland with space
class FarmLand():
    #initialize the users land with rows and columns of soil
    def __init__(self, numRows=3, numCols=6):
        self.numRows = numRows
        self.numCols = numCols
        # self.land = [[None]*numCols]*numRows
        self.land = []
        for _ in range(self.numRows):
            self.land.append(self.numCols * [None])


    #when the user purchases more land
    def addLand(self):
        self.numRows += 1
        newList = self.numCols * [None]
        self.land.append(newList)


    #if the user has their land trampled by zombies (maybe we don't want this?)
    def removeLand(self, numTrampled):
        self.numRows = self.numRows - numTrampled

        # Initial checks
        if (self.numRows) <= 0:
            return False
        for _ in range(numTrampled):
            self.land.pop(self.numRows)
        return True

        # Remove last list from farmland
        # Using list.pop(index)
