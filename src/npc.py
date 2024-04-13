import random
from directions import direction_handling


class NPC:
    global name
    name = "Victor's Ghost"

    def __init__(self, data, current_room, verb_handler_instance):
        self.states = ["IDLE", "MOVE", "ATTACK", "LOOT"]
        self.current_state = random.choices(self.states, [0.4, 0.5, 0.08, 0.02])[0]
        self.inventory = []
        self.data = data
        self.current_room = current_room
        self.direction_handler = direction_handling(current_room, data, verb_handler_instance)
        self.available_enemies = False
        self.available_items = False

    def NPC_available_items_enemies(self, current_room):
        room_data = next(room for room in self.data['rooms'] if room['name'] == current_room)

        if room_data.get('zombies', 0) > 0:
            self.available_enemies = True
        else:
            self.available_enemies = False

        items = room_data.get('items', [])
        if items and all(item for item in items):
            self.available_items = True
        else:
            self.available_items = False

        return self.available_enemies, self.available_items

    def NPC_change_state(self):
        probabilities = [0.4, 0.5, 0.08, 0.02]
        possible_states = self.states.copy()

        if not self.available_items:
            possible_states.remove("LOOT")
            probabilities.pop(3)
        if not self.available_enemies:
            possible_states.remove("ATTACK")
            probabilities.pop(2)

        self.current_state = random.choices(possible_states, probabilities)[0]

    def NPC_act(self,verb_handler_instance):
        if self.current_state == "IDLE":
            print(f"\n{name} is just looking around...\n")
        elif self.current_state == "MOVE":
            return self.NPC_move()
        elif self.current_state == "LOOT":
            return self.NPC_loot(verb_handler_instance)
        elif self.current_state == "ATTACK":
            return self.NPC_attack(self.data)

    def NPC_move(self):
        while True:
            old_room = self.current_room
            next_rooms = self.direction_handler.get_all_next_rooms(self.current_room)
            rooms = list(next_rooms.values())
            rooms[0] = rooms[0].capitalize()

            if not next_rooms:
                raise ValueError(f"\n{name} is in {self.current_room}, which has no connected rooms.")

            possible_directions = [direction for direction, room in next_rooms.items() if room != 'outside']

            if not possible_directions:
                print(f"\n{name} is stuck in {self.current_room} as all paths lead outside.")
                break

            direction = random.choice(possible_directions)

            self.current_room = next_rooms[direction]

            message = random.choice(self.data["NPCmessages"])

            print(f"\n{message} {name} moved from {old_room} to {self.current_room}.\n")
            break

    def NPC_loot(self, verb_handler_instance):
        current_room_name = self.current_room
        current_room = next((room for room in self.data['rooms'] if room['name'] == current_room_name), None)

        if current_room:
            items = current_room.get('items', [])
            if items and items[0] != "":
                for item_name in items:
                    if item_name not in self.inventory:
                        if item_name == 'batteries':
                            print(f"\n{name} tried to loot batteries, but you already used them.")
                        if item_name == 'latch':
                            print(f"{name} tried to loot the latch, but the basement's strong zombies didn't allow him!")
                        elif item_name in verb_handler_instance.inventory:
                            print(f"\n{name} wanted to take the {item_name}, but you already got it first.")
                        else:
                            self.inventory.append(item_name)
                            verb_handler_instance.inventory.append(item_name)
                            print(f"\n{name} has looted {item_name}, and you also got it.")
            else:
                print("\nThere are no items in this room to loot.")
        else:
            print("\nThe current room does not exist in the game data.")

    def NPC_attack(self, data):
        if self.current_state == 'ATTACK':
            zombies_present = False
            for room in self.data['rooms']:
                if room['name'] == self.current_room:
                    if room['zombies'] > 0:
                        zombies_present = True
                        break
            if zombies_present:
                for room in self.data['rooms']:
                    if room['name'] == self.current_room:
                        room['zombies'] -= 1
                        print(f"\n{name} just attacked and killed a zombie! There are {room['zombies']} zombie(s) "
                              f"left in {self.current_room}.\n")
                        break
            return