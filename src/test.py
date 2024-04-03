# from player import Player
# from character import ZombieNPC
# from combat import Combat
import random
from npc import NPC

def test_NPC():
    # Mock data
    data = {
            "roomConnections": {
                "bathroom": {
                  "south": "bedroom"
                },
                "bedroom": {
                  "north": "bathroom",
                  "east": "hallway"
                },
                "hallway": {
                  "west": "bedroom",
                  "east": "office",
                  "up": "attic"
                },
                "office": {
                  "west": "hallway",
                  "down": "living room"
                },
                "living room": {
                  "up": "office",
                  "down": "basement",
                  "west": "foyer"
                },
                "foyer": {
                  "east": "living room",
                  "west": "kitchen",
                  "north": "outside"
                },
                "kitchen": {
                  "south": "garage",
                  "east": "foyer"
                },
                "garage": {
                  "north": "kitchen"
                },
                "basement": {
                  "up": "living room"
                },
                "attic": {
                  "down": "hallway"
                }
            }
        }
    # Replace this with your actual game data

    currentRoom = 'bedroom'  # Replace this with the name of the current room
    room = {}  # Replace this with an actual room object

    # mock items
    items = "Axe"

    # mock verb handler instance
    verb_handler_instance = None

    # Create an instance of the NPC class
    npc = NPC(data, currentRoom, items, verb_handler_instance)

    npc.current_state = 'LOOT'

    # TEST #3 -- Test NPC_loot when there are available items in room

'''
    # [PASSED] TEST #1 -- Test NPC_change_state method with available items and available enemies
    initial_state = npc.current_state
    print("Initial state:\n", npc.current_state)
    npc.NPC_change_state(available_items=True, available_enemies=False)
    print("Current state:", npc.current_state)
'''


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
