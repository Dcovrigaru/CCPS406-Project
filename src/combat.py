import random
from character import Player, player_stats, NPC

class PlayerDefeatedException(Exception):
    pass

class Combat:

    def __init__(self, data):
        self.data = data
        self.zombie_stats = NPC('zombie', 1, 10)

    def player_attack(self, current_weapon, current_room):
        room_data = next(room for room in self.data['rooms'] if room['name'] == current_room)

        if current_weapon in self.data['weapons'] and current_weapon == 'gun':
            weapon = self.data['weapons'][current_weapon]

            if weapon['ammo'] > 0: # If the gun has ammo, proceed
                weapon['ammo'] -= 1
                print(f"{weapon['attack_message']}")
                room_data['zombies'] -= 1
                print("There are " + str(room_data['zombies']) + " zombies left in the room.")
                print(f"You have {weapon['ammo']} bullets left.")
            else:
                print("Out of ammo!") #If the gun has no ammo, no attack can be made

        elif current_weapon == "axe":
            attacks = 0
            total_damage = 0
            health = player_stats.health
            while self.zombie_stats.is_alive():
                damage = random.randint(20, 35)  # Example random damage for demonstration
                self.zombie_stats.take_damage(damage)
                attacks += 1
                total_damage += damage
                # Zombie attacks back after each player's attack
                zombie_damage = random.randint(1, 10)
                player_stats.take_damage(zombie_damage)
                if not player_stats.is_alive():
                    print(
                        f"You attacked the {self.zombie_stats.name} {attacks} times, dealing a total of {total_damage} damage.\n"
                        f"You were attacked for {int(health) - int(player_stats.health)} damage.\n"
                        f"You have {player_stats.health} health remaining.\n"
                        f"You are dead.")

                    raise PlayerDefeatedException("Player is defeated.")
            # Decrement the number of zombies in the current room
            for room in self.data['rooms']:
                if room['name'] == current_room:
                    room['zombies'] -= 1
                    self.zombie_stats = NPC('zombie', 1, 10)
                    break
            print(
                f"You attacked the {self.zombie_stats.name} {attacks} times, dealing a total of {total_damage} damage.\n"
                f"You were attacked for {int(health) - int(player_stats.health)} damage.\n"
                f"You have {player_stats.health} health remaining.\n"
                f"There are {room_data['zombies']} zombies left in the room.")
