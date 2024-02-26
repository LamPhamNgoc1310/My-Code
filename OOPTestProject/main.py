from character import Hero, Enemy
from weapon import short_bow, iron_sword

# This way of init with the name of variable is much easier to look and understand
hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)

enemy = Enemy(name = "Enemy", health = 100, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
