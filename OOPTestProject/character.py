from weapon import fists

class Character:
    # -> is the return type
    def __init__(self, name: str, health: float) -> None:
        self.name = name
        self.health = health
        self.maxhp = health
        # self.damage = damage

        self.weapon = fists
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        # max function to set the maximum baseline
        # remember to add an end if 0
        target.health = max(target.health, 0)
        # Idea: use overload method to calculate the damage and print the name of
        # item used
        print(f"{self.name} attacked with {self.weapon.name} and dealt {self.weapon.damage} damage")

# the Hero subclass will inherit the Character class
class Hero(Character):
    def __init__(self, name: str, health: float) -> None:
        # Could have initialize variables like below 
        # but using superclass is more convenient, and 
        # more logical
        
        # self.name = name
        # self.health = health
        # self.maxhp = health
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name} as a weapon!")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: float, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon