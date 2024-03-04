from combat import Combat
from verbs import VerbHandler
from directions import DirectionHandling, compass
#Importing Json
import json
with open('../data/GameData.json') as f:
    data = json.load(f)

# Extract items and verbs from the data
verbs = data['verbs']
items = data['items']
subroom_name = "safe"  # Replace "your_subroom_name" with the actual name of the subroom
y = None
for subroom in data['subrooms']:
    if subroom['name'] == subroom_name:
        y = subroom.get('locked')
        break

# Now y contains the value of the 'locked' attribute of the subroom with the specified name


#Class Instances/Variables
currentRoom = "attic"
UserCurrentRoom = DirectionHandling(currentRoom, data)
player = None
npc = None
#Main Variables
#print(y)
print(data['story']['intro'] + '\n')
for room in data['rooms']:
    if room['name'] == currentRoom:
        print(room['first_text'])

def main():
    verb_handler = VerbHandler(items, UserCurrentRoom, npc, player, data)
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

