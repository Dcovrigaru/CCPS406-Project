# from player import Player
# from character import ZombieNPC
# from combat import Combat
from npc import NPC

'''
def test_combat_scenario():
    print("=== Combat Scenario Test ===\n")
    
    # Setup: Create player and NPC
    player = Player("Jake", 100)
    npc = ZombieNPC("Zombie", 50, 10, 20, is_friendly=False)

    print(f"Player created: {player.name} with {player.health} health.")
    print(f"NPC created: {npc.name} with {npc.health} health, Damage range: {npc.damage_min}-{npc.damage_max}\n")
    
    # Player actions: Add items and equip weapon
    player.add_item("Gun")
    player.equip_weapon("Gun")
    print("\nPlayer Inventory after adding and equipping a weapon:")
    player.list_inventory()
    
    # Initiate combat
    combat = Combat(player, npc)
    print("\nCombat starts:")
    combat.player_attack()  # Player attacks
    
    # NPC retaliation if alive
    if npc.is_alive():
        combat.npc_attack()
    else:
        print(f"\nThe {npc.name} was defeated and cannot retaliate.")
    
    # Display final statuses
    print("\n=== Final Statuses ===")
    print(f"{player.name} - Health: {player.health}")
    print(f"{npc.name} - Health: {npc.health} (Alive: {npc.is_alive()})")



if __name__ == "__main__":
    test_combat_scenario()
'''


import random
from NPC import NPC  # Assuming your source file is named NPC.py

def test_NPC():
    # Mock data
    data = {}  # Replace this with your actual game data
    current_room = 'bedroom'  # Replace this with the name of the current room
    available_items = True  # Replace with actual availability
    available_enemies = True  # Replace with actual availability
    room = {}  # Replace this with an actual room object

    # Create an instance of the NPC class
    npc = NPC(data, current_room)

    # Test change_state method
    npc.change_state(available_items, available_enemies)
    print("Current state:", npc.current_state)

    # Test act method
    action_result = npc.act(room)
    print("Action result:", action_result)

    # You can add more test cases as needed

if __name__ == "__main__":
    test_NPC()
