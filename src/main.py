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
            zombies.append(Zombie(id=f'Zombie_{i}', health=10, damage_min=5, damage_max=10))
    return zombies

def main():
    global currentRoom
    print(data['story']['intro'])
    
    while player.healthStatus():
        # Handle room change
        zombies = spawn_zombies(currentRoom)

        # Display room description and items
        for room in data['rooms']:
            if room['name'] == currentRoom:
                print(room['first_text'])

        # If there are zombies in the room, initiate combat
        if zombies:
            combat_instance = Combat(player, zombies, data)
            combat_instance.handle_room_combat()

            # Check if player is still alive after combat
            if not player.healthStatus():
                print("Game over!")
                break
                # Check if all zombies in the room are defeated
        if not zombies:
            print("All zombies defeated. You can now explore further.")

            # Update the number of zombies in the current room in the JSON data
            for room in data['rooms']:
                if room['name'] == currentRoom:
                    room['zombies'] = 0  # Set the number of zombies in the room to 0
                    break

        # Continue exploring or take other actions
        # Add your logic here based on the player's input


        # Get user input
        user_input = input("Enter an action: ").lower()

        # Process user input with VerbHandler
        # Inside the main function after handling user input
        if user_input in compass:
            UserCurrentRoom.move(user_input)
            currentRoom = UserCurrentRoom.currentRoom
            # Update player's current room
            player.update_current_room(currentRoom)

        elif user_input == "exit":
            print("Exiting game.")
            break
        else:
            verb_handler = VerbHandler(data['items'], UserCurrentRoom, player, zombies, data, combat_instance, player.inventory)
            verb_handler.handle_action(user_input)

        # Check if all zombies in the room are defeated
        if not zombies:
            print("All zombies defeated. You can now explore further.")

        # Continue exploring or take other actions
        # Add your logic here based on the player's input

if __name__ == "__main__":
    main()
