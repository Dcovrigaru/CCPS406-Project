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

        direction = direction.lower()

        if direction == 'current' or direction =='c':
            print(f'You are currently in the {self.currentRoom}.')
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



##this below function is called on line 27. it prints the JSON messages for entering rooms.
def RoomMessages(currentRoom):
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'GameData.JSON')
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

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
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=2)

            return



#this is called at the beginning of the game once just to reset the times_entered,
# since the above func writes to the json to increment them
def ResetNewGame():
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'GameData.JSON')

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    print("\n\t ***WELCOME TO DEATH ESCAPE***\n\t",data.get('story', {}).get('intro', ''))   #print intro
    print(data.get('rooms', [])[0].get('first_text', '')) #print attic message

    # Reset times_entered for each room
    for room in data.get('rooms', []):
        if room['name'] == 'attic':
            room['times_entered'] = 1#player begins in attic, so attic times_entered starts at 1 unlike the rest of the rooms
        else:
            room['times_entered'] = 0

    # Write the modified data back to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)





