# verbs.py

# Define the list of verbs
verbs = ["open", "take", "use", "wield", "attack", "inventory"]

class VerbHandler:
    def __init__(self):
        pass

    def handle_action(self, user_input):
        # Split the user input into words
        words = user_input.split()

        # Extract the verb (first word)
        verb = words[0]

        # Check if the verb is in the list of verbs
        if verb in verbs:
            # Call the corresponding method based on the verb
            if verb == "open":
                self.handle_open()
            elif verb == "take":
                self.handle_take()
            elif verb == "use":
                self.handle_use()
            elif verb == "wield":
                self.handle_wield()
            elif verb == "attack":
                self.handle_attack()
            elif verb == "inventory":
                self.handle_inventory()
        else:
            print("Invalid action. Please try again.")

    def handle_open(self):
        # Implement open action logic
        print("Handling open action...")

    def handle_take(self):
        # Implement take action logic
        print("Handling take action...")

    def handle_use(self):
        # Implement use action logic
        print("Handling use action...")

    def handle_wield(self):
        # Implement wield action logic
        print("Handling wield action...")

    def handle_attack(self):
        # Implement attack action logic
        print("Handling attack action...")

    def handle_inventory(self):
        # Implement inventory action logic
        print("Handling inventory action...")
