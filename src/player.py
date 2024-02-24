# player.py

#Adding code here  this is a test

class Player:
    def __init__(self, name, health=200):
        self.name = name
        self.health = health
        self.inventory = []

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"{item} added to inventory.")
        else:
            print(f"{item} is already in inventory.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print("Item not found in inventory.")

    def list_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(item)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died.")
        else:
            print(f"{self.name} now has {self.health} health.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed to {self.health} health.")

'''
def test_player():
    print("Testing Player class...")
    player = Player("Hero", 100)
    player.add_item("Sword")
    player.add_item("Health Potion")
    player.list_inventory()
    player.take_damage(10)
    player.heal(5)
    player.remove_item("Sword")
    player.list_inventory()

if __name__ == "__main__":
    test_player()
'''
