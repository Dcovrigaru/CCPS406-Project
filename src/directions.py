class DirectionHandling:
    def __init__(self, currentRoom, data, verb_handler_instance):
        self.currentRoom = currentRoom
        self.data = data
        self.verb_handler = verb_handler_instance

    def move(self, direction):
        direction = direction.lower()
        if direction == 'look':
            for room in self.data['rooms']:
                if room['name'] == self.currentRoom:
                    print(room['first_text'].format(zombiecount=room['zombies']))
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
                                print(room['first_text'].format(zombiecount=room['zombies']))
                            else:
                                print(room['after_text'])
                            room['times_entered'] += 1
            else:
                print(f"You cannot go {targetDirection} from the {self.currentRoom}.")

    def getNextRoom(self, direction):
        return self.data['roomConnections'].get(self.currentRoom, {}).get(direction)

    def getAllNextRooms(self, room):
        try:
            return self.data['roomConnections'].get(room)
        except KeyError:
            #--debug print(f"{room} in getAllNextRooms")
            print("Key 'roomConnections' not found in the data.")

    def AllowedToChangeRooms(self, nextRoom):
        # if currentRoom has zombies, but you've already been to the room you're trying to change to, then it'll allow you to.
        # but if you haven't been to the nextRoom before, then it doesn't matter if it has zombies or not; you need to clear currentRoom of zombies before going there.
        for room in self.data['rooms']:
            if (self.currentRoom == room['name'] and room['zombies']!=0):
                for room2 in self.data['rooms']:
                    if nextRoom == room2['name'] and room2['times_entered']==0:
                        print(f"Uh oh, there's {room['zombies']} zombie(s) in the way blocking your path. Clear the room of zombies first.")
                        return False
        if nextRoom not in ('living room','hallway','basement', 'outside'): #these are the only rooms which are locked
            return True
        inventory = self.verb_handler.inventory
        if nextRoom== self.data['rooms'][1]['name']: #hallway
            if self.data['items'][1]['name'] in inventory and self.data['items'][0]['used_status'] == True:
                return True  #if axe in inventory, and batteries have been used, then allowed to go to hallway
            else:
                print(self.data['rooms'][0]['notallowed'])
                return False
        if nextRoom==self.data['rooms'][5]['name']: #living room
            if self.data['items'][7]['used_status'] == True:
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
        if nextRoom==self.data['rooms'][10]['name']:  #if trying to go north in foyer (which ends the game) without having used the latch
            if self.data['items'][8]['used_status'] == True:
                return True
            else:
                print(self.data['rooms'][8]['notallowed'])
                return False