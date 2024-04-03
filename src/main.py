import json
import sys
import time
from combat import Combat
from combat import PlayerDefeatedException
from character import player_stats
from verbs import VerbHandler
from directions import DirectionHandling
from npc import NPC

def initialize_game_data():
    with open('../data/GameData.json') as f:
        return json.load(f)

def reset_game_data():
    with open('../data/GameData_initial.json') as f:
        return json.load(f)


def play_game(data):

    NPC_currentRoom = None
    NPC_verb_handler_instance = None

    # Create an instance of the NPC class

    currentRoom = "attic"

    UserCurrentRoom = DirectionHandling(currentRoom, data, None)
    verb_handler = VerbHandler(data['items'], UserCurrentRoom, data)

    NPC_currentRoom = "bedroom"  # Assuming NPC spawns in the bedroom initially
    NPC_verb_handler_instance = verb_handler  # Pass the verb_handler instance to NPC
    UserCurrentRoom.verb_handler = verb_handler
    npc = NPC(data, NPC_currentRoom, NPC_verb_handler_instance)

    turn_count = 0
    totalPlayTime = 0

    print("Welcome to death escape. Choose your difficulty:")
    print("e - Easy (infinite turns)")
    print("m - Medium (40 turns)")
    print("h - Hard (30 turns)")

    while True:
        user_choice = input().lower()
        if user_choice == 'e' or user_choice == 'easy':
            turn_limit = float('inf')
            player_stats.health = 200
            break
        elif user_choice == 'm' or user_choice == 'medium':
            turn_limit = 40
            player_stats.health = 150
            break
        elif user_choice == 'h' or user_choice == 'hard':
            turn_limit = 30
            break
        else:
            print("Invalid choice. Please select e, m, or h.")

    print(f"\n\n{data['story']['intro']}\n\n{data['rooms'][0]['first_text']}")
    StartTime = time.time()

    while UserCurrentRoom.currentRoom != 'outside' and (turn_count != turn_limit if turn_limit != float('inf') else True):
        user_input = input("Enter in an action: ").lower()

        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif user_input in data['compass']:
            UserCurrentRoom.move(user_input)
        elif user_input == "exit":
            checking_quit = input("Are you sure you want to quit? (y/n): ").lower()
            if checking_quit == "yes" or checking_quit == "y":
                print("Bye.")
                sys.exit()
            else:
                print("Guess we'll continue.")
                continue
        elif user_input.split(" ")[0] in data['verbs']:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in data['verbs']:
            print(f"What are you trying to {user_input} ?")
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue

        npc.NPC_available_items_enemies(npc.currentRoom) # First run the available items
        npc.NPC_change_state() # Then change state based on the available items
        npc.NPC_act(NPC_verb_handler_instance) #Then act based on NPC current state

        turn_count += 1

    EndTime = time.time()
    totalPlayTime += EndTime - StartTime

    minutes = int(totalPlayTime // 60)
    seconds = totalPlayTime % 60

    if UserCurrentRoom.currentRoom == 'outside':
        print(data['story']['gameEnd'])
        print("\nYou finished the game in {} minutes and {:.2f} seconds. Hope you had fun!".format(minutes, seconds))
    elif turn_count == turn_limit:
        print(f"\nYou ran out of turns, you used a total of {turn_count} turns. Better luck next time!")
        print("\nYou Played the game for {} minutes and {:.2f} seconds. Hope you had fun!".format(minutes, seconds))

def main():
    while True:
        game_data = initialize_game_data()
        try:
            play_game(game_data)
        except PlayerDefeatedException:
            pass
        except Exception as e:
            print(f"An error occurred: {e}")
        reset = input("\nDo you want to play again? (yes/no): ").lower()
        if reset != 'yes' and reset != 'y':
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()