from verbs import *
from player import *
compass = ["n","e","w","s","u","d","up","east","west","down","north","south","current","c"]


class DirectionHandling:
    def __init__(self, currentRoom, data, verb_handler_instance):
        self.currentRoom = currentRoom
        self.data = data
        self.verb_handler = verb_handler_instance


    def move(self, direction):
        possibleDirections = {
            's': 'south','n': 'north','w': 'west','e': 'east','u': 'up','d': 'down','south': 'south','north': 'north',
            'west': 'west','east': 'east','up': 'up','down': 'down'
        }

        direction = direction.lower()

        if direction == 'current' or direction =='c':
            for room in self.data['rooms']:
                if room['name'] == self.currentRoom:
                    print(room['currentText'])
            return


        if direction in possibleDirections:
            targetDirection = possibleDirections[direction]
            nextRoom = self.getNextRoom(targetDirection)

            if nextRoom:
                if self.AllowedToChangeRooms(nextRoom):
                    self.currentRoom = nextRoom
                    for room in self.data['rooms']:
                        if room['name'] == self.currentRoom:
                            if room['times_entered'] == 0:
                                room['times_entered'] += 1
                                print(room['first_text'])
                            else:
                                room['times_entered'] += 1
                                print(room['after_text'])


            else:
                print(f"You cannot go {targetDirection} from the {self.currentRoom}.")

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


    def AllowedToChangeRooms(self, nextRoom):
        inventory = self.verb_handler.inventory
        for room in self.data['rooms']:
            if room['name']=='attic' and nextRoom=='hallway':
                if 'axe' in inventory and room['usedBatteries']==True:
                    return True
                else:
                     print(room['tryingdownwithoutpoweroraxe'])
                     return False
            if room['name']=='office' and nextRoom == 'living room':
                if 'doorkey' in inventory:
                    return True
                else:
                    print(room['downwithlockeddoor'])
                    return False
            if room['name']=='living room' and nextRoom == 'basement':
                if 'flashlight' in inventory:
                    return True
                else:
                    print(room['unlockedbasementbutnoflashlight'])
                    return False

        return True














