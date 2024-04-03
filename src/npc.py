import json
import random
from directions import DirectionHandling


class NPC:
    def __init__(self, data, currentRoom, verb_handler_instance):
        self.states = ["IDLE", "MOVE", "ATTACK", "LOOT"]
        self.currentState = random.choices(self.states, [0.4, 0.4, 0.15, 0.05])[0]
        self.inventory = []
        self.data = data
        self.currentRoom = 'bedroom'  # NPC spawns in the bedroom
        self.directionHandler = DirectionHandling(currentRoom, data, verb_handler_instance)
        self.available_enemies = False
        self.available_items = False

    def NPC_available_items_enemies(self, current_room):
        # Get the data for the current room
        room_data = next(room for room in self.data['rooms'] if room['name'] == current_room)

        # Check if there are any zombies in the room
        if room_data.get('zombies', 0) > 0:
            self.available_enemies = True
        else:
            self.available_enemies = False

        # Check if the items dictionary is not empty and does not contain empty strings
        items = room_data.get('items', [])
        if items and all(item for item in items):
            self.available_items = True
        else:
            self.available_items = False

        return self.available_enemies, self.available_items

    def NPC_change_state(self):
        probabilities = [0.4, 0.4, 0.15, 0.05]
        possible_states = self.states.copy()

        if not self.available_items:
            possible_states.remove("LOOT")
            probabilities.pop(3)
        if not self.available_enemies:
            possible_states.remove("ATTACK")
            probabilities.pop(2)

        self.currentState = random.choices(possible_states, probabilities)[0]

    def NPC_act(self):
        if self.currentState == "IDLE":
            print("NPC is idling...\n")
        elif self.currentState == "MOVE":
            return self.NPC_move()
        elif self.currentState == "LOOT":
            return self.NPC_loot()
        elif self.currentState == "ATTACK":
            return self.NPC_attack(self.data)

    def NPC_move(self):
        while True:
            # Store previous room
            oldRoom = self.currentRoom

            # Get all possible next rooms
            nextRooms = self.directionHandler.getAllNextRooms(self.currentRoom)
            rooms = list(nextRooms.values())
            rooms[0] = rooms[0].capitalize()
            # print(", ".join(rooms) + " are the next rooms")

            # If there are no connected rooms, raise an error
            if not nextRooms:
                raise ValueError(f"The NPC is in {self.currentRoom}, which has no connected rooms.")

            # Choose a random direction
            direction = random.choice(list(nextRooms.keys()))

            # List of possible messages
            messages = [
                "Nice play!",
                "Okay, I see what you did there...",
                "My turn!",
                "GG!",
                "Lookout!",
                "Heads up!",
                "Brace yourself!",
                "Here we go!",
                "On the move!",
                "Advancing forward!"
            ]

            # Move the NPC to the new room
            self.currentRoom = nextRooms[direction]

            # Select a random message from the list
            message = random.choice(messages)

            print(f"{message} NPC moved from {oldRoom} to {self.currentRoom}.\n")

            # If the current room is 'outside', move back to the previous room
            if self.currentRoom == 'outside':
                print(f"NPC is outside, moving back to {oldRoom}.\n")
                self.currentRoom = oldRoom
            else:
                break

    def NPC_loot(self):
        # Load the game data from the JSON file
        with open('../data/GameData.json') as f:
            data = json.load(f)

        # Get the current room of the NPC
        current_room_name = self.currentRoom

        # Find the current room in the data
        current_room = next((room for room in data['rooms'] if room['name'] == current_room_name), None)

        if current_room:
            items = current_room.get('items', [])
            if items and items[0] != "":
                for item_name in items:
                    if item_name in self.inventory:
                        print(f"You already have the {item_name} in your inventory.")
                        continue
                    self.inventory.append(item_name)
                    print(f"The NPC has looted {item_name}.")
            else:
                print("There are no items in this room to loot.")
        else:
            print("The current room does not exist in the game data.")

    def NPC_attack(self, data):
        # check if current state is ATTACK
        if self.currentState == 'ATTACK':
            # check if 'room' dictionary contains 'zombie' key-value pair >=1
            zombies_present = False
            for room in self.data['rooms']:
                if room['name'] == self.currentRoom:
                    if room['zombies'] > 0:
                        zombies_present = True  # Sets true if zombies are found in the room
                        break
            if zombies_present:  # Checks if there are any zombies to attack
                for room in self.data['rooms']:
                    if room['name'] == self.currentRoom:
                        room['zombies'] -= 1
                        print(f"NPC just attacked and killed a zombie! There are {room['zombies']} zombie(s) left in {self.currentRoom}.\n")
                        break
            return


