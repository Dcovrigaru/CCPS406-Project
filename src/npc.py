import random
from src import verbs
from verbs import VerbHandler
from directions import DirectionHandling
class NPC:
    def __init__(self, data, currentRoom):
        self.states = ["IDLE", "MOVE", "ATTACK", "LOOT"]
        self.current_state = random.choices(self.states, [0.4, 0.4, 0.15, 0.05])[0]
        self.inventory = []
        self.currentRoom = 'bedroom'  # NPC spawns in the bedroom
        self.directionHandler = DirectionHandling(data, currentRoom)
        self.VerbHandler = VerbHandler(data, currentRoom)  # Instantiate VerbHandler with appropriate parameters

    def change_state(self, available_items, available_enemies):
        probabilities = [0.4, 0.4, 0.15, 0.05]
        possible_states = self.states.copy()

        if not available_items:
            possible_states.remove("LOOT")
            probabilities.pop(3)
        if not available_enemies:
            possible_states.remove("ATTACK")
            probabilities.pop(2)

        self.current_state = random.choices(possible_states, probabilities)[0]


    def act(self, room):
        if self.current_state == "IDLE":
            return "NPC is idling."
        elif self.current_state == "MOVE":
            return self.move(room)
        elif self.current_state == "ATTACK":
            return self.attack(room)
        elif self.current_state == "LOOT":
            return self.loot(room)

    def move(self, direction):
        # Check if the move is legal
        if direction in self.directionHandler.data['rooms'][self.currentRoom]['exits']:
            self.directionHandler.move(direction)
        else:
            print(f"The NPC cannot move {direction} from the {self.currentRoom}.")
        # Implement movement logic here
        # NPC spawns in bedroom
        pass

    class Combat:
        def __init__(self, data):
            self.data = data

        def npc_attack(self, damage_min, damage_max, current_room):
            # Calculate damage dealt by NPC
            damage = random.randint(damage_min, damage_max)

            # Reduce zombie health
            for room in self.data['rooms']:
                if room['name'] == current_room['name']:
                    room['zombie_health'] -= damage
                    # If zombie's health drops to or below 0, remove the zombie from the room
                    if room['zombie_health'] <= 0:
                        room['zombies'] -= 1
                        room['zombie_health'] = 100  # Reset zombie's health
                        return f"NPC attacks the zombie for {damage} damage. The zombie has been defeated."
                    else:
                        return f"NPC attacks the zombie for {damage} damage. The zombie's health is now {room['zombie_health']}."
            return "No zombie found in the current room."

    def loot(self, item_name):
        # Ability to pick up any item in game
        # Ability to pick up only items it sees
        def loot(self, item_name):
            room = next((room for room in self.data['rooms'] if room['name'] == self.current_room.currentRoom), None)
            if room and item_name in room.get('items', []) or any(
                    subroom.get('items', []) for subroom in room.get('subrooms', [])):
                # Call the handle_take function from VerbHandler
                self.VerbHandler.handle_take(item_name)
                self.inventory.append(item_name)
                return f"The NPC has looted {item_name}."
            else:
                return f"I don't see a {item_name} here to loot."
