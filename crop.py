import random

class Crop:
    def __init__(self, growTime, buyPrice, sellPrice, dropChance, cropType, cropState, daysPlanted):
        self.growTime = growTime # grow time of the crop
        self.buyPrice = buyPrice # buy price of the crop
        self.sellPrice = sellPrice # sell price of the crop
        self.dropChance = dropChance # drop chance of seed when harvested
        self.cropType = cropType # type of crop, cash or food
        self.cropState = cropState # state of crop, seed or produce
        self.daysPlanted = daysPlanted # number of days planted


    # Changes the grow speed of the crop ( event related )
    def speedChange(self, multiplier):
        self.growTime *= multiplier

    # chance the crop returns a seed when harvested
    def shouldDropSeed(self) -> bool:
        return random.randrange(0, 100) <= self.dropChance

    # Changes the buy price of the crop ( event related )
    def buyChange(self, multiplier):
        self.buyPrice *= multiplier

    # Changes the sell price of the crop (event related )
    def sellChange( self, mulitplier):
        self.sellPrice *= mulitplier

    # Checks to see if the crop has been planted long enough to become a "produce"
    def checkState(self):
        if self.daysPlanted > 0:
            self.cropState = "growing"
        if self.daysPlanted == self.growTime:
            self.cropState = "produce"
        return self.cropState

    # Increments the days planted
    def incrementDay(self):
        self.daysPlanted += 1

    # Checks to see if the crop is ready to be harvested
    def isHarvestable(self):
        if self.cropState == "produce":
            return True
        else:
            return False

    # Cash Crops

class DoneCrops():
    def newBeet(self):
        return Crop(3, 2, 7, 25, "cash", "seed", 0 ) # Quick Grow time but worth less

    def newYam(self):
        return Crop(5, 4, 12, 25, "cash", "seed", 0) # Medium Grow time medium price

    def newPumpkin(self):
        return Crop(7, 7, 20, 25, "cash", "seed", 0) # Longer to grow but worth more

    def newCranberry(self):
        return Crop(1, 5, 6, 0, "cash", "seed", 0) # 1 day turn around, meant for a pinch but little gain

    # Food Crops

    def newParsnip(self):
        return Crop(4, 8, 10, 25, "food", "seed", 0) # quickest grow time for a food crop

    def newSweetPotato(self):
        return Crop(6, 6, 8, 50, "food", "seed", 0) # medium grow time for food but costs less

    def newWheat(self):
        return Crop( 8, 4, 6, 50, "food", "seed", 0) # long grow time for food but cheapest price

    def newCorn(self):
        return Crop( 14, 1, 6, 75, "food", "seed", 0) # longest grow time, one whole cycle but extremely cheap