from loc import Locale;

class World: 
    def __init__(self):
        self.dungeons = [
            Locale("Steel Pitts Dungeon", "You have reached the Steel Pitts Dungeon. Enjoy!",
          "Steel Pitts Dungeon contains steampunk steel golems", {'West': 'The Coral Labyrinth Dungeon'}),
            Locale("The Coral Labyrinth Dungeon", "This area is a big green coral reef",
             "You see that within the reef there are many poisonous fish in the reef",
             {'East': 'Steel Pitts Dungeon', 'South': 'The matrix Dungeon'}),
            Locale("The matrix Dungeon", "This area is a digitalized city",
            "you see that there are many red and blue pills on the ground of the matix dungeon", {'North': 'The Coral Labyrinth Dungeon'})
        ]

        self.navigation = [
        ["West"],
        ["East", "South"],
        ["North"]
        ]

    def getNavigation(self):
        return self.navigation
    
    def getdungeons(self):
        return self.dungeons

