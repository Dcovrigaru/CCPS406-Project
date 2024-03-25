
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
                                print(room['first_text'])
                            else:
                                print(room['after_text'])
                            room['times_entered'] += 1
            else:
                print(f"You cannot go {targetDirection} from the {self.currentRoom}.")

    def getNextRoom(self, direction):
        return self.data['roomConnections'].get(self.currentRoom, {}).get(direction)

    def AllowedToChangeRooms(self, nextRoom):
        if nextRoom not in ('living room','hallway','basement'):
            return True
        inventory = self.verb_handler.inventory
        if nextRoom== self.data['rooms'][1]['name']: #hallway
            if self.data['items'][1]['name'] in inventory and self.data['items'][0]['used_status'] == True:
                return True  #if axe in inventory, and batteries have been used, then allowed to go to hallway
            else:
                print(self.data['rooms'][0]['notallowed'])
                return False
        if nextRoom==self.data['rooms'][5]['name']: #living room
            if self.data['items'][7]['name'] in inventory or self.data['items'][7]['used_status'] == True:
                return True  #if doorkey in inventory
            else:
                print(self.data['rooms'][4]['notallowed'])
                return False
        if nextRoom==self.data['rooms'][9]['name']: #basement
            if self.data['items'][10]['used_status'] == False: #if diary hasn't been used. doesnt matter if user has flashlight or not,
                print(self.data['rooms'][5]['downwithoutdiary']) #the passage is still locked to the basement if diary hasnt been used.
                return False
            else:
                if self.data['items'][4]['name'] not in inventory: #if diary has been used, but no flashlight
                    print(self.data['rooms'][5]['unlockedbasementbutnoflashlight'])
                    return False
            return True  #if both above pass, that means diary.used == True and flashlight is in inventory. ready to go to basement