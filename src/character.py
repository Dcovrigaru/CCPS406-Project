class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} takes {damage} damage! {self.name} now has {self.health}")

    def is_alive(self):
        return self.health > 0

    def get_name(self):
        return self.name

class Player(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.inventory = []
        self.current_weapon = None

    def list_inventory(self):
        if self.inventory:
            print("Inventory contains:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

class NPC(Character):
    def __init__(self, name, damage_min, damage_max, health=100, is_friendly=False, shout=None):
        super().__init__(name, health)
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.is_friendly = is_friendly
        self.shout = shout

    def speak(self):
        if self.is_friendly:
            return f"The friendly {self.name} says: '{self.shout}'"
        else:
            return f"The hostile {self.name} growls menacingly."


player_stats = Player('player')