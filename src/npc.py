class NPC:
    def __init__(self, name, health, damage_min, damage_max, is_friendly=False, shout=None):
        self.name = name
        self.health = health
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.is_friendly = is_friendly
        self.shout = shout

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} is defeated.")
        else:
            print(f"{self.name} takes {damage} damage, remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def speak(self):
        if self.is_friendly:
            return f"The friendly {self.name} says: '{self.shout}'"
        else:
            return f"The hostile {self.name} growls menacingly."
