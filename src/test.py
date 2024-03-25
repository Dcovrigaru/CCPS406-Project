from character import Player
from character import NPC
from combat import Combat

def test_combat_scenario():
    print("=== Combat Scenario Test ===\n")
    
    # Setup: Create player and NPC
    player = Player("Jake", 100)
    npc = NPC("Zombie", 50, 10, 20, is_friendly=False)
    
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
