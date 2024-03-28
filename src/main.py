from combat import Combat
from verbs import VerbHandler
from directions import DirectionHandling
#Importing Json
import json
import sys  #for the exit command to end game prematurely
with open('../data/GameData.json') as f:
    data = json.load(f)

# Extract items and verbs from the data
verbs = data['verbs']
items = data['items']

#Class Instances/Variables
currentRoom = "attic"
player = None
npc = None
#Main Variables


UserCurrentRoom = DirectionHandling(currentRoom, data, None) #leave as None here.
verb_handler = VerbHandler(items, UserCurrentRoom, npc, player, data)
UserCurrentRoom.verb_handler = verb_handler# this is needed so DirectionHandling can access the inventory attribute of player

def main():
    print(f"\n\n{data['story']['intro']}\n\n{data['rooms'][0]['first_text']}")
    while UserCurrentRoom.currentRoom!='outside':
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif user_input in data['compass']:
            #Direction input
            UserCurrentRoom.move(user_input)
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            checking_quit = input("Are you sure you want to quit? (y/n): ").lower()
            print(user_input.split(" "))
            if checking_quit == ("yes") or checking_quit == ("y"):
                print("Bye.")
                sys.exit() #end program here, NOT just while loop, since games ending message is after while loop.
            else:
                print("Guess we'll continue.")
                continue
        elif user_input.split(" ")[0] in verbs:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in verbs:
            # Send an error message if there is only one word and it is a verb
            print(f"What are you trying to {user_input} ?")
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue
    print(data['story']['gameEnd']) #ending message. Hooray!


if __name__ == "__main__":
    main()
