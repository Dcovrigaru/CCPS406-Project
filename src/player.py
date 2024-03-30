import random
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self.current_weapon = None

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} now has {self.health} health.")

    def healthStatus(self):
        return self.health > 0

    def list_inventory(self):
        if self.inventory:
            print("Inventory contains:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
            
    def hasKey(self, key_name):
        return key_name in self.inventory

    class NPC:
        def __init__(self, player):
            self.player = player
            self.state = "IDLE"

        def change_state(self, room):
            states = ["IDLE", "MOVE"]
            if room.has_item():
                states.append("LOOT")
            if room.has_zombie():
                states.append("ATTACK")

            weights = [40, 40, 15, 5] if len(states) == 4 else [50, 50]
            self.state = random.choices(states, weights=weights, k=1)[0]

        def act(self, room):
            self.change_state(room)
            if self.state == "IDLE":
                return "NPC is idle."
            elif self.state == "MOVE":
                return self.move(room)
            elif self.state == "LOOT":
                return self.loot(room)
            elif self.state == "ATTACK":
                return self.attack(room)

        def move(self, room):
            # Implement movement logic here
            pass

        def loot(self, room):
            if room.has_item():
                item = room.get_item()
                self.player.inventory.append(item)
                return f"NPC looted {item}."
            else:
                return "No items to loot."

        def attack(self, room):
            if room.has_zombie():
                # Implement attack logic here
                pass
            else:
                return "No zombies to attack."
