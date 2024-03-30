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