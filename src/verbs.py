import json
from directions import DirectionHandling
# Read data from JSON file
with open('../data/GameData.json') as f:
    data = json.load(f)

# Extract items and verbs from the data
verbs = data['verbs']
items = data['items']
weapons = data['weapons']
print()
print(verbs)
print(items)
if data['weapons']['gun']['is_wielded']:
    print("The gun is wielded.")
else:
    print("The gun is not wielded.")
weapon_names = [data["weapons"][weapon]["name"] for weapon in data["weapons"]]

print(weapon_names)
class VerbHandler:
    def __init__(self, items, current_room):
        self.items = items
        self.inventory = []
        self.current_room = current_room

    def handle_action(self, user_input):
        # Split the user input into words
        words = user_input.split()
        # Extract the verb (first word)
        verb = words[0]

        # Check if the verb is in the list of verbs
        if verb in verbs:
            # Check if there's a second word (after the verb)
            if len(words) > 1:

                # Join the remaining words to form the item name
                item_name = ' '.join(words[1:])
                # Check if the verb is not "inventory" and the item is in the items list
                if verb != "inventory":
                    if verb == "take":
                        self.handle_take(item_name)
                    elif item_name in self.items or item_name in self.inventory:
                        # Call the corresponding method with the item name
                        getattr(self, f"handle_{verb}")(item_name)
                    else:
                        print(f"You haven't found '{item_name}' yet.")
                # If verb is "inventory", call the corresponding method without item
                elif verb == "attack":
                    if words[1] == "zombie":
                        self.handle_attack(words[1])
                    else:
                        print("You can only attack a zombie!")
            elif verb == "inventory":
                getattr(self, f"handle_{verb}")()
            else:
                # No item provided
                print("No item provided. Please try again.")
        else:
            print("Invalid action. Please try again.")

    def handle_open(self, item_name):
        # Implement open action logic
        print(f"Handling open action for item: {item_name}...")

    def handle_take(self, item_name):
        # Check if the item is already in the inventory
        if item_name in self.inventory:
            print(f"You already have the {item_name} in your inventory.")
            return

        # Check if the item is present in the current room
        item_present_in_room = False
        for room in data['rooms']:
            if room['name'] == self.current_room.currentRoom and item_name in room['items']:
                item_present_in_room = True
                break

        if not item_present_in_room:
            print(f"I dont see a {item_name}")
            return

        # Add the item to inventory if it's present in the current room
        print(f"You took the {item_name}.")
        self.inventory.append(item_name)
        for item in data['items']:
            if item['name'] == item_name:
                print(item['TakenText'])
                break


    def handle_use(self, item_name):
        # Check if the item is in the inventory
        if item_name in self.inventory:
            # Implement use action logic
            print(f"Handling use action for item: {item_name}...")
        else:
            print(f"You don't have the {item_name} in your inventory.")

    def handle_wield(self, item_name):
        # Check if the item is in the inventory
        if item_name not in self.inventory:
            print(f"You don't have the {item_name} in your inventory.")
            return
        elif item_name not in weapon_names:
            print(f"Are you sure {item_name} is a weapon?")
            return

        # Check if any other weapon is wielded and unwield it
        for weapon, details in data['weapons'].items():
            if weapon != item_name and details['is_wielded']:
                details['is_wielded'] = False
                print(f"You were wielding the {weapon}, you have unwielded it.")

        # Wield the selected weapon
        if not data['weapons'][item_name]['is_wielded']:
            data['weapons'][item_name]['is_wielded'] = True
            print(f"You are now wielding the {item_name}")
        else:
            print(f"The {item_name} is already wielded")

    def handle_attack(self, item_name):
        # Implement attack action logic
        print(f"Handling attack action for item: {item_name}...")

    def handle_inventory(self):
        if len(self.inventory) == 0:
            print("You haven't picked anything up")
        else:
            for item_name in self.inventory:
                for item in data['items']:
                    if item['name'] == item_name:
                        print(f"[{item['name']}]\t{item['desc']}")
                        break