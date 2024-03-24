import random
class Combat:
    def __init__(self, player, zombies, game_data):
        self.player = player
        self.zombies = zombies
        self.zombies_encountered = False  # Flag to track if zombies have been encountered
        self.game_data = game_data

    def player_attack(self, zombie):
        weapon_damage = {
            "bare hands": (10, 20),
            "axe": (20, 30),
            "gun": (30, 50)
        }
        damage_range = weapon_damage.get(self.player.current_weapon, weapon_damage["bare hands"])
        damage = random.randint(*damage_range)
        if self.player.current_weapon:
            print(f"{self.player.id} attacks {zombie.id} with {self.player.current_weapon}!")
        else:
            print(f"{self.player.id} attacks {zombie.id} with bare hands!")
        if random.random() < 0.3:  # 30% chance for the player's attack to miss
            print(f"{self.player.id} misses the attack!")
            return 0  # No damage dealt if the attack misses
        else:
            zombie.take_damage(damage)
            return damage

    def zombie_attack(self, zombie):
        damage = random.randint(1, 10)  # Placeholder for zombie's damage
        self.player.take_damage(damage)
        print(f"{zombie.id} attacks {self.player.id} for {damage} damage!")
        if not self.player.healthStatus():
            print(f"{self.player.id} has been defeated. Game over.")
            return False
        return True

    def handle_room_combat(self):
        if not self.zombies:
            print("No zombies in the room.")
            return True

        # Print the message indicating the number of zombies only if they have not been encountered before
        if not self.zombies_encountered:
            print(f"There are {len(self.zombies)} zombies here.")
            self.zombies_encountered = True

        while self.player.healthStatus() and any(zombie.healthStatus() for zombie in self.zombies):
            for zombie in self.zombies:
                # Zombie attacks first
                if zombie.healthStatus() and self.player.healthStatus():
                    zombie_damage = zombie.attack()
                    self.player.take_damage(zombie_damage)
                    print(f"{zombie.id} attacks {self.player.id} for {zombie_damage} damage!")
                    if not self.player.healthStatus():
                        print(f"{self.player.id} has been defeated. Game over.")
                        return False

                # Player attacks
                if self.player.healthStatus() and zombie.healthStatus():
                    action = input("Enter action: ").lower()
                    if action == "attack":
                        player_damage = self.player_attack(zombie)
                        if not zombie.healthStatus():
                            print(f"{zombie.id} has been defeated.")
                            self.zombies.remove(zombie)
                            if not self.zombies:
                                # Update the number of zombies in the room to 0 after defeating all zombies
                                self.update_zombies()
                            break
                        if player_damage > 0:
                            print(f"{zombie.id} takes {player_damage} damage, remaining health: {zombie.health}")
                            if not self.zombies_attack(zombie):
                                return False
                        else:
                            print(f"{zombie.id} misses the attack!")
                    elif action == "exit":
                        print("Exiting game.")
                        return False
                    else:
                        print("Invalid action. Try again.")

                    if not self.player.healthStatus():
                        print("Game over!")
                        return False

        print("All zombies defeated. You are victorious!")
        return True


    def update_zombies(self):
        # Update the number of zombies in the current room in the game data
        for room in self.game_data['rooms']:
            if room['name'] == self.player.current_room:
                room['zombies'] = 0  # Set the number of zombies in the room to 0
                break
