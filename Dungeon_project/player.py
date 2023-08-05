from world import World

class Player:
    def __init__(self, name):
        self.name = name
        self.world = World()
        self.currentLocale = self.world.getdungeons()[0]
        self.moveCount = 0
        self.score = 0

    def getname(self):
        return self.name
    def getmovecount(self):
        return self.moveCount
    def getscore(self):
        return self.score
    def setMovecount(self, count):
        self.moveCount += count

    def move(self, roomnum, newdirection):
        #if self.world.getdungeons()[roomnum].getName() == self.currentLocale.getName():
        if newdirection in self.world.getNavigation()[roomnum]:
            newroom = self.world.getdungeons()[roomnum].getdirection()[newdirection]
            self.moveCount += 1

            for i in range(len(self.world.getdungeons())):
                if self.world.getdungeons()[i].getName() == newroom:
                    roomnum = i

            if self.world.getdungeons()[roomnum].getVisited() == False:
                self.score += 1
                self.world.getdungeons()[roomnum].setVisited(True)

            return (newroom, roomnum)
        else:
            return None
