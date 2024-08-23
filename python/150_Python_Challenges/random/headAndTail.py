import random
while True:
    coin = random.choice(["h", "t"])
    user = input("head or tail?(h/t)")
    user = user.lower()
    if user == coin:
        print("You win!")
    else:
        print("Oof, bad luck!")
