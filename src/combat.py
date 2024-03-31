import random
from character import Player
from character import player_stats
from character import ZombieNPC

zombie_stats = ZombieNPC('zombie', 1, 10, )

class PlayerDefeatedException(Exception):
    pass
class Combat:

    def __init__(self, data):
        self.data = data

    def player_attack(self, current_weapon, current_room):
        room_data = next(room for room in self.data['rooms'] if room['name'] == current_room)
        if current_weapon == "gun":
            # Decrement the number of zombies in the current room
            for room in self.data['rooms']:
                if room['name'] == current_room:
                    room['zombies'] -= 1
                    break
            print("There are " + str(room_data['zombies']) + " zombies left in the room")

        elif current_weapon == "axe":
            # Implement your own logic here for axe damage calculation
            damage = random.randint(20, 35)  # Example random damage for demonstration
            # Decrement the number of zombies in the current room
            for room in self.data['rooms']:
                if room['name'] == current_room:
                    global zombie_stats
                    zombie_stats.take_damage(damage)
                    if not zombie_stats.is_alive():
                        room['zombies'] -= 1
                        zombie_stats = NPC('zombie', 1, 10, )
                    if not self.attack():
                        raise PlayerDefeatedException("Player is defeated")
                    print("There are " + str(room_data['zombies']) + " zombies left in the room")
                    break

    def attack(self):
        damage = random.randint(1, 10)  # Placeholder for zombie's damage
        player_stats.take_damage(damage)
        print(f"{zombie_stats.name} attacks {player_stats.name} for {damage} damage!")
        if not player_stats.is_alive():
            print(f"You are dead.")
            return False
        return True