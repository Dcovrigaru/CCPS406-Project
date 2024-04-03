import json
import sys
import time
import random
from combat import PlayerDefeatedException
from character import player_stats
from verbs import VerbHandler
from directions import DirectionHandling
from npc import NPC

# Declare turn_limit as a global variable
turn_limit = 0


def npc_random_room(data):
    filtered_rooms = [room for room in data["rooms"] if room["name"] != "attic"]
    random_room = random.choice(filtered_rooms)
    return random_room["name"]


def initialize_game_data():
    with open('../data/GameData.json') as f:
        return json.load(f)


def reset_game_data():
    with open('../data/GameData_initial.json') as f:
        return json.load(f)

def help_menu():
    print("1. Instructions")
    print("2. Tips and Tricks")

    choice = input("Enter your choice (1, 2, or anything else to go back): ")

    if choice == '1':
        print("Instructions: [Insert game instructions here]")
        input("Press Enter to return to the game...")
    elif choice == '2':
        print("Tips and Tricks: [Insert tips and tricks here]")
        input("Press Enter to return to the game...")
    else: print("Going back now")

def game_menu():
    global turn_limit
    hard_turns = 70
    medium_turns = 82
    easy_hp = 200
    medium_hp = 150
    hard_hp = 100
    print("*" * 40)
    print("*" + " " * 38 + "*")
    print("*" + " " * 7 + "Welcome to Death Escape!" + " " * 7 + "*")
    print("*" + " " * 38 + "*")
    print("*" * 40)
    while True:

        print("1. Instructions")
        print("2. Tips and Tricks")
        print("3. Proceed")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("Instructions: [Insert game instructions here]")
            input("Press Enter to return to the menu...")
        elif choice == '2':
            print("Tips and Tricks: [Insert tips and tricks here]")
            input("Press Enter to return to the menu...")
        elif choice == '3':
            print("Welcome to death escape. Choose your difficulty:")
            print(f"e - Easy (infinite turns & {easy_hp}HP)")
            print(f"m - Medium ({medium_turns} turns & {medium_hp}HP)")
            print(f"h - Hard ({hard_turns} turns & {hard_hp}HP)")

            while True:
                user_choice = input().lower()
                if user_choice in ('e', 'easy'):
                    turn_limit = float('inf')
                    player_stats.health = easy_hp
                    break
                elif user_choice in ('m', 'medium'):
                    turn_limit = medium_turns
                    player_stats.health = medium_hp
                    break
                elif user_choice in ('h', 'hard'):
                    turn_limit = hard_turns
                    player_stats.health = hard_hp
                    break
                else:
                    print("Invalid choice. Please select e, m, or h.")
            print("Proceeding with the game...")
            break
        else:
            print("Invalid input! Please enter 1, 2, or 3.")


def play_game(data):
    global turn_limit
    # npc_current_room = None
    # npc_verb_handler_instance = None
    current_room = "attic"
    user_current_room = DirectionHandling(current_room, data, None)
    verb_handler = VerbHandler(data['items'], user_current_room, data)
    npc_current_room = npc_random_room(data)
    npc_verb_handler_instance = verb_handler
    user_current_room.verb_handler = verb_handler
    npc = NPC(data, npc_current_room, npc_verb_handler_instance)
    turn_count = 0
    total_play_time = 0
    game_menu()
    print(f"\n\n{data['story']['intro']}\n\n{data['rooms'][0]['first_text']}")
    start_time = time.time()

    while user_current_room.currentRoom != 'outside' and (
            turn_count != turn_limit if turn_limit != float('inf') else True):
        user_input = input("Enter in an action: ").lower()

        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif user_input in data['compass']:
            user_current_room.move(user_input)
        elif user_input == "exit":
            checking_quit = input("Are you sure you want to quit? (y/n): ").lower()
            if checking_quit == "yes" or checking_quit == "y":
                break
            else:
                print("Guess we'll continue.")
                continue
        elif user_input.split(" ")[0] in data['verbs']:
            verb_handler.handle_action(user_input)
        elif len(user_input.split()) == 1 and user_input in data['verbs']:
            print(f"What are you trying to {user_input} ?")
        elif user_input == 'help':
            print("Game Paused")
            help_menu()
            print("Game Unpaused")
            continue
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue

        npc.NPC_available_items_enemies(npc.currentRoom)
        npc.NPC_change_state()
        npc.NPC_act(npc_verb_handler_instance)

        turn_count += 1

    end_time = time.time()
    total_play_time += end_time - start_time

    minutes = int(total_play_time // 60)
    seconds = total_play_time % 60

    if user_current_room.currentRoom == 'outside':
        print(data['story']['gameEnd'])
        print(
            "\nYou finished the game in {} minutes and {:.2f} seconds, using {} out of {} total turns. Hope you had "
            "fun!".format(
                minutes, seconds, turn_count, turn_limit))
    elif turn_count == turn_limit:
        print(f"\nYou ran out of turns, you used a total of {turn_count} turns. Better luck next time!")
        print("You played the game for {} minutes and {:.2f} seconds. Hope you had fun!".format(minutes, seconds))
    else:
        print(f"\nYou used a total of {turn_count} turns!")
        print("You played the game for {} minutes and {:.2f} seconds. Hope you had fun!".format(minutes, seconds))


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
            sys.exit()


if __name__ == "__main__":
    main()
