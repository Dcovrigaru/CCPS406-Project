from combat import Combat

class VerbHandler:
    def __init__(self, items, current_room, player, npc, data):
        self.items = items
        self.inventory = []
        self.wielded_weapon = None
        self.current_room = current_room
        self.player = player
        self.npc = npc
        self.data = data
        self.combat_instance = Combat(player, npc, data)

    def handle_action(self, user_input):
        verbs = self.data['verbs']
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
                    elif verb == "attack":
                        self.handle_attack(item_name)
                    elif item_name in self.items or item_name in self.inventory or verb == "open":
                        # Call the corresponding method with the item name
                        getattr(self, f"handle_{verb}")(item_name)
                    elif verb == "use":
                        self.handle_use(item_name)
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
        zombies_present = False
        for room in self.data['rooms']:
            if room['name'] == self.current_room.currentRoom:
                if room['zombies'] > 0:
                    zombies_present = True  # Sets true if zombies are found in the room
                    break

        if zombies_present:  # Checks if there are any zombies to attack
            print("You can't open anything with zombies nearby")
            return
        room = next((room for room in self.data['rooms'] if room['name'] == self.current_room.currentRoom), None)
        is_subroom = item_name in room.get('subrooms', [])
        if not is_subroom:
            print(f"I don't see a {item_name} here.")
            return


        if room and 'subrooms' in room:
            for subroom_name in room['subrooms']:
                subroom = next((subroom for subroom in self.data['subrooms'] if subroom['name'] == subroom_name), None)
                if subroom and subroom['name'] == item_name and subroom.get('name', '') == 'safe':
                    if subroom.get('locked', True):
                        # If the safe is locked, prompt the user for the guess
                        correct_number = subroom.get('correct_number', '')  # Get the correct number for the safe
                        user_guess = input("Enter your guess (5 digits): ")
                        if self.check_guess(correct_number, user_guess):
                            # If the guess is correct, set 'locked' to False and print a success message
                            subroom['locked'] = False
                            print(subroom.get('unlocked_message', "The room is unlocked."))
                        else:
                            print("Sorry, your guess was incorrect.")
                        return
                    else:
                        # If the safe is already unlocked, print a message and return
                        print(subroom.get('openafter', "The room is already unlocked."))
                        subroom['locked'] = False  # Ensure that 'locked' is set to False
                        return
                elif subroom and subroom.get('locked', False) and 'unlocker' in subroom and subroom[
                    'unlocker'] in self.inventory:
                    subroom['locked'] = False
                    print(subroom.get('unlocked_message', "The room is unlocked."))
                    return
                elif subroom and subroom.get('locked', True) and 'unlocker' in subroom and subroom[
                    'unlocker'] not in self.inventory:
                    print(subroom.get('locked_message', "You don't have the necessary item to unlock this room."))
                    return
                else:
                    print(subroom.get('openafter', "The room is already unlocked."))
                    return
        print(f"I don't see a {item_name} here.")
    def handle_take(self, item_name):
        # Check if the item is already in the inventory
        if item_name in self.inventory:
            print(f"You already have the {item_name} in your inventory.")
            return

        # Find the current room
        current_room = next((room for room in self.data['rooms'] if room['name'] == self.current_room.currentRoom),
                            None)
        if current_room:
            # Check if the item is directly in the room (not in a subroom)
            if item_name in current_room['items']:
                self.inventory.append(item_name)
                for item in self.data['items']:
                    if item['name'] == item_name:
                        print(item.get('TakenText', ""))
                        break
                return

            # Check if the item is in a locked subroom
            if 'subrooms' in current_room:
                for subroom_name in current_room['subrooms']:
                    subroom = next((subroom for subroom in self.data['subrooms'] if subroom['name'] == subroom_name),
                                   None)
                    if subroom and item_name in subroom.get('items', []):
                        if subroom.get('locked', True):
                            print(f"I don't see a {item_name}.")
                            return
                        else:
                            print(f"You took the {item_name}.")
                            self.inventory.append(item_name)
                            for item in self.data['items']:
                                if item['name'] == item_name:
                                    print(item.get('TakenText', ""))
                                    break
                            return

        # Item not found in the current room
        print(f"I don't see a {item_name} here.")

    def handle_use(self, item_name):
        # Loop through all items in the data
        for item in self.data['items']:
            # Check if the current item's name matches the provided item_name
            if item['name'] == item_name:
                # Check if the 'used_status' key is present in the item
                if 'used_status' in item:
                    # Check if the item has already been used and is not in the inventory
                    if item['used_status'] and item_name not in self.inventory:
                        print("You already used this item, you don't have it anymore")
                        return

        # Check if the item is not in the inventory
        if item_name not in self.inventory:
            print(f"You don't have the {item_name} in your inventory.")
            return

        # Loop through all items in the data
        for item in self.data['items']:
            # Check if the current item's name matches the provided item_name
            if item['name'] == item_name:
                # Check if the 'used_status' key is present in the item
                if 'used_status' in item:
                    # Check if the item has not been used yet
                    if not item['used_status']:
                        # Check if the current room matches the required location
                        if self.current_room.currentRoom == item['req_location']:
                            item['used_status'] = True
                            self.inventory.remove(item_name)
                            # Print the 'UseText' of the item if available
                            if 'UseText' in item:
                                print(item['UseText'])
                                return
                        else:
                            print(f"{item['name']} cannot be used here.")
                            return
                    else:
                        print(f"{item['name']} has already been used.")
                        return
                break

        # If no item is found with the provided name
        else:
            print(f"No item found with the name '{item_name}'")

        # Print the 'UseText' of the item if available
        for item in self.data['items']:
            if item['name'] == item_name:
                print(item.get('UseText', ""))
                break
        return

    def handle_wield(self, item_name):  # Function for handling the verb 'wield'
        weapons = self.data['weapons']
        weapon_names = [self.data["weapons"][weapon]["name"] for weapon in self.data["weapons"]]
        # Check if the item is in the inventory
        if item_name not in self.inventory:  # Checking to see if the player has the said item
            print(f"You don't have the {item_name} in your inventory.")
            return
        elif item_name not in weapon_names:  # Checking to see if the item is even a weapon capable of wielding
            print(f"Are you sure {item_name} is a weapon?")
            return

        # Check if any other weapon is wielded and unwield it
        for weapon, details in self.data['weapons'].items():
            if weapon != item_name and details['is_wielded']:
                details['is_wielded'] = False
                print(f"You were wielding the {weapon}, you have unwielded it.")

        # Wield the selected weapon
        if not self.data['weapons'][item_name]['is_wielded']:
            self.data['weapons'][item_name]['is_wielded'] = True
            self.wielded_weapon = item_name
            print(f"You are now wielding the {self.wielded_weapon}")
        else:
            print(f"The {item_name} is already wielded")

    def handle_attack(self, item_name):  # Function for handling the verb 'attack'
        # Implement attack action logic
        if item_name != "zombies" and item_name != "zombie":
            print(f"Uh oh, you can't attack a {item_name}")
            return
        zombies_present = False
        for room in self.data['rooms']:
            if room['name'] == self.current_room.currentRoom:
                if room['zombies'] > 0:
                    zombies_present = True  # Sets true if zombies are found in the room
                    break

        if not zombies_present:  # Checks if there are any zombies to attack
            print("There are no zombies in this room")
            return

        # Check if the player is wielding a weapon
        if self.wielded_weapon is None:  # Checking if a player is wielding a weapon
            print(f"You are not wielding any weapon to attack with")
            return
        else:
            self.combat_instance.player_attack(self.wielded_weapon,
                                               self.current_room.currentRoom)  # Calls the player_attack to handle attacks
            # print(data['weapons'][self.wielded_weapon]['attack_message'])

    def handle_inventory(self):  # Function for handling the verb 'inventory'
        if len(self.inventory) == 0:  # Displays a message if the inventory is empty
            print("You haven't picked anything up")
        else:
            for item_name in self.inventory:
                for item in self.data['items']:
                    if item['name'] == item_name:
                        print(
                            f"[{item['name']}]\t{item['desc']}")  # Displays each item vertically in a list side by side its description
                        break

    def check_guess(self, correct_number, user_guess):
        """Check how many digits are in the correct position."""
        correct_count = 0
        if (len(user_guess)) != 5:
            print("Remeber, this safe accepts a 5 digit number")
            return False
        for i in range(len(correct_number)):
            if correct_number[i] == user_guess[i]:
                correct_count += 1
        if correct_count == 5:
            print("Congratulations! You guessed the number correctly:", correct_number)
            return True
        else:
            print("You have", correct_count, "digits in the right position.")

    # The rest of your code where you call the check_guess() function remains the same.

