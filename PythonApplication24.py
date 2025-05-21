import random

class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.max_health = health  # Add max health for healing
        self.health = health
        self.attack = attack

    def display_info(self):
        print(f"--- {self.name} ---")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print("-" * (len(self.name) + 6))

    def attack_target(self, target):
        if target.health <= 0:
            print(f"{target.name} is already defeated and cannot be attacked.")
            return

        damage = self.attack + random.randint(0, self.level // 2)  # Add a small bonus from level
        target.health -= damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage.")
        if target.health <= 0:
            target.health = 0
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name}'s Health: {target.health}/{target.max_health}")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} restores {amount} health. Current health: {self.health}/{self.max_health}")


class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor  # Unique property: armor

    def display_info(self):
        super().display_info()
        print(f"Armor: {self.armor}")

    def attack_target(self, target):
        if target.health <= 0:
            print(f"{target.name} is already defeated and cannot be attacked.")
            return

        effective_attack = self.attack + (self.armor // 5)  # Small bonus from armor to attack
        damage = effective_attack + random.randint(0, self.level // 2)
        
        target.health -= damage
        print(f"Warrior {self.name} attacks {target.name} with {effective_attack} power and deals {damage} damage.")
        if target.health <= 0:
            target.health = 0
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name}'s Health: {target.health}/{target.max_health}")


class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana  # Unique property: mana
        self.max_mana = mana  # Add max mana for restoration

    def display_info(self):
        super().display_info()
        print(f"Mana: {self.mana}/{self.max_mana}")

    def cast_spell(self, target):
        if self.mana >= 20:  # Spell cost
            if target.health <= 0:
                print(f"{target.name} is already defeated.")
                return

            spell_damage = self.attack * 1.5 + random.randint(0, self.level)  # Stronger spell attack
            self.mana -= 20
            target.health -= spell_damage
            print(f"Mage {self.name} casts a spell on {target.name} and deals {spell_damage} magic damage.")
            if target.health <= 0:
                target.health = 0
                print(f"{target.name} has been defeated!")
            else:
                print(f"{target.name}'s Health: {target.health}/{target.max_health}, {self.name}'s Mana: {self.mana}/{self.max_mana}")
        else:
            print(f"{self.name} doesn't have enough mana to cast the spell.")

    def restore_mana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        print(f"{self.name} restores {amount} mana. Current mana: {self.mana}/{self.max_mana}")


class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows  # Unique property: number of arrows

    def display_info(self):
        super().display_info()
        print(f"Arrows: {self.arrows}")

    def shoot_arrow(self, target):
        if self.arrows > 0:
            if target.health <= 0:
                print(f"{target.name} is already defeated.")
                return

            arrow_damage = self.attack * 1.2 + random.randint(0, self.level // 2)  # Slightly stronger arrow attack
            self.arrows -= 1
            target.health -= arrow_damage
            print(f"Archer {self.name} shoots at {target.name} and deals {arrow_damage} damage. Arrows left: {self.arrows}")
            if target.health <= 0:
                target.health = 0
                print(f"{target.name} has been defeated!")
            else:
                print(f"{target.name}'s Health: {target.health}/{target.max_health}")
        else:
            print(f"{self.name} has run out of arrows!")

    def collect_arrows(self, amount):
        self.arrows += amount
        print(f"{self.name} collects {amount} arrows. Total arrows: {self.arrows}")


def simulate_battle(character1, character2):
    print("\n" + "=" * 30)
    print(f"Battle begins between {character1.name} and {character2.name}!")
    print("=" * 30)

    round_num = 1
    while character1.health > 0 and character2.health > 0:
        print(f"\n--- Round {round_num} ---")
        
        if isinstance(character1, Mage) and character1.mana >= 20:
            character1.cast_spell(character2)
        elif isinstance(character1, Archer) and character1.arrows > 0:
            character1.shoot_arrow(character2)
        else:
            character1.attack_target(character2)

        if character2.health <= 0:
            break  
        if isinstance(character2, Mage) and character2.mana >= 20:
            character2.cast_spell(character1)
        elif isinstance(character2, Archer) and character2.arrows > 0:
            character2.shoot_arrow(character1)
        else:
            character2.attack_target(character1)

        round_num += 1
        
        input("Press Enter for the next round...") # Can replace with time.sleep(1)

    print("\n" + "=" * 30)
    if character1.health > 0:
        print(f"Winner: {character1.name}!")
    elif character2.health > 0:
        print(f"Winner: {character2.name}!")
    else:
        print("Draw! Both characters are defeated.")
    print("=" * 30)

if __name__ == "__main__":
    # Create characters
    hero1 = Character("Hero", 5, 100, 20)
    hero2 = Character("Villain", 5, 90, 22)

    # Display character information
    hero1.display_info()
    hero2.display_info()

    # Create heroes of different classes
    warrior = Warrior("Conan", 10, 150, 25, 10)
    mage = Mage("Merlin", 9, 80, 30, 100)
    archer = Archer("Legolas", 8, 90, 28, 50)

    print("\n--- Class Heroes Information ---")
    warrior.display_info()
    mage.display_info()
    archer.display_info()

    # Simulate battles
    print("\n--- Battle Simulation 1 ---")
    warrior_copy = Warrior("Conan Copy", 10, 150, 25, 10) # Copy for a new battle
    mage_copy = Mage("Merlin Copy", 9, 80, 30, 100)
    simulate_battle(warrior_copy, mage_copy)

    print("\n--- Battle Simulation 2 ---")
    archer_copy = Archer("Legolas Copy", 8, 90, 28, 50)
    enemy_warrior = Warrior("Goblin", 7, 120, 20, 5)
    simulate_battle(archer_copy, enemy_warrior)

    # Example of health/mana/arrow restoration
    print("\n--- Restoration Demonstration ---")
    warrior.health = 50
    warrior.heal(30) # Restores health

    mage.mana = 30
    mage.restore_mana(50) # Restores mana

    archer.arrows = 10
    archer.collect_arrows(20) # Collects arrows