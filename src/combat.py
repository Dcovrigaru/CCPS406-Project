import random

class Combat:
    def __init__(self, player, npc):
        self.player = player
        self.npc = npc

    def player_attack(self):
        if not self.player.current_weapon:
            print("You have no weapon equipped.")
            return

        if self.player.current_weapon == "Gun":
            damage = 35  # Fixed damage for simplicity
            message = "Boom, the zombie is dead."
        elif self.player.current_weapon == "Axe":
            damage = random.randint(20, 35)  # Variable damage for the axe
            message = "Lucky, your axe killed the zombie." if damage > 30 else "Bodyshot, the zombie is injured."

        self.npc.take_damage(damage)
        print(message)

        if not self.npc.is_alive():
            print(f"{self.npc.name} has been defeated.")

    def npc_attack(self):
        if not self.npc.is_alive():
            print(f"{self.npc.name} can no longer attack.")
            return

        damage = random.randint(self.npc.damage_min, self.npc.damage_max)
        self.player.take_damage(damage)
        print(f"Ow, that hurt. {self.npc.name} did {damage} damage. You now have {self.player.health} health left.")
