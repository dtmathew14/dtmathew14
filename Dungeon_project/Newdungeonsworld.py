from loc import *
from player import *
from world import *

dungeons = [ {'name': 'Steel Pitts Dungeon', 'summary': 'this area contains steampunk steel golems',
'details': 'You see that within the steel dungeon that the golems can only move forwards and backwards', "item": "stone dagger", "was_visited": False, 'direction' : {'West': 'The Coral Labyrinth Dungeon'}},
        {'name': 'The Coral Labyrinth Dungeon', 'summary': 'This area is a big green coral reef',
'details': 'You see that within the reef there are many poisonous fish in the reef',"item": "vial of poison", 'was_visited': False, 'direction' : {'East': 'Steel Pitts Dungeon', 'South': 'The matrix Dungeon'}},
            {'name': 'The matrix Dungeon', 'summary': 'This area is a digitalized city', 
'details': 'you see that there are many red and blue pills on the ground of the matix dungeon',"item": "Black pill", 'was_visited': False, 'direction': {'North': 'The Coral Labyrinth Dungeon'}} ]

currentroom = [
    ["West"],
    ["East", "South"],
    ["North"]
    ]

inventory = []

room : str = 'Steel Pitts Dungeon'
direction : str = ''
roomnum = 0
playerObj = None

def main():
    intro()
    room_loop()
    
def intro():
    global playerObj

    print("DUNGEONS WORLD")
    playerObj = Player(input("Enter a name:"))
    print(f"You will travel through dungeons world as {playerObj.getname()}. You will be able to move to several different locations with descriptions. If you get stuck, type [help] for a list of commands.")

def getroom():
    print(f"you are in {room}")

def room_loop():
    global room
    global roomnum
    global playerObj

    while room != 'Quit':
        getroom()
        direction = input(str('Enter your move:\n')).title()
        if direction == 'Quit':
            break 
        
        elif direction == "Help": 
            print("Valid commands are North, South, East, West, Quit, Help, Examine")

        elif direction == "Examine":
            examine = input("do you want to examine the room, yes or no ").title()
            if examine == "Yes": 
                print(dungeons[roomnum]['details'])
                print(dungeons[roomnum]['summary'])
            elif print(dungeons[roomnum][3]):
                print("You win")


            else: 
                print("Back to room")
        else:
            m = playerObj.move(roomnum, direction)
            if m == None:
                print("That is not a valid move, try again.")
                playerObj.setMovecount(-1)
            else:
                room = m[0]
                roomnum = m[1]

    print("your score is", str(playerObj.getscore()))

    print(f"Thank you for playing {playerObj.getname()}, © 2022 by Daniel Mathew.")

main()
