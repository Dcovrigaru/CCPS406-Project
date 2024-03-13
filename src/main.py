from combat import Combat
from verbs import VerbHandler
from directions import DirectionHandling, compass
from player import Player
#Importing Json
import json
with open('../data/GameData.json') as f:
    data = json.load(f)

# Extract items and verbs from the data
verbs = data['verbs']
items = data['items']

#Class Instances/Variables
currentRoom = "attic"
UserCurrentRoom = DirectionHandling(currentRoom, data)
player_name = input("Enter your character's name: ")
player = Player(player_name, health=100)
npc = None
#Main Variables
print('\n' * 2)
print(data['story']['intro'])
print('\n' * 2)
for room in data['rooms']:
    if room['name'] == currentRoom:
        print(room['first_text'])

def main():
    verb_handler = VerbHandler(items, UserCurrentRoom, npc, player, data) #Calling the verb class
    while True:
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        #Checking all input
        if len(user_input) == 0:
            print(f"{player_name} You're probably supposed to write something.")
            continue
        elif user_input in compass:
            #Direction input
            UserCurrentRoom.move(user_input)
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            checking_quit = input(f"{player_name} Are you sure you want to quit? (y/n): ").lower()
            print(user_input.split(" "))
            if checking_quit == ("yes") or checking_quit == ("y"):
                print(f"Bye {player_name}")
                break
            else:
                print("Guess well continue")
                continue
        elif user_input.split(" ")[0] in verbs:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in verbs:
            # Send an error message if there is only one word and it is a verb
            print(f"What are you trying to {user_input} ?")
        else:
            print(f"Not sure what {user_input} means. Try again {player_name}!")
            continue

if __name__ == "__main__":
    main()

