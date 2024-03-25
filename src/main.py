import json
from combat import Combat
from verbs import VerbHandler
from directions import DirectionHandling, compass
from characters import Player, Zombie

# Load game data
with open('../data/GameData.json') as f:
    data = json.load(f)

# Initialize player
player_name = input("Enter your character's name: ")
player = Player(id=player_name, health=100, damage_min=20, damage_max=35)

# Initialize current room and direction handling
currentRoom = "attic"
UserCurrentRoom = DirectionHandling(currentRoom, data)

# Function to spawn zombies based on room data
def spawn_zombies(room_name):
    room_info = next((room for room in data['rooms'] if room['name'] == room_name), None)
    zombies = []
    if room_info and 'zombies' in room_info:
        for i in range(room_info['zombies']):
            zombies.append(Zombie(id=f'Zombie_{i}', health=10, damage_min=1, damage_max=10))
    return zombies

def main():
    global currentRoom
    print(data['story']['intro'])
    
    while player.healthStatus():
        zombies = spawn_zombies(currentRoom)

        for room in data['rooms']:
            if room['name'] == currentRoom:
                print(room['first_text'])

        if zombies:
            combat_instance = Combat(player, zombies, data)
            combat_instance.handle_room_combat()

            if not player.healthStatus():
                print("Game over!")
                break

        if not zombies:
            print("You can now explore further.")

            for room in data['rooms']:
                if room['name'] == currentRoom:
                    room['zombies'] = 0
                    break

        user_input = input("Enter an action: ").lower()

        if user_input in compass:
            UserCurrentRoom.move(user_input)
            currentRoom = UserCurrentRoom.currentRoom
            player.update_current_room(currentRoom)
        elif user_input == "exit":
            print("Exiting game.")
            break
        else:
            verb_handler = VerbHandler(data['items'], UserCurrentRoom, player, zombies, data, None, player.inventory)
            verb_handler.handle_action(user_input)

        if not zombies:
            print("All zombies defeated. You can now explore further.")

if __name__ == "__main__":
    main()
