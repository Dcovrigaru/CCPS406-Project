verbs = ["open", "take", "use", "wield", "attack", "inventory"]

class VerbHandler:
    def __init__(self, items):
        self.items = items

    def handle_action(self, user_input):
        # Split the user input into words
        words = user_input.split()

        # Extract the verb (first word)
        verb = words[0]

        # Check if the verb is in the list of verbs
        if verb in verbs:
            # Check if there's a second word (after the verb)
            if len(words) > 1:
                # Check if the verb is not "inventory" and the item is in the items list
                if verb != "inventory" and words[1] in self.items:
                    item_name = words[1]
                    # Call the corresponding method with the item name
                    getattr(self, f"handle_{verb}")(item_name)
                # If verb is "inventory", call the corresponding method without item
                elif verb == "inventory":
                    getattr(self, f"handle_{verb}")()
                elif verb == "attack":
                    if words[1] == "zombie":
                        self.handle_attack(words[1])
                    else:
                        print("You can only attack a zombie!")
                else:
                    print(f"Item '{words[1]}' not found.")
            else:
                # No item provided
                print("No item provided. Please try again.")
        else:
            print("Invalid action. Please try again.")

    def handle_open(self, item_name):
        # Implement open action logic
        print(f"Handling open action for item: {item_name}...")

    def handle_take(self, item_name):
        # Implement take action logic
        print(f"Handling take action for item: {item_name}...")

    def handle_use(self, item_name):
        # Implement use action logic
        print(f"Handling use action for item: {item_name}...")

    def handle_wield(self, item_name):
        # Implement wield action logic
        print(f"Handling wield action for item: {item_name}...")

    def handle_attack(self, item_name):
        # Implement attack action logic
        print(f"Handling attack action for item: {item_name}...")

    def handle_inventory(self):
        # Implement inventory action logic
        print("Handling inventory action...")
