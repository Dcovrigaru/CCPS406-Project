# Class Instances/Variables
from verbs import VerbHandler, verbs
from directions import DirectionHandling

UserCurrentRoom = DirectionHandling(currentRoom="attic")

# Main Variables
items = ["antique key", "flashlight", "pistol", "axe", "riddle", "paper", "journal", "pistol", "lockpick", "diary", "batteries", "rusty key"]
compass = ["n", "e", "w", "s", "u", "d", "up", "east", "west", "down", "north", "south", "current", "c"]
"""
Paper = Safe Passcode Paper
Rusty Key = Key for Stairs Between Office Room and Living Room
Antique Key = Key for Front Door
"""

# Class Instances/Variables
from verbs import VerbHandler, verbs
from directions import DirectionHandling

UserCurrentRoom = DirectionHandling(currentRoom="attic")

# Main Variables
items = ["antique key", "flashlight", "pistol", "axe", "riddle", "paper", "journal", "pistol", "lockpick", "diary", "batteries", "rusty key"]
compass = ["n", "e", "w", "s", "u", "d", "up", "east", "west", "down", "north", "south", "current", "c"]
"""
Paper = Safe Passcode Paper
Rusty Key = Key for Stairs Between Office Room and Living Room
Antique Key = Key for Front Door
"""

def main():
    verb_handler = VerbHandler(items)
    while True:
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        # Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif user_input in compass:
            # Direction input
            UserCurrentRoom.move(user_input)
        # Other command inputs (beyond this line)
        elif user_input == "exit":
            break
        else:
            verb = user_input.split(" ")[0]
            # Check if the verb is valid
            if verb in verbs:
                # Call the handle_action method directly with the user input
                verb_handler.handle_action(user_input)
                if len(user_input.split()) == 1:
                    # Send an error message if there is only one word and it is a verb
                    print(f"What are you trying to {verb} ?")
            else:
                print(f"Not sure what {user_input} means. Try again!")

if __name__ == "__main__":
    main()

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file separate from main?
"""


"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file separate from main?
"""
