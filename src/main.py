#Importing Json
import json
with open('../data/GameData.json') as f:
    data = json.load(f)

# Extract items and verbs from the data
verbs = data['verbs']
items = data['items']

#Class Instances/Variables
from verbs import VerbHandler
from directions import DirectionHandling
UserCurrentRoom = DirectionHandling(currentRoom="attic")

#Main Variables
compass = ["n","e","w","s","u","d","up","east","west","down","north","south","current","c"]
"""
Paper = Safe Passcode Paper
Rusty Key = Key for Stairs Between Office Room and Living Room
Antique Key = Key for Front Door
"""
def main():
    verb_handler = VerbHandler(items, UserCurrentRoom)
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

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file seperate from main?
"""