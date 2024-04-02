import json
import random
#from verbs import VerbHandler
from directions import DirectionHandling
class NPC:
    def __init__(self, data, currentRoom, items, verb_handler_instance):
        self.states = ["IDLE", "MOVE", "ATTACK", "LOOT"]
        #self.current_state = random.choices(self.states, [0.4, 0.4, 0.15, 0.05])[0]
        self.currentState = "LOOT" # LOOT TEST CASE
        self.inventory = []
        self.data = data
        self.currentRoom = 'attic'  # NPC spawns in the bedroom
        #self.currentRoom = 'hallway'  # LOOT TEST CASE
        self.directionHandler = DirectionHandling(currentRoom, data, verb_handler_instance)
        #self.verbHandler = VerbHandler(items, currentRoom, data)  # Instantiate VerbHandler with appropriate parameters

    def NPC_change_state(self, available_items, available_enemies):
        probabilities = [0.4, 0.4, 0.15, 0.05]
        possible_states = self.states.copy()

        if not available_items:
            possible_states.remove("LOOT")
            probabilities.pop(3)
        if not available_enemies:
            possible_states.remove("ATTACK")
            probabilities.pop(2)

        self.currentState = random.choices(possible_states, probabilities)[0]

    def NPC_act(self):
        if self.currentState == "IDLE":
            return "NPC is idling."
        elif self.currentState == "MOVE":
            return self.NPC_move()
        elif self.currentState == "LOOT":
            return self.NPC_loot(self.currentRoom)
    def NPC_move(self):
        # Store previous room
        oldRoom = self.currentRoom

        # Get all possible next rooms
        nextRooms = self.directionHandler.getAllNextRooms(self.currentRoom)
        print(f"{nextRooms} is the next room")

        # If there are no connected rooms, raise an error
        if not nextRooms:
            raise ValueError(f"The NPC is in {self.currentRoom}, which has no connected rooms.")

        # Choose a random direction
        direction = random.choice(list(nextRooms.keys()))

        # Move the NPC to the new room
        self.currentRoom = nextRooms[direction]
        print(f"Lookout! NPC moved from {oldRoom} to {self.currentRoom}\n")

    def NPC_loot(self, room):
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
