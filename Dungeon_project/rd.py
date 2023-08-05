rooms = {

        'Start Area': {'name': 'Start Area', 'move south': 'West Yard', 'move east': 'Main Courtyard', 'item': 'rock'},
        'West Yard': {'name': 'West Yard', 'move north': 'Start Area', 'item': 'necklace'},
        'Main Courtyard': {'name': 'Main Courtyard', 'move north': 'North Yard', 'move east': 'East Yard',
                           'move south': 'South Yard', 'move west': 'Start Area', 'item': 'ring'},
        'South Yard': {'name': 'South Yard', 'move north': 'Main Courtyard', 'move east': 'Maintenance Shed',
                       'item': 'pendant'},
        'Maintenance Shed': {'name': 'Maintenance Shed', 'move west': 'South Yard', 'item': 'old key'},
        'East Yard': {'name': 'East Yard', 'move west': 'Main Courtyard', 'move north': 'Main Gate',
                      'item': 'picture frame'},
        'Main Gate': {'name': 'Main Gate', 'move south': 'East Yard', 'item': 'main gate'},
        'North Yard': {'name': 'North Yard', 'move east': 'Catacombs: Entrance', 'move south': 'Main Courtyard',
                       'item': 'gate'},
        'Catacombs: Entrance': {'name': 'Catacombs: Entrance', 'move east': 'Catacombs: North Wing',
                                'move west': 'North Yard', 'item': 'bracelet'},
        'Catacombs: North Wing': {'name': 'Catacombs: North Wing', 'move west': 'Catacombs: Entrance',
                                  'move south': 'Catacombs: Main Tunnel', 'item': 'vase'},
        'Catacombs: Main Tunnel': {'name': 'Catacombs: Main Tunnel', 'move north': 'Catacombs: North Wing',
                                   'move south': 'Catacombs: South Wing', 'item': 'rusty key'},
        'Catacombs: South Wing': {'name': 'Catacombs: South Wing', 'move north': 'Catacombs: Main Tunnel',
                                  'item': 'bolt cutters'}
    }

player_room = rooms['Start Area']

directions = ['move north', 'move south', 'move east', 'move west']

how2 = ('For movement type: move north, south, east, or west\nFor actions type: collect (item)'
)

player_inv = []

prol = ('text')

ending = ('text'
          'You collected: ', player_inv)

fail = ('text')

print('Welcome to Graverobber')

print('For directions type: ?')

print('For prologue, type: prologue')

print('You enter the graveyard.')

while True:

    print('You are in the {}.'.format(player_room['name']))

    print('Your current inventory: {}\n'.format(player_inv))

    user_input = input('What would you like to do? ')
    if user_input == 'prologue':
        print(prol)
    elif user_input == '?':
        print(how2)
    elif user_input in directions:
        if user_input in player_room:
            player_room = rooms[player_room[user_input]]
            if player_room == rooms['Main Gate']:
                if 'bolt cutters' in player_inv:
                    print(ending)
                    break
                else:
                    print(fail)
                    break
            if player_room['item']:
                print('You see a {}'.format(''.join(player_room['item'])))
        else:
            print('You cannot move in that direction')
    elif user_input == 'exit':
        break
    elif user_input == ('collect ' + rooms[player_room]['item']):
        if rooms[player_room]['item'] and player_inv:
            print('You already have this item in your inventory!')
        else:
            player_inv.append(rooms[player_room][user_input])
    else:
        print('Invalid command')