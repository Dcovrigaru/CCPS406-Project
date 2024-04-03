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

    NPC_currentRoom = None
    NPC_verb_handler_instance = None

    # Create an instance of the NPC class
    npc = NPC(data, NPC_currentRoom, NPC_verb_handler_instance)

    #npc.NPC_available_items_enemies(npc.NPC_currentRoom)

    for i in range(1, 100):
        print(f"NPC run #{i} values:\n")

        print(f"Initial state: {npc.currentState}")
        print(f"Current room: {npc.currentRoom}\n")
        npc.NPC_available_items_enemies(npc.currentRoom) # First run the available items
        print(f"Available items: {npc.available_items}, Available enemies:{npc.available_enemies}\n")
        npc.NPC_change_state() # Then change state based on the available items
        #npc.inventory = ['axe']
        #npc.currentState = 'ATTACK'
        print(f"Current state: {npc.currentState}")
        npc.NPC_act() #Then act based on NPC current state

        print("\n")



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
