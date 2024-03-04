
compass = ["n","e","w","s","u","d","up","east","west","down","north","south","current","c"]
class DirectionHandling:
    def __init__(self, currentRoom, data):
        self.currentRoom = currentRoom
        self.data = data

    def move(self, direction):
        possibleDirections = {
            's': 'south','n': 'north','w': 'west','e': 'east','u': 'up','d': 'down','south': 'south','north': 'north',
            'west': 'west','east': 'east','up': 'up','down': 'down'
        }

        direction = direction.lower()

        if direction == 'current' or direction =='c':
            print(f'You are currently in the {self.currentRoom}.')
            return


        if direction in possibleDirections:
            targetDirection = possibleDirections[direction]
            nextRoom = self.getNextRoom(targetDirection)

            if nextRoom:
                self.currentRoom = nextRoom
                for room in self.data['rooms']:
                    if room['name'] == self.currentRoom:
                        if room['times_entered'] == 0:
                            room['times_entered'] += 1
                            print(room['first_text'])
                        else:
                            print(room['after_text'])


            else:
                print(f'You cannot go {targetDirection} from the {self.currentRoom}.')
        else:
            print('Invalid command.')

    def getNextRoom(self, direction):
        roomConnections = {
            'bathroom': {'south': 'bedroom'},
            'bedroom': {'north': 'bathroom', 'east': 'hallway'},
            'hallway': {'west': 'bedroom', 'east': 'office', 'up': 'attic'},
            'office': {'west': 'hallway', 'down': 'living room'},
            'living room': {'up': 'office', 'down': 'basement', 'west': 'foyer'},
            'foyer': {'east': 'living room', 'west': 'kitchen'},
            'kitchen': {'south': 'garage', 'east': 'foyer'},
            'garage': {'north': 'kitchen'},
            'basement': {'up': 'living room'},
            'attic': {'down': 'hallway'}
        }

        return roomConnections.get(self.currentRoom, {}).get(direction)



