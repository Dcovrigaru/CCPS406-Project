import random
class Character:
    def __init__(self, id, health, damage_min, damage_max):
        self.id = id
        self.health = health
        self.damage_min = damage_min
        self.damage_max = damage_max

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.on_death()
        else:
            print(f"{self.id} takes {damage} damage, remaining health: {self.health}")

    def healthStatus(self):
        return self.health > 0

    def attack(self):
        return random.randint(self.damage_min, self.damage_max)

    def on_death(self):
        print(f"{self.id} is defeated.")

class Zombie(Character):
    def __init__(self, id, health=10, damage_min=1, damage_max=10):
        super().__init__(id, health, damage_min, damage_max)

    def healthStatus(self):
        return self.health > 0
    
class Player(Character):
    def __init__(self, id, health, damage_min, damage_max):
        super().__init__(id, health, damage_min, damage_max)
        self.current_room = None  # Initialize current room attribute
        self.current_weapon = "bare hands"  # Initialize current weapon attribute

    # Define method to update current room
    def update_current_room(self, room):
        self.current_room = room

    def healthStatus(self):
        return self.health > 0
    
    def on_death(self):
        super().on_death()
        print(f"Game Over. {self.id} has been defeated.")
