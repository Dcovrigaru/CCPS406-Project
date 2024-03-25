
class DirectionHandling:
    def __init__(self, currentRoom, data, verb_handler_instance):
        self.currentRoom = currentRoom
        self.data = data
        self.verb_handler = verb_handler_instance

    def move(self, direction):
        direction = direction.lower()
        if direction == 'current' or direction =='c':
            for room in self.data['rooms']:
                if room['name'] == self.currentRoom:
                    print(room['currentText'])
            return
        if direction in self.data['possibleDirections']:
            targetDirection = self.data['possibleDirections'][direction]
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
        return self.data['roomConnections'].get(self.currentRoom, {}).get(direction)

    def AllowedToChangeRooms(self, nextRoom):
        if nextRoom not in ('living room','hallway','basement'):
            return True
        inventory = self.verb_handler.inventory
        if nextRoom=='hallway':
            if self.data['items'][1]['name'] in inventory:# and self.data['rooms'][0][list(self.data['rooms'][0].keys())[6]]==True:
                return True
            else:
                print(self.data['rooms'][0]['notallowed'])
                return False
        if nextRoom=='living room':
            if self.data['items'][7]['name'] in inventory:
                return True
            else:
                print(self.data['rooms'][4]['notallowed'])
                return False
        ##do for going down to basement from living room. text for basement is locked, then text for basement unlocked but no flashlight
        #if nextRoom == 'basement':