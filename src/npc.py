import random
from verbs import VerbHandler
from directions import DirectionHandling
class NPC:
    def __init__(self, data, currentRoom, items, verb_handler_instance):
        self.states = ["IDLE", "MOVE", "ATTACK", "LOOT"]
        self.current_state = random.choices(self.states, [0.4, 0.4, 0.15, 0.05])[0]
        self.inventory = []
        self.currentRoom = 'bedroom'  # NPC spawns in the bedroom
        self.directionHandler = DirectionHandling(currentRoom, data, verb_handler_instance)
        self.verbHandler = VerbHandler(items, currentRoom, data)  # Instantiate VerbHandler with appropriate parameters

    def NPC_change_state(self, available_items, available_enemies):
        probabilities = [0.4, 0.4, 0.15, 0.05]
        possible_states = self.states.copy()

        if not available_items:
            possible_states.remove("LOOT")
            probabilities.pop(3)
        if not available_enemies:
            possible_states.remove("ATTACK")
            probabilities.pop(2)

        self.current_state = random.choices(possible_states, probabilities)[0]

    def NPC_act(self):
        if self.current_state == "IDLE":
            return "NPC is idling."
        elif self.current_state == "MOVE":
            return self.NPC_move()
        elif self.current_state == "LOOT":
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

    def NPC_loot(self, item_name):
        # Ability to pick up any item in game
        # Ability to pick up only items it sees
        room = next((room for room in self.data['rooms'] if room['name'] == self.current_room.currentRoom), None)
        if room and item_name in room.get('items', []) or any(
                subroom.get('items', []) for subroom in room.get('subrooms', [])):
            # Call the handle_take function from VerbHandler
            self.verbHandler.handle_take(item_name)
            self.inventory.append(item_name)
            return f"The NPC has looted {item_name}."
        else:
            return f"I don't see a {item_name} here to loot."

