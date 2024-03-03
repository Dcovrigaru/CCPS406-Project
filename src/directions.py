import json
import os


class DirectionHandling:

    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    def move(self, direction):
        possibleDirections = {
            's': 'south','n': 'north','w': 'west','e': 'east','u': 'up','d': 'down','south': 'south','north': 'north',
            'west': 'west','east': 'east','up': 'up','down': 'down'
        }
        hasSpecialCurrentMessage = ['attic', 'kitchen', 'garage', 'basement']
        direction = direction.lower()

        if direction == 'current' or direction =='c':
            FilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'GameData.JSON')
            with open(FilePath, 'r') as file:
                data = json.load(file)
            for room in data.get('rooms', []):
                if room['name'] == self.currentRoom:
                    if room['name'] in hasSpecialCurrentMessage:
                        print(room['currentText']) #prints current message if in special four rooms above
                    else:
                        print(room['after_text'])   #otherwise just prints the after_text for 'current' command
            return

        if direction in possibleDirections:
            targetDirection = possibleDirections[direction]
            nextRoom = self.getNextRoom(targetDirection)

            if nextRoom:
                self.currentRoom = nextRoom
                RoomMessages(self.currentRoom)
            else:
                print(f'You cannot go {targetDirection} from the {self.currentRoom}.')


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



##this below function is called on line 37. it prints the JSON messages for entering rooms.
def RoomMessages(currentRoom):
    FilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'GameData.JSON')
    with open(FilePath, 'r') as file:
        data = json.load(file)
    # search for the current room in the JSON data
    for room in data.get('rooms', []):
        if room['name'] == currentRoom:
            # Increment times_entered
            room['times_entered'] += 1

            if room['times_entered'] > 1:
                print(room['after_text'])
            else:
                print(room['first_text'])

            # increment times_entered and write to JSON file
            with open(FilePath, 'w') as file:
                json.dump(data, file, indent=2)

            return



#this is called at the beginning of the game once just to reset the times_entered,
# since the above func writes to the json to increment them
def ResetNewGame():
    FilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'GameData.JSON')

    with open(FilePath, 'r') as file:
        data = json.load(file)

    print("\n\t ***WELCOME TO DEATH ESCAPE***\n\t",data.get('story', {}).get('intro', ''))   #print intro
    print(data.get('rooms', [])[0].get('first_text', '')) #print attic message

    # Reset times_entered for each room
    for room in data.get('rooms', []):
        if room['name'] == 'attic':
            room['times_entered'] = 1#player begins in attic, so attic times_entered starts at 1 unlike the rest of the rooms
        else:
            room['times_entered'] = 0

    # rewrite times_entered default values back to JSON file
    with open(FilePath, 'w') as file:
        json.dump(data, file, indent=2)





