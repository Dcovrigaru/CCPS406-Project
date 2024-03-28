import random

class Combat:
    def __init__(self, player, npc, data):
        self.player = player
        self.npc = npc
        self.data = data

    def player_attack(self, current_weapon, current_room):
        room_data = next(room for room in self.data['rooms'] if room['name'] == current_room)
        if current_weapon == "gun":
            # Decrement the number of zombies in the current room
            for room in self.data['rooms']:
                if room['name'] == current_room:
                    room['zombies'] -= 1
                    break



            print(self.data['weapons'][current_weapon]['attack_message'])
            print("There are " + str(room_data['zombies']) + " zombies left in the room.")

        elif current_weapon == "axe":
            # Implement your own logic here for axe damage calculation
            damage = random.randint(20, 35)  # Example random damage for demonstration
            # Decrement the number of zombies in the current room
            for room in self.data['rooms']:
                if room['name'] == current_room:
                    room['zombies'] -= 1

                    print(self.data['weapons'][current_weapon]['attack_message'])
                    print("There are " + str(room_data['zombies']) + " zombies left in the room.")
                    break

    def npc_attack(self):
        if not self.npc.is_alive():
            print(f"{self.npc.name} can no longer attack.")
            return

        damage = random.randint(self.npc.damage_min, self.npc.damage_max)
        self.player.take_damage(damage)
        print(f"Ow, that hurt. {self.npc.name} did {damage} damage. You now have {self.player.health} health left.")
