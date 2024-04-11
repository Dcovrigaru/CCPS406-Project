class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            pass
        else:
            pass

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
    def __init__(self, name, damage_min, damage_max, health=100):
        super().__init__(name, health)
        self.damage_min = damage_min
        self.damage_max = damage_max





player_stats = Player('player')