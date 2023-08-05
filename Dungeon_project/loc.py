class Locale:
    def __init__(self, name, summary, details, direction):
        self.name = name
        self.summary = summary
        self.details = details
        self.visited = False
        self.direction = direction
    def getdirection(self):
        return self.direction
    def setdirection(self, direction):
        self.direction = direction
    def getName(self):
        return self.name
    def getDetails(self):
        return self.details
    def getVisited(self):
        return self.visited
    def setName(self, n):
        self.name = n
    def setDetails(self, d):
        self.details = d
    def setVisited(self, vis):
        self.visited = vis
    def __str__(self):
        if (self.visited == False):
            result = self.summary
        else:
            result = "You are at " + self.name + "."
        return result
