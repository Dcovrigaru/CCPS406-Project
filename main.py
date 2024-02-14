#Class Instances/Variables
from verbs import VerbHandler, verbs
from directions import DirectionHandling
verb_handler = VerbHandler()
UserCurrentRoom = DirectionHandling(currentRoom="attic")

#Main Variables
verb_list = ["open", "take", "use", "wield", "attack", "inventory"]
items_list = ["antique key", "flashlight", "pistol", "axe", "riddle", "paper" "journal", "pistol", "lockpick", "diary", "batteries", "rusty key"]
compass = ["n","e","w","s","u","d","up","east","west","down","north","south","current","c"]
"""
Paper = Safe Passcode Paper
Rusty Key = Key for Stairs Between Office Room and Living Room
Antique Key = Key for Front Door
"""
def main():
    while True:
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif len(user_input) == 1:
            #Direction input
            if user_input in compass:
                UserCurrentRoom.move(user_input)
            else:
                print(f"Not sure what {user_input} means. Try again!")
                continue
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            break
        elif user_input.split(" ")[0] in verb_list:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in verbs:
            # Send an error message if there is only one word and it is a verb
            print(f"What are you trying to {user_input} ?")
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue

if __name__ == "__main__":
    main()

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file seperate from main?
"""