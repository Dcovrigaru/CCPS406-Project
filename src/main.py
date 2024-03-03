#Class Instances/Variables
from verbs import VerbHandler, verbs
from directions import *
UserCurrentRoom = DirectionHandling(currentRoom="attic") #player starts in attic

#Main Variables
items = ["key", "flashlight", "pistol", "axe", "scribe", "paper" "journal", "lockpick", "diary", "batteries", "key"]
compass = ["n", "e", "w", "s", "u", "d", "up", "east", "west", "down", "north", "south", "current", "c"]


def main():
    ResetNewGame()     #this resets times_entered for all rooms back to 0 (attic to 1) and prints games intro message
    verb_handler = VerbHandler(items)
    while True:
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif user_input in compass:
            #Direction input
            UserCurrentRoom.move(user_input)
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            break
        elif user_input.split(" ")[0] in verbs:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in verbs:
            # Send an error message if there is only one word and it is a verb
            print(f"What are you trying to {user_input} ?")
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue

if __name__ == "__main__":
    main()

