class direction_handling:
    def __init__(self, current_room, data, verb_handler_instance):
        self.current_room = current_room
        self.data = data
        self.verb_handler = verb_handler_instance

    def move(self, direction):
        direction = direction.lower()
        if direction == 'look':
            for room in self.data['rooms']:
                if room['name'] == self.current_room:
                    print(room['first_text'].format(zombie_count=room['zombies']))
            return
        if direction in self.data['possible_directions']:
            target_direction = self.data['possible_directions'][direction]
            next_room = self.get_next_room(target_direction)
            if next_room:
                if self.allowed_to_change_rooms(next_room):
                    self.current_room = next_room
                    for room in self.data['rooms']:
                        if room['name'] == self.current_room:
                            if room['times_entered'] == 0:
                                print(room['first_text'].format(zombie_count=room['zombies']))
                            else:
                                print(room['after_text'])
                            room['times_entered'] += 1
            else:
                print(f"You cannot go {target_direction} from the {self.current_room}.")

    def get_next_room(self, direction):
        return self.data['room_connections'].get(self.current_room, {}).get(direction)

    def get_all_next_rooms(self, room):
        try:
            return self.data['room_connections'].get(room)
        except KeyError:
            #--debug print(f"{room} in getAllNextRooms")
            print("Key 'room_connections' not found in the data.")

    def allowed_to_change_rooms(self, next_room):
        # if currentRoom has zombies, but you've already been to the room you're trying to change to, then it'll allow you to.
        # but if you haven't been to the nextRoom before, then it doesn't matter if it has zombies or not; you need to clear currentRoom of zombies before going there.
        for room in self.data['rooms']:
            if (self.current_room == room['name'] and room['zombies']!=0):
                for room2 in self.data['rooms']:
                    if next_room == room2['name'] and room2['times_entered']==0:
                        print(f"Uh oh, there's {room['zombies']} zombie(s) in the way blocking your path. Clear the room of zombies first.")
                        return False
        if next_room not in ('living room', 'hallway', 'basement', 'outside'): #these are the only rooms which are locked
            return True
        inventory = self.verb_handler.inventory
        if next_room== self.data['rooms'][1]['name']: #hallway
            if self.data['items'][1]['name'] in inventory and self.data['items'][0]['used_status'] == True:
                return True  #if axe in inventory, and batteries have been used, then allowed to go to hallway
            else:
                print(self.data['rooms'][0]['not_allowed'])
                return False
        if next_room==self.data['rooms'][5]['name']: #living room
            if self.data['items'][7]['used_status'] == True:
                return True  #if doorkey in inventory
            else:
                print(self.data['rooms'][4]['not_allowed'])
                return False
        if next_room==self.data['rooms'][9]['name']: #basement
            if self.data['items'][10]['used_status'] == False: #if diary hasn't been used. doesnt matter if user has flashlight or not,
                print(self.data['rooms'][5]['down_without_diary']) #the passage is still locked to the basement if diary hasnt been used.
                return False
            else:
                if self.data['items'][4]['name'] not in inventory: #if diary has been used, but no flashlight
                    print(self.data['rooms'][5]['no_flashlight'])
                    return False
            return True  #if both above pass, that means diary.used == True and flashlight is in inventory. ready to go to basement
        if next_room == self.data['rooms'][10]['name']:  # if trying to go north in foyer (which ends the game) without having used the latch
            if self.data['items'][8]['used_status'] == True:
                return True
            else:
                print(self.data['rooms'][8]['not_allowed'])
                return False