# from player import Player
# from character import ZombieNPC
# from combat import Combat
import random
import json
from npc import NPC

def test_NPC():
    # Mock data
    with open('../data/GameData.json') as f:
        data = json.load(f)
    # Replace this with your actual game data

    currentRoom = None
        #'hallway'  # Replace this with the name of the current room
    room = {}  # Replace this with an actual room object

    # mock items
    items = None

    # mock verb handler instance
    verb_handler_instance = None

    # Create an instance of the NPC class
    npc = NPC(data, currentRoom, items, verb_handler_instance)


    # [PASSED] TEST #1 -- Test NPC_change_state method with available items and available enemies
    initial_state = npc.currentState
    print("Initial state:\n", npc.currentState)
    npc.NPC_change_state(available_items=True, available_enemies=False)
    print("Current state:", npc.currentState)

    # TEST #3 -- Test NPC_loot when there are available items in room
    expected_output = f"The NPC has looted {items}."  # replace with the expected output
    npc.NPC_loot(currentRoom)
    print(f"The NPC is in {npc.currentRoom} and looted {npc.inventory}!")




'''
    # [PASSED] TEST #2 –– Test NPC_move function 
    old_room = npc.currentRoom
    npc.NPC_move()
    new_room = npc.currentRoom

    if old_room != new_room:
        print("Test passed: NPC moved from", old_room, "to", new_room, "\n")
    else:
        print("Test failed: NPC did not move")
'''


if __name__ == "__main__":
    test_NPC()
