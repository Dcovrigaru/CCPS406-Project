class NPC:
    def __init__(self, id, health, is_friendly=False, shout=None):
        self.id = id
        self.health = health
        self.is_friendly = is_friendly
        self.shout = shout

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} is defeated.")
        else:
            print(f"{self.name} takes {damage} damage, remaining health: {self.health}")

    def healthStatus(self):
        return self.health > 0

    def speak(self):
        if self.is_friendly:
            return f"The friendly {self.name} says: '{self.shout}'"
        else:
            return f"The hostile {self.name} growls menacingly."
