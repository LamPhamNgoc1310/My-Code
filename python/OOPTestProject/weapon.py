class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: float, value: float) -> None: 
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

iron_sword = Weapon(name="Iron Sword", 
                    weapon_type = "sword", 
                    damage = 5, 
                    value = 10)
short_bow = Weapon(name="Short Bow", 
                   weapon_type = "bow", 
                   damage = 4, 
                   value = 8)
fists = Weapon(name = "Fists", 
               weapon_type="fists", 
               damage = 2, 
               value = 0)
        